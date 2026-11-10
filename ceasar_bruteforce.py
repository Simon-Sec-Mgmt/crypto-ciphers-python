_________ ___________   _____    _________   _____ __________                             
\_   ___ \\_   _____/  /  _  \  /   _____/  /  _  \\______   \                            
/    \  \/ |    __)_  /  /_\  \ \_____  \  /  /_\  \|       _/                            
\     \____|        \/    |    \/        \/    |    \    |   \                            
 \______  /_______  /\____|__  /_______  /\____|__  /____|_  /                            
        \/        \/         \/        \/         \/       \/                             
__________                __        ___________                                           
\______   \_______ __ ___/  |_  ____\_   _____/__________   ____  ____      ______ ___.__.
 |    |  _/\_  __ \  |  \   __\/ __ \|    __)/  _ \_  __ \_/ ___\/ __ \     \____ <   |  |
 |    |   \ |  | \/  |  /|  | \  ___/|     \(  <_> )  | \/\  \__\  ___/     |  |_> >___  |
 |______  / |__|  |____/ |__|  \___  >___  / \____/|__|    \___  >___  > /\ |   __// ____|
        \/                         \/    \/                    \/    \/  \/ |__|   \/     

def decrypt_shift(text, shift):
    """Décale chaque lettre vers l'arrière de `shift` positions."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # on recule de `shift`, modulo 26 pour revenir dans l'alphabet
            decoded = chr((ord(char) - base - shift) % 26 + base)
            result.append(decoded)
        else:
            result.append(char)  # espaces et ponctuation inchangés
    return ''.join(result)


def bruteforce_caesar(ciphertext):
    """Teste les 26 décalages possibles et affiche chaque résultat."""
    print(f"Texte chiffré : {ciphertext}\n")
    for shift in range(26):
        plaintext = decrypt_shift(ciphertext, shift)
        print(f"Shift {shift:2d} : {plaintext}")


# Fréquence moyenne de chaque lettre en anglais (en %), utilisée comme référence
ENGLISH_FREQ = {
    'A': 8.2, 'B': 1.5, 'C': 2.8, 'D': 4.3, 'E': 12.7, 'F': 2.2,
    'G': 2.0, 'H': 6.1, 'I': 7.0, 'J': 0.15, 'K': 0.77, 'L': 4.0,
    'M': 2.4, 'N': 6.7, 'O': 7.5, 'P': 1.9, 'Q': 0.095, 'R': 6.0,
    'S': 6.3, 'T': 9.1, 'U': 2.8, 'V': 0.98, 'W': 2.4, 'X': 0.15,
    'Y': 2.0, 'Z': 0.074,
}


def chi_squared_score(text):
    """Mesure l'écart entre les fréquences de lettres du texte et
    celles attendues en anglais. Plus le score est bas, plus le texte
    ressemble à du vrai anglais."""
    text = text.upper()
    letters = [c for c in text if c.isalpha()]
    n = len(letters)
    if n == 0:
        return float('inf')

    counts = {letter: 0 for letter in ENGLISH_FREQ}
    for c in letters:
        counts[c] += 1

    score = 0.0
    for letter, expected_pct in ENGLISH_FREQ.items():
        observed = counts[letter]
        expected = expected_pct / 100 * n
        if expected > 0:
            score += (observed - expected) ** 2 / expected
    return score


def auto_crack_caesar(ciphertext):
    """Teste les 26 décalages en silence, note chacun par analyse de
    fréquence, et retourne seulement le meilleur candidat — sans
    afficher les 25 autres possibilités."""
    best_shift = None
    best_score = float('inf')
    best_plaintext = None

    for shift in range(26):
        candidate = decrypt_shift(ciphertext, shift)
        score = chi_squared_score(candidate)
        if score < best_score:
            best_score = score
            best_shift = shift
            best_plaintext = candidate

    return best_shift, best_plaintext


if __name__ == "__main__":
    message = input("Texte chiffré à décrypter : ")

    shift, plaintext = auto_crack_caesar(message)
    print(f"Texte chiffré : {message}")
    print(f"Shift détecté : {shift}")
    print(f"Texte déchiffré : {plaintext}")
