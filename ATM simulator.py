import tkinter as tk
from tkinter import messagebox

class ATMGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")

        # Initialize ATM object
        self.atm = ATM()

        # Create labels
        self.label_balance = tk.Label(root, text="Balance: $0.00", font=('Arial', 14))

        # Create entry and labels for deposit and withdrawal
        self.entry_amount = tk.Entry(root, font=('Arial', 12))
        self.label_deposit = tk.Label(root, text="Enter Deposit Amount:", font=('Arial', 12))
        self.label_withdraw = tk.Label(root, text="Enter Withdrawal Amount:", font=('Arial', 12))

        # Create buttons
        self.button_check_balance = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.button_deposit = tk.Button(root, text="Deposit", command=self.deposit)
        self.button_withdraw = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.button_exit = tk.Button(root, text="Exit", command=root.destroy)

        # Place widgets on grid
        self.label_balance.grid(row=0, column=0, columnspan=2, pady=10)
        self.button_check_balance.grid(row=1, column=0, columnspan=2, pady=10)
        self.label_deposit.grid(row=2, column=0, pady=10)
        self.entry_amount.grid(row=2, column=1, pady=10)
        self.button_deposit.grid(row=3, column=0, columnspan=2, pady=10)
        self.label_withdraw.grid(row=4, column=0, pady=10)
        self.button_withdraw.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_exit.grid(row=6, column=0, columnspan=2, pady=10)

    def check_balance(self):
        balance_message = self.atm.check_balance()
        messagebox.showinfo("Balance", balance_message)

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            deposit_message = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", deposit_message)
            self.update_balance_label()

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            withdraw_message = self.atm.withdraw(amount)
            messagebox.showinfo("Withdrawal", withdraw_message)
            self.update_balance_label()

    def get_amount(self):
        try:
            amount = float(self.entry_amount.get())
            return amount
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
            return None

    def update_balance_label(self):
        balance_message = self.atm.check_balance()
        self.label_balance.config(text=balance_message)

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return f"Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"

if __name__ == "__main__":
    root = tk.Tk()
    atm_gui = ATMGUI(root)
    root.mainloop()
