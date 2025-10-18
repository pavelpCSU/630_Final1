import subprocess
import sys
from datetime import datetime, timezone, timedelta
import os

PST = timezone(timedelta(hours=-8))
now_pst = datetime.now(PST)

OUTPUT_DIR = "Output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
EXPORT_MD = os.path.join(OUTPUT_DIR, f"harness_output_{now_pst.strftime('%Y%m%d_%H%M%S')}_PST.md")

def run_harness_and_capture(extra_args=None):
    cmd = [sys.executable, "benchmark_rubric_harness.py"]
    if extra_args:
        cmd += extra_args
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.stdout, proc.stderr, proc.returncode

def main():
    extra_args = sys.argv[1:]
    print(f"Running benchmark harness: python3 benchmark_rubric_harness.py {' '.join(extra_args)}")
    out, err, code = run_harness_and_capture(extra_args)
    with open(EXPORT_MD, "w") as f:
        f.write(f"# Benchmark Harness Output\n\n")
        f.write(f"*Exported: {datetime.now().isoformat()}*\n\n")
        f.write("```")
        f.write(out)
        f.write("\n```")
        if err:
            f.write("\n---\n**STDERR:**\n\n")
            f.write("```")
            f.write(err)
            f.write("\n```")
    print(f"\nExported Markdown to: {EXPORT_MD}")

if __name__ == "__main__":
    main()