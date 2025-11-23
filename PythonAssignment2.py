'''
Ifsalary<30,000→5%
Ifsalaryis30,000–70,000→15%
Ifsalary>70,000→25%
'''

def calculate_tax(salary):
    if salary < 30000:
        tax_rate = 0.05
    elif 30000 <= salary <= 70000:
        tax_rate = 0.15
    else:
        tax_rate = 0.25
    tax = salary * tax_rate
    return tax

# Example usage
salary = float(input("Enter your salary:"))
tax = calculate_tax(salary)
print(f"The calculated tax on a salary of {salary} is: {tax}")