import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Initialize CurrencyRates object
        self.c = CurrencyRates()

        # Predefined list of currencies
        self.currency_list = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]

        # Create labels and entry widgets
        self.label_amount = tk.Label(root, text="Amount:")
        self.label_from = tk.Label(root, text="From Currency:")
        self.label_to = tk.Label(root, text="To Currency:")
        self.entry_amount = tk.Entry(root)
        
        # Create dropdown menus for currency selection
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.from_currency_menu = ttk.Combobox(root, textvariable=self.from_currency_var, values=self.currency_list)
        self.to_currency_menu = ttk.Combobox(root, textvariable=self.to_currency_var, values=self.currency_list)
        self.from_currency_menu.set("USD")  # Set default currency to USD
        self.to_currency_menu.set("USD")  # Set default currency to USD

        # Create convert button
        self.button_convert = tk.Button(root, text="Convert", command=self.convert_currency)

        # Create result label
        self.label_result = tk.Label(root, text="", font=('Arial', 12))

        # Place widgets on grid
        self.label_amount.grid(row=0, column=0, padx=10, pady=10)
        self.label_from.grid(row=1, column=0, padx=10, pady=10)
        self.label_to.grid(row=2, column=0, padx=10, pady=10)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10)
        self.from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
        self.to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
        self.button_convert.grid(row=3, columnspan=2, pady=10)
        self.label_result.grid(row=4, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.entry_amount.get())
            from_currency = self.from_currency_var.get().upper()
            to_currency = self.to_currency_var.get().upper()

            rate = self.c.get_rate(from_currency, to_currency)
            converted_amount = round(amount * rate, 2)

            result_message = f"{amount} {from_currency} is {converted_amount} {to_currency}"
            self.label_result.config(text=result_message)

        except ValueError:
            self.label_result.config(text="Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverterGUI(root)
    root.mainloop()
