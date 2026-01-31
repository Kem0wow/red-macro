import customtkinter as ctk

class CollectPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="COLLECT")
        self.label.pack(anchor="center")
        self.label.pack_propagate(False)