import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0  # track number of reps
# Create global variable to manage timer
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    check_label.config(text='')
    global reps
    reps = 0 # reset rep to zero



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps  # call the global variable
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    # if it's the 8th rep:
    if reps == 8:
        title_label.config(text='Break', bg=YELLOW, fg=RED, font=(FONT_NAME, 38, 'bold'))
        count_down(long_break_sec)
    # if it's the 2nd/4th/6th rep:
    if reps % 2 == 0:
        title_label.config(text='Break', bg=YELLOW, fg=PINK, font=(FONT_NAME, 38, 'bold'))
        count_down(short_break_sec)
    # if it's the 1st/3rd/5th/7th rep:
    if reps % 2 != 0:
        title_label.config(text='Work', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 38, 'bold'))
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Create the window
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text='{}:{}'.format(count_min, format(count_sec, '02d')))
    if count > 0:
        global timer  # call the global variable
        timer = window.after(1000, count_down, count - 1)  # assign count down to timer variable
    else:
        start_timer()
        # to add check mark each time when we complete a working rep
        mark = ''
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += '✔'
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

# Label

title_label = tk.Label()
title_label.config(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 38, 'bold'))
title_label.grid(column=1, row=0)


def start_click():
    start_timer()


# Start button
start_button = tk.Button()
start_button.config(text='Start', highlightthickness=0, command=start_click)
start_button.grid(column=0, row=2)

# reset button
reset_button = tk.Button()
reset_button.config(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# check mark label
check_label = tk.Label()
check_label.config(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
check_label.grid(column=1, row=3)

window.mainloop()
