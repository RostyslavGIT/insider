import logging
import sys
from pathlib import Path

# Create logs directory if it doesn't exist
logs_dir = Path('logs')
logs_dir.mkdir(parents=True, exist_ok=True)

# Set up handlers
stream_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler(logs_dir / 'myapp.log', "w")

# Create and configure the named logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(filename)s -> line: %(lineno)d | %(levelname)s | %(asctime)s >>> %(message)s",
                              datefmt='%Y-%m-%d %H:%M')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)