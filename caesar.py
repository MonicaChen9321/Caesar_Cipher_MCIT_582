charSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numChars = len(charSet)


def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    plaintext = plaintext.upper().replace(' ','')

    for ch in plaintext:
      if ch in charSet:
        newText = charSet[(charSet.find(ch) + key)%numChars]
        ciphertext = ciphertext + newText
      else:
        ciphertext = ciphertext + ch
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    ciphertext = ciphertext.upper()

    for ch in ciphertext:
      if ch in charSet:
        newText = charSet[(charSet.find(ch) - key)%numChars]
      else:
        newText = ch
      plaintext = plaintext + newText

    return plaintext

def main():
  print(encrypt(1,"BASE"))
  print(decrypt(1,"CBTF"))
  print(encrypt(-3, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))
  print(decrypt(-3, "QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD"))
  print(encrypt(-120, "QE@@#$"))
  print(decrypt(-120, "AO@@#$"))

if __name__ == '__main__':
    main()
