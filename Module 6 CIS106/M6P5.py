# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:28:23 2026

@author: shama
"""

last_name = input("Enter employee last name: ").strip()
salary = float(input("Enter employee salary ($): "))
job_level = int(input("Enter job level: "))


if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5 and job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10


bonus_amount = salary * bonus_rate


print("\n" + "="*35)
print(f"{'Payroll Summary':<18}{'Details/Figures':>15}")
print("="*35)
print(f"{'Employee Last Name:':<18}{last_name:>15}")
print(f"{'Job Level:':<18}{job_level:>15.2f}")
print(f"{'Salary:':<18}{salary:>15.2f}")
print(f"{'Bonus Rate:':<18}{bonus_rate:>15.2f}")
print("-"*35)
print(f"{'Computed Bonus:':<18}{bonus_amount:>15.2f}")
print("="*35)