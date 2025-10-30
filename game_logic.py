import random
from ascii_art import STAGES


def get_random_word():
    """Returns a random word for the game"""
    words = ["python", "winter", "freeze", "icicle", "snowflake", "holiday", "cold"]
    return random.choice(words)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display snowman stage and word progress"""
    stage_index = min(mistakes, len(STAGES) - 1)
    print("\n" + "=" * 40)
    print(STAGES[stage_index])
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("-" * 40)

    display_word = " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])
    print(f"Word: {display_word}")
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print("=" * 40 + "\n")


def play_game():
    """Main game loop"""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown! ☃️")
    print("Guess the word before the snowman melts!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # win/lose checks
        if all(l in guessed_letters for l in secret_word):
            print(f"🎉 You saved the snowman! The word was '{secret_word}'.\n")
            break
        if mistakes >= max_mistakes:
            print(f"💧 The snowman melted! The word was '{secret_word}'.\n")
            break

        # input validation
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single letter (A–Z).")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Nice! '{guess}' is in the word.")
        else:
            print(f"❌ Nope! '{guess}' is not in the word.")
            mistakes += 1


def start_game():
    """Allows replay"""
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("\nThanks for playing Snowman Meltdown! ❄️\n")
            break