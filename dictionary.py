def get_spanish_translation(category, word):
    """
    Function to get the Spanish translation of a word from a specific category.
    :param category: The category of the word (e.g., 'greetings', 'colors').
    :param word: The English word to translate.
    :return: The Spanish translation or a message if not found.
    """
    spanish_dict = {
        "greetings": {
            "hello": "hola",
            "goodbye": "adiós",
            "please": "por favor",
            "thank_you": "gracias",
            "you're_welcome": "de nada"
        },
        "colors": {
            "red": "rojo",
            "blue": "azul",
            "green": "verde",
            "yellow": "amarillo",
            "black": "negro",
            "white": "blanco"
        },
        "numbers": {
            1: "uno",
            2: "dos",
            3: "tres",
            4: "cuatro",
            5: "cinco"
        }
    }

    # Check if category exists
    if category in spanish_dict:
        # Check if the word exists in the category
        if word in spanish_dict[category]:
            return spanish_dict[category][word]
        else:
            return f"'{word}' not found in category '{category}'."
    else:
        return f"Category '{category}' not found."

# Example usage
print(get_spanish_translation("greetings", "hello"))  # Output: hola
print(get_spanish_translation("colors", "blue"))  # Output: azul
print(get_spanish_translation("numbers", 3))  # Output: tres
print(get_spanish_translation("greetings", "hi"))  # Output: 'hi' not found in category 'greetings'.

