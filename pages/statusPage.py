import tkinter as tk


class StatusPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        group = tk.LabelFrame(self, text="Status Information", padx=10, pady=10)
        group.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Checkbutton(group, text="Auto Restart on Failure").pack(anchor="w")
        tk.Checkbutton(group, text="Show Notifications").pack(anchor="w")
