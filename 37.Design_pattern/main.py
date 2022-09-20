
class Logger(object):

    class __Logger:
        def __init__(self):
            self.file_name = None

        def __str__(self):
            return "{}!r  {}".format(self, self.file_name)

        def _write_log(self, level, msg):
            with open(self.file_name, 'as') as log1:
                log1.write("[{}] {}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warning(self, msg):
            self._write_log("WARNING", msg)

        def info(self, msg):
            self._write_log("INFORMATION", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls):
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance

    def __setattr__(self, f_name):
        return setattr(self.instance, f_name)

    def __getattribute__(self, f_name):
        return getattr(self.instance, f_name)
