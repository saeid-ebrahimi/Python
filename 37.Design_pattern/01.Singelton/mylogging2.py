def write_log(level:str, msg:str,filename:str):
    with open(filename,'a') as log_file:
        log_file.write("[{0}] {1}\n".format(level,msg))


def critical(msg):
    write_log("CRITICAL", msg, "log1.txt")

def error(msg):
    write_log("ERROR", msg,"log1.txt")

def warning(msg):
    write_log("CRITICAL", msg,"log1.txt")

def debug(msg):
    write_log("DEBUG", msg,"log1.txt")

def info(msg):
    write_log("INFO", msg,"log1.txt")

