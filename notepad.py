from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

dark_primary = "#18181a"
dark_secondary = "#5d5d63"
dark_mode_text = "#e6e6eb"


primarycolor = dark_primary
secondarycolor = dark_secondary
text_mode_color = dark_mode_text

window = Tk()
window.geometry("1280x720") 
window['background'] = primarycolor

icon = PhotoImage(file= 'headphone.png')
window.iconphoto(True, icon)
title = window.title("To-Do List")
window.title()

#Button Functions
def delete():
    listbox.delete(listbox.curselection())

def clear():
    listbox.delete(0, END)

def submissions():
    entrycontent = entry.get()
    if entrycontent == '' or entrycontent == ' ':
        messagebox.showerror(title= 'Empty Space', message= "You can't enter an empty entry")
    else:    
        listbox.insert(listbox.size(), entry.get())
        entry.delete(0, END)

#Menu Functions
def instruction():
    new_window = Toplevel(bg='#879fd4')
    #instruction
    clear_instruct = Label(new_window, text='Press Esc or clear to clear the listbox', font=("Times New Roman", 10), bg=secondarycolor, fg=text_mode_color )
    clear_instruct.pack(expand=True)
    enter_instruct = Label(new_window, text='Press Enter or the Enter button to submit the entry', font=("Times New Roman", 10), bg=secondarycolor, fg=text_mode_color)
    enter_instruct.pack(expand=True)
    delete_instruct = Label(new_window, text='Press backspace or the Delete button to Delete the currently selected', font=("Times New Roman", 10), bg=secondarycolor, fg=text_mode_color)
    delete_instruct.pack(expand=True)
    full_instruct = Label(new_window, text='Full screen is recommended', font=("Times New Roman", 10), bg=secondarycolor, fg=text_mode_color)
    full_instruct.pack(expand=True)

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"), ("HTML File", ".html"), ("All Files", ".*")])
    filetext = str(listbox.get(0, END))
    file.write(filetext)
    file.close()

def excite():
    exit()

#Keybind Functions
def enterer(event):
    entrycontent = entry.get()
    if entrycontent == '' or entrycontent == ' ':
        messagebox.showerror(title= 'Empty Space', message= "You can't enter an empty entry")
    else:    
        listbox.insert(listbox.size(), entry.get())
        entry.delete(0, END)

def deleter(event):
    listbox.delete(listbox.curselection())


def clearer(event):
    listbox.delete(0, END)

#Keybinds
window.bind("<BackSpace>", deleter)
window.bind("<Return>", enterer)
window.bind("<Escape>", clearer)

#Menu Bar
menubar = Menu(window, bg=secondarycolor, fg=text_mode_color)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, bg=secondarycolor, fg=text_mode_color)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Instructions", command= instruction)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command= excite)

#Label
mainframe = Frame(window)
mainframe.pack(side=TOP)
mainframe['background'] = secondarycolor

todo_name = Label(mainframe, text="To-Do List", font=("Calibri", 25), bg=secondarycolor, fg=text_mode_color)
todo_name.pack()

#Listbox
listbox = Listbox(mainframe, bg=secondarycolor, fg=text_mode_color, font=("Constantia", 25), width= 40 )
listbox.pack()

#Bottom Frame
frame = Frame(window)
frame.pack(side=BOTTOM)

#Entry and Buttons
entry = Entry(frame, font=("consolas", 25), bg=secondarycolor, fg=text_mode_color, width=30, bd=0)
entry.pack(side=LEFT)
clear_button = Button(frame, text='Clear', font=("consolas", 15), bg=secondarycolor, fg=text_mode_color, command=clear, width= 7, borderwidth=2)
clear_button.pack(side=RIGHT)
delete_button = Button(frame, text='Delete', font=("consolas", 15), bg=secondarycolor, fg=text_mode_color, command=delete, width= 7, borderwidth=2)
delete_button.pack(side=RIGHT)
submit = Button(frame, text='Enter', font=("consolas", 15), bg=secondarycolor, fg=text_mode_color, command=submissions, width= 7, borderwidth=2)
submit.pack(side=RIGHT)


listbox.config(height=listbox.size())


window.mainloop()