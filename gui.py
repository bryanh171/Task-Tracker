from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, Listbox, Entry, Button, END, SINGLE, BOTH, NONE
import datetime
import json


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("1280x720")
window.configure(bg = "#DEB7F1")
window.title('Task Tracker')

#Sets current time with dateime lib
current_time = datetime.datetime.now()
hour = current_time.hour

#Determines time of day
if int(hour) < 10:
    greeting_time = "Morning"
elif  10 <= int(hour) <= 15:
    greeting_time = "Afternoon"
else:
    greeting_time = "Evening"
    
task_list = Listbox(font=("Playfair Display", 35, 'bold'), height=8, selectmode=NONE, bg="#ab99b5")
task_list.place(x=626, y=98)

#Adds task to Listbox and also calls upon save_tasks command   
def add_task():
    task = entry_1.get()
    if task != "":
        task_list.insert(END, task)
        task_list.itemconfig(END, fg="white")
        entry_1.delete(0, END)
        save_tasks()

#loads in saved tasks from JSON file
def load_tasks():
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    task_list.insert(END, task["text"])
                    task_list.itemconfig(END, fg=task["color"])
        except FileNotFoundError:
            pass

#Saves Tasks to JSON file        
def save_tasks():
    data = []
    for i in range(task_list.size()):
        text = task_list.get(i)
        color = task_list.itemcget(i, "fg")
        data.append({"text": text, "color": color})
    with open("tasks.json", "w") as f:
            json.dump(data, f)

#deletes task from Listbox and JSON file            
def delete_task():
    task_index = task_list.curselection()
    if task_index:
        task_list.delete(task_index)
        save_tasks()

load_tasks()

canvas = Canvas(
    window,
    bg = "#DEB7F1",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    158.0,
    23.0,
    anchor="nw",
     text=f"Good {greeting_time}",
    fill="#FFFFFF",
    font=("Playfair Display", 39 * -1, 'bold')
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png")
    )
image_1 = canvas.create_image(
    926.0,
    358.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    925.0,
    50.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#dab2ec",
    command=add_task,
    relief="flat"
)
button_1.place(
    x=94.0,
    y=646.0,
    width=343.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#7f6889",
    command=delete_task,
    relief="flat"
)
button_2.place(
    x=758.0,
    y=648.0,
    width=340.0,
    height=43.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    279.5,
    611.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=62.0,
    y=587.0,
    width=435.0,
    height=46.0
)

#Brings Listbox to top layer of window
task_list.lift()

            
window.resizable(False, False)
window.mainloop()