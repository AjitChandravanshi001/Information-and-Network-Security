def dynamic_caesar_encrypt(text, base_shift):
    result = ""
    
    for i, char in enumerate(text):
        if char.isalpha():
        
            shift = base_shift + i
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    
    return result

def dynamic_caesar_decrypt(text, base_shift):
    result = ""
    
    for i, char in enumerate(text):
        if char.isalpha():
            # Reverse the dynamic shift
            shift = base_shift + i
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    
    return result


plain_text = "Network Security!"
base_shift_value = 5

encrypted_text = dynamic_caesar_encrypt(plain_text, base_shift_value)
print("Encrypted:", encrypted_text)

decrypted_text = dynamic_caesar_decrypt(encrypted_text, base_shift_value)
print("Decrypted:", decrypted_text)
