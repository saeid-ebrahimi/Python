import mylogging

mylogging.critical("Bad usage")

try:
    a = 10/0
except:
    mylogging.error("Divided by zero")