vowels = ["a", "e", "i", "o", "u"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def vowels_character(char: str) -> str:
    if char == "a":
        return "z"
    else:
        index = alphabet.index(char)
        while True:
            index = (index - 1) % len(alphabet)
            if alphabet[index] not in vowels:
                return alphabet[index]


def consonants_character(char: str) -> str:
    if char == "z":
        return "a"
    else:
        index = alphabet.index(char)
        while True:
            index = (index + 1) % len(alphabet)
            if alphabet[index] in vowels:
                return alphabet[index]


def replace_character(word: str) -> str:
    return "".join(vowels_character(char) if char in vowels else consonants_character(char) for char in word)


if __name__ == "__main__":
    print(replace_character("abcdtuvwxyz"))  # Output: "zeeeutaaaaa"

