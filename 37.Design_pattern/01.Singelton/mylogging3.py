class MyLogger:
    def __init__(self,filename):
        self.filename=filename

    def __write_log(self,level:str, msg:str):
        with open(self.filename,'a') as log_file:
            log_file.write("[{0}] {1}\n".format(level,msg))

    def critical(self,msg):
        self.__write_log("CRITICAL", msg)

    def error(self,msg):
        self.__write_log("ERROR", msg)

    def warning(self,msg):
        self.__write_log("CRITICAL", msg)

    def debug(self,msg):
        self.__write_log("DEBUG", msg)

    def info(self,msg):
        self.__write_log("INFO", msg)

    # def __getattribute__(self, name) # when we use attributes it will called