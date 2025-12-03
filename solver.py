import sys

def load_words(path="/usr/share/dict/words"):
    """Loads words from the system dictionary."""
    try:
        with open(path, 'r') as f:
            # Read all words, strip whitespace, and convert to lowercase
            return [line.strip().lower() for line in f]
    except FileNotFoundError:
        print(f"Error: Dictionary file not found at {path}")
        sys.exit(1)

def solve(central_letter, other_letters, words):
    """
    Finds words that match the Spelling Bee criteria.
    
    Args:
        central_letter: The mandatory letter.
        other_letters: The other allowed letters.
        words: A list of valid English words.
        
    Returns:
        A set of matching words.
    """
    central_letter = central_letter.lower()
    allowed_letters = set(central_letter + other_letters.lower())
    
    matches = set()
    
    for word in words:
        # Criteria 1: Length 4 or more
        if len(word) < 4:
            continue
            
        # Criteria 2: Must contain central letter
        if central_letter not in word:
            continue
            
        # Criteria 3: Must only contain allowed letters
        # We check if the set of characters in the word is a subset of allowed_letters
        if set(word).issubset(allowed_letters):
            matches.add(word)
            
    return sorted(list(matches))

def main():
    print("Welcome to the Spelling Bee Solver!")
    print("Loading dictionary...")
    words = load_words()
    print(f"Dictionary loaded with {len(words)} words.")
    
    while True:
        print("\n--- New Puzzle ---")
        central = input("Enter the central letter: ").strip()
        if not central or len(central) != 1 or not central.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        others = input("Enter the other 6 letters (no spaces): ").strip()
        if not others or not others.isalpha():
             print("Please enter valid letters.")
             continue

        print(f"\nSolving for Central: '{central}', Others: '{others}'...")
        found_words = solve(central, others, words)
        
        if found_words:
            print(f"\nFound {len(found_words)} words:")
            # Sort by length (descending) then alphabetical
            found_words.sort(key=lambda x: (-len(x), x))
            
            for word in found_words:
                is_pangram = set(word) == set(central + others)
                prefix = "🌟 " if is_pangram else "  "
                print(f"{prefix}{word}")
        else:
            print("No words found.")
            
        if input("\nSolve another? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
