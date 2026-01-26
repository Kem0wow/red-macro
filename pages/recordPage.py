import tkinter as tk


class RecordPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(
            self,
            text="Record Page",
            font=("Arial", 18)
        )
        label.pack(pady=20)
