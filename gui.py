import dearpygui.dearpygui as dpg
import sys
from gui_helper import g_gui, Timer
from utility import is_window_exist, set_window_transparent
from logger import g_logger
from os import system
from win32api import GetAsyncKeyState
from event_loop import event_loop

def main():
    g_logger.log_to_console(g_logger.info, "Renderer initialized")
    dpg.create_context()
    with dpg.font_registry():
        dpg.add_font("fonts/Rubik.ttf", 16, tag="fira_code")
        dpg.bind_font("fira_code")

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 10, 10, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 10, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 6, 6, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 0, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_IndentSpacing, 21, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 15, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 8, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)
            
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (15, 15, 15, 229), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (20, 20, 20, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Border, (76, 76, 76, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (53, 53, 53, 138), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (71, 71, 71, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (71, 71, 71, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (43, 43, 43, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (48, 48, 48, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (35, 35, 35, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (5, 5, 5, 135), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (0, 0, 0, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (79, 79, 79, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (104, 104, 104, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (86, 86, 86, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (99, 96, 96, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (104, 104, 104, 188), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (114, 114, 114, 211), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (114, 114, 114, 198), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Header, (94, 93, 93, 79), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Separator, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Tab, (60, 60, 60, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (100, 100, 100, 255), category=dpg.mvThemeCat_Core)

    with dpg.window(tag="Primary Window", label="Ellohim CSGO", width=600, height=400, no_move=True, min_size=[250,250], no_collapse=True, on_close=lambda:sys.exit(0)):
        with dpg.handler_registry():
            dpg.add_mouse_drag_handler(callback=g_gui.drag_viewport)
        with dpg.tab_bar(label="Tabbar"):
            with dpg.tab(label="Player"):
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(label="Glow ESP", tag="esp")
                    dpg.add_checkbox(label="No Flash", tag="remove_flash")
                    dpg.add_checkbox(label="Trigger Bot", tag="trigget_bot")
                    dpg.add_checkbox(label="Aimbot", tag="aimbot")
                
            with dpg.tab(label="Skin Changer"):
                dpg.add_combo(label="Skin List")
    dpg.bind_theme(global_theme)
    vp = dpg.create_viewport(title='Ellohim CSGO External', small_icon="fonts/Ellohim.ico", width=600, height=400, always_on_top=True, decorated=False, clear_color=(37.0, 37.0, 38.0, 100.0))
    dpg.setup_dearpygui()
    dpg.show_viewport()

    timer = Timer(0.1)

    while dpg.is_dearpygui_running():
        if is_window_exist("Counter-Strike: Global Offensive"):
            #Option
            event_loop.game_func(timer.update())

        if GetAsyncKeyState(0x2D)&0x1: g_gui.m_opened = not g_gui.m_opened
        if g_gui.m_opened:g_gui.show_vp()
        if not g_gui.m_opened:g_gui.hide_vp()

        if not is_window_exist("Counter-Strike: Global Offensive"): sys.exit(0)
        window_width = dpg.get_item_width("Primary Window")
        window_height = dpg.get_item_height("Primary Window")
        dpg.set_viewport_height(window_height)
        dpg.set_viewport_width(window_width)
        set_window_transparent("Ellohim CSGO External", 229)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    try:
        main()
    except Exception as er:
        g_gui.hide_vp()
        g_logger.log_to_console(g_logger.warning, "Renderer Failed To Start")
        g_logger.log_to_console(g_logger.warning, f"Reason : {er}")
        dpg.stop_dearpygui()
        system("pause")