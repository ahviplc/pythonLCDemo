import dearpygui.dearpygui as dpg

"""
> Dear PyGui: A fast and powerful Graphical User Interface Toolkit for Python with minimal dependencies

https://github.com/hoffstadt/DearPyGui

https://hub.fastgit.org/hoffstadt/DearPyGui

https://github1s.com/hoffstadt/DearPyGui

https://hub.fastgit.org/hoffstadt/DearPyGui/wiki

https://hub.fastgit.org/Pcothren/DearPyGui-Examples
"""
dpg.show_style_editor()

def save_callback(sender, app_data, user_data):
    print(dpg)
    print("Save Clicked")
    for i in dpg.get_all_items():
        print(i)
    print(sender, app_data, user_data, dpg.get_value(2))
    print(sender, app_data, user_data, dpg.get_value(3))
    print(sender, app_data, user_data, dpg.get_value(4))
    print(sender, app_data, user_data, dpg.get_value(21))


with dpg.window(id=0, label="Example Window By LC", width=500, height=500):
    dpg.add_text(id=1, label="Hello world Hello LC", show_label=True)
    # label – 覆盖“name”作为标签。
    # id – 用于以编程方式引用项目的唯一 id。如果标签未使用，这将是标签
    text_input = dpg.add_input_text(id=2, label="MyInput")
    text_slider = dpg.add_slider_float(id=3, label="MySlider")
    text_input2 = dpg.add_input_text(id=4, label="name", default_value="LC")
    dpg.add_button(id=5, label="Save", callback=save_callback, user_data=text_input)

dpg.setup_viewport()
dpg.start_dearpygui()
