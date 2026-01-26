import tkinter as tk


class CollectPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(
            self,
            text="Collect Page",
            font=("Arial", 18)
        )
        label.pack(pady=20)
