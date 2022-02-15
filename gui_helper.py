import dearpygui.dearpygui as dpg
from utility import show_minimized

class g_gui():
    m_opened = True
    def hide_vp():
        dpg.minimize_viewport()

    def show_vp():
        show_minimized("Ellohim CSGO External")

    def drag_viewport():
        drag_deltas = dpg.get_mouse_drag_delta()
        viewport_current_pos = dpg.get_viewport_pos()
        if dpg.is_item_hovered("Primary Window"):
            dpg.set_viewport_pos([viewport_current_pos[0] + drag_deltas[0],viewport_current_pos[1] + drag_deltas[1]])

class Timer:
    def __init__(self, interval):
        self.total_time = dpg.get_total_time()
        self.last_total_time = dpg.get_total_time()
        self.interval = interval

    def update(self):
        self.total_time = dpg.get_total_time()
        delta_time = dpg.get_total_time() - self.last_total_time
        if delta_time > self.interval:
            self.last_total_time = self.total_time
            return True
        return False