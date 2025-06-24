def multi_shift_caesar_encrypt(text, shifts):
    result = ""
    shift_count = len(shifts)
    
    for i, char in enumerate(text):
        if char.isalpha():
          
            shift = shifts[i % shift_count]
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    
    return result

def multi_shift_caesar_decrypt(text, shifts):
    result = ""
    shift_count = len(shifts)
    
    for i, char in enumerate(text):
        if char.isalpha():
            
            shift = shifts[i % shift_count]
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    
    return result


plain_text = "Secure Data!"
shift_values = [4, 7, 2]  

encrypted_text = multi_shift_caesar_encrypt(plain_text, shift_values)
decrypted_text = multi_shift_caesar_decrypt(encrypted_text, shift_values)

# Display results
print("Plain Text:     ", plain_text)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)
