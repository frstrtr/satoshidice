import random

# Initialize variables to track user's balance, total bets, and total losses
balance = 100  # Starting balance (e.g., 1 Bitcoin)
total_bets = 0
total_losses = 0

# Define winning thresholds and their corresponding multipliers
winning_thresholds = [
    65,
    649,
    1289,
    2596,
    6488,
    21627,
    32440,
    43253,
    48103,
    58982,
    61790,
]

multipliers = [1000, 100, 50, 25, 10, 3, 2, 1.5, 1.33, 1.1, 1.05]

while balance > 0:
    # User inputs bet amount and selects a multiplier
    bet_amount = int(
        input(
            f"Your Balance: {balance} satoshis\nEnter Bet Amount (0 to stop playing): "
        )
    )

    # Check if the user wants to stop playing
    if bet_amount <= 0:
        break

    if bet_amount > balance:
        print("Insufficient balance. Please enter a valid bet amount.")
        continue

    # Calculate the probability and print it along with the multiplier
    total_outcomes = 65536  # Total possible outcomes (0-65535)

    for index, threshold in enumerate(winning_thresholds, start=1):
        probability = (threshold + 1) / total_outcomes * 100
        multiplier = multipliers[index - 1]
        print(
            f"{index}\t - Multiplier: {multiplier},\t Probability: {probability:.2f}%"
        )

    multiplier_choice = int(input(f"Select Multiplier (1-{len(multipliers)}): "))

    if multiplier_choice < 1 or multiplier_choice > len(multipliers):
        print("Invalid multiplier choice. Please select a valid multiplier.")
        continue

    # Deduct the bet amount from the user's balance
    balance -= bet_amount

    # Simulate the random number generation (0-65,535)
    random_number = random.randint(0, 65535)

    # Determine the outcome and multiplier
    outcome = "Lose"
    payout = 0
    if random_number <= winning_thresholds[multiplier_choice - 1]:
        outcome = "Win"
        payout = multipliers[multiplier_choice - 1] * bet_amount
        balance += payout
    else:
        total_losses += bet_amount

    total_bets += bet_amount

    print(f"Random Number: {random_number}, You {outcome}!")
    print(f"Payout: {payout} satoshis\n")

print(f"Total Bets: {total_bets} satoshis")
print(f"Total Losses: {total_losses} satoshis")
print(f"Final Balance: {balance} satoshis")
