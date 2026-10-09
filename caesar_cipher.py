def make_shifter(char, shift):
    code = ""
    if char.isalpha():
        base= ord('A') if char.isupper() else ord('a')
        code = chr((ord(char)-base + shift)%26 + base)
    return code

def caesar_cipher(text, shift):
    if not shift:
        return text
    s = int(shift)

    choice = input("Do you want to encrypt or decrypt('e' or 'd'): ").strip()
    if choice[0].lower() == 'd':
        s = -(s)
    elif choice[0].lower() == 'e':
        pass
    else:
        raise ValueError("Invalid option")  
    return "".join(map(lambda char: make_shifter(char, s), text))


print(caesar_cipher("hello",1))
print(caesar_cipher("ifmmp",1))
print(caesar_cipher("khoor, zruog!", 3))
print(caesar_cipher("hello World", 3))
print(caesar_cipher('xyz', 2))
