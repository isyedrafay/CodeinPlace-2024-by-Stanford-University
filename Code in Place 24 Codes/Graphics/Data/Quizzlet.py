def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo",
    }
    score = 0

    for english_word in translations:
        spanish_translation = translations[english_word]
        result = ask_question(english_word, spanish_translation)
        if result:
            score += 1

    print(f"You got {score}/{len(translations)} words correct, come study again soon!")


def ask_question(english_word, spanish_translation):
    """
    this asks question from user and return if ans is correct or not (bool)
    """
    user_guess = input(f"What is the Spanish translation for {english_word}? ")

    isCorrect = user_guess == spanish_translation

    print(
        "That is correct!\n"
        if isCorrect
        else f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.\n"
    )

    return isCorrect


if __name__ == '__main__':
    main()