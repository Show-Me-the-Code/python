import socket
import SocketServer as socketserver
import select
REMOTE_SERVER = '127.0.0.1'
REMOTE_PORT = 9999
LOCAL_SERVER = '127.0.0.1'
LOCAL_PORT = 10001
PORT = 10000
BUFFER = 4096
#Hello
if __name__ == '__main__':
    main()