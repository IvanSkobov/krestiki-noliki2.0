import tkinter as tk
from tkinter import messagebox

# Основные переменные
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("400x400")

concurrent_player = "x"
buttons = []
score_x = 0
score_o = 0

# Проверка победителя
def check_winner():
    for i in range(3):
        # Проверка строк
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        # Проверка столбцов
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True

    # Проверка главной диагонали
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    # Проверка побочной диагонали
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    return False

# Проверка ничьей
def is_draw():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

# Обновление счета
def update_score():
    global score_x, score_o
    if concurrent_player == "x":
        score_x += 1
    else:
        score_o += 1
    score_label.config(text=f"Счет: X - {score_x} | O - {score_o}")

    if score_x == 3 or score_o == 3:
        winner = "X" if score_x == 3 else "O"
        messagebox.showinfo("Игра окончена", f"Игрок {winner} выиграл серию!")
        window.quit()

# Сброс игры
def reset_game():
    global concurrent_player
    for row in buttons:
        for button in row:
            button['text'] = ""
    concurrent_player = "x"
    score_label.config(text=f"Счет: X - {score_x} | O - {score_o}")

# Ход игрока
def on_click(row, col):
    global concurrent_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = concurrent_player
    buttons[row][col]['fg'] = "red" if concurrent_player == "x" else "blue"

    if check_winner():
        update_score()
        messagebox.showinfo("Игра окончена", f"Игрок {concurrent_player.upper()} победил!")
        reset_game()
    elif is_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()

    concurrent_player = "o" if concurrent_player == "x" else "x"

# Выбор роли
def choose_player(player):
    global concurrent_player
    concurrent_player = player
    start_screen.destroy()

start_screen = tk.Toplevel(window)
start_screen.title("Выберите роль")
start_screen.geometry("200x100")

tk.Label(start_screen, text="Выберите, чем вы хотите играть:", font=("Arial", 12)).pack(pady=5)
tk.Button(start_screen, text="X", font=("Arial", 12), command=lambda: choose_player("x")).pack(side=tk.LEFT, padx=10)
tk.Button(start_screen, text="O", font=("Arial", 12), command=lambda: choose_player("o")).pack(side=tk.RIGHT, padx=10)

window.withdraw()  # Скрываем основное окно до выбора роли
start_screen.protocol("WM_DELETE_WINDOW", window.quit)  # Закрытие программы при закрытии стартового экрана

start_screen.wait_window()
window.deiconify()

# Создание поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 20),
            width=5,
            height=2,
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_button = tk.Button(window, text="Сброс", font=("Arial", 12), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Счетчик побед
score_label = tk.Label(window, text=f"Счет: X - {score_x} | O - {score_o}", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3, pady=5)

window.mainloop()