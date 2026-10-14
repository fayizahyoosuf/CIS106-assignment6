# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:14:06 2026

@author: shama
"""

tickets = int(input("Enter number of concert tickets: "))


if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10 and tickets <= 24:
    price_per_ticket = 60.00
elif tickets >= 5 and tickets <= 9:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00


total_cost = tickets * price_per_ticket


print("\n" + "="*35)
print(f"{'Ticket Summary':<18}{'Totals':>15}")
print("="*35)
print(f"{'Number of Tickets:':<18}{tickets:>15.2f}")
print(f"{'Price Per Ticket:':<18}{price_per_ticket:>15.2f}")
print("-"*35)
print(f"{'Total Cost:':<18}{total_cost:>15.2f}")
print("="*35)