# Menu with multiple items and accelerators

import tkinter as tk

win = tk.Tk()
win.title("Week 4")
win.geometry("300x200+400+100")
win.iconbitmap("python.ico")

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
# Adds an "Exit" command that closes the application 
# and underlines the second character ("x").
file_menu.add_command(label="Exit", command=win.destroy, underline=1)
# Creates a menu item under the menu bar.
help_menu = tk.Menu(menubar, tearoff=False)
# Adds an "About..." command.
help_menu.add_command(label="About...")
# Adds the file_menu to the menubar with the label "File".
# The underline=0: first character ("F") will be underlined.
menubar.add_cascade(label="File", menu=file_menu, underline=0)
# Adds the help_menu to the menubar with the label "Help".
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()