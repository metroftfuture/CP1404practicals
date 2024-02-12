"""
CP1404: Practical 1
Student name: Tenzin Yoezer
Program: shop calculator
"""
discount = 0.1
total_price = 0

num = int(input("Enter number of items: "))
while num < 0:
    num = int(input("Number of items should be positive. Enter again: "))

for items in range(num):
    price = float(input("Price of item: "))
    total_price += price

if total_price >= 100:
    discount_price = total_price * discount
    final_price = total_price - discount_price
else:
    final_price = total_price

print(f"Total price for {num} items is ${final_price:.2f}")