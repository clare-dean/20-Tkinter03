###############################################################################
# DONE: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk
window = tk.Tk()
window.title("Form")

bg_color = "white"  
fg_color = "black"  

window.configure(background=bg_color)

fields = [
    ("Name", 30),
    ("Address Line 1", 40),
    ("Address Line 2", 40),
    ("City", 30),
    ("State", 5),
    ("Zip Code", 10),
    ("Phone Number", 15),
    ("Email Address", 30)
]

frame = tk.Frame(window, bg=bg_color)
frame.pack(padx=10, pady=10)

for field_name, field_width in fields:
    label = tk.Label(frame, text=field_name, bg=bg_color, fg=fg_color)
    label.grid(sticky="w", pady=2)
    entry = tk.Entry(frame, width=field_width)
    entry.grid(sticky="we", pady=2)

submit_button = tk.Button(window, text="Submit", bg="pink", fg="white", width=20)
submit_button.place(relx=0.5, rely=1.0, anchor="s", y=-10)

window.mainloop()