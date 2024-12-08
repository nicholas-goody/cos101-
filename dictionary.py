def get_spanish_translations(category, words):
    """
    Function to get the Spanish translations for a list of words in a specific category.
    :param category: The category of the words (e.g., 'greetings', 'colors').
    :param words: A list of English words to translate.
    :return: A dictionary with English words as keys and Spanish translations as values.
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
    if category not in spanish_dict:
        return f"Category '{category}' not found."

    translations = {}
    for word in words:
        translation = spanish_dict[category].get(word, f"'{word}' not found in '{category}'")
        translations[word] = translation

    return translations

# Example usage
words_to_translate = ["hello", "please", "goodbye"]
category = "greetings"
translations = get_spanish_translations(category, words_to_translate)
print(translations)  # Output: {'hello': 'hola', 'please': 'por favor', 'goodbye': 'adiós'}

# Example usage with colors
words_to_translate = ["red", "blue", "pink"]
category = "colors"
translations = get_spanish_translations(category, words_to_translate)
print(translations)  # Output: {'red': 'rojo', 'blue': 'azul', 'pink': "'pink' not found in 'colors'"}
