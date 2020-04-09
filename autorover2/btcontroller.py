import bluetooth
import rover as rover
import re




class BtController(object):

    rov = rover.Rover()
    rov.debug = False
    rov.speed(0)

    def __init__(self, debug=False, db="config"):
        self.server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.port = 1
        self.server_socket.bind(("",self.port))
        self.server_socket.listen(1)
        self.client_socket,address = self.server_socket.accept()
        print("Accepted connection from ",address)



    def runcar(self):
        while True:
            res = self.client_socket.recv(1024)
            self.client_socket.send(res)
            if res == 'q':
                print ("Quit")
                break
            else:
                if res == 'SS':
                    self.rov.stop()
                elif res == 'FF':
                    self.rov.forward()
                elif res == 'BB':
                    self.rov.reverse()
                elif res == 'LL':
                    self.rov.left_turn()
                elif res == 'RR':
                    self.rov.right_turn()
                elif bool(re.match("^S\d{1}S$",res)) == True:
                    s = int(res[1:2])
                    self.rov.speed(s * 10)
                    print("Speed set to", s * 10)

                if res != 'SS':
                    print("Received:",res)

        client_socket.close()
        server_socket.close()


def test():
	import time
	back_wheels = BtController()
	back_wheels.runcar()




if __name__ == '__main__':
	test()