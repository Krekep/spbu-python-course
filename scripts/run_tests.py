import subprocess
import sys
import os


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)

    tests_dir = os.path.join(project_root, "tests")

    subprocess.check_call([sys.executable, "-m", "pytest", "-vv", "-s", tests_dir])


if __name__ == "__main__":
    main()
