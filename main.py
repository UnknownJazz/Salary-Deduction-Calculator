def calculate_sss():
    return 1200

def calculate_philhealth(salary):
    return (salary * 0.05) / 2

def calculate_pagibig():
    return 100

def calculate_tax():
    return 1875  # Placeholder for now

def compute_deductions(salary):
    sss_contribution = calculate_sss()
    philhealth_contribution = calculate_philhealth(salary)
    pagibig_contribution = calculate_pagibig()
    tax_deduction = calculate_tax()

    total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
    net_salary = salary - total_deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss_contribution)
    print("PhilHealth Deduction:", philhealth_contribution)
    print("Pag-IBIG Deduction:", pagibig_contribution)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)


salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)
