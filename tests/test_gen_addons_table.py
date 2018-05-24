import os
import subprocess
import sys


def test_1():
    dirname = os.path.dirname(__file__)
    cwd = os.path.join(dirname, 'test_repo')
    readme_filename = os.path.join(dirname, 'test_repo', 'README.md')
    with open(readme_filename) as f:
        readme_before = f.read()
    readme_expected_filename = os.path.join(
        dirname, 'test_repo', 'README.md.expected',
    )
    with open(readme_expected_filename) as f:
        readme_expected = f.read()
    try:
        res = subprocess.call([
            sys.executable, '-m', 'tools.gen_addons_table',
        ], cwd=cwd)
        assert res == 0
        with open(readme_filename) as f:
            readme_after = f.read()
        assert readme_after == readme_expected
    finally:
        with open(readme_filename, 'w') as f:
            f.write(readme_before)
