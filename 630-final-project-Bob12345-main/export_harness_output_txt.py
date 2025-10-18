import subprocess
import sys
from datetime import datetime, timezone, timedelta
import os

# Set PST timezone (UTC-8, no DST handling for simplicity)
PST = timezone(timedelta(hours=-8))
now_pst = datetime.now(PST)

OUTPUT_DIR = "Output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
EXPORT_TXT = os.path.join(OUTPUT_DIR, f"harness_output_{now_pst.strftime('%Y%m%d_%H%M%S')}_PST.txt")

def run_harness_and_capture(extra_args=None):
    cmd = [sys.executable, "benchmark_rubric_harness.py"]
    if extra_args:
        cmd += extra_args
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.stdout, proc.stderr, proc.returncode

def main():
    extra_args = sys.argv[1:]  # Forward all extra args
    print(f"Running benchmark harness: python3 benchmark_rubric_harness.py {' '.join(extra_args)}")
    out, err, code = run_harness_and_capture(extra_args)
    with open(EXPORT_TXT, "w") as f:
        f.write(out)
        if err:
            f.write("\n---\nSTDERR:\n\n")
            f.write(err)
    print(f"\nExported plain text output to: {EXPORT_TXT}")
    print("\nYou can open this file in any text editor for review or further processing.")

if __name__ == "__main__":
    main()