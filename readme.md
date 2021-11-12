# How to use
Check `main.py` to get an overall idea on how to use it.

1. import both color log formats and custom formatter classes

```
from custom_formatter import CustomFormatter
from color_log_formats import ColorLogFormats
```

2. Set logging options like how you do it normally
3. Assign the `format` you want to use for the logger to format variable
4. Create a `CustomFormatter.FORMATS` object by specifying the colors and styles. You can add multiple colors and styles to each log levels. See the example below.
```
CustomFormatter.FORMATS = {
    logging.DEBUG: ColorLogFormats.BLUE_FG + format + ColorLogFormats.RESET,
    logging.INFO: ColorLogFormats.MAGENTA_FG + format + ColorLogFormats.RESET,
    logging.WARNING: ColorLogFormats.YELLOW_FG + format + ColorLogFormats.RESET,
    logging.ERROR: ColorLogFormats.BLACK_BG + ColorLogFormats.RED_FG + ColorLogFormats.ITALIC + format + ColorLogFormats.RESET,
    logging.CRITICAL: ColorLogFormats.RED_BG + ColorLogFormats.WHITE_FG +
    ColorLogFormats.UNDERLINE + format + ColorLogFormats.RESET
}
```
5. Log normally
```
logger.debug("This is debug logging")
logger.info("This is info logging")
logger.warning("This is warn logging")
logger.error("This is error logging")
logger.critical("This is critical logging")
```


## Here's a list of all the colors and styles
```
    # Misc
    RESET = '\x1b[0m'
    BOLD = '\x1b[1m'
    FAINT = '\x1b[2m'
    ITALIC = '\x1b[3m'
    UNDERLINE = '\x1b[4m'

    # Basic Foreground Colors
    BLACK_FG = '\x1b[30m'
    RED_FG = '\x1b[31m'
    GREEN_FG = '\x1b[32m'
    YELLOW_FG = '\x1b[33m'
    BLUE_FG = '\x1b[34m'
    MAGENTA_FG = '\x1b[35m'
    CYAN_FG = '\x1b[36m'
    WHITE_FG = '\x1b[37m'
    DEFAULT_FG = '\x1b[39m'

    # Basic Background Colors
    BLACK_BG = '\x1b[40m'
    RED_BG = '\x1b[41m'
    GREEN_BG = '\x1b[42m'
    YELLOW_BG = '\x1b[43m'
    BLUE_BG = '\x1b[44m'
    MAGENTA_BG = '\x1b[45m'
    CYAN_BG = '\x1b[46m'
    WHITE_BG = '\x1b[47m'
    DEFAULT_BG = '\x1b[49m'

    # Bright Foreground Colors
    BRIGHT_BLACK_FG = '\x1b[90m'
    BRIGHT_RED_FG = '\x1b[91m'
    BRIGHT_GREEN_FG = '\x1b[92m'
    BRIGHT_YELLOW_FG = '\x1b[93m'
    BRIGHT_BLUE_FG = '\x1b[94m'
    BRIGHT_MAGENTA_FG = '\x1b[95m'
    BRIGHT_CYAN_FG = '\x1b[96m'
    BRIGHT_WHITE_FG = '\x1b[97m'

    # Bright Background Colors
    BRIGHT_BLACK_BG = '\x1b[100m'
    BRIGHT_RED_BG = '\x1b[101m'
    BRIGHT_GREEN_BG = '\x1b[102m'
    BRIGHT_YELLOW_BG = '\x1b[103m'
    BRIGHT_BLUE_BG = '\x1b[104m'
    BRIGHT_MAGENTA_BG = '\x1b[105m'
    BRIGHT_CYAN_BG = '\x1b[106m'
    BRIGHT_WHITE_BG = '\x1b[107m'
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)