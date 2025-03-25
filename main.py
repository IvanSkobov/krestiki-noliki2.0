Update main.py
e84426b
main.py
@@ -0,0 +1,52 @@
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x300")


concurrent_player = "x"
buttons = []

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] !="":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] !="":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
           return True
    return False




def on_click(row, col):
    global concurrent_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = concurrent_player

    if check_winner():
        messagebox.showinfo(f"Игра-окончена", f"Игрок {concurrent_player } победил!!!")


    concurrent_player = "0" if concurrent_player == "x" else "x"
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)



window.mainloop()