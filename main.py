import logging
import os
from pathlib import Path

from loguru import logger
from uvicorn import Config, Server

from custom_logging import CustomizeLogger

PORT = int(os.environ.get("PORT", 8080))
LOG_LEVEL = logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG"))
JSON_LOGS = True if os.environ.get("JSON_LOGS", "0") == "1" else False


if __name__ == '__main__':
    server = Server(
        Config(
            "app.api:app",
            host="0.0.0.0",
            log_level=LOG_LEVEL,
            port=PORT, 
            reload=True
        ),
    )

    server.run()
