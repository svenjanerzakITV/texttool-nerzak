def create_acronym(phrase: str) -> str:
    """Create an acronym from a phrase.

    Args:
        phrase (str): The phrase to create an acronym from.

    Returns:
        str: The acronym.
    """
    if not isinstance(phrase, str):
        raise TypeError("Phrase must be a string.")

    words = phrase.split()
    if len(words) == 0:
        raise ValueError("Phrase must contain at least one word.")

    articles = {"a", "an", "the", "and", "but", "or", "nor", "on", "at", "to", "by", "in"}

    acronym = ""
    for word in words:
        if word.lower() not in articles:
            acronym += word[0].upper()

    return acronym