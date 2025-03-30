import pyAesCrypt
password = input('Введите пароль для шифрования файла: ')

pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)