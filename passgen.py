import tkinter as tk
import random
import string
import tkinter as tk
import random
import string


def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        result_label.config(text="Please enter a valid length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Generated Password: {password}")
    result_text.config(state=tk.DISABLED)


def reset():
    length_entry.delete(0, tk.END)
    result_label.config(text="")
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size and position
window_width = 400
window_height = 380
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

length_frame = tk.Frame(root)
length_label = tk.Label(length_frame, text="Enter password length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, width=15)
length_entry.pack(side=tk.LEFT)
length_frame.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD)
result_text.pack(padx=10, pady=10)
result_text.config(state=tk.DISABLED)

reset_button = tk.Button(root, text="Reset", command=reset, bg="#FF5733", fg="white")
reset_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()


def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        result_label.config(text="Please enter a valid length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Generated Password: {password}")
    result_text.config(state=tk.DISABLED)


def reset():
    length_entry.delete(0, tk.END)
    result_label.config(text="")
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Password Generator by AMOGH")


window_width = 400
window_height = 380
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


title_label = tk.Label(root, text="Password Generator by Amogh ", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

length_frame = tk.Frame(root)
length_label = tk.Label(length_frame, text="Enter password length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, width=20)
length_entry.pack(side=tk.LEFT)
length_frame.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD)
result_text.pack(padx=10, pady=10)
result_text.config(state=tk.DISABLED)

reset_button = tk.Button(root, text="Reset", command=reset, bg="#FF5733", fg="white")
reset_button.pack(pady=10)


root.mainloop()