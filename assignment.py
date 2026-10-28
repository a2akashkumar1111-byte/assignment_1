user_name = input("Enter student name :")
income = float(input("monthly income :"))
mobile = float(input("mobile/internet expenses :"))
food_expense = float(input("Amount spend on food :"))
travel_expense = float(input("Amount spend on travel :"))
study = float(input("study material expenses :"))
other = float(input("other expenses :"))
saving_goal = float(input("Enter your saving goal :"))
total_expenses = mobile + food_expense + travel_expense + study + other
remaining_balance = income - total_expenses
saving_percentage = (remaining_balance * 100) / income
daily_spending = total_expenses / 30
weekly_spending = total_expenses / 4
print(f"Hello {user_name}, your total expenses are {total_expenses} and your remaining balance is {remaining_balance}. /n Your saving percentage is {saving_percentage:.2f}%")
print(f"Your daily spending is {daily_spending:.2f} and your weekly spending is {weekly_spending:.2f}")