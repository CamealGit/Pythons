import tkinter as tk
from tkinter import simpledialog

print("Welcome to the Budget Management App")


class Expense:
    def __init__(self, income, cost, date, category):
        self.income = income
        self.cost = cost
        self.date = date
        self.category = category

    def display(self):
        return f"Your income: {self.income}\nYour cost: {self.cost}\nDate: {self.date}\nCategory: {self.category}"

    def calculate(self):
        result = self.income - self.cost
        return result


root = tk.Tk()
root.geometry("500x500")
root.withdraw()

expenses_list = []
total_income = 0
query = 'y'

while query.lower() == 'y':
    try:
        income = float(simpledialog.askstring("Input", "Enter your income: "))
        cost = float(simpledialog.askstring("Input", "Enter your cost: "))
    except ValueError:
        print("Invalid input entered")
        break

    date = simpledialog.askstring("Input", "Enter the date DD-MM-YYYY: ")
    category = simpledialog.askstring("Input", "Enter the category: ")
    query = simpledialog.askstring("Input", "Do you want to continue entering data? y/n")

    user_expense = Expense(income, cost, date, category)
    user_expense.display()

    expenses_list.append(user_expense)
    total_income += user_expense.calculate()

if query.lower() != "y":
    print("Thank you, here are your statistics \n-----------------------------")
    for user_expense in expenses_list:
        print(user_expense.display())
        print(f"Your balance is: {user_expense.calculate()} $")
        print("-----------------------------")
    print(f"Total income: {total_income} $")

    root.destroy()
