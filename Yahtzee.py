import tkinter as tk
from Player import Player

class Yahtzee:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_state("zoomed")
        self.root.title("Nombre de joueurs")
        
        self.player_count = 0
        self.entry_players = None
        self.label_error = None

        self.create_main_window()

    def create_main_window(self):
        tk.Label(self.root, text="Nombre de joueurs:").pack()
        self.entry_players = tk.Entry(self.root)
        self.entry_players.pack()
        self.label_error = tk.Label(self.root, fg="red")
        self.label_error.pack()
        tk.Button(self.root, text="Valider", command=self.start_game).pack()

    def start_game(self):
        try:
            self.player_count = int(self.entry_players.get())
            if self.player_count <= 0:
                raise ValueError("Nombre de joueurs doit être positif!")
            self.open_player_names_window()
        except ValueError as e:
            self.label_error.config(text=str(e))

    def open_player_names_window(self):
        self.root.destroy()

        self.player_names_window = tk.Tk()
        self.player_names_window.wm_state("zoomed")
        self.player_names_window.title("Noms des Joueurs")

        self.entry_list = []
        for i in range(self.player_count):
            tk.Label(self.player_names_window, text=f"Nom joueur {i+1}:").pack()
            entry = tk.Entry(self.player_names_window)
            entry.pack()
            self.entry_list.append(entry)

        tk.Button(self.player_names_window, text="Valider", command=self.start_game).pack()
        self.player_names_window.mainloop()

    def open_game_window(self):
        self.game_window = tk.Toplevel(self.root)
        self.game_window.wm_state("zoomed")
        self.game_window.title("Yahtzee")

        # Add GUI for the game here

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    yahtzee_game = Yahtzee()
    yahtzee_game.start()