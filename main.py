import tkinter as tk
import tkinter.ttk as ttk

from pages.recordPage import RecordPage
from pages.settingPage import SettingsPage
from pages.statusPage import StatusPage
from pages.collectPage import CollectPage
from pages.gatherPage import GatherPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bee Swarm Macro")
        self.geometry("500x280")
        self.resizable(False, False)

        # Tab sistemi
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Sayfalar
        self.record_page = RecordPage(self.notebook)
        self.settings_page = SettingsPage(self.notebook)
        self.status_page = StatusPage(self.notebook)
        self.collect_page = CollectPage(self.notebook)
        self.gather_page = GatherPage(self.notebook)

        # Tab ekleme
        self.notebook.add(self.gather_page, text="Gather")
        self.notebook.add(self.collect_page, text="Collect")
        self.notebook.add(self.status_page, text="Status")
        self.notebook.add(self.settings_page, text="Settings")
        self.notebook.add(self.record_page, text="Record (Dev Panel)")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()