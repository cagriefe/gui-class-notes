# Menu with a check button

import tkinter as tk

# Function to print the state of the check button and update the label
def print_state():
    print(check_state.get())
    label1.configure(text=f"State: {check_state.get()}")

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
# and underlines the first character ("N").
file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
# Adds an "Open..." command and underlines the first character ("O").
file_menu.add_command(label="Open...", underline=0)
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
# Adds an "Exit" command that closes the application 
# and underlines the second character ("x").
file_menu.add_command(label="Exit", command=win.destroy, underline=1)

# Creates a menu item under the menu bar.
help_menu = tk.Menu(menubar, tearoff=False)
# Adds a check button with the label "Send stats", 
# binds it to the check_state variable, and sets the command to print_state.
help_menu.add_checkbutton(label="Send stats", onvalue=True, 
                          variable=check_state, command=print_state)
# Adds a separator line in the menu.
help_menu.add_separator()
# Adds an "About..." command.
help_menu.add_command(label="About...")

# Adds the file_menu to the menubar with the label "File".
# The underline=0 parameter specifies that the first character ("F") will be underlined.
menubar.add_cascade(label="File", menu=file_menu, underline=0)
# Adds the help_menu to the menubar with the label "Help".
menubar.add_cascade(label="Help", menu=help_menu)

# Label to display the state of the check button
label1 = tk.Label(win, text="State")
label1.pack()

win.mainloop()