import socket
import sys
import time


def server():
    print("creating server...")
    time.sleep(2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', 12139)
    print("starting up on {} port {}".format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
       # Wait for a connection
       print('waiting for a connection')
       connection, client_address = sock.accept()
       try:
           print('connection from', client_address)

           # Receive the data in small chunks and retransmit it
           while True:
               data = connection.recv(16)
               print('received {!r}'.format(data))
               if data:
                   print('sending data back to the client')
                   connection.sendall(data)
               else:
                   print('no data from', client_address)
                   break

       finally:
           # Clean up the connection
           connection.close()
def clienteasy():
    import socket
    import sys


    def get_constants(prefix):
        """Create a dictionary mapping socket module
        constants to their names.
        """
        return {
            getattr(socket, n): n
            for n in dir(socket)
            if n.startswith(prefix)
        }


    families = get_constants('AF_')
    types = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')

    # Create a TCP/IP socket
    sock = socket.create_connection(('localhost', 10000))

    print('Family  :', families[sock.family])
    print('Type    :', types[sock.type])
    print('Protocol:', protocols[sock.proto])
    print()

    try:

        # Send data
        message = b'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()