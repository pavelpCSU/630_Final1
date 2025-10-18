
# Harness Output Exporter
"""
This script runs the benchmark harness and exports all output (annotations, tables, and analysis) to both Markdown and CSV files for easy import into Google Docs or Google Sheets.
"""



import sys
from datetime import datetime, timezone, timedelta
import re
import os
import subprocess

# Set PST timezone (UTC-8, no DST handling for simplicity)
PST = timezone(timedelta(hours=-8))
now_pst = datetime.now(PST)

OUTPUT_DIR = "Output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
EXPORT_MD = os.path.join(OUTPUT_DIR, f"harness_output_{now_pst.strftime('%Y%m%d_%H%M%S')}_PST.md")
EXPORT_CSV = os.path.join(OUTPUT_DIR, f"harness_output_{now_pst.strftime('%Y%m%d_%H%M%S')}_PST.csv")

def run_and_get_txt_file():
    # Run the TXT exporter and find the latest txt file in Output
    subprocess.run([sys.executable, "export_harness_output_txt.py"], check=True)
    txt_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".txt") and f.startswith("harness_output_")]
    if not txt_files:
        print("No TXT output file found in Output directory.")
        sys.exit(1)
    # Get the most recently modified txt file
    txt_files.sort(key=lambda f: os.path.getmtime(os.path.join(OUTPUT_DIR, f)), reverse=True)
    return os.path.join(OUTPUT_DIR, txt_files[0])

def read_output_file(input_path):
    with open(input_path, 'r') as f:
        return f.read(), '', 0

def extract_tables_from_output(output):
    # Find all tables in the output (header line, separator, then data rows)
    tables = []
    lines = output.splitlines()
    i = 0
    current_title = None
    while i < len(lines):
        # Look for a problem or solution section for context
        if lines[i].startswith('==='):
            current_title = lines[i].strip('= ').strip()
            i += 1
        elif lines[i].startswith('---'):
            # e.g. --- Problem1-copilot-GPT-4.1-python (Python) ---
            current_title = lines[i].strip('- ').strip()
            i += 1
        elif re.match(r"\s*Input Size\s*\|", lines[i]):
            header = lines[i].strip()
            sep = lines[i+1] if i+1 < len(lines) else ''
            data = []
            j = i+2
            while j < len(lines) and '|' in lines[j] and not lines[j].strip().startswith('---'):
                data.append(lines[j].strip())
                j += 1
            tables.append((header, data, current_title))
            i = j
        else:
            i += 1  # Always increment to avoid infinite loop
    return tables

def write_csv_from_tables(tables, csv_path):
    import csv
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for idx, (header, data, title) in enumerate(tables):
            if idx > 0:
                writer.writerow([])  # Blank line between tables
            if title:
                writer.writerow([title])
            headers = [h.strip() for h in header.split('|')]
            writer.writerow(headers)
            for row in data:
                cells = [c.strip() for c in row.split('|')]
                writer.writerow(cells)


def main():
    print("Running TXT export script to generate latest output...")
    txt_path = run_and_get_txt_file()
    print(f"Reading output from: {txt_path}")
    out, err, code = read_output_file(txt_path)
    # Write Markdown output
    with open(EXPORT_MD, "w") as f:
        f.write(f"# Benchmark Harness Output\n\n")
        f.write(f"*Exported: {datetime.now().isoformat()}*\n\n")
        f.write("```")
        f.write(out)
        f.write("\n```")
    # Extract and write CSV tables
    tables = extract_tables_from_output(out)
    write_csv_from_tables(tables, EXPORT_CSV)
    print(f"\nExported Markdown to: {EXPORT_MD}")
    print(f"Exported CSV tables to: {EXPORT_CSV}")
    print("\nTo add to Google Docs or Sheets:")
    print("- For tables, open the CSV in Google Sheets or import directly.")
    print("- For full output, use the Markdown file as before.")

if __name__ == "__main__":
    main()
