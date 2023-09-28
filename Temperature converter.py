import tkinter as tk
from tkinter import ttk


def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""

    return (fahrenheit - 32) * 5/9

def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Create labels
        self.label_unit = tk.Label(root, text="Select Unit:")
        self.label_value = tk.Label(root, text="Enter Value:")

        # Create unit option menu
        self.unit_var = tk.StringVar()
        self.unit_options = ["Fahrenheit", "Celsius"]
        self.unit_menu = ttk.Combobox(root, textvariable=self.unit_var, values=self.unit_options)
        self.unit_menu.set(self.unit_options[0])  # Set default unit

        # Create entry widget for value
        self.entry_value = tk.Entry(root)

        # Create conversion buttons
        self.button_convert = tk.Button(root, text="Convert", command=self.convert_temperature)

        # Create result label
        self.label_result = tk.Label(root, text="Result:")

        # Place widgets on grid
        self.label_unit.grid(row=0, column=0, pady=10)
        self.unit_menu.grid(row=0, column=1, pady=10)
        self.label_value.grid(row=1, column=0, pady=10)
        self.entry_value.grid(row=1, column=1, pady=10)
        self.button_convert.grid(row=2, column=0, columnspan=2, pady=10)
        self.label_result.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            value = float(self.entry_value.get())
            selected_unit = self.unit_var.get()

            if selected_unit == "Fahrenheit":

                result = f_to_c(value)
                self.label_result.config(text=f"{value:.2f} °F is {result:.2f} °C")
            elif selected_unit == "Celsius":
                result = c_to_f(value)
                self.label_result.config(text=f"{value:.2f} °C is {result:.2f} °F")

        except ValueError:
            self.label_result.config(text="Invalid Input")


if __name__ == "__main__":
    root = tk.Tk()
    converter = TemperatureConverter(root)

    
    root.mainloop()
