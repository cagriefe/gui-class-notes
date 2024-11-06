# Sub menu

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

# Creates a submenu under the file_menu.
sub_menu = tk.Menu(file_menu, tearoff=False)
# Adds a "Zoom in" command to the submenu.
sub_menu.add_command(label="Zoom in")
# Adds a "Zoom out" command to the submenu.
sub_menu.add_command(label="Zoom out")

# Adds the sub_menu to the file_menu under the label "Editor".
file_menu.add_cascade(label="Editor", menu=sub_menu)
file_menu.add_separator()
# Adds an "Exit" command that closes the application 
# and underlines the second character ("x").
file_menu.add_command(label="Exit", command=win.destroy, underline=1)

# reates a menu item under the menu bar.
help_menu = tk.Menu(menubar, tearoff=False)
# Adds an "About..." command.
help_menu.add_command(label="About...")

# Adds the file_menu to the menubar with the label "File".
# The underline=0 parameter specifies that the first character ("F") will be underlined.
menubar.add_cascade(label="File", menu=file_menu, underline=0)
# Adds the help_menu to the menubar with the label "Help".
menubar.add_cascade(label="Help", menu=help_menu)

win.mainloop()