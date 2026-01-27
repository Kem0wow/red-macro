import tkinter as tk
from tkinter import ttk

class GatherPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fields = [
            "None", "Sunflower", "Dandelion", "Mushroom", "Blue Flower", "Clover",
            "Strawberry", "Spider", "Bamboo", "Pineapple", "Stump", "Cactus",
            "Pumpkin", "Pine Tree", "Rose", "Mountain Top", "Pepper", "Coconut"
        ]
        self.patterns = ["e_lol", "XSnake", "ZigZag"]
        self.hive_travel_options = ["Walk", "Reset"]
        
        self.clipboard = None
        self.copy_indicators = []

        self.pack(fill="x", padx=10, pady=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(4, weight=1)

        # ================= TITLES =================
        tk.Label(self, text="Gather (Field Rotation)", font=("Arial", 10, "bold"))\
            .grid(row=0, column=0)

        ttk.Separator(self, orient="vertical").grid(row=0, column=1, sticky="ns", padx=6)

        tk.Label(self, text="Pattern", font=("Arial", 10, "bold"))\
            .grid(row=0, column=2)

        ttk.Separator(self, orient="vertical").grid(row=0, column=3, sticky="ns", padx=6)

        tk.Label(self, text="Until Stop (time/pack)", font=("Arial", 10, "bold"))\
            .grid(row=0, column=4)

        ttk.Separator(self, orient="horizontal")\
            .grid(row=1, column=0, columnspan=5, sticky="ew", pady=6)

        # Row 1
        self.create_gather_row(2, "1:")
        
        ttk.Separator(self, orient="horizontal")\
            .grid(row=3, column=0, columnspan=5, sticky="ew", pady=6)
        
        # Row 2
        self.create_gather_row(4, "2:")
        
        ttk.Separator(self, orient="horizontal")\
            .grid(row=5, column=0, columnspan=5, sticky="ew", pady=6)
        
        # Row 3
        self.create_gather_row(6, "3:")
        
        ttk.Separator(self, orient="horizontal")\
            .grid(row=7, column=0, columnspan=5, sticky="ew", pady=6)

        control_frame = tk.Frame(self)
        control_frame.grid(row=8, column=0, columnspan=5, sticky="ew", pady=(0, 10))
        control_frame.columnconfigure(4, weight=1)

        start_btn = ttk.Button(control_frame,
                               text="Start [F1]", width=10)
        start_btn.grid(row=0, column=0, padx=5, sticky="w")

        pause_btn = ttk.Button(control_frame,
                               text="Pause [F2]", width=10)
        pause_btn.grid(row=0, column=1, padx=5, sticky="w")

        stop_btn = ttk.Button(control_frame,
                              text="Stop [F3]", width=10)
        stop_btn.grid(row=0, column=2, padx=5, sticky="w")

        hive_num_lbl = tk.Label(
            control_frame,
            text="Hive (from left): ",
            font=("Arial", 9)
        )
        hive_num_lbl.grid(row=0, column=3, padx=5, sticky="w")

        self.hive_num_var = tk.IntVar(value=1)
        hive_num_spin = ttk.Spinbox(
            control_frame,
            from_=1,
            to=6,
            width=3,
            textvariable=self.hive_num_var,
            state="readonly"
        )
        hive_num_spin.grid(row=0, column=4, padx=5, sticky="w")

        version_lbl = tk.Label(
            control_frame,
            text="v1.0",
            font=("Arial", 10)
        )
        version_lbl.grid(row=0, column=6, padx=5, sticky="e")

        try:
            from PIL import Image, ImageTk
            github_pil = Image.open("icons/github.png")
            github_pil = github_pil.resize((27, 27), Image.Resampling.LANCZOS)
            github_img = ImageTk.PhotoImage(github_pil)
            github_label = tk.Label(control_frame, image=github_img, cursor="hand2", bg=self.cget("bg"))
            github_label.image = github_img
            github_label.grid(row=0, column=5, padx=5, sticky="e")
            github_label.bind("<Button-1>", lambda e: self.open_github())
        except:
            pass

    def create_gather_row(self, row, label_text):
        # ================= GATHER =================
        gather_frame = tk.Frame(self)
        gather_frame.grid(row=row, column=0, sticky="nw")

        g_top = tk.Frame(gather_frame)
        g_top.pack(anchor="w")

        tk.Label(g_top, text=label_text, font=("Arial", 10, "bold"))\
            .pack(side="left", padx=(0, 4))

        field_combo = ttk.Combobox(
            g_top,
            values=self.fields,
            state="readonly",
            width=17
        )
        field_combo.pack(side="left")

        g_bottom = tk.Frame(gather_frame)
        g_bottom.pack(anchor="w", pady=(2, 0))

        copy_indicator = tk.Label(
            g_bottom, 
            text="●", 
            font=("Arial", 12),
            fg="gray"
        )
        copy_indicator.pack(side="left", padx=(0, 2))
        self.copy_indicators.append(copy_indicator)
        
        row_index = len(self.copy_indicators) - 1

        ttk.Button(g_bottom, text="Copy", width=6, 
                   command=lambda idx=row_index: self.copy_settings(
                       idx, field_combo, pattern_combo, 
                       shift_check, until_entry, 
                       pack_spin, hive_combo))\
            .pack(side="left", padx=(0, 4))
        ttk.Button(g_bottom, text="Paste", width=6,
                   command=lambda: self.paste_settings(field_combo, pattern_combo,
                                                       shift_check, until_entry,
                                                       pack_spin, hive_combo))\
            .pack(side="left")

        ttk.Separator(self, orient="vertical")\
            .grid(row=row, column=1, sticky="ns", padx=6)

        # ================= PATTERN =================
        pattern_frame = tk.Frame(self)
        pattern_frame.grid(row=row, column=2, sticky="nw")

        pattern_combo = ttk.Combobox(
            pattern_frame,
            values=self.patterns,
            state="readonly",
            width=17
        )
        pattern_combo.pack(anchor="w")

        shift_var = tk.BooleanVar(value=False)
        shift_check = tk.Checkbutton(
            pattern_frame,
            text="Gather w/Shift Lock",
            variable=shift_var
        )
        shift_check.pack(anchor="w", pady=(2, 0))
        shift_check.var = shift_var

        ttk.Separator(self, orient="vertical")\
            .grid(row=row, column=3, sticky="ns", padx=6)

        # ================= UNTIL =================
        until_frame = tk.Frame(self)
        until_frame.grid(row=row, column=4, sticky="nw")

        until_var = tk.IntVar(value=0)
        pack_var = tk.IntVar(value=75)

        until_top = tk.Frame(until_frame)
        until_top.pack(anchor="w")

        vcmd = (self.register(self.validate_3_digit), "%P")

        until_entry = tk.Entry(
            until_top,
            width=4,
            textvariable=until_var,
            validate="key",
            validatecommand=vcmd
        )
        until_entry.pack(side="left", padx=(0, 4))

        tk.Label(until_top, text="mins / pack %")\
            .pack(side="left", padx=(0, 6))

        pack_spin = ttk.Spinbox(
            until_top,
            from_=30,
            to=100,
            increment=5,
            width=3,
            textvariable=pack_var,
            state="readonly"
        )
        pack_spin.pack(side="left")
        
        until_bottom = tk.Frame(until_frame)
        until_bottom.pack(anchor="w", pady=(2, 0))

        tk.Label(until_bottom, text="To Hive By:")\
            .pack(side="left", padx=(0, 4))

        hive_combo = ttk.Combobox(
            until_bottom,
            values=self.hive_travel_options,
            state="readonly",
            width=7
        )
        hive_combo.pack(side="left")  

    def copy_settings(self, row_index, field_combo, pattern_combo, shift_check, 
                     until_entry, pack_spin, hive_combo):
        self.clipboard = {
            'field': field_combo.get(),
            'pattern': pattern_combo.get(),
            'shift': shift_check.var.get(),
            'until': until_entry.get(),
            'pack': pack_spin.get(),
            'hive': hive_combo.get(),
            'source_row': row_index
        }
        
        for indicator in self.copy_indicators:
            indicator.config(fg="gray")
        
        self.copy_indicators[row_index].config(fg="dodgerblue")
        
    def paste_settings(self, field_combo, pattern_combo, shift_check,
                      until_entry, pack_spin, hive_combo):
        if hasattr(self, 'clipboard') and self.clipboard is not None:
            if self.clipboard['field']:
                field_combo.set(self.clipboard['field'])
            if self.clipboard['pattern']:
                pattern_combo.set(self.clipboard['pattern'])
            shift_check.var.set(self.clipboard['shift'])
            until_entry.delete(0, tk.END)
            until_entry.insert(0, self.clipboard['until'])
            pack_spin.set(self.clipboard['pack'])
            if self.clipboard['hive']:
                hive_combo.set(self.clipboard['hive'])

    def validate_3_digit(self, value):
        if value == "":
            return True
        return value.isdigit() and len(value) <= 3

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/Kem0wow/bss-macro")