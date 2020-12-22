from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.1.0"
APP_NAME = "Hugging FastAPI"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH")
QUESTION_ANSWER_MODEL: str = config("QUESTION_ANSWER_MODEL")
