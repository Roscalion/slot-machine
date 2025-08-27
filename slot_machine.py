import random

# Define a dictionary of symbols and their respective payouts for three of a kind
# These represent typical slot machine symbols in a simplified form.
SYMBOL_PAYOUTS = {
    'Cherry': 5,
    'Lemon': 10,
    'Orange': 15,
    'Plum': 20,
    'Bell': 25,
    'Bar': 50,
    'Seven': 100,
}


def spin_slot_machine() -> list[str]:
    """Simulate spinning a simple three‑reel slot machine.

    Returns a list of three randomly chosen symbols.
    """
    return random.choices(list(SYMBOL_PAYOUTS.keys()), k=3)


def calculate_payout(spin_result: list[str]) -> int:
    """Calculate the payout based on the slot machine result.

    If all three symbols match, return the corresponding payout defined in
    SYMBOL_PAYOUTS. If only two symbols match, return a small prize (2 credits).
    Otherwise, return 0.
    """
    # Check if all three symbols match
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return SYMBOL_PAYOUTS[spin_result[0]]

    # Check for exactly two matching symbols
    for symbol in set(spin_result):
        if spin_result.count(symbol) == 2:
            return 2

    # No matches
    return 0


def interactive_slot_machine(starting_credits: int = 100, cost_per_spin: int = 5) -> None:
    """Run an interactive slot machine game in the terminal.

    The player starts with a number of credits and pays a fixed cost per spin.
    After each spin, the result and any winnings are displayed. The game ends
    when the player chooses to stop or runs out of credits.

    Args:
        starting_credits: Number of credits the player starts with.
        cost_per_spin: Cost deducted from the player's credits on each spin.
    """
    credits = starting_credits
    print("Welcome to the Simple Slot Machine Game!")
    print(
        f"You start with {credits} credits. Each spin costs {cost_per_spin} credits.\n"
    )

    while credits >= cost_per_spin:
        # Prompt user to spin
        spin_input = input(
            "Do you want to spin the slot machine? (y/n): "
        ).strip().lower()
        if spin_input != "y":
            break

        # Deduct the cost of a spin
        credits -= cost_per_spin

        # Perform the spin
        result = spin_slot_machine()
        payout = calculate_payout(result)
        credits += payout

        # Display the result and payout
        print(f"\nSpin result: {' | '.join(result)}")
        if payout > 0:
            print(f"Congratulations! You won {payout} credits!")
        else:
            print("Sorry, you didn't win this time.")
        print(f"Credits remaining: {credits}\n")

    print("\nGame Over!\n")
    print(f"Final credits: {credits}")


def simulate_spins(num_spins: int = 10) -> None:
    """Simulate a series of slot machine spins automatically.

    This function is useful for demonstrating the slot machine logic without
    requiring interactive input. It will spin the slot machine a given number
    of times and print the results and payouts for each spin.

    Args:
        num_spins: Number of spins to simulate.
    """
    print(f"Simulating {num_spins} slot machine spins...\n")
    for i in range(1, num_spins + 1):
        result = spin_slot_machine()
        payout = calculate_payout(result)
        print(f"Spin {i}: {' | '.join(result)} -> Payout: {payout}")


if __name__ == "__main__":
    # If executed directly, first show a few simulated spins and then
    # offer the interactive game. This makes it convenient to see how
    # the game works both automatically and interactively.
    simulate_spins(5)
    print("\nNow starting the interactive game. You can skip by pressing 'n'.\n")
    interactive_slot_machine()