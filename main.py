from data import alphabet_to_morse, morse_to_alphabet

def encode(decoded):
    morsestring = []

    decoded = decoded.upper()
    words = decoded.split(" ")
    for word in words:
        letters = list(word)

        morseword = []
        for letter in letters:
            morseletter = alphabet_to_morse[letter]
            morseword.append(morseletter)

        word = "/".join(morseword)
        morsestring.append(word)

    return " ".join(morsestring)


def decode(encoded):
    characterstring = []

    words = encoded.split(" ")
    for word in words:
        letters = word.split("/")

        characterword = []
        for letter in letters:
            characterletter = morse_to_alphabet[letter]
            characterword.append(characterletter)

        word = "".join(characterword)
        characterstring.append(word)

    return " ".join(characterstring)

stuff = input("Enter the stuff: ")
print(encode(stuff))
print(decode(encode(stuff)))