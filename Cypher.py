#Caesar Cipher by Dawson Harris
#This program will either Encrypt or Decrypt a given message

#Initializing variables that will be used

plainTxt = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
cipherTxt = ['D','K','R','B','N','G','O','V','C','T','A','Z','E','F','Y','L','H','S','Q','P','I','X','U','J','M','W',' ']
encrypted = ''
decrypted = ''
messageHolder = input('Please enter your message: ')
message = messageHolder.upper()
promptHolder = input('Would you like to Encrypt or Decrypt this message?: ')
prompt = promptHolder.upper()

#This section will encrypt the message
#And display the cipher on the screen
if prompt == 'Encrypt':
    for letter in message:
        for object in range(0,len(plainTxt)):
            if letter == plainTxt[object]:
                encrypted += (cipherTxt[object] + "")
    print(encrypted)

#This section will decrypt the given message
#And display the plaintext on screen
else:
    for letter in message:
        for object in range(0,len(cipherTxt)):
            if letter == cipherTxt[object]:
                decrypted += (plainTxt[object] + "")
    print(decrypted)
