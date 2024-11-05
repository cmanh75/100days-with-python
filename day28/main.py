from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
section = 1
mark = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global section, mark
    window.after_cancel(timer)
    section = 1
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    mark = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global section, mark, timer
    if timer != None:
        window.after_cancel(timer)
    if section == 8:
        count_down(LONG_BREAK_MIN * 60)
        section = 1
        title_label.config(text="BREAK", fg=RED)
        return 
    if section % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="BREAK", fg=PINK)
        mark += "✔"
        check_marks.config(text=mark)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="WORK", fg=GREEN)
    section += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_png)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)

window.mainloop()