# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:03:21 2026

@author: shama
"""

part_number = input("Enter part number: ").strip()
quantity = int(input("Enter quantity: "))


if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00


total_cost = quantity * unit_cost


print("\n" + "="*35)
print(f"{'Item Description':<18}{'Value':>15}")
print("="*35)
print(f"{'Part Number:':<18}{part_number:>15}")
print(f"{'Quantity:':<18}{quantity:>15.2f}")
print(f"{'Cost Per Unit:':<18}{unit_cost:>15.2f}")
print("-"*35)
print(f"{'Total Cost:':<18}{total_cost:>15.2f}")
print("="*35)