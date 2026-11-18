"""news-image-20261117 entry (@polersyer): write the infographic to
/output/entry.png.

The image (entry.png, beside this file) is a 1024x1024 newspaper-style
front page summing up Tuesday 17 November 2026's world news in eight
stories, composed programmatically with PIL (see build_image.py).

Deterministic: a plain file copy, no network, no randomness — running
this program twice writes identical bytes both times.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1 << 20  # competition limit: 1 MiB


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


if not os.path.isfile(SOURCE):
    raise SystemExit(f"missing source image: {SOURCE}")

os.makedirs(OUT_DIR, exist_ok=True)
DEST = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SOURCE, DEST)

# Fail loudly instead of silently submitting a truncated or corrupt copy:
# the competition runs this program twice and both runs must produce the
# same bytes, so verify the output is byte-identical to the source and
# within the 1 MiB size limit.
if _sha256(DEST) != _sha256(SOURCE):
    raise SystemExit("entry.png copy mismatch: output differs from source")
if os.path.getsize(DEST) > MAX_BYTES:
    raise SystemExit(f"entry.png too large: {os.path.getsize(DEST)} bytes")
print("wrote entry.png")
