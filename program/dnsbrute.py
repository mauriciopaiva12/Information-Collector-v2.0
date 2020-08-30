import sys
import dns.resolver
import time

a = 1

class DNSBRUTE():
    def __init__(self, host, wlist, type_in):
        self.host = host
        self.wlist = wlist
        self.type_in = type_in
    pass

    def running(self):

        global a

        if(self.wlist == 'S' or self.wlist == 's'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_All.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' Por algum motivo o arquivo nessesário não foi encontrado. \nPortanto o DNS Brute será encerrado' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    alvo = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(alvo, self.type_in)
                    for result in results:
                        print('\033[32m' + 'Alvo: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(alvo, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        elif(self.wlist == 'M' or self.wlist == 'm'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_Extra.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' Por algum motivo o arquivo nessesário não foi encontrado. \nPortanto o DNS Brute será encerrado' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    alvo = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(alvo, self.type_in)
                    for result in results:
                        print('\033[32m' + 'Alvo: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(alvo, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        elif(self.wlist == 'L' or self.wlist == 'l'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_All.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' Por algum motivo o arquivo nessesário não foi encontrado. \nPortanto o DNS Brute será encerrado' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    target = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(alvo, self.type_in)
                    for results in result:
                        print('\033[32m' + 'Alvo: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(target, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        else:
            print('\033[31m' + 'Comando não compativel' + '\033[0;0m')
            time.sleep(10)
            sys.exit(1)