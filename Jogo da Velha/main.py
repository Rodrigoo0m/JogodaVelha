import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = "X"
        self.game_mode = None
        self.player_names = {"X": "", "O": ""}
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.initialize_game()

    def initialize_game(self):
        self.game_mode = simpledialog.askstring("Modo de Jogo", "Digite '1' para jogar contra o computador ou '2' para dois jogadores")
        if self.game_mode not in ["1", "2"]:
            self.game_mode = "2"

        if self.game_mode == "2":
            self.player_names["X"] = simpledialog.askstring("Nome do Jogador", "Nome do Jogador X:")
            self.player_names["O"] = simpledialog.askstring("Nome do Jogador", "Nome do Jogador O:")
        else:
            self.player_names["X"] = simpledialog.askstring("Nome do Jogador", "Seu nome:")
            self.player_names["O"] = "Computador"

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font="Arial 20", height=2, width=5,
                                   command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player
            if self.check_winner():
                winner = self.current_player
                messagebox.showinfo("Fim de Jogo", f"{self.player_names[winner]} venceu!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_game()
            else:
                self.switch_player()
                if self.game_mode == "1" and self.current_player == "O":
                    self.computer_move()

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        return all(all(cell != "" for cell in row) for row in self.board)

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.button_click(row, col)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.board[i][j] = ""
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

# Cria e executa o jogo
game = TicTacToe()
game.run()
