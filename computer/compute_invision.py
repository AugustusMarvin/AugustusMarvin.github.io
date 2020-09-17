import tkinter as tk
from setting import Settings
def run_compute():
    ai_setting = Settings()
    window = tk.Tk()
    window.title(ai_setting.title_1)
    window.geometry(ai_setting.geo)
    one = tk.Button(window, text="1", command = lambda: onClick("1"))
    window.mainloop()
def onClick(key):
    global expstr #全局变量
    if key == "=":
        result_1 = round(eval(expstr), 2) #结果保留两位小数
        result["text"] = result_1
expstr = ""
history_label_obj_list = []
run_compute()