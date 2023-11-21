# Define rules for performance evaluation
def evaluate_performance(employee):
    if employee['productivity'] > 80 and employee['attendance'] > 90:
        return "Excellent"
    elif employee['productivity'] > 70 and employee['attendance'] > 80:
        return "Good"
    else:
        return "Needs Improvement"

# Initialize an empty list to store employee evaluations
employee_evaluations = []

# Define the number of employees to evaluate
num_employees = int(input("Enter the number of employees to evaluate: "))

# Loop to collect employee information and evaluate performance
for i in range(num_employees):
    employee = {}
    employee['name'] = input(f"Enter employee {i + 1} name: ")
    employee['productivity'] = float(input("Enter employee productivity (0-100): "))
    employee['attendance'] = float(input("Enter employee attendance (0-100): "))
    
    # Evaluate employee performance
    performance = evaluate_performance(employee)
    
    # Append the evaluation to the list
    employee_evaluations.append((employee['name'], performance))

# Output the evaluations for all employees
print("Employee Evaluations:")
for name, performance in employee_evaluations:
    print(f"{name}'s performance is: {performance}")
