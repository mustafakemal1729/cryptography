def caesar_cipher(text: str, shift: int) -> str:
    """returns a cipher where each letter in the plaintext is 'shifted' a certain number of places down the alphabet."""
    # initialize an empty string for the result
    result = ""

    # loop over each character in the text
    for char in text:
        # check if the character is an alphabet letter
        if char.isalpha():
            unicode_offset = 65 if char.isupper() else 97

            encrypted_char = chr(
                (ord(char) + shift - unicode_offset) % 26 + unicode_offset
            )

            result += encrypted_char
        else:
            # append it to result
            result += char
    return result
