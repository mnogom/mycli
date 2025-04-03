import subprocess

import pytest

APP = "tests/test_app_all_arg_types/app.py"


@pytest.mark.parametrize(
    "command, expected",
    [
        # Use only requirement arguments
        (
            [APP, "Hello, World!", "Alexander"],
            b"Send to Alexander: Hello, World! from Konstantin\n",
        ),
        # Use short flag and replace it
        (
            [APP, "-l", "Hello, World!", "Alexander"],
            b"Send to Alexander: HELLO, WORLD! from Konstantin\n",
        ),
        (
            [APP, "Hello, World!", "-l", "Alexander"],
            b"Send to Alexander: HELLO, WORLD! from Konstantin\n",
        ),
        (
            [APP, "Hello, World!", "Alexander", "-l"],
            b"Send to Alexander: HELLO, WORLD! from Konstantin\n",
        ),
        # Use long flag
        (
            [APP, "--loud", "Hello, World!", "Alexander"],
            b"Send to Alexander: HELLO, WORLD! from Konstantin\n",
        ),
        # Use short named argument
        (
            [
                APP,
                "Hello, World!",
                "Alexander",
                "--from",
                "Anonymous",
                "--loud",
            ],
            b"Send to Alexander: HELLO, WORLD! from Anonymous\n",
        ),
        # Use long named argument
        (
            [APP, "Hello, World!", "Alexander", "-f", "Anonymous", "--loud"],
            b"Send to Alexander: HELLO, WORLD! from Anonymous\n",
        ),
    ],
)
def test_app_with_flag(command, expected):
    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = proc.communicate()
    assert out == expected
    assert err == b""
    assert proc.returncode == 0
