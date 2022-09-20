
def critical(msg):
    with open("filename.txt","a") as log_file:
        log_file.write("[CRITICAL] {0}\n".format(msg))

def error(msg):
    with open("filename.txt","a") as log_file:
        log_file.write("[Error] {0}\n".format(msg))

def warning(msg):
    with open("filename.txt","a") as log_file:
        log_file.write("[WARNING] {0}\n".format(msg))

def info(msg):
    with open("filename.txt","a") as log_file:
        log_file.write("[INFO] {0}\n".format(msg))

def debug(msg):
    with open("filename.txt","a") as log_file:
        log_file.write("[DEBUG] {0}".format(msg))
