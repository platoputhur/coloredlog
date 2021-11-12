import logging
from custom_formatter import CustomFormatter
from color_log_formats import ColorLogFormats

logger = logging.getLogger("custom_log_formats")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
if not logger.hasHandlers():
    logger.addHandler(ch)
logger.addHandler(ch)

# Sample usage
format = "%(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
CustomFormatter.FORMATS = {
    logging.DEBUG: ColorLogFormats.BLUE_FG + format + ColorLogFormats.RESET,
    logging.INFO: ColorLogFormats.MAGENTA_FG + format + ColorLogFormats.RESET,
    logging.WARNING: ColorLogFormats.YELLOW_FG + format + ColorLogFormats.RESET,
    logging.ERROR: ColorLogFormats.BLACK_BG + ColorLogFormats.RED_FG + ColorLogFormats.ITALIC + format + ColorLogFormats.RESET,
    logging.CRITICAL: ColorLogFormats.RED_BG + ColorLogFormats.WHITE_FG +
    ColorLogFormats.UNDERLINE + format + ColorLogFormats.RESET
}


logger.debug("This is debug logging")
logger.info("This is info logging")
logger.warning("This is warn logging")
logger.error("This is error logging")
logger.critical("This is critical logging")
