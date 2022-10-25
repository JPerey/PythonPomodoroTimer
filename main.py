from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#EEEEEE"
RED = "#e7305b"
GREEN = "#829460"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    window.after(1000, countdown, count - 1)
    print(count)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro = Tomato")
background = PhotoImage(file="tomato.png")
window.config(padx=100, pady=50, bg=GREEN)
countdown(5)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(100, 112, image=background)
canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 25, "bold"))
canvas.config()
canvas.grid(column=1, row=1)

title_label = Label(text="POMO TIMER", fg=WHITE, bg=GREEN, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

checks = Label(text="✔", bg=GREEN)
checks.grid(column=1, row=2)

start = Button(text="START", highlightthickness=0, font=(FONT_NAME, 16))
start.grid(column=0, row=2)

reset = Button(text="RESET", highlightthickness=0, font=(FONT_NAME, 16))
reset.grid(column=2, row=2)

window.mainloop()
