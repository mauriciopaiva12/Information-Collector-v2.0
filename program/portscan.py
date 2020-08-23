import socket
import sys

portp = [21, 22, 25, 53, 80, 110, 135, 136, 137, 138, 139, 143, 443, 3306, 3389]
portany = range(65536)

class PORTSCAN:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    pass

    def running_scan(self):
        if(self.port == 'pattern'):
            global portp
            print('SCANNING...')
            print('\n' + '-'*59 + '\n')
            for portu in portp:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                code = client.connect_ex((self.ip, portu))
                code_transfer = str(code)
                if(code_transfer == '0'):
                    print('PORT: {} <----> '.format(portu) + '\033[32m' + 'OPEN' + '\033[0;0m')
                    print('\n' + '-'*24 + '\n')
                else:
                    print('PORT: {} <----> '.format(portu) + '\033[31m' + 'CLOSED' + '\033[0;0m')
                    print('\n' + '-'*24 + '\n')
            print('SCANNING COMPLETED')
            print('\n' + '-'*59 + '\n')
        elif(self.port == 'all'):
            global portany
            print('SCANNING...')
            print('\n' + '-'*59 + '\n')
            for portu in portany:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                code = client.connect_ex((self.ip, portu))
                code_transfer = str(code)
                if(code_transfer == '0'):
                    print('PORT: {} <----> '.format(portu) + '\033[32m' + 'OPEN' + '\033[0;0m')
                    print('\n' + '-'*24 + '\n')
            print('SCANNING COMPLETED')
            print('\n' + '-'*59 + '\n')
        else:
            print('\033[31m' + 'Command not valid' + '\033[0;0m')
            sys.exit(1)
    pass