import socket

url = input('Enter: ')
try:
    part = url.split('/')
    host = part[2]
except:
    print('That is not a properly formated URL')
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

while True:
    data = mysock.recv(3000)
    if (len(data) < 1):
        break
    print(data.decode(), len(data), end='' )

mysock.close()
