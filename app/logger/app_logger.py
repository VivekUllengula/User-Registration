import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(messages)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
    level=logging.INFO
)

logger = logging.getLogger(__name__)

