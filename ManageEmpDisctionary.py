employee_records = {
    "john": {"age": 30, "department": "HR", "Salary": 50000},
    "bob": {"age": 32, "department": "IT", "Salary": 80000},
    "lam": {"age": 35, "department": "C-level", "Salary": 180000},
    "Pam": {"age": 30, "department": "HR", "Salary": 40000},
    "Ram": {"age": 32, "department": "IT", "Salary": 90000},
    "Lax": {"age": 35, "department": "C-level", "Salary": 1180000}
}

def AddOrUpdateEmployee(employee_records, name, age, dept, salary):
    employee_records[name] = {"age": age, "department": dept, "Salary": salary}

def Calculate_average_salary(employee_records):
    total_salary = sum(details["Salary"] for details in employee_records.values())
    total_average_salary = total_salary / len(employee_records) if employee_records else 0;
    return total_average_salary


print(f'Average Salary of total employee is {Calculate_average_salary(employee_records)}')

