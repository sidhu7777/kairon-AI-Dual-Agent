from src.utils.logger import logger

def handle_exception(e):
    logger.error(f"Exception occurred: {str(e)}")
    raise e
