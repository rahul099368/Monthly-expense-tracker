name = input("enter your name :- ")
monthly_income = int(input("enter your monthly income :- "))
rent = int(input("enter your monthly rent :- "))
food_expenses = int(input("enter your monthly food expenses :- "))
travel_expenses = int(input("enter your monthly travel expenses :- "))
entertainment_expenses = int(input("enter your monthly entertainment expenses :- "))
other_expenses = int(input("enter your mothly other expenses :- "))
saving_target = float(input("enter your saving target :- "))
total_expenses = rent + food_expenses + travel_expenses + entertainment_expenses + other_expenses
remaining_money = monthly_income - total_expenses
saving_percentage = (remaining_money / monthly_income) * 100
daily_avg_spending = total_expenses / 30
weekly_avg_spending = total_expenses / 7

print("------MONTHLY EXPENSES REPORT------")
print(f"name: {name}")
print(f"Monthly Income: ₹{monthly_income}")
print(f"Total Expenses: ₹{total_expenses}")
print(f"Remaining Money: ₹{remaining_money}")
print(f"Saving Percentage: {saving_percentage:.2f}%")
print("------BONUS REPORT------")
print(f"Daily Average Spending: ₹{daily_avg_spending:.2f}")
print(f"Weekly verage spending: ₹{weekly_avg_spending:.2f}")
if saving_target >= saving_percentage:
 target = saving_target - saving_percentage
 print(f"Your Saving Target Left For This Month: {target}%")
else :
 target = saving_percentage - saving_target
 print(f"You Save More {target}% From Your Montlhy Saving Target")


