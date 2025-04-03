import subprocess
from pathlib import Path
import json


def test_app_with_serializer_1():
    command = [
        Path(__file__).parent / "app.py",
        '{"x": "y"}',
        "-a",
        '{"foo": "bar"}',
    ]

    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = proc.communicate()
    assert err == b""
    assert json.loads(out.decode("utf-8").replace("'", '"')) == {
        "x": "y",
        "foo": "bar",
    }
    assert proc.returncode == 0
