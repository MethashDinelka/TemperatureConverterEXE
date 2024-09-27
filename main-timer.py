import customtkinter as tk
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def update_slider_value(value):
    label3.configure(font=("Times New Roman", 18), text=f"Target Time: {int(value)} min")

def countdown(time_left):
    if time_left > 0:
        time_min = time_left // 60
        time_sec = time_left % 60
        label_time.configure(text=f"{time_min:02d} : {time_sec:02d}")
        root.after(1000, countdown, time_left - 1)  # Call countdown after 1 second
    else:
        label_time.configure(text="Time's up!")

def start_timer():
    value = int(slider.get())  # Get the slider value
    total_seconds = value * 60  # Convert to seconds
    countdown(total_seconds)

def clos():
    root.destroy()

root = tk.CTk()

width, height = 700, 500

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int((display_width / 2) - (width / 2))
top = int((display_height / 2) - (height / 2))

tk.set_appearance_mode("system")
root.title("Timer")
root.iconbitmap(resource_path("icon.ico"))
root.configure(fg_color="lightblue")
root.geometry(f"{width}x{height}+{left}+{top}")
root.resizable(False, False)

label = tk.CTkLabel(root, text="TIMER", fg_color="transparent", font=("FarCry", 50), text_color="black")
label.pack()

label_credit = tk.CTkLabel(root, text="Soft By Methash Dinelka©", text_color="black")
label_credit.pack()

label2 = tk.CTkLabel(root, text="")
label2.pack()

label32 = tk.CTkLabel(root, text="")
label32.pack()

slider = tk.CTkSlider(root, from_=1, to=20, command=update_slider_value)
slider.pack()

label3 = tk.CTkLabel(root, text="Slide Your Preferred Value", font=("Times New Roman", 18), text_color="red")
label3.pack()

label320 = tk.CTkLabel(root, text="")
label320.pack()

button = tk.CTkButton(root, fg_color="green", font=("Elephant", 17), text="Click To Begin", command=start_timer)
button.pack()

label_time = tk.CTkLabel(root, text="00:00", font=("FarCry", 120), text_color="blue")
label_time.pack()

# Add some spacing
label3203 = tk.CTkLabel(root, text="")
label3203.pack()

# Close button placed at the bottom, with padding
cls_btn = tk.CTkButton(root, text="Close", font=("Elephant", 30), fg_color="red", command=clos)
cls_btn.pack(pady=20)  # Add padding to push it up a bit from the bottom

root.mainloop()
