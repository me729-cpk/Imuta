import sys
from pathlib import Path

from streamlit.web import cli as stcli

import models.subject
import models.topic
import core.study_manager
import models.study_session

def main():
    if getattr(sys, "frozen", False):
        app_path = Path(getattr(sys, "_MEIPASS")) / "app.py"
    else:
        app_path = Path(__file__).resolve().parent / "app.py"

    sys.argv = [
        "streamlit",
        "run",
        str(app_path),
        "--global.developmentMode=false",
        "--server.port=8501",
        "--browser.serverPort=8501",
        "--server.headless=false"
    ]

    stcli.main()


if __name__ == "__main__":
    main()