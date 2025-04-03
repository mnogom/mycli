import subprocess
from pathlib import Path


def test_app_with_serializer_2():
    command = [Path(__file__).parent / "app.py", "1,2,3,4,5"]

    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = proc.communicate()
    assert err == b""
    assert out == b"15\n"
    assert proc.returncode == 0
