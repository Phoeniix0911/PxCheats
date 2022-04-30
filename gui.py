import dearpygui.dearpygui as dpg
import random, win32gui

class GUI():
    def __init__(self) -> None:
        self.v1 = self.get_random_string()
        
    def get_random_string(self) -> None:
        strings = ['A',
        'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'U', 'P', 'R', 'S', 'T', 'W', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'u', 'p', 'r', 's', 't', 'w', 'y', 'z',
        '1','2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '&', '(', ')', '-', '_', '=', '+']
        return ''.join(random.choice(strings) for _ in range(10, 15))
    
    def _log(self, sender, app_data, user_data):
        print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    
    def menu(self):
        dpg.create_context()
        dpg.create_viewport(title=self.v1, width=416, height=300)
        dpg.setup_dearpygui()

        with dpg.window(label='Menu', user_data='menu', tag='#menu', width=400, height=300, no_close=True, no_move=True):
            dpg.add_checkbox(label='Glow ESP', user_data='Glow_ESP', tag='Glow_ESP')
            dpg.add_checkbox(label='Bunny Hop', user_data='Bunny_Hop', tag='Bunny_Hop')
            dpg.add_checkbox(label='No Flash', user_data='No_Flash', tag='No_Flash')
            dpg.add_slider_float(label='No Flash strength', default_value=255.0, min_value=0.0, max_value=255.0, user_data='noflash_strength', tag='noflash_strength')

        dpg.show_viewport()
