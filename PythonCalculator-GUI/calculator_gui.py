import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from calculator import Calculator


class CalculatorGUI(Calculator):
    def __init__(self):
        Calculator.__init__(self)

        # Initialize the default root window
        self.window = tk.Tk()
        self.window.geometry("500x400")
        self.window.title("Python-Calculator")

        # Get the font families after creating the default root window
        self.font_families = tkfont.families()
        self.selected_font = "Helvetica"

        def add_to_calculation(symbol):
            self.add_to_calculation(symbol)
            self.text_block.delete(1.0, "end")
            self.text_block.insert(1.0, self.calculation)

        def evaluate_calculation():
            self.evaluate_calculation()
            self.text_block.delete(1.0, "end")
            self.text_block.insert(1.0, self.calculation)

        def clear_field():
            self.clear_field()
            self.text_block.delete(1.0, "end")

        def perform_calculation():
            self.perform_calculation()
            self.text_block.delete(1.0, "end")
            self.text_block.insert(1.0, self.calculation)

        # Create the text block widget
        self.text_block = tk.Text(self.window, height=2, width=20, font=(self.selected_font, 28))
        self.text_block.grid(columnspan=5)

        # Create number buttons
        for i in range(1, 10):
            btn = tk.Button(self.window, text=str(i), command=lambda i=i: add_to_calculation(i), width=6,
                            font=(self.selected_font, 18))
            btn.grid(row=(i - 1) // 3 + 2, column=(i - 1) % 3 + 1)

        # Create operator buttons
        self.btn_plus = tk.Button(self.window, text="+", command=self.add, width=6, font=(self.selected_font, 18))
        self.btn_plus.grid(row=2, column=4)
        self.btn_minus = tk.Button(self.window, text="-", command=self.subtract, width=6, font=(self.selected_font, 18))
        self.btn_minus.grid(row=3, column=4)
        self.btn_divide = tk.Button(self.window, text="÷", command=self.divide, width=6, font=(self.selected_font, 18))
        self.btn_divide.grid(row=4, column=4)
        self.btn_multiply = tk.Button(self.window, text="×", command=self.multiply, width=6,
                                       font=(self.selected_font, 18))
        self.btn_multiply.grid(row=5, column=4)
        self.btn_open = tk.Button(self.window, text="(", command=lambda: add_to_calculation("("), width=6,
                                  font=(self.selected_font, 18))
        self.btn_open.grid(row=5, column=1)
        self.btn_close = tk.Button(self.window, text=")", command=lambda: add_to_calculation(")"), width=6,
                                   font=(self.selected_font, 18))
        self.btn_close.grid(row=5, column=3)
        self.btn_clear = tk.Button(self.window, text="C", command=clear_field, width=14,
                                   font=(self.selected_font, 18))
        self.btn_clear.grid(row=6, column=3, columnspan=2)
        self.btn_exit_now = tk.Button(self.window, text="Exit", command=self.window.destroy, width=14,
                                      font=(self.selected_font, 18))
        self.btn_exit_now.grid(row=6, column=1, columnspan=2)
        self.btn_is_equal_to = tk.Button(self.window, text="=", command=perform_calculation, width=6,
                                         font=(self.selected_font, 18))
        self.btn_is_equal_to.grid(row=5, column=2)

        # Create additional math function buttons
        self.btn_square_root = tk.Button(self.window, text="√", command=self.square_root, width=6,
                                         font=(self.selected_font, 18))
        self.btn_square_root.grid(row=2, column=5)
        self.btn_power_of_2 = tk.Button(self.window, text="x²", command=self.power_of_2, width=6,
                                        font=(self.selected_font, 18))
        self.btn_power_of_2.grid(row=3, column=5)
        self.btn_factorial = tk.Button(self.window, text="!", command=self.factorial, width=6,
                                       font=(self.selected_font, 18))
        self.btn_factorial.grid(row=4, column=5)

        # Create "0" button and decimal point button
        self.btn_0 = tk.Button(self.window, text="0", command=lambda: add_to_calculation("0"), width=6,
                               font=(self.selected_font, 18))
        self.btn_0.grid(row=5, column=0)
        self.btn_decimal = tk.Button(self.window, text=".", command=lambda: add_to_calculation("."), width=6,
                                     font=(self.selected_font, 18))
        self.btn_decimal.grid(row=6, column=0)

        self.window.mainloop()


if __name__ == "__main__":
    calc = CalculatorGUI()
