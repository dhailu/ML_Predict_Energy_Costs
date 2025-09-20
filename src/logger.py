import logging
import os
from datetime import datetime



LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

# Debug print so you can see the path at startup
print(f"[LOGGER INIT] Logging to: {LOG_FILE}")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

# Optional: also log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger("").addHandler(console_handler)


######################

# LOG_FILE = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
# logs_path = os.path.join(os.getcwd(), "log", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)


# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#      filename =  LOG_FILE_PATH,
#      format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#      level= logging.INFO,

# )

# if __name__ == "__main__":
#     logging.info("Logging has started")
####################




