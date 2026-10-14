# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:31:15 2026

@author: shama
"""

quantity = int(input("Enter the quantity of widgets: "))


if quantity > 10000:
    price = 10.00
elif quantity >= 5000 and quantity <= 10000:
    price = 20.00
else:
    price = 30.00

# Calculations
extended_price = quantity * price
tax_amount = extended_price * 0.07
total_cost = extended_price + tax_amount


print("\n" + "="*35)
print(f"{'Description':<18}{'Amount':>15}")
print("="*35)
print(f"{'Quantity:':<18}{quantity:>15.2f}")
print(f"{'Price Per Unit:':<18}{price:>15.2f}")
print(f"{'Extended Price:':<18}{extended_price:>15.2f}")
print(f"{'Tax Amount (7%):':<18}{tax_amount:>15.2f}")
print("-"*35)
print(f"{'Total Cost:':<18}{total_cost:>15.2f}")
print("="*35)