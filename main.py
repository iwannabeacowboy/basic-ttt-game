from tkinter import *
import random

def next_turn(row, column):
    global player, fplayer_wins, splayer_wins

    if buttons[row][column]["text"] == "" and check_winner() is False:

         if player == players[0]:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=f"{players[1]} turn")

            elif check_winner() is True:
                label.config(text=f"{players[0]} wins")
                fplayer_wins += 1
                score.config(text=f"{players[0]}: {fplayer_wins}     {players[1]}: {splayer_wins}", font=("Arial", 10))

            elif check_winner() == "Tie":
                label.config(text="Tie")

         else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=f"{players[0]} turn")

            elif check_winner() is True:
                label.config(text=f"{players[1]} wins")
                splayer_wins += 1
                score.config(text=f"{players[0]}: {fplayer_wins}     {players[1]}: {splayer_wins}", font=("Arial", 10))

            elif check_winner() == "Tie":
                label.config(text="Tie")

def check_winner():
    
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="#2aa63d")
            buttons[row][1].config(bg="#2aa63d")
            buttons[row][2].config(bg="#2aa63d")
            return True
        
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="#2aa63d")
            buttons[1][column].config(bg="#2aa63d")
            buttons[2][column].config(bg="#2aa63d")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="#2aa63d")
        buttons[1][1].config(bg="#2aa63d")
        buttons[2][2].config(bg="#2aa63d")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="#2aa63d")
        buttons[1][1].config(bg="#2aa63d")
        buttons[2][0].config(bg="#2aa63d")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#eecd60")
        return "Tie"

    return False

def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False

    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()

window.title("Tic-Tac-Toe Game")
window.iconbitmap("ttt_icon.ico")

players = ["X","O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=f"{player} turn", font=("Arial", 20))
label.pack()

fplayer_wins = 0
splayer_wins = 0

score = Label(text=f"{players[0]}: {fplayer_wins}     {players[1]}: {splayer_wins}", font=("Arial", 10))
score.pack()

reset_button = Button(text="Restart", font=("Arial", 10), command=new_game)
reset_button.pack(side = BOTTOM)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=("Arial", 10), width=10, height=4,
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()