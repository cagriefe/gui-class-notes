# Message and dialog boxes II

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog as fd

# Function to open a file dialog and display the selected file path
def open_file():
    file_filter = (
        ("All types", "*.*"),
        ("Text file", "*.txt"),
        ("PDF file", "*.pdf")
    )
    selected_file = fd.askopenfilename(filetypes=file_filter)
    tk.Label(win, text=selected_file).pack()
# Function to print the state of the check button
def print_state():
    print(check_state.get())
# Function to exit the application with a confirmation dialog
def exit_app():
    dialog_result = msg.askyesno(title="Exit", 
                                 message="Sure to exit?")
    # dialog_result = msg.askyesnocancel(title="Exit",
    #                            message="Sure to exit?")
    if dialog_result:
        win.destroy()

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

# Variable for the check button state
check_state = tk.BooleanVar()
# Creates a menu bar.
menubar = tk.Menu(win)
# Configures the main window to use menubar as its menu.
win.configure(menu=menubar)
# Creates a menu item under the menu bar. 
# Disables the ability to tear off the menu into a separate window.
file_menu = tk.Menu(menubar, tearoff=False)
# Adds a "New" command with an accelerator (keyboard shortcut) "Ctrl+N" 
# and underlines the first character ("N"). Shows a warning message when clicked.
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0,
                      command=lambda: msg.showwarning(title="Warning",
                                                      message="Unsaved will lost."))
# Adds an "Open..." command and underlines the first character ("O").
# Opens a file dialog when clicked.
file_menu.add_command(label="Open...", underline=0, command=open_file)
# Adds a separator line in the menu.
file_menu.add_separator()
# Creates a submenu under the file_menu.
sub_menu = tk.Menu(file_menu, tearoff=False)
# Adds a "Zoom in" command to the submenu.
sub_menu.add_command(label="Zoom in")
# Adds a "Zoom out" command to the submenu.
sub_menu.add_command(label="Zoom out")
# Adds the sub_menu to the file_menu under the label "Editor".
file_menu.add_cascade(label="Editor", menu=sub_menu)
# Adds a separator line in the menu.
file_menu.add_separator()
# Adds an "Exit" command that calls exit_app to close the application 
# and underlines the second character ("x").
file_menu.add_command(label="Exit", command=exit_app, underline=1)
# Creates a menu item under the menu bar.
help_menu = tk.Menu(menubar, tearoff=False)
# Adds a check button with the label "Send anonymous stats", 
# binds it to the check_state variable, and sets the command to print_state.
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False,
                          variable=check_state, command=print_state)
# Adds a separator line in the menu.
help_menu.add_separator()
# Adds an "About..." command that shows an information message when clicked.
help_menu.add_command(label="About...",
                      command=lambda: msg.showinfo(title="About",
                                                   message="SEN4017\nFall 2024"))
# Adds the file_menu to the menubar with the label "File".
# The underline=0: first character ("F") will be underlined.
menubar.add_cascade(label="File", menu=file_menu, underline=0)
# Adds the help_menu to the menubar with the label "Help".
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()