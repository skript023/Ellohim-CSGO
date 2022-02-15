import dearpygui.dearpygui as dpg
import features as option

class event_loop:
    def game_func(activate):
        if activate:
            option.player_esp(dpg.get_value("esp"))
            option.no_flash(dpg.get_value("remove_flash"))
            option.trigger_bot(dpg.get_value("trigger_bot"))
            option.skin_changer(dpg.get_value("force_skin"))