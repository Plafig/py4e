import socket

url = input("Plese enter url: ")
count = 0
try:
    short_url = url.split('/')[2]
    #print('Debug: ',short_url[2])

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((short_url, 80))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()

    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        count = count + len(data)
        #print("Debug: ", data)
        if count < 3000:
            print(data.decode(),end='')
        if len(data) < 1:
            break
    print('\n', count)

    mysock.close()
except:
    print("Entered an improperly formatted or non-existent URL")