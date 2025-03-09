def compute_deductions(monthly_salary):
    sss_contribution = 1200
    philhealth_contribution = (monthly_salary * 0.05) / 2
    pagibig_contribution = 100
    tax_deduction = 1875  # Placeholder for fixed tax

    total_deductions = (
        sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
    )
    net_salary = monthly_salary - total_deductions

    print("Gross Salary:", monthly_salary)
    print("SSS Deduction:", sss_contribution)
    print("PhilHealth Deduction:", philhealth_contribution)
    print("Pag-IBIG Deduction:", pagibig_contribution)
    print("Tax Deduction:", tax_deduction)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)


salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)
