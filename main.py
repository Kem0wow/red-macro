import customtkinter as ctk
import ctypes
import os
import webbrowser

from pages.gatherPage import GatherPage
from pages.collectPage import CollectPage
from pages.statusPage import StatusPage
from pages.toolPage import ToolPage
from pages.settingPage import SettingPage
from pages.imgBtn import ImageButton

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

appid = "precise.macro.app"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Precision Macro")
        self.resizable(False, False)
        self.iconbitmap("./icons/logov2.ico")

        # ==== TOP BAR ====
        self.topbar = ctk.CTkFrame(self, height=40, fg_color="#1e1e1e")
        self.topbar.pack(fill="x", side="top")
        # ==== TOP BAR ====

        # ==== CONTENT ====
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True)
        # ==== CONTENT ====

        # ==== BOT BAR ====
        self.botbar = ctk.CTkFrame(self, height=80, fg_color="#1e1e1e")
        self.botbar.pack(fill="x", side="bottom")
        # ==== BOT BAR ====

        # ==== PAGES ====
        self.pages = {
            "Gather": GatherPage(self.content),
            "Collect": CollectPage(self.content),
            "Status": StatusPage(self.content),
            "Tools": ToolPage(self.content),
            "Settings": SettingPage(self.content),
        }

        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)
        # ==== PAGES ====

        # ==== TOP BAR ELEMENTS ====
        self.buttons = {}

        for name in self.pages:
            self.container = ctk.CTkFrame(
                self.topbar,
                width=120,
                height=40,
                fg_color="transparent"
            )
            self.container.pack(side="left")
            self.container.pack_propagate(False)

            self.btn = ctk.CTkButton(
                self.container,
                text=name,
                width=115,
                height=40,
                corner_radius=6,
                fg_color="transparent",
                hover=False,
                border_color="#727272",
                border_width=1,
                command=lambda n=name: self.show_page(n)
            )
            self.btn.pack(side="top")

            self.buttons[name] = self.btn
        # ==== TOP BAR ELEMENTS ====

        # === BOT BAR ELEMENTS ===
        self.stat_lbl = ctk.CTkLabel(
            self.botbar,
            text="Status:",
            font=("Arial", 20, "bold")
        )
        self.stat_lbl.place(x=10, y=5)

        self.stat_val_lbl = ctk.CTkLabel(
            self.botbar,
            text="Ready",
            font=("Arial", 20),
            text_color="#B2B2B2"
        )
        self.stat_val_lbl.place(x=360, y=5, anchor="ne")

        self.start_btn = ImageButton(
            self.botbar,
            image_path="./icons/start.png",
            width=100,
            height=30,
            image_height=16,
            image_width=16,
            text="START [F1]",
            command=lambda: print("START")
        )
        self.start_btn.place(x=10, y=39)

        self.pause_btn = ImageButton(
            self.botbar,
            image_path="./icons/pause.png",
            width=100,
            height=30,
            image_height=16,
            image_width=16,
            text="PAUSE [F2]",
            command=lambda: print("PAUSE")
        )
        self.pause_btn.place(x=135, y=39)

        self.stop_btn = ImageButton(
            self.botbar,
            image_path="./icons/stop.png",
            width=100,
            height=30,
            image_height=16,
            image_width=16,
            text="STOP [F3]",
            command=lambda: print("STOP")
        )
        self.stop_btn.place(x=259, y=39)

        self.spacer = ctk.CTkFrame(
            self.botbar,
            fg_color="white",
            width=3,
            height=60
        )
        self.spacer.place(x=380, y=10)

        self.github = ImageButton(
            self.botbar,
            image_path="./icons/github.png",
            width=50,
            height=50,
            fg_color="transparent",
            hover=False,
            image_height=40,
            image_width=40,
            text="",
            command=lambda: webbrowser.open("https://github.com/Kem0wow/precision-macro")           
        )
        self.github.place(x=550, y=35)

        # === BOT BAR ELEMENTS ===

        self.show_page("Gather")


    def show_page(self, name):
        for page in self.pages.values():
            page.lower()
        self.pages[name].lift()

        for btn in self.buttons.values():
            btn.configure(fg_color="transparent")

        self.buttons[name].configure(fg_color="#333333")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()