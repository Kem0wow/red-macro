import tkinter as tk
import tkinter.ttk as ttk


class CollectPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ==================== Configuration ====================
        mondo_list = ["Kill", "Buff"]
        mondo_loot_list = ["Random", "Ignore"]
        ant_list = ["Pass", "Challenge"]

        # ==================== Collect Section ====================
        collect_group = tk.LabelFrame(self, text=" Collect ", font=("Arial", 10, "bold"), width=150)
        collect_group.pack(fill="y", padx=5, side="left")
        collect_group.pack_propagate(False)

        collect_frame = tk.Frame(collect_group)
        collect_frame.pack(fill="y", padx=5, pady=5)

        clock_check = tk.Checkbutton(collect_frame, text="Clock (tickets)", font=("Arial", 10))
        clock_check.grid(row=0, column=0, sticky="w")

        mondo_check = tk.Checkbutton(collect_frame, text="Mondo", font=("Arial", 10))
        mondo_check.grid(row=1, column=0, sticky="w")
        
        mondo_cbox = ttk.Combobox(collect_frame, values=mondo_list, state="readonly", width=5)
        mondo_cbox.set(mondo_list[0])
        mondo_cbox.grid(row=1, column=0, sticky="w", padx=81)

        mondo_loot_lbl = tk.Label(collect_frame, text="Loot:", font=("Arial", 10))
        mondo_loot_cbox = ttk.Combobox(collect_frame, values=mondo_loot_list, state="readonly", width=6)

        ant_check = tk.Checkbutton(
            collect_frame,
            text="Ant",
            font=("Arial", 10)
        )
        ant_check.grid(row=3, column=0, sticky="w")

        ant_cbox = ttk.Combobox(
            collect_frame,
            values=ant_list,
            state="readonly",
            width=9
        )
        ant_cbox.grid(row=3, column=0, sticky="w", padx=57)

        honeystrom_check = tk.Checkbutton(
            collect_frame,
            text="Honeystrom",
            font=("Arial", 10)
        )
        honeystrom_check.grid(row=4, column=0, sticky="w")

        memo_match_normal = tk.Checkbutton(collect_frame, text="Normal Memo", font=("Arial", 10))
        memo_match_normal.grid(row=5, column=0, sticky="w")

        memo_match_mega = tk.Checkbutton(collect_frame, text="Mega Memo", font=("Arial", 10))
        memo_match_mega.grid(row=6, column=0, sticky="w")

        memo_match_extreme = tk.Checkbutton(collect_frame, text="Extreme Memo", font=("Arial", 10))
        memo_match_extreme.grid(row=7, column=0, sticky="w")

        def toggle_loot_visibility(event=None):
            if mondo_cbox.get() == "Kill":
                mondo_loot_lbl.grid(row=2, column=0, sticky="w", padx=20)
                mondo_loot_cbox.grid(row=2, column=0, sticky="w", padx=75)
            else:
                mondo_loot_lbl.grid_forget()
                mondo_loot_cbox.grid_forget()

        mondo_cbox.bind("<<ComboboxSelected>>", toggle_loot_visibility)
        toggle_loot_visibility()  # Initial state

        # ==================== Beesmas Section ====================
        beesmas_group = tk.LabelFrame(self, text=" Beesmas ", font=("Arial", 10, "bold"), height=110)
        beesmas_group.pack(fill="x", pady=5, side="bottom")
        beesmas_group.pack_propagate(False)

        # ==================== Dispenser Section ====================
        dispenser_group = tk.LabelFrame(self, text=" Dispenser ", font=("Arial", 10, "bold"), width=200)
        dispenser_group.pack(fill="y", pady=5, side="left")
        dispenser_group.pack_propagate(False)

        dispenser_frame = tk.Frame(dispenser_group)
        dispenser_frame.pack(fill="x", padx=5)

        honey_check = tk.Checkbutton(dispenser_frame, text="Honey", font=("Arial", 10))
        honey_check.grid(row=0, column=0, sticky="w")

        treat_check = tk.Checkbutton(dispenser_frame, text="Treat", font=("Arial", 10))
        treat_check.grid(row=1, column=0, sticky="w")

        blueberry_check = tk.Checkbutton(dispenser_frame, text="Blueberry", font=("Arial", 10))
        blueberry_check.grid(row=2, column=0, sticky="w")

        starwberry_check = tk.Checkbutton(dispenser_frame, text="Strawberry", font=("Arial", 10))
        starwberry_check.grid(row=3, column=0, sticky="w")

        rj_check = tk.Checkbutton(dispenser_frame, text="Royal Jelly", font=("Arial", 10))
        rj_check.grid(row=0, column=1, sticky="w")

        glue_check = tk.Checkbutton(dispenser_frame, text="Glue", font=("Arial", 10))
        glue_check.grid(row=1, column=1, sticky="w")

        robopass_check = tk.Checkbutton(dispenser_frame, text="Robo Pass", font=("Arial", 10))
        robopass_check.grid(row=2, column=1, sticky="w")

        # ==================== Blender Section ====================
        blender_group = tk.LabelFrame(self, text=" Blender ", font=("Arial", 10, "bold"), width=130)
        blender_group.pack(fill="y", pady=5, side="right")
        blender_group.pack_propagate(False)