import os
import logging
from uvicorn import Config, Server
from loguru import logger
from custom_logging import CustomizeLogger
from pathlib import Path

logger = logging.getLogger(__name__)

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
