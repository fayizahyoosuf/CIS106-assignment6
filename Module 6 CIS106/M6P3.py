# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:08:31 2026

@author: shama
"""

principle = float(input("Enter CD principle amount ($): "))
years = int(input("Enter years to maturity: "))


if principle > 100000:
    if years == 5:
        interest_rate = 0.06
    else:
        interest_rate = 0.02
elif principle >= 50000 and principle <= 100000:
    if years == 10:
        interest_rate = 0.05
    elif years == 5:
        interest_rate = 0.04
    else:
        interest_rate = 0.02
else:
    interest_rate = 0.02


first_year_interest = principle * interest_rate


print("\n" + "="*40)
print(f"{'CD Component':<22}{'Financials':>15}")
print("="*40)
print(f"{'Principle Amount:':<22}{principle:>15.2f}")
print(f"{'Years to Maturity:':<22}{years:>15.2f}")
print(f"{'Interest Rate:':<22}{interest_rate:>15.2f}")
print("-"*40)
print(f"{'First Year Interest:':<22}{first_year_interest:>15.2f}")
print("="*40)