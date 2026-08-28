import os
import platform
from pathlib import Path

VERSION = "0.10.11a0"
PROCESSING_BUILD_NUMBER = 1433

if not (PY5_HOME := os.environ.get("PY5_HOME")):
    if platform.system() == "Windows":
        PY5_HOME = Path.home() / "AppData" / "Local" / "py5"
    else:
        PY5_HOME = Path.home() / ".cache" / "py5"
