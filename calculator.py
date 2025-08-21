import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, height=50, bd=0, bg="lightgray")
        input_frame.pack(side="top", fill="both")

        input_field = tk.Entry(input_frame, font=('Arial', 18), textvariable=self.input_text, justify="right")
        input_field.pack(expand=True, fill="both", ipady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                button = tk.Button(row_frame, text=btn, font=('Arial', 18), relief='ridge', borderwidth=1,
                                   command=lambda b=btn: self.on_button_click(b))
                button.pack(side="left", expand=True, fill="both")

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
