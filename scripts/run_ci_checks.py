"""Run the same class of checks CI runs: syntax compilation, then unit tests."""
import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    print("== Syntax check ==")
    ok = all(
        [
            compileall.compile_dir(str(ROOT / "tests"), quiet=1),
            compileall.compile_file(str(ROOT / "medilink_contract.py"), quiet=1),
            compileall.compile_file(str(ROOT / "config.py"), quiet=1),
            compileall.compile_file(str(ROOT / "demo_summary.py"), quiet=1),
        ]
    )
    if not ok:
        print("Syntax check failed.")
        return 1

    print("== Unit tests ==")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
