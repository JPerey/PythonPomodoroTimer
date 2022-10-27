from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#EEEEEE"
RED = "#e7305b"
GREEN = "#829460"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 1
checkmarks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():
    global checkmarks
    global reps
    window.after_cancel(timer)
    checkmarks = ""
    reps = 1
    checks.config(text=checkmarks)
    title_label.config(text="POMO")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def add_checkmark():
    global reps
    global checkmarks
    checkmarks += "✔"
    checks.config(text=checkmarks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    short_work_sesh = 1500
    short_break_sesh = 300
    long_break_sesh = 1200
    global reps

    if reps == 1 or reps % 2 == 1:
        title_label.config(text="WORK")
        countdown(short_work_sesh)
    elif reps % 2 == 0 and reps < 8:
        title_label.config(text="BREAK")
        add_checkmark()
        countdown(short_break_sesh)
    elif reps == 8:
        title_label.config(text="BREAK")
        add_checkmark()
        countdown(long_break_sesh)
    else:
        reset_clock()


def countdown(count):
    global reps
    global timer
    if count >= 0:
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds >= 10:
            canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        else:
            canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
        timer = window.after(1000, countdown, count - 1)
        if count == 0:
            reps += 1
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro = Tomato")
background = PhotoImage(file="tomato.png")
window.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 25, "bold"))
canvas.config()
canvas.grid(column=1, row=1)

title_label = Label(text="POMO", fg=WHITE, bg=GREEN, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

checks = Label(text=checkmarks, bg=GREEN)
checks.grid(column=1, row=2)

start = Button(text="START", highlightthickness=0, font=(FONT_NAME, 16), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="RESET", highlightthickness=0, font=(FONT_NAME, 16), command=reset_clock)
reset.grid(column=2, row=2)

# function calls

window.mainloop()
