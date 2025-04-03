import subprocess
from pathlib import Path


def test_app_with_custom_class():
    command = [
        Path(__file__).parent / "app.py",
        "/root/somedir/",
        "file.txt",
    ]

    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = proc.communicate()

    assert out == b"Creating '/root/somedir/file.txt'\n"
    assert err == b""
    assert proc.returncode == 0
