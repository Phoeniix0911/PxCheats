__author__ = 'Phoeniix / https://github.com/Phoeniix0911'
__version__ = '1.0.0'

import pymem
import pymem.process
import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import re, os, threading, winsound, ctypes, time
from offsets import *
from memory import *
from gui import *
from local import *
from ctypes import *
from enum import IntEnum
from entity import *

def Glow_ESP():
    while True:
        try:
            if dpg.get_value('Glow_ESP'):
                glow_manager = game_handle.read_int(client_dll + dwGlowObjectManager)

            for i in range(1, 32):
                entity = game_handle.read_int(client_dll + dwEntityList + i * 0x10)

                if entity:
                    entity_team_id = game_handle.read_int(entity + m_iTeamNum)
                    entity_glow = game_handle.read_int(entity + m_iGlowIndex)

                    if entity_team_id == 3:
                        game_handle.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))
                        game_handle.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                        game_handle.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))
                        game_handle.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
                        game_handle.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

        except Exception as err:
            pass
        time.sleep(0.1)

def Radar_Hack():
    while True:
        try:
            if dpg.get_value('Radar_Hack') and ent.in_game():
                for entity in ent.entity_list:
                    if entity[2] == 40:
                        ent.set_is_visible(entity[1], True)
        except Exception as err:
            pass
        time.sleep(0.1)

def Bunny_Hop():
    while True:
        try:
            if dpg.get_value('Bunny_Hop') and lp.get_current_state() == 5:
                while ctypes.windll.user32.GetAsyncKeyState(0x20):
                    if ent.get_flag(lp.local_player()) == 257:
                        lp.force_jump(5)
                        time.sleep(0.01)
                    else:
                        lp.force_jump(4)
                        time.sleep(0.01)
        except Exception as err:
            pass
        time.sleep(0.001)

def No_Flash():
    temp = 0
    while True:
        try:
            if dpg.get_value('No_Flash') and ent.in_game():
                if lp.get_flashbang_duration() > 0:
                    lp.set_flashbang_alpha(dpg.get_value('noflash_strength'))
                    temp = dpg.get_value('noflash_strength')
            elif dpg.get_value('No_Flash') == False and temp != 255.0:
                lp.set_flashbang_alpha(255.0)
        except Exception as err:
            pass
        time.sleep(0.1)

def start_threads():
    try:
        window.menu()
        threading.Thread(target=Glow_ESP, name='Glow_ESP').start()
        threading.Thread(target=Radar_Hack, name='Radar_Hack').start()
        threading.Thread(target=Bunny_Hop, name='Bunny_Hop').start()
        threading.Thread(target=No_Flash, name='No_Flash').start()

    except Exception as err:
        print(f'Threads have been canceled! Exiting...\nReason: {err}\nExiting...')
        os._exit(0)

if __name__ == '__main__':
    try:
        print(f'By: {__author__}\nVersion: {__version__}')
        mem = Memory(game_handle, client_dll, client_dll_size, engine_dll)
        window = GUI()
        lp = LocalPlayer(mem)
        ent = Entity(mem)
        start_threads()
        dpg.start_dearpygui()
    except (Exception, KeyboardInterrupt) as err:
        print(f'Failed to initialize!\nReason: {err}\nExiting...')
        os._exit(0)