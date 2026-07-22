from loguru import logger

logger.add(
    "logs.log",
    rotation="5 MB"
)