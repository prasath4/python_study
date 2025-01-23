""" 
    Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs). 
    It is simple to use and provides an extensive range of tools for building interactive desktop applications.
    Tkinter works as a wrapper for the Tcl/Tk GUI toolkit.

Basic Concepts of Tkinter
    WIDGETS:

        The building blocks of the GUI. Examples include buttons, labels, text fields, frames, etc.
        Geometry Management:

Tkinter provides three methods to arrange widgets in a window:
   --pack(): Packs widgets into the window.
   --grid(): Places widgets in a tabular format.
   --place(): Allows widgets to be positioned explicitly.

Events and Callbacks:

   You can bind functions to events, such as a button click.

"""


"""-------------------------------------------------------------------------------------------------"""

# from tkinter import *
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")  # Set the size of the window (width x height)

# Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=10)  # Adds the label to the window with padding

# Add a button
def on_button_click():
    label.config(text="Button Clicked!")  # Change label text

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
root.mainloop()


"""-------------------------------------------------------------------------------------------------"""

from tkinter import *

root=Tk()
button=Button(root, text='Click Me',command=root.quit)
button.pack()
root.mainloop()
