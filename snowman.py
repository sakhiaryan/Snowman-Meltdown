import random

# --- Snowman ASCII Art stages ---
STAGES = [
    # Stage 0: Full snowman
    r"""
     ___  
    /___\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    r"""
     ___  
    /___\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    r"""
     ___  
    /___\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    r"""
     ___  
    /___\ 
    """
]

# --- Hilfsfunktionen ---
def get_random_word():
    # Platzhalter-Wortliste für jetzt – ersetzbar durch Datei/API
    words = ["python", "snow", "winter", "freeze", "icicle"]
    return random.choice(words)

def display_game_state(mistakes, secret_word, guessed_letters):
    # Safety: begrenze mistakes auf gültigen Bereich
    stage_index = max(0, min(mistakes, len(STAGES) - 1))
    print(STAGES[stage_index])

    # Wortanzeige: bereits geratene Buchstaben zeigen, Rest Unterstriche
    display = []
    for ch in secret_word:
        display.append(ch if ch in guessed_letters else "_")
    print("Word:", " ".join(display))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown! ❄️")
    # Schritt 2: Nur Zustand anzeigen + eine Eingabe abfragen (Logik später erweitern)
    display_game_state(mistakes, secret_word, guessed_letters)

    # Eine Probe-Eingabe (die echte Prüf-Logik folgt in späteren Schritten)
    guess = input("Guess a letter: ").strip().lower()
    print("You guessed:", guess)

    # Zum Testen kannst du hier mistakes manuell erhöhen und erneut anzeigen:
    # mistakes += 1
    # display_game_state(mistakes, secret_word, guessed_letters)

if __name__ == "__main__":
    play_game()