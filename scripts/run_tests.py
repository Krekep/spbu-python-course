import subprocess
import os
import sys
import shared


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)

    subprocess.check_call(["python", "-m", "pytest", "-vv", "-s", shared.TESTS])


if __name__ == "__main__":
    main()
