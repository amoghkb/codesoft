import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cal - Amogh")

        self.entry = tk.Entry(root, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),  # Added the clear button
        ]

        for button_text, row, col in buttons:
            self.create_button(button_text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=('Arial', 16), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif value == 'C':  # Clear the display
            self.entry.delete(0, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
