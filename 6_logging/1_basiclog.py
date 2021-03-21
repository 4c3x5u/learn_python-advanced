# use the built-in logging module
import logging


def main():
    # use `basicConfig` to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename="1_output.log",
                        filemode="w")

    # try out each of the logging levels
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    # output formatted strings to the log
    logging.info(f"Here's a {'string'} variable and an int: {10}")


if __name__ == "__main__":
    main()
