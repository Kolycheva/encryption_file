import pyAesCrypt
from getpass import getpass
password = getpass(prompt='Введите пароль: ')

infile = input('Введите имя файла для шифрования (например: data.txt) ')

outfile = input('Введите имя зашифрованного файла с расширением .aes (например: data.txt.aes) ')

pyAesCrypt.encryptFile(infile, outfile, password)

outfile2 = input('Введите имя расшифрованного файла (например: dataout.txt) ')
pyAesCrypt.decryptFile(outfile, outfile2, password)
