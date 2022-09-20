class Logger(object):

    class __Logger:
        def __init__(self, filename: str) -> object:
            self.filename = filename

        def __write_log(self, level: str, msg: str) -> None:
            with open(self.filename, 'a') as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg: str) -> None:
            self.__write_log("CRITICAL", msg)

        def error(self, msg: str) -> None:
            self.__write_log("ERROR", msg)

        def warning(self, msg: str) -> None:
            self.__write_log("CRITICAL", msg)

        def debug(self, msg: str) -> None:
            self.__write_log("DEBUG", msg)

        def info(self, msg: str) -> None:
            self.__write_log("INFO", msg)

    instance = None

    @classmethod
    def __new__(cls) -> object:
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance

    def __getattribute__(self, name: str):
        return getattr(self.instance, name)

    def __setattr__(self, name: str):
        return setattr(self.instance, name)