from socket import *

cli_s = socket(AF_INET, SOCK_STREAM)

ip_add = input("Enter valid ip address : ")

port = int(input("Enter valid port : "))
cli_s.connect((ip_add, port))

sentence = input('Input a sentence ')
cli_s.sendall(sentence.encode('utf-8'))

new_sen = cli_s.recv(1024).decode('utf-8')

print("New sentence from server : ", new_sen)

cli_s.close()