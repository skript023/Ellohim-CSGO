from utility import is_window_exist
from time import sleep
from pymem import Pymem
import pymem
from logger import g_logger

print(fr"""{g_logger.CGREEN2}
  _____  _____   _____  ____    ______      _                        _ 
 / ____|/ ____| / ____|/ __ \  |  ____|    | |                      | |
| |    | (___(_) |  __| |  | | | |__  __  _| |_ ___ _ __ _ __   __ _| |
| |     \___ \ | | |_ | |  | | |  __| \ \/ / __/ _ \ '__| '_ \ / _` | |
| |____ ____) || |__| | |__| | | |____ >  <| ||  __/ |  | | | | (_| | |
 \_____|_____(_)\_____|\____/  |______/_/\_\\__\___|_|  |_| |_|\__,_|_|
{g_logger.CEND}""")
g_logger.logger("Waiting Game Window")
while not is_window_exist("Counter-Strike: Global Offensive"):
    sleep(0)

pm = Pymem("csgo.exe")
g_logger.logger(f"Process id: {hex(pm.process_id).upper()} Process Handle : {str(pm.process_handle)}")

class pattern_scan():
    def __init__(self, module, name, signature) -> None:
        self.signature_scan(module, name, signature)

    def insert_string(self, string, str_to_insert, index) -> str:
        return string[:index] + str_to_insert + string[index:]

    def signature_scan(self, module:str, name:str, signature:str):
        self.target_module = module
        self.first = signature
        self.second = self.insert_string(self.first, r"\x", 0)
        self.third = self.second.replace(r" ", r"\x")
        self.final = self.third.replace(r"\x?", r".")
        base = pymem.process.module_from_name(pm.process_handle, module)#.lpBaseOfDll
        self.Pointer = pymem.pattern.pattern_scan_module(pm.process_handle, base, self.final.encode())
        self.SignatureName = name
        self.SigPattern = signature
        return self

    def add(self, offset):
        self.final_ptr = pm.read_uint(self.Pointer + offset)
        return self

    def sub(self, offset):
        self.final_ptr = pm.read_uint(self.Pointer - offset)
        return self

    def count(self, offset):
        self.final_ptr = pm.read_uint(self.final_ptr) + offset
        return self

    def scan(self):
        try:
            g_logger.logger(f"{self.SignatureName} : {self.target_module}+{hex(self.final_ptr-pm.base_address).upper()}")
            return self.final_ptr
        except Exception as e:
            g_logger.logger(e)