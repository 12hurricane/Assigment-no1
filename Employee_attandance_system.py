employees = {  
    "Ali": 26,  
    "Sara": 23,  
    "Ahmed": 18,  
    "Ayesha": 30  
}  

def calculate_salary(days):  
    if days == 26:
        return 30000
    elif 20 <= days <= 25:
        return 30000 * 0.80
    elif days < 20:
        return 30000 * 0.50
    else:
        return "Invalid attendance"

full_salary_count = 0  # Challenge: Counter for employees receiving full salary

for name, days in employees.items():  
    salary = calculate_salary(days)  
  
    if salary == 30000:
        full_salary_count += 1
        print(f"Employee: {name}, Salary: Rs. {salary}")
    elif salary == "Invalid attendance":
        print(f"Employee: {name}, Attendance: {days} days ({salary})")
    else:
        print(f"Employee: {name}, Salary: Rs. {salary}")

print(f"\nNumber of employees who received full salary: {full_salary_count}")