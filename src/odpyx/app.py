from typing import Any
from flask import Flask

app = Flask(__name__)









@app.errorhandler(404)
def fallback(_) -> Any:
    return {
        "playerDataDelta": {
            "modified": {},
            "deleted": {}
        }
    }
