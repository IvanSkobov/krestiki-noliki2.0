import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("350x400")

concurrent_player = "x"
wins = {"x": 0, "0": 0}  # Счетчик побед
buttons = []
game_over = False  # Флаг окончания игры


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False


def check_draw():
    return all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3))


def reset_board():
    global concurrent_player, game_over
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""
    game_over = False
    concurrent_player = "x"


def on_click(row, col):
    global concurrent_player, game_over

    if buttons[row][col]['text'] != "" or game_over:
        return

    buttons[row][col]['text'] = concurrent_player

    if check_winner():
        wins[concurrent_player] += 1
        messagebox.showinfo("Игра окончена",
                            f"Игрок {concurrent_player} победил!\nСчет: X - {wins['x']}, O - {wins['0']}")
        game_over = True
        check_series_winner()
        return

    if check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        game_over = True
        return

    concurrent_player = "0" if concurrent_player == "x" else "x"


def check_series_winner():
    if wins["x"] == 3:
        messagebox.showinfo("Поздравляем!", "Игрок X выиграл серию из 3 игр!")
        reset_game()
    elif wins["0"] == 3:
        messagebox.showinfo("Поздравляем!", "Игрок O выиграл серию из 3 игр!")
        reset_game()


def reset_game():
    global wins
    wins = {"x": 0, "0": 0}
    reset_board()


def choose_symbol(symbol):
    global concurrent_player, buttons
    concurrent_player = symbol

    # Удаляем стартовые кнопки
    start_label.pack_forget()
    btn_x.pack_forget()
    btn_o.pack_forget()

    create_board()


def create_board():
    global buttons
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                            command=lambda r=i, c=j: on_click(r, c))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row.append(btn)
        buttons.append(row)

    reset_btn = tk.Button(window, text="Сбросить", font=("Arial", 14), command=reset_board)
    reset_btn.grid(row=3, column=1, pady=10)


# Окно выбора символа
start_label = tk.Label(window, text="Выберите символ:", font=("Arial", 14))
start_label.pack()
btn_x = tk.Button(window, text="X", font=("Arial", 14), command=lambda: choose_symbol("x"))
btn_x.pack()
btn_o = tk.Button(window, text="O", font=("Arial", 14), command=lambda: choose_symbol("0"))
btn_o.pack()

window.mainloop()