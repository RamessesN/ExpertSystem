"""
Author: Stanley ZHAO (Yuwei ZHAO)
Date Created: 2024-11-27
Description: This is a hardware detection expert system used to simulate the application of mathematical logic in expert system.
"""

import json as js
import tkinter as tk
from tkinter import messagebox
from inference_engine import inference_engine


def load_knowledge_base(file_path):
    """
    Load the knowledge base file. Reads the specified JSON file and loads its contents into a Python dictionary.
    If the file path is invalid or the file format is incorrect, an appropriate error is raised.

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
        Initialize the graphical user interface of the hardware diagnostic expert system.
        Set the window title, size, and load the knowledge base.

        :param root:
            root (tk.Tk): tkinter main window instance
        """
        self.root = root
        self.root.title("Version 2.0")
        self.root.geometry("300x400")
        self.center_window()
        self.knowledge_base = load_knowledge_base("./knowledge_base.json")

        self.create_widgets()

    def center_window(self):
        """
        Calculate the screen size and center the window. This method adjusts the position of the application window
        at the center of the screen.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 300
        window_height = 400
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        self.root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    def create_widgets(self):
        """
        Create the graphical interface components of the application, including a title, a symptom checkbox,
        an inference button, and a result display area.
        """
        title_label = tk.Label(self.root, text="Hardware Diagnose System", font=("微软雅黑", 20, "bold"), background="aqua", width=250, height=2)
        title_label.pack(pady=10)

        self.conditions = self.knowledge_base.get("conditions", [])
        self.check_vars = {}

        for condition in self.conditions:
            var = tk.BooleanVar()
            check_button = tk.Checkbutton(self.root, text=condition, variable=var)
            check_button.pack(anchor="w")
            self.check_vars[condition] = var

        infer_button = tk.Button(self.root, text="Infer", command=self.infer)
        infer_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def infer(self):
        """
        Inference is performed based on the symptoms selected by the user. The conditions selected by the user are
        examined and the inference engine is used to infer the conclusion.
        If no condition is selected, the user has to select again.
        """
        user_facts = [condition for condition, var in self.check_vars.items() if
                      var.get()]

        if not user_facts:
            messagebox.showwarning("Input error", "Please show alternative options")
            return

        conclusion = inference_engine(self.knowledge_base, user_facts)
        self.result_label.config(text=f"Inference Result:\n{conclusion}")


if __name__ == "__main__":
    """
    Program entry to start the GUI application. Create the main tkinter window and run the application.
    """
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()