from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FA7070"
RED = "#C6EBC5"
GREEN = "#A1C298"
YELLOW = "#FBF2CF"
FONT_NAME = "Courier"
reps = 0
timer = None
paused_time = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    counter.config(text="")
    start.config(text="Start", command=start_timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # Changes the input times of minutes into seconds so the clock can run
    work_sec = int(work_time.get()) * 60
    short_break_sec = int(short_break_time.get()) * 60
    long_break_sec = int(long_break_time.get()) * 60

    # Causes the changes of the screen depending on which rep the clock is on to distinguish the different count down parts
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="MINI BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# Let's the timer be paused for any reason and changes the start button to resume


def pause_timer():
    window.after_cancel(timer)
    start.config(text="Resume", command=resume_timer)

# The function that when the resume button is pressed to keep counting from the time that it was paused at


def resume_timer():
    global paused_time
    count_down(paused_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # changes the min to seconds for the so that the display can be correct
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # When the there is less than 10 seconds left the program will use the computer system bell sound to dig at each second leading up to the change in timer
    if count_min == 0 and count_sec <= 10:
        window.bell()

    # when the remainder of the count / 60 is less than 10 it adds the leading 0 to the timer still looks like a clock
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # set the timer text to look how we want it to with time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # actually causes the window to essentially refresh with each second and subtracts 1 from the count(time total) so that the counter actually is seen decreasing

    # saves the time if the timer is paused so it can be restarted
    if count > 0:
        global timer
        global paused_time
        paused_time = count
        timer = window.after(1000, count_down, count - 1)

    else:
        # Continually starts the time at the switches of the sessions
        start_timer()
        # Calls the pop up notification of a session switch
        notify()
        # keeps track of the work sessions and adds the check marks to keep count
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        counter.config(text=marks)

    # when the timer is started it changes the start button to say pause and give it the pause functionality
    start.config(text="Pause", command=pause_timer)

# ---------------------------- NOTIFY OF CHANGE POPUP ------------------------------- #


def notify():
    global reps
    global pop_up

    rounds = math.floor(reps / 2)
    # creating the pop up as a top level window, it should show above everything
    pop_up = Toplevel()
    pop_up.title("Pomodoro Timer")
    pop_up.config(bg=YELLOW, padx=20, pady=20)
    pop_up.lift()

    pop_up_label = Label(pop_up, bg=YELLOW, fg=GREEN,
                         font=(FONT_NAME, 20, "bold"))
    pop_up_label.grid(column=1, row=1, pady=5)

    pop_continue = Button(pop_up, text="Continue", bg=YELLOW, font=(
        FONT_NAME, 20, "bold"), highlightthickness=0, command=lambda: close_pop("continue"))
    pop_continue.grid(column=1, row=2, pady=5)

    pop_pause = Button(pop_up, text="Pause", bg=YELLOW, font=(
        FONT_NAME, 20, "bold"), highlightthickness=0, command=lambda: close_pop("pause"))
    pop_pause.grid(column=1, row=3, pady=5)

    pop_reset = Button(pop_up, text="Reset", bg=YELLOW, font=(
        FONT_NAME, 20, "bold"), highlightthickness=0, command=lambda: close_pop("reset"))
    pop_reset.grid(column=1, row=4, pady=5)

    pop_close = Button(pop_up, text="Finished", bg=YELLOW, font=(
        FONT_NAME, 20, "bold"), highlightthickness=0, command=lambda: close_pop("close"))
    pop_close.grid(column=1, row=5, pady=5)

    if reps % 8 == 0:
        pop_up_label.config(
            text=f"You've completed {rounds} work rounds time for a break!", fg=RED)
    elif reps % 2 == 0:
        pop_up_label.config(text="Take a mini break!", fg=PINK)
    else:
        pop_up_label.config(text="Time to work.", fg=GREEN)

    # This will close the pop up if the user does not hit one of the buttons after 10 seconds
    pop_up.after(10000, lambda: pop_up.destroy())

# the pop ups button functionality mirrors the original window
# this will close the pop up and do the designated function of it all


def close_pop(choice):
    pop_up.destroy()

    if choice == "pause":
        pause_timer()
    elif choice == "reset":
        reset_timer()
    elif choice == "close":
        close_it_all()
    else:
        pass

# the finish button of the pop up will close the whole program if the user is done


def close_it_all():
    window.quit()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

bg_photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=bg_photo)
timer_text = canvas.create_text(
    100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=5, pady=5)

timer_label = Label(text="POMODORO TIMER", fg=GREEN, font=(
    FONT_NAME, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

counter = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
counter.grid(column=1, row=4)

start = Button(text="Start", bg=YELLOW, font=(
    FONT_NAME, 20, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=6, pady=10)

reset = Button(text="Reset", bg=YELLOW, font=(
    FONT_NAME, 20, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=1, row=6, pady=10)

reset = Button(text="Finished", bg=YELLOW, font=(
    FONT_NAME, 20, "bold"), highlightthickness=0, command=close_it_all)
reset.grid(column=2, row=6, pady=10)


# the input function of setting the timer to have specific min work and breaks
time_entry_label = Label(text="Set the times you want below and hit start.",
                         fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
time_entry_label.grid(column=1, row=1, pady=5)

# set the work time takes whole numbers to represent the minutes
work_time = Entry(width=7,  fg=GREEN, justify="center", font=(
    FONT_NAME, 20, "bold"), bg="white", insertbackground=GREEN, insertwidth=5)
work_time.insert(END, string="25")
work_time.grid(column=0, row=2, padx=5)
work_time_label = Label(text="min of work", fg=GREEN,
                        bg=YELLOW, font=(FONT_NAME, 15, "bold"))
work_time_label.grid(column=0, row=3, padx=5)

# set the short break time takes whole numbers to represent the minutes
short_break_time = Entry(width=7, bg="white", fg=GREEN, justify="center", font=(
    FONT_NAME, 20, "bold"), insertbackground=GREEN, insertwidth=5)
short_break_time.insert(END, string="5")
short_break_time.grid(column=1, row=2, padx=5)
short_break_time_label = Label(
    text="min for mini break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
short_break_time_label.grid(column=1, row=3, padx=5)

# set the long break time takes whole numbers to represent the minutes
long_break_time = Entry(width=7, bg="white", fg=GREEN, justify="center", font=(
    FONT_NAME, 20, "bold"), insertbackground=GREEN, insertwidth=5)
long_break_time.insert(END, string="20")
long_break_time.grid(column=2, row=2, padx=5)
long_break_time_label = Label(
    text="min for long break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
long_break_time_label.grid(column=2, row=3, padx=5)


# keeps the program open and going
window.mainloop()
