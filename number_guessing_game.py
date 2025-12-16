import random

print("🎮 NUMBER GUESSING GAME 🎮")

while True:
    print("\nChoose Difficulty Level:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    level = input("Enter level (1/2/3): ")

    if level == "1":
        max_num = 50
        max_attempts = 10
    elif level == "2":
        max_num = 100
        max_attempts = 7
    elif level == "3":
        max_num = 200
        max_attempts = 5
    else:
        print("❌ Invalid choice")
        continue

    secret = random.randint(1, max_num)
    attempts = 0

    print(f"\nGuess a number between 1 and {max_num}")

    while attempts < max_attempts:
        try:
            guess_input = input("Enter your guess: ")
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Exiting game.")
            exit()
        try:
            guess = int(guess_input)
        except ValueError:
            print("❌ Please enter a valid integer.")
            continue

        if not 1 <= guess <= max_num:
            print(f"⚠️ Please enter a number between 1 and {max_num}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low 🔽")
        elif guess > secret:
            print("Too high 🔼")
        else:
            print(f"🎉 You won in {attempts} attempts!")
            break
    else:
        print(f"😢 You lost! The number was {secret}")

    try:
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Exiting game.")
        break
    if play_again not in ("yes", "y"):
        print("Thanks for playing 👋")
        break
