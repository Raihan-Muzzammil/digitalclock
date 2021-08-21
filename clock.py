from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import datetime
import time
import pytz
from winsound import *


green = "#00ff00"
cyan = "cyan"
Main = Tk()
Main.title("Clock")
Main.geometry('1000x600')


style = ttk.Style()

style.theme_create("ting", parent="alt", settings={
    "TNotebook": {"configure": {"tab_margins": [2, 5, 2, 0]}},
    "TNotebook.Tab":
    {"configure": {"padding": [5, 1], "background": green}, "map": {"background": [("selected", cyan)], "expand": [("selected", [1, 1, 1, 0])]}}, 'TCombobox':
    {'configure': {'selectbackground': 'black', 'fieldbackground': 'black', 'background': 'cyan'}}})

style.theme_use("ting")

timer_counter_num = 66600
timer_running = False


def bye():
    exit()


def countdown_timer():
    global timer_time
    timer_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while timer_time > -1:
        minute, second = (timer_time // 60, timer_time % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        timer_tab.update()
        time.sleep(1)
        if timer_time == 0:
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        timer_time -= 1
    PlaySound("F:\KSI – Holiday.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)
    popupmsg("Time's up fella, Get working ! ", "Timer Done!!")


def popupmsg(msg, title):
    global popup
    popup = tk.Tk()
    popup.title(title)
    popup.geometry("550x225")
    popup.configure(bg="black")
    label = tk.Label(popup, text=msg, font=("BEBASNEUE-REGULAR", 20), bg="black", fg="#00ff00")
    label.pack(side="top", fill="x", padx=20, pady=50)
    b1 = tk.Button(popup, text="Okay", font=("Balgin Black SmCondensed", 10, 'bold'), command=stopalarm2, padx=10, pady=10, bg="black", fg="cyan")
    b1.pack(anchor="center")
    popup.mainloop()


def stopalarm2():
    PlaySound(None, SND_ASYNC)
    global popup
    popup.destroy()


def stopalarm():
    PlaySound(None, SND_ASYNC)


def timer(work):
    if work == 'stop':
        global timer_time
        timer_time = False
        stopalarm()


def get_timezone():
    tz_any = pytz.timezone(timezone_choice.get())
    datetime_tz = datetime.datetime.now(tz_any)
    timezone_display.config(
        text="The Date and Time of the selected timezone is : \n" + datetime_tz.strftime("%d-%m-%Y \n %H:%M:%S  %p"),
        font=("Balgin Black SmCondensed", 15, 'bold'), bg='black', fg='cyan')


def clock():
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date, time1 = date_time.split()
    time2, time3 = time1.split('/')
    hour, minutes, seconds = time2.split(':')
    if 12 < int(hour) < 24:
        timings = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
        timings = time2 + ' ' + time3
    time_label.config(text=timings)
    date_label.config(text=date)
    time_label.after(1000, clock)


tabs = Notebook(Main)
clock_tab = tk.Frame(tabs, bg='black')
timer_tab = tk.Frame(tabs, bg='black')
world_tab = tk.Frame(tabs, bg='black')


tabs.add(clock_tab, text="Clock")
tabs.add(timer_tab, text="Timer")
tabs.add(world_tab, text="World Clock")
tabs.pack(expand=1, fill="both")


clock_lab_blank = tk.Label(clock_tab, font=("KG Happy", 20, 'bold'), text="Clock", bg='black', fg='black')
clock_lab_blank.pack(anchor='center')
clock_lab_blank = tk.Label(clock_tab, font=("KG Happy", 70, 'bold'), text="Clock", bg='black', fg='#00ff00', padx=10, pady=2)
clock_lab_blank.pack(anchor='center')
time_label = tk.Label(clock_tab, font=("Balgin Display ExtraLight", 40), foreground="#00ff00", background="black", padx=10, pady=10)
time_label.pack(anchor="center")
date_label = Label(clock_tab, font=("Balgin Display ExtraLight", 35), foreground="#00ff00", background="black")
date_label.pack(anchor="s")
clock_lab_blank = tk.Label(clock_tab, font=("KG Happy", 20, 'bold'), text="Clock", bg='black', fg='black')
clock_lab_blank.pack(anchor='center')
tk.Button(clock_tab, text='QUIT', font=('Balgin Black SmCondensed', 10), bg='black', fg='#00ff00', padx=10, pady=10, command=bye).pack(anchor="s")

timer_lab_blank = tk.Label(timer_tab, font=("KG Happy", 70, 'bold'), text="Timer", bg='black', fg='#00ff00', padx=10, pady=50)
timer_lab_blank.grid(column=4, row=0)

timer_lab_blank = tk.Label(timer_tab, font=("KG Happy", 50, 'bold'), text="Clock", bg='black', fg='black')
timer_lab_blank.grid(column=0, row=0)

hrs = StringVar()
tk.Label(timer_tab, font=("Balgin Display Medium", 13, 'bold'), text="Hours", bg='black', fg='cyan').grid(row=2, column=3)
tk.Entry(timer_tab, textvariable=hrs, width=5, font=('Balgin Display Medium', 14), bg='black', fg='#00ff00').grid(row=3, column=3)
hrs.set('0')

mins = StringVar()
tk.Label(timer_tab, font=("Balgin Display Medium", 13, 'bold'), text="Minutes", bg='black', fg='cyan').grid(row=2, column=4)
tk.Entry(timer_tab, textvariable=mins, width=5, font=('Balgin Display Medium', 14), bg='black', fg='#00ff00').grid(row=3, column=4)
mins.set('0')

sec = StringVar()
tk.Label(timer_tab, font=("Balgin Display Medium", 13, 'bold'), text="Seconds", bg='black', fg='cyan').grid(row=2, column=5)
tk.Entry(timer_tab, textvariable=sec, width=5, font=('Balgin Display Medium', 14), bg='black', fg='#00ff00').grid(row=3, column=5)
sec.set('0')

tk.Label(timer_tab, font=('Balgin Black SmCondensed', 22), text='Set the Timer', bg='black', fg='#00ff00').grid(row=1, column=4)
timer_lab_blank = tk.Label(timer_tab, font=("KG Happy", 20, 'bold'), text="Clock", bg='black', fg='black')
timer_lab_blank.grid(column=4, row=5)
tk.Button(timer_tab, text='START', font=('Balgin Black SmCondensed', 10,), bg='black', fg='#00ff00', padx=10, pady=10, command=countdown_timer).grid(row=6, column=4)
tk.Button(timer_tab, text='STOP', font=('Balgin Black SmCondensed', 10,), bg='black', fg='#00ff00', padx=14, pady=14, command=lambda: timer('stop')).grid(row=6, column=3)
tk.Button(timer_tab, text='QUIT', font=('Balgin Black SmCondensed', 10,), bg='black', fg='#00ff00', padx=14, pady=14, command=bye).grid(row=6, column=5)

wclock_lab_blank = tk.Label(world_tab, font=("KG Happy", 20, 'bold'), text="Clock", bg='black', fg='black')
wclock_lab_blank.pack(anchor='center')
wclock_lab_blank = tk.Label(world_tab, font=("KG Happy", 60, 'bold'), text="World Clock", bg='black', fg='#00ff00', padx=10, pady=10)
wclock_lab_blank.pack(anchor='center')
timezone_choice = ttk.Combobox(world_tab, values=[x for x in pytz.common_timezones], width=50, background='black', foreground='#00ff00')
timezone_choice.set("Asia/Kolkata")
timezone_choice.pack(anchor='s', padx=10, pady=10)
timezone_display = tk.Label(world_tab, bg='black', fg='#00ff00')
timezone_display.pack(anchor="s", pady=20)

tk.Button(world_tab, text='Get Time and Date', font=('Balgin Black SmCondensed', 15), bg='black', fg='#00ff00', padx=2, pady=2, command=get_timezone).pack(anchor='s')
wclock_lab_blank = tk.Label(world_tab, font=("KG Happy", 20, 'bold'), text="Clock", bg='black', fg='black')
wclock_lab_blank.pack(anchor='center')
tk.Button(world_tab, text='QUIT', font=('Balgin Black SmCondensed', 10), bg='black', fg='#00ff00', padx=10, pady=10, command=bye).pack(anchor='s')

clock()
Main.mainloop()
