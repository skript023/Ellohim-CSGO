import datetime as date
import shutil
import os
import inspect
import os.path
import colorama

colorama.init()

class LogTypes():
    info = "INFO"
    warning = "WARNING"
    
    CEND      = '\33[0m' #CEND      = '\33[0m' for Terminal Only
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

class Logger(LogTypes):
    def __init__(self) -> None:
        time = date.datetime.now()
        self.posix_time = f"[{time.hour}:{time.minute}:{time.second}]"
        self.is_signature_loaded = False
    
    def log_to_console(self, log_level:str, message:str):
        caller_filename_full = inspect.stack()[1].filename
        caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]
        file_location = f"{os.environ['APPDATA']}\\Ellohim External\\Ellohim Log.log"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        time = date.datetime.now()
        file = open(file_location,"a")
        
        file.write(f"[{time.hour}:{time.minute}:{time.second}] [{log_level}] [{caller_filename_only}.pyc:{inspect.stack()[1][2]}:{inspect.stack()[1][3]}] {message} \n")
        match log_level:
            case self.info:
                print(f"{self.CGREEN2}[{time.hour}:{time.minute}:{time.second}] {message}{self.CEND}")
            case self.warning:
                print(f"{self.CRED2}[{time.hour}:{time.minute}:{time.second}] {message}{self.CEND}")
        
        file.close()

    def logger(self, message:str):
        print(f"{self.CGREEN2}{self.posix_time} {message}{self.CEND}")

    def log_to_file(self, message:str):
        caller_filename_full = inspect.stack()[1].filename
        caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]
        file_location = f"{os.environ['APPDATA']}\\Ellohim External\\Ellohim Log.log"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        time = date.datetime.now()
        file = open(file_location,"a")
        
        file.write(f"[{time.hour}:{time.minute}:{time.second}] [LOG FILE] [{caller_filename_only}.pyc:{inspect.stack()[1][2]}:{inspect.stack()[1][3]}] {message} \n")
        file.close() 

    def clean_log_file(self):
        file_location = f"{os.environ['APPDATA']}\\Ellohim External\\Ellohim Log.log"
        open(file_location,"w").close()

    def copy_file(self, src, dst):
        shutil.copyfile(src, dst)

    def rename_file(self, scr, dst):
        os.rename(scr, dst)

g_logger = Logger()