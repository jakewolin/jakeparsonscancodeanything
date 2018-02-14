alphabet = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? " 
key = "wSk'\\t7X>MzG?fY5=c8LhW`~a]:13i/.oPjI(g&B$^;uV9|A \"rdN!ReU<@60pKZ,Q)nlTD[42-#bEH_vFx%Oy*J{qs}C+m"

def encrypt(message):
    result=""
    for letter in message:
        loc=alphabet.find(letter)
        result+=key[loc]
    return result


def decrypt(message):
    result=""
    for letter in message:
        loc=key.find(letter)
        result+=alphabet[loc]
    return result


unencrypted_message = "*(hElLo, mY name is J%^7s)*"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
