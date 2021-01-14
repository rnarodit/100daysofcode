alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caeser (text , shift_amount, operation):
    final_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if(operation == "encode"):
            new_position = position + shift_amount
        elif operation == "decode":
            new_position = position - shift_amount
        final_text += alphabet[new_position]
    print(f"The {operation}d text is {final_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(text, shift, direction)