import pattern_scanner as scanner
from logger import g_logger

class Pointers():
    def __init__(self) -> None:
        self.glow_manager = scanner.pattern_scan("client.dll", "Glow Object Mgr", "A1 ? ? ? ? A8 01 75 4B").add(25).count(0).scan()
        self.dwEntityList = scanner.pattern_scan("client.dll", "Entity", "BB ? ? ? ? 83 FF 01 0F 8C ? ? ? ? 3B F8").add(1).scan()
        self.dwLocalPlayer = scanner.pattern_scan("client.dll", "Local Player", "55 8B EC A1 ? ? ? ? 83 EC 18 57").add(4).scan()
        self.dwForceAttack = scanner.pattern_scan("client.dll", "ForceAttack", "89 0D ? ? ? ? 8B 0D ? ? ? ? 8B F2 8B C1 83 CE 04").add(2).scan()
        self.dwClientState = scanner.pattern_scan("engine.dll", "Client State", "A1 ? ? ? ? ? ? ? ? 00 00 C3 CC CC CC CC 55 8B EC 8A 45").add(1).count(0).scan()#"A2 ? ? ? ? ? ? ? ? CC A0" sub 0x16/22
        self.dwClientState_GetLocalPlayer  = scanner.pattern_scan("engine.dll", "Get Local Player", "8B 80 ? ? ? ? 40 C3").add(0).count(2).scan()
        self.dwInput = scanner.pattern_scan("client.dll", "Input", "B9 ? ? ? ? F3 0F 11 04 24 FF 50 10").add(0).count(1).scan()
        self.clientstate_net_channel = scanner.pattern_scan("engine.dll", "Net Channel", "8B 8F ? ? ? ? 8B 01 8B 40 18").add(0).count(2).scan()
        self.clientstate_last_outgoing_command = scanner.pattern_scan("engine.dll", "Last Outgoing Command", "8B 8F ? ? ? ? 8B 87 ? ? ? ? 41").add(0).count(2).scan()
        self.dwbSendPackets = scanner.pattern_scan("engine.dll", "Send Packets", "B3 01 8B 01 8B 40 10 FF D0 84 C0 74 0F 80 BF ? ? ? ? ? 0F 84").add(0).scan()
        self.dwClientState_ViewAngles = 19856
        g_logger.logger("Pointer Initialized")
g_pointers = Pointers()
