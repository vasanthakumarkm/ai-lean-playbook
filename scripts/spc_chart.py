# SPC Control Chart Generator
# AI + Lean Six Sigma DMAIC Playbook
# Usage: python spc_chart.py --input data.csv --metric "Defect Rate" --output spc_chart.png
# Demo:  python spc_chart.py --demo
#
# Input CSV format:
#   Date,Measurement
#   2026-01-01,12.5
#   2026-01-02,11.8
#
# Output:
#   - X-bar control chart saved as PNG
#   - UCL, LCL, and mean printed to console
#   - Out-of-control points highlighted in red
#   - Summary statistics printed

import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def load_data(filepath):
    """Load measurement data from CSV file."""
    try:
        df = pd.read_csv(filepath)
        df.columns = [col.strip() for col in df.columns]
        if 'Measurement' in df.columns:
            measure_col = 'Measurement'
        elif 'Value' in df.columns:
            measure_col = 'Value'
        else:
            measure_col = df.columns[1]
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        else:
            df['Date'] = range(1, len(df) + 1)
        df['Measurement'] = pd.to_numeric(df[measure_col], errors='coerce')
        df = df.dropna(subset=['Measurement'])
        return df
    except FileNotFoundError:
        print(f"ERROR: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR loading data: {e}")
        sys.exit(1)


def calculate_control_limits(measurements, sigma_multiplier=3):
    """Calculate X-bar, UCL, and LCL."""
    mean = np.mean(measurements)
    std = np.std(measurements, ddof=1)
    ucl = mean + sigma_multiplier * std
    lcl = mean - sigma_multiplier * std
    lcl = max(lcl, 0)  # LCL cannot be negative for rates/counts
    return mean, ucl, lcl, std


def detect_out_of_control(measurements, mean, ucl, lcl):
    """Detect out-of-control points using Nelson Rules 1, 2, and 3."""
    ooc_indices = []
    ooc_reasons = {}

    # Rule 1: 1 point beyond 3-sigma control limits
    for i, val in enumerate(measurements):
        if val > ucl or val < lcl:
            ooc_indices.append(i)
            ooc_reasons[i] = 'Rule 1: Beyond 3-sigma limits'

    # Rule 2: 8 consecutive points on same side of mean
    for i in range(len(measurements) - 7):
        window = measurements[i:i + 8]
        above = all(v > mean for v in window)
        below = all(v < mean for v in window)
        if above or below:
            for j in range(i, i + 8):
                if j not in ooc_indices:
                    ooc_indices.append(j)
                    ooc_reasons[j] = 'Rule 2: 8 consecutive points same side'

    # Rule 3: 6 points trending up or down
    for i in range(len(measurements) - 5):
        window = measurements[i:i + 6]
        trending_up = all(window[j] < window[j + 1] for j in range(5))
        trending_down = all(window[j] > window[j + 1] for j in range(5))
        if trending_up or trending_down:
            for j in range(i, i + 6):
                if j not in ooc_indices:
                    ooc_indices.append(j)
                    ooc_reasons[j] = 'Rule 3: 6-point trend'

    return sorted(set(ooc_indices)), ooc_reasons


def generate_spc_chart(df, metric_name, output_path, sigma_multiplier=3):
    """Generate and save the SPC X-bar control chart."""
    measurements = df['Measurement'].values
    n = len(measurements)

    mean, ucl, lcl, std = calculate_control_limits(measurements, sigma_multiplier)
    ooc_indices, ooc_reasons = detect_out_of_control(list(measurements), mean, ucl, lcl)

    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    x = range(n)

    in_control = [i for i in x if i not in ooc_indices]
    ax.plot(x, measurements, color='#58a6ff', linewidth=1.5, zorder=2, label='Measurements')
    ax.scatter(in_control, [measurements[i] for i in in_control],
               color='#58a6ff', s=50, zorder=3)

    if ooc_indices:
        ax.scatter(ooc_indices, [measurements[i] for i in ooc_indices],
                   color='#f85149', s=80, zorder=4, label='Out of Control')
        for idx in ooc_indices:
            reason = ooc_reasons.get(idx, '')
            ax.annotate(f'  {reason.split(":")[0]}',
                        (idx, measurements[idx]),
                        fontsize=7, color='#f85149', va='bottom')

    ax.axhline(y=mean, color='#3fb950', linewidth=1.5, linestyle='-',
               label=f'Mean = {mean:.2f}')
    ax.axhline(y=ucl, color='#d29922', linewidth=1.5, linestyle='--',
               label=f'UCL = {ucl:.2f}')
    ax.axhline(y=lcl, color='#d29922', linewidth=1.5, linestyle='--',
               label=f'LCL = {lcl:.2f}')
    ax.fill_between(x, lcl, ucl, alpha=0.08, color='#3fb950')

    ax.set_title(f'SPC X-bar Control Chart: {metric_name}',
                 fontsize=14, color='white', pad=15, fontweight='bold')
    ax.set_xlabel('Observation / Time Period', fontsize=11, color='#8b949e')
    ax.set_ylabel(metric_name, fontsize=11, color='#8b949e')
    ax.tick_params(colors='#8b949e')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='upper right', facecolor='#161b22', edgecolor='#30363d',
              labelcolor='white', fontsize=9)

    summary_text = (
        f'n = {n} observations\n'
        f'Mean = {mean:.3f}\n'
        f'Std Dev = {std:.3f}\n'
        f'UCL = {ucl:.3f}\n'
        f'LCL = {lcl:.3f}\n'
        f'Out-of-control: {len(ooc_indices)}'
    )
    props = dict(boxstyle='round', facecolor='#161b22', edgecolor='#30363d', alpha=0.9)
    ax.text(0.01, 0.97, summary_text, transform=ax.transAxes, fontsize=8,
            verticalalignment='top', bbox=props, color='#8b949e')

    fig.text(0.99, 0.01,
             'AI + Lean Six Sigma Playbook | github.com/vasanthakumarkm/ai-lean-playbook',
             ha='right', va='bottom', fontsize=7, color='#30363d')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    return mean, ucl, lcl, std, ooc_indices, ooc_reasons


def print_summary(metric_name, n, mean, ucl, lcl, std, ooc_indices, ooc_reasons):
    """Print SPC analysis summary to console."""
    print('\n' + '=' * 60)
    print(f'  SPC ANALYSIS SUMMARY: {metric_name}')
    print('=' * 60)
    print(f'  Observations (n)        : {n}')
    print(f'  Process Mean (X-bar)    : {mean:.4f}')
    print(f'  Standard Deviation      : {std:.4f}')
    print(f'  Upper Control Limit     : {ucl:.4f}')
    print(f'  Lower Control Limit     : {lcl:.4f}')
    print(f'  Out-of-control points   : {len(ooc_indices)}')
    if ooc_indices:
        print('\n  Out-of-control details:')
        for idx in ooc_indices:
            reason = ooc_reasons.get(idx, 'Unknown')
            print(f'    - Point {idx + 1}: {reason}')
    verdict = 'IN CONTROL' if not ooc_indices else 'OUT OF CONTROL - INVESTIGATE'
    print(f'\n  Process Status: {verdict}')
    print('=' * 60 + '\n')


def create_sample_data(output_path='sample_data.csv'):
    """Generate sample CSV data for demo mode."""
    import random
    random.seed(42)
    dates = pd.date_range(start='2026-01-06', periods=30, freq='W')
    measurements = []
    for i in range(30):
        base = 12.0 if i < 12 else 5.0  # Improvement after week 12
        val = round(base + random.gauss(0, 1.5), 2)
        measurements.append(max(0, val))
    measurements[5] = 18.5   # Inject out-of-control spike
    measurements[6] = 17.2
    df = pd.DataFrame({'Date': dates.strftime('%Y-%m-%d'), 'Measurement': measurements})
    df.to_csv(output_path, index=False)
    print(f'Sample data written to: {output_path}')
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='SPC Control Chart Generator - AI + Lean Six Sigma Playbook'
    )
    parser.add_argument('--input', type=str, default=None,
                        help='Path to input CSV (columns: Date, Measurement)')
    parser.add_argument('--metric', type=str, default='Process Metric',
                        help='Metric name for chart title')
    parser.add_argument('--output', type=str, default='spc_chart.png',
                        help='Output PNG path (default: spc_chart.png)')
    parser.add_argument('--sigma', type=float, default=3.0,
                        help='Sigma multiplier for control limits (default: 3)')
    parser.add_argument('--demo', action='store_true',
                        help='Run with auto-generated sample data')
    args = parser.parse_args()

    if args.demo or args.input is None:
        print('Running in DEMO mode with auto-generated sample data...')
        input_path = create_sample_data('sample_data.csv')
        metric = 'Defect Rate (%)'
        output = 'spc_demo_output.png'
    else:
        input_path = args.input
        metric = args.metric
        output = args.output

    print(f'Loading data from: {input_path}')
    df = load_data(input_path)
    print(f'Loaded {len(df)} observations.')

    mean, ucl, lcl, std, ooc_indices, ooc_reasons = generate_spc_chart(
        df, metric, output, args.sigma
    )
    print_summary(metric, len(df), mean, ucl, lcl, std, ooc_indices, ooc_reasons)
    print(f'Chart saved to: {output}')


if __name__ == '__main__':
    main()
