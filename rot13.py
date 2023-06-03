def rot13(text):
    """
    Encrypts the given text using the ROT13 cipher.
    """

    if not isinstance(text, str):
        raise ValueError("text must be a string!")

    result = ""

    # loop over each character in the text
    for char in text:
        # check if the character is an alphaber letter
        if char.isalpha():
            # determine the unicode offset based on whether the letter is uppercase or lowercase
            unicode_offset = 65 if char.isupper() else 97
            # encrypt the letter
            encrypted_letter = chr((ord(char) + 13 - unicode_offset) % 26 + unicode_offset)
            # append it to result
            result += encrypted_letter
        else:
            # append it as is
            result += char
    return result
