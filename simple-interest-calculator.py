# Simple Interest Calculator

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display result
print(f"Simple Interest = {simple_interest}")
