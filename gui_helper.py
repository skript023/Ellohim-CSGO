import dearpygui.dearpygui as imgui

class GuiHelper():
    def hide_vp(self):
        imgui.minimize_viewport()
        return False

    def drag_viewport(self):
        drag_deltas = imgui.get_mouse_drag_delta()
        viewport_current_pos = imgui.get_viewport_pos()
        if imgui.is_item_hovered("Primary Window"):
            imgui.set_viewport_pos([viewport_current_pos[0] + drag_deltas[0],viewport_current_pos[1] + drag_deltas[1]])

g_gui = GuiHelper()