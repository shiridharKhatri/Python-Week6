def vowConsCounter(character, delimiter = " "):
    """
        This function takes a character as input and returns the number of vowels and consonants in the character
        input/arguments : str
        returns: int, int
        delimiter is the cha character on basis of which we seperate the words from the sentence
    """
    words = character.strip().strip(".!?").split(delimiter)
    vowelCount,consonantCount = 0, 0
    for word in words:
        if word.isdigit():
            continue
        if not word.strip(",:").isalpha():
            return None
        for char in word.strip().strip(",:"):
            if char.upper() in "AEIOU":
                vowelCount += 1
            else:
                consonantCount += 1
    return vowelCount, consonantCount
character = input("Enter any sentence >> ")
print("Number of vowels and consolnants are : ", vowConsCounter(character))
vowelCount, consonantCount = vowConsCounter(character)
print(vowelCount, consonantCount)