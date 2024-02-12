"""
CP1404 : Practical 1
Student name: Tenzin Yozer
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales_boundary = 1000
ten_percent_sales = 10/100
fifteen_percent_sales = 15/100

bonus = 0

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < sales_boundary:
        bonus = sales * ten_percent_sales
    else:
        bonus = sales * fifteen_percent_sales

    print(f"Bonus = {bonus}$")
    sales = float(input("Enter sales: $"))