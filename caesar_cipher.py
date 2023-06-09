def caesar_cipher(text: str, shift: int):
    """
    Encrypts the given text using the Caesar cipher.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not isinstance(shift, int):
        raise ValueError("shift must be an integer")

    # initialize an empty string for the result
    result = ""

    # loop over each character in the text
    for char in text:
        # check if the character is an alphabet letter
        if char.isalpha():
            # determine the unicode offset based on whether the letter is uppercase or lowercase
            unicode_offset = 65 if char.isupper() else 97
            # encrypt the letter
            encrypted_char = chr(
                (ord(char) + shift - unicode_offset) % 26 + unicode_offset
            )
            # append the encrypted char to the result
            result += encrypted_char
        else:
            # append it as is
            result += char
    return result
