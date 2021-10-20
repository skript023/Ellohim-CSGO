from pattern_scanner import pm
from pointers import g_pointers
import memory
import keyboard
import time
from win32gui import GetWindowText, GetForegroundWindow
from offset_helper import g_offset

mm = memory.Memory()

def player_esp(activate:bool):
    if activate:
        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(g_pointers.dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + g_offset.m_iTeamNum)
                entity_glow = pm.read_int(entity + g_offset.m_iGlowIndex)
                
                if entity_team_id == 2:  # Terrorist
                    #print(hex(glow_manager + entity_glow * 0x38 + 0x28))
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x10, float(0))   # B
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(g_pointers.glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    #print(hex(glow_manager + entity_glow * 0x38 + 0x28))
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x10, float(1))   # B
                    pm.write_float(g_pointers.glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(g_pointers.glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

def no_flash(activate:bool):
    if activate:
        player = pm.read_int(g_pointers.dwLocalPlayer-0x654)
        if player:
            flash_value = player + g_offset.m_flFlashMaxAlpha
            if flash_value:
                pm.write_float(flash_value, float(0))

def trigger_bot(activate:bool):
    if activate:
        trigger_key = "shift"
        # if not keyboard.is_pressed(trigger_key):
        #         time.sleep(0.1)

        # if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
        #     return

        #if keyboard.is_pressed(trigger_key):
        player = pm.read_int(g_pointers.dwLocalPlayer)
        entity_id = pm.read_int(player + g_offset.m_iCrosshairId)
        entity = pm.read_int(g_pointers.dwEntityList + (entity_id - 1) * 0x10)

        entity_team = pm.read_int(entity + g_offset.m_iTeamNum)
        player_team = pm.read_int(player + g_offset.m_iTeamNum)

        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
            pm.write_int(g_pointers.dwForceAttack, 6)

            #time.sleep(0.006)
def force_full_update():
    pm.write_int(g_pointers.dwClientState + 0x174, -1)
    

def skin_changer(activate:bool):
    if activate:
        weapon_id_previous = 0
        weapon_id_previous_2 = 0
        once = False
        for i in range(64):
            Player = pm.read_uint(g_pointers.dwLocalPlayer)
            weapon_index = pm.read_uint(Player + g_offset.m_hActiveWeapon + i * 0x4) & 0xFFF
            weapon_entity = pm.read_uint(g_pointers.dwEntityList + (weapon_index - 0x1) * 0x10)
            if weapon_entity:
                weapon_id = pm.read_int(weapon_entity + g_offset.m_iItemDefinitionIndex)
                # weapon_account_id = pm.read_int(weapon_entity + g_offset.m_iAccountID)
                # my_account_id = pm.read_uint(weapon_entity + g_offset.m_OriginalOwnerXuidLow)

                if weapon_id != weapon_id_previous and not once:
                    weapon_id_previous = weapon_id
                    force_full_update()
                    once = True
                
                if weapon_id != weapon_id_previous_2:
                    weapon_id_previous_2 = weapon_id
                    force_full_update()

                pm.write_int(weapon_entity + g_offset.m_iItemIDLow, -1)
                pm.write_int(weapon_entity + g_offset.m_nFallbackPaintKit, 1)
                pm.write_int(weapon_entity + g_offset.m_nFallbackStatTrak, 1)
                pm.write_int(weapon_entity + g_offset.m_nFallbackSeed, 1)
                pm.write_float(weapon_entity + g_offset.m_flFallbackWear, 1.0)
                #pm.write_int(weapon_entity + g_offset.m_iAccountID, my_account_id)
