def calculateNetSalary(salary,tax_rate):
    return salary-(salary*tax_rate)

salary=75000.5
tax_rate=0.18
print(f"{calculateNetSalary(salary,tax_rate):.2f}")