from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def times_reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    # Reset all the labels
    timer_title.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0 and reps <= 7:
        count_down(SHORT_BREAK_MIN * 60)
        timer_title.config(text='Break', fg=PINK)
    elif reps == 8:
        reps = 0
        count_down(LONG_BREAK_MIN * 60)
        timer_title.config(text='Break', fg=RED)
    else:
        count_down(WORK_MIN * 60)
        timer_title.config(text='WORK', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    reps += 1
    # Create the watch formate 01:35
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_seconds}')   # There is a problema, the counter starts
    # as 5:0 and I want 5:00, I fix it with line 25-26
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✅'
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Method')
window.config(padx=100, pady=50, bg=YELLOW)   # Related to pixes, Change the background color


# def something(thing):
 #   print(thing)

#window.after(1000, something, "Hello")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)   # Same size as the image
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)  # Half of the width and height
# Text in the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# Text
timer_title = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 38), background=YELLOW)
timer_title.grid(column=1, row=0)

# Buttons

start = Button(text='Start', font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', font=(FONT_NAME, 10), highlightthickness=0, command=times_reset)
reset.grid(column=2, row=2)

check_marks = Label(text='✅', highlightthickness=0, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()