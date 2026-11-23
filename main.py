# SPDX-License-Identifier: MIT
"""make.fun news-image-20261122 entry.

Reproduces the submitted front-page image for Sunday 22 November 2026
("The Daily Ledger": COP31 collapses in Antalya).

The program is fully deterministic and needs no network: it reads the
bundled entry.png next to this file, checks that it really is the
1024x1024 PNG we submitted, copies its bytes verbatim to the output
directory, and then re-reads the copy to prove the bytes are identical.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def read_png_bytes(source: Path) -> bytes:
    """Read the bundled image and validate its PNG header and size."""
    data = source.read_bytes()
    if len(data) < 33:
        raise ValueError(f"entry.png is too short: {len(data)} bytes")
    if data[:8] != PNG_MAGIC:
        raise ValueError("entry.png does not start with the PNG signature")
    if data[12:16] != b"IHDR":
        raise ValueError("entry.png first chunk is not IHDR")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            f"entry.png is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    return data


def sha256_hex(data: bytes) -> str:
    """Return the lowercase hex SHA-256 digest of *data*."""
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    data = read_png_bytes(source)
    digest = sha256_hex(data)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)

    written = target.read_bytes()
    if written != data:
        raise ValueError("output bytes differ from entry.png")
    if sha256_hex(written) != digest:
        raise ValueError("output SHA-256 differs from entry.png")

    print(f"entry.png: {len(data)} bytes, sha256 {digest}")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
