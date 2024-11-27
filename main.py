"""
Author: Stanley ZHAO (赵禹惟)
Date Created: 2024-11-27
Description: 这是一个硬件检测专家系统, 用于模拟数理逻辑在专家系统中的应用。
"""

import json as js
import tkinter as tk
from tkinter import messagebox
from inference_engine import inference_engine


def load_knowledge_base(file_path):
    """
    加载知识库文件。读取指定的JSON文件，并将其内容加载到Python字典中。
    如果文件路径无效或文件格式不正确，则会引发适当的错误。

    :param file_path:
        file_path (str): Path to the knowledge base file

    :return knowledge_base:
        dict: The knowledge base content parsed from the JSON file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        knowledge_base = js.load(file)
    return knowledge_base


class ExpertSystemApp:
    def __init__(self, root):
        """
        初始化硬件诊断专家系统的图形用户界面。设置窗口标题、大小并加载知识库。

        :param root:
            root (tk.Tk): tkinter main window instance
        """
        self.root = root
        self.root.title("硬件检测专家系统 Verson1.0")
        self.root.geometry("280x400")
        self.center_window()
        self.knowledge_base = load_knowledge_base("./knowledge_base.json")

        self.create_widgets()

    def center_window(self):
        """
        计算屏幕大小并使窗口居中。这个方法用于调整应用程序窗口出现在屏幕中心的位置。
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 280
        window_height = 400
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        self.root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    def create_widgets(self):
        """
        创建应用程序的图形界面组件，包括标题、症状复选框、推断按钮和结果显示区域。
        """
        title_label = tk.Label(self.root, text="硬件检测专家系统", font=("微软雅黑", 20, "bold"), background="aqua", width=250, height=2)
        title_label.pack(pady=10)

        self.conditions = self.knowledge_base.get("conditions", [])
        self.check_vars = {}

        for condition in self.conditions:
            var = tk.BooleanVar()
            check_button = tk.Checkbutton(self.root, text=condition, variable=var)
            check_button.pack(anchor="w")
            self.check_vars[condition] = var

        infer_button = tk.Button(self.root, text="推理", command=self.infer)
        infer_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def infer(self):
        """
        根据用户选择的症状执行推断。检查用户选择的条件，并使用推理引擎推断出结论。
        如果没有选择条件，则提示用户选择条件。
        """
        user_facts = [condition for condition, var in self.check_vars.items() if
                      var.get()]

        if not user_facts:
            messagebox.showwarning("输入错误", "请选择可选项")
            return

        conclusion = inference_engine(self.knowledge_base, user_facts)
        self.result_label.config(text=f"推理结果:\n{conclusion}")


if __name__ == "__main__":
    """
    程序的入口点，启动GUI应用程序。创建tkinter主窗口并运行应用程序。
    """
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()