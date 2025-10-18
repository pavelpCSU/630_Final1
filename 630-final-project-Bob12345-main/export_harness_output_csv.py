# Harness Output Exporter (CSV Only)
"""
This script runs the benchmark harness and exports all summary tables to a CSV file for easy import into Google Sheets or Google Docs.
"""

import subprocess
import sys
import os
from datetime import datetime, timezone, timedelta

PST = timezone(timedelta(hours=-8))
now_pst = datetime.now(PST)

OUTPUT_DIR = "Output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
EXPORT_CSV = os.path.join(OUTPUT_DIR, f"harness_output_{now_pst.strftime('%Y%m%d_%H%M%S')}_PST.csv")

def run_and_get_txt_file():
    # Forward all extra args to TXT exporter
    subprocess.run([sys.executable, "export_harness_output_txt.py"] + sys.argv[1:], check=True)
    # Find the most recent TXT file in the output directory
    txt_files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith('.txt')])
    if not txt_files:
        raise RuntimeError("No TXT output found.")
    return os.path.join(OUTPUT_DIR, txt_files[-1])

def extract_tables_from_txt(txt_path):
    # Dummy implementation: extract all lines containing commas (CSV-like)
    tables = []
    with open(txt_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        if ',' in line:
            tables.append(line.strip())
    return tables

def main():
    txt_path = run_and_get_txt_file()
    tables = extract_tables_from_txt(txt_path)
    with open(EXPORT_CSV, "w") as f:
        for row in tables:
            f.write(row + "\n")
    print(f"Exported CSV summary to: {EXPORT_CSV}")

if __name__ == "__main__":
    main()