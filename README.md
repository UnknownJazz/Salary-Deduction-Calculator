# Salary Deductions Calculator

## Overview
This program calculates salary deductions based on government-mandated contributions in the Philippines, including SSS, PhilHealth, Pag-IBIG, and tax. The code has been refactored in stages to improve readability, modularity, maintainability, and error handling.

## Features
- Computes salary deductions for SSS, PhilHealth, Pag-IBIG, and tax.
- Implements a modular approach with separate functions for each deduction.
- Uses Object-Oriented Programming (OOP) for better structure and scalability.
- Includes input validation and error handling for robustness.

## Refactored Changes

### **Stage 1: Improve Code Readability**
- Renamed variables to be more descriptive (e.g., `sss` → `sss_contribution`).
- Applied consistent formatting and spacing for clarity.
- Used proper indentation and line breaks for better readability.

### **Stage 2: Convert to Modular Functions**
- Extracted deduction calculations into separate functions:
  - `calculate_sss()`
  - `calculate_philhealth(salary)`
  - `calculate_pagibig()`
  - `calculate_tax()`
- Ensured that the `compute_deductions()` function only handles logic and calls helper functions.

### **Stage 3: Implement OOP**
- Created a `SalaryDeductions` class to encapsulate all deduction-related calculations.
- Defined instance methods for each contribution calculation.
- Introduced the `compute_deductions()` method to return all deductions in a structured format.

### **Stage 4: Add Input Validation & Error Handling**
- Wrapped salary input in a `try-except` block to catch non-numeric values.
- Added validation to prevent negative salary inputs.
- Ensured program does not crash due to invalid input.

## Technical Debt Identified
- **Poor Naming Conventions:** Variable names were unclear and inconsistent.
- **Lack of Modular Functions:** The original code had all calculations in a single function, making it hard to maintain.
- **Hardcoded Values:** SSS, Pag-IBIG, and tax values were fixed instead of dynamically determined.
- **No Error Handling:** No input validation, leading to potential runtime errors.
- **Code Duplication:** Some calculations could be reused but were inline instead.

## Refactoring Improvements Made
- Improved readability with descriptive variable names and better formatting.
- Refactored into modular functions for maintainability and clarity.
- Implemented OOP to encapsulate related calculations within a class.
- Added input validation and error handling to make the program more robust.

## Challenges Faced & Solutions
- **Ensuring Modular Functions Remain Simple:** Some functions were too complex initially, so they were broken down further.
- **Handling Fixed Tax Values:** Placeholder values were kept but structured to allow future dynamic computation.
- **Error Handling for User Input:** Initially, only numeric checks were included, but further validation was added to catch negative inputs.

## Usage
### **Running the Program**
1. Run the script in a Python environment:
   ```sh
   python salary_deduction_calculator.py
   ```
2. Enter a valid salary when prompted.
3. The program will output the gross salary, deductions, and net salary.

### **Example Output**
```
Enter your monthly salary: 30000
Gross Salary: 30000.00
SSS Deduction: 1200.00
PhilHealth Deduction: 750.00
Pag-IBIG Deduction: 100.00
Tax Deduction: 1875.00
Total Deductions: 3925.00
Net Salary: 26075.00
```

## Future Improvements
- Implement dynamic tax computation based on tax brackets.
- Allow deductions to be read from an external configuration file.
- Add unit tests for each function.

## Author
Chas Omer M. Madlos


