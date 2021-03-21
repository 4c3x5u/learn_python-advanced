import logging

extdata = {"user": "4c3x5u"}


def myfunc():
    logging.debug("This is a debug-level log message", extra=extdata)


def main():
    fmtstr = "%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:" \
             "%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"

    # set the output file and debug level
    logging.basicConfig(level=logging.DEBUG,
                        filename="2_output.log",
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    # try out each of the logging levels
    logging.info("This is an info-level log message", extra=extdata)
    logging.warning("This is a warning-level log message", extra=extdata)

    myfunc()


if __name__ == "__main__":
    main()
