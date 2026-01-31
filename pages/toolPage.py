import customtkinter as ctk

class ToolPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="TOOL")
        self.label.pack(anchor="center")
        self.label.pack_propagate(False)