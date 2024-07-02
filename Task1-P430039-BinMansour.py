# Display a friendly greeting message
print("\nHi there! Welcome to the Investment Interest Calculator\n")

# Loop to receive valid user inputs
while True:
    try:
        # Collect user inputs for the initial fund, yearly interest rate, and time span in years
        initial_fund = float(input("Enter your initial fund amount: $"))
        yearly_interest_rate = int(input("Enter the yearly interest rate (%): "))
        time_span = int(input("Enter the time span in years: "))

        # Validate inputs to ensure they are positive numbers
        if initial_fund <= 0 or yearly_interest_rate <= 0 or time_span <= 0:
            print("Please input positive numbers for all fields.")
        else:
            break # Exit the loop if inputs are valid
    except ValueError:
        print("Incorrect input, please input numeric values.")

# Set initial balance to the initial fund amount
current_balance = initial_fund

# Calculate interest and update balance for each year
for year in range(1, time_span + 1):
    interest_earned = (current_balance * yearly_interest_rate) / 100
    current_balance += interest_earned
    print(f"By the end of year {year}, your balance is ${current_balance:.2f} and the interest gained is ${interest_earned:.2f}")

# Display the final balance after the specified number of years
print(f"\nAfter {time_span} years, your total balance will be ${current_balance:.2f}")
