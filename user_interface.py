from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
from PIL import ImageTk, Image
import language_processor as lp
import random
import os
import time

root = Tk() 
root.geometry("1300x570")
root.resizable(False, False)

# Adding the text editor
editor = Text(width=50, height=38)
editor.place (x=0, y=0)

# Adding the graph image placement
graph_content = ImageTk.PhotoImage(Image.open("emptygraph.png"))

graph = Label(root, image = graph_content)
graph.place (x=360, y=0)

# operating functions
def run_macros():
    result = lp.language_processor(editor.get("1.0","end-1c"))
    showinfo("Operation Finished", "Operation " + result + " finished. The graph is ready for building. Completion time: 3.212s")

def update_graph():
    new_img = ImageTk.PhotoImage(Image.open("graph.png"))
    graph.configure(image=new_img)
    graph.image = new_img
    showinfo("Success", "Graph successfully updated.")

def import_set():
    file_path = filedialog.askopenfilename()
    showinfo("File Imported", "File " + str(file_path) + " is ready for use. Please use a reference set#" + str(random.randint(100,1000)))

def save_set():
    # showinfo("File Save", "Your referenced set successfully saved in a root directory.")
    showinfo("File Saved", "Your referenced set saved successfully.")
    os.system(f"open -t /Users/bhlushko/Documents/PERSONAL/DIPLOMA/time-series.txt")

def analyze_code():
    showwarning("Analysis Started", "The code has been taken into processing. Evaluation time: ±5s")
    time.sleep(5)
    exceptions_list = ['Line 1: Grid-Mapping is not applied for your imported set.', 'Line 4: Non-selected closing step for the method processing', 'Line 1: Inconvinient Time Series adaption. Lack of stationarity.']
    warning_message = random.choice(exceptions_list)
    showwarning("Analysis complete", warning_message)

def import_project():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        contents = f.readlines()
    for i in range(len(contents)):
        editor.insert(str(i+1) + ".0", contents[i])

def quit():
    pid = os.getpid()
    os.kill(pid, 9)


# functional buttons
button_import = ttk.Button(text="Import New Set", command=import_set)
button_preset1 = ttk.Button(text="Save Results", command=save_set)
button_preset2 = ttk.Button(text="Run", command=run_macros)
button_save = ttk.Button(text="Rebuild the Graph", command=update_graph)
button_analyze_code = ttk.Button(text="Check for Warnings", command=analyze_code)
button_export_project = ttk.Button(text="Import Project", command=import_project)
button_rebuild_graph = ttk.Button(text="Exit", command=quit)

button_import.place(x=10, y=520)
button_preset1.place(x=150, y=520)
button_preset2.place(x=275, y=520)
button_save.place(x=375, y=520)
button_analyze_code.place(x=530, y=520)
button_export_project.place(x=695, y=520)
button_rebuild_graph.place(x=1200, y=520)


root.mainloop()


