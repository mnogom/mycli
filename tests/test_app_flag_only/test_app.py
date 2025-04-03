import subprocess
from pathlib import Path


def test_app_with_flag():
    command = [Path(__file__).parent / "app.py", "--foo"]

    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = proc.communicate()
    assert out == b"bar\n"
    assert err == b""
    assert proc.returncode == 0
