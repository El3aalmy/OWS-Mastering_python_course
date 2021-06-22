# -------------------------------------------------
# -- Advanced lessons => Add loggin to your code --
# -------------------------------------------------
# - Print out to console or file 
# - Print logs of what happens
# -------------------------------------------------
# - Debug 
# - Info
# - Warning 
# - Error
# - Critical
# ----------
# name => loggin module give it to the default logger.
# ----------------------------------------------------
# Basic donfig 
# - level => level of severity 
# - filename => file name and extension
# - mode => mode of the file a => append
# - format => format for the log message 
# ---------------------------------------------------
# getlogger => return a logger with the specified name 
# ---------------------------------------------------

import logging

# print(dir(logging))

logging.basicConfig(filename="my_app.log", 
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s =>  '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")


# logging.warning("This is critical message")

my_logger = logging.getLogger("Hasan")

my_logger.warning("This is critical message")
