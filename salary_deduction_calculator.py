class SalaryDeductions:
    def __init__(self, salary):
        self.salary = salary

    def calculate_sss(self):
        return 1200

    def calculate_philhealth(self):
        return (self.salary * 0.05) / 2

    def calculate_pagibig(self):
        return 100

    def calculate_tax(self):
        return 1875  # Placeholder for tax calculation

    def compute_deductions(self):
        sss_contribution = self.calculate_sss()
        philhealth_contribution = self.calculate_philhealth()
        pagibig_contribution = self.calculate_pagibig()
        tax_deduction = self.calculate_tax()

        total_deductions = sss_contribution + philhealth_contribution + pagibig_contribution + tax_deduction
        net_salary = self.salary - total_deductions

        return {
            "Gross Salary": self.salary,
            "SSS Deduction": sss_contribution,
            "PhilHealth Deduction": philhealth_contribution,
            "Pag-IBIG Deduction": pagibig_contribution,
            "Tax Deduction": tax_deduction,
            "Total Deductions": total_deductions,
            "Net Salary": net_salary,
        }

def main():
    try:
        salary = float(input("Enter your monthly salary: "))
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        deductions = SalaryDeductions(salary).compute_deductions()

        for key, value in deductions.items():
            print(f"{key}: {value:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
