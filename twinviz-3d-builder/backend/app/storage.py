import os
from pathlib import Path
from .core.config import settings

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_upload(file_stream, filename: str) -> str:
    target = UPLOAD_DIR / filename
    with open(target, 'wb') as f:
        f.write(file_stream)
    return str(target)

def get_upload_path(filename: str) -> str:
    return str(UPLOAD_DIR / filename)

def remove_file(filename: str):
    p = UPLOAD_DIR / filename
    if p.exists():
        p.unlink()
