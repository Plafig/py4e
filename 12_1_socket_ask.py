import socket

url = input("Plese enter url: ")

try:
    short_url = url.split('/')[2]
    #print('Debug: ',short_url[2])

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((short_url, 80))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()

    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print("Entered an improperly formatted or non-existent URL")