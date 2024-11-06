# Simple menu

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
# Adds a command to the file_menu with the label "Exit". 
# When selected, it will call win.destroy to close the application.
file_menu.add_command(label="Exit", command=win.destroy)

# Adds the file_menu to the menubar with the label "File". 
# The underline=0 parameter specifies that the first character ("F") will be underlined,
# which can be used as a keyboard shortcut (press Alt + F on Windows).
menubar.add_cascade(label="File", menu=file_menu, underline=0)

win.mainloop()