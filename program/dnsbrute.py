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

        if(self.wlist == 'small'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_Common.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' For some reason the required file was not found. \nSo the Brute DNS will be shut down' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    target = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(target, self.type_in)
                    for result in results:
                        print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(target, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        elif(self.wlist == 'medium'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_Extra.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' For some reason the required file was not found. \nSo the Brute DNS will be shut down' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    target = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(target, self.type_in)
                    for result in results:
                        print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(target, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        elif(self.wlist == 'large'):
            try:
                arq = open('../w_lists/Filenames_or_Directories_All.wordlist')
                subdos = arq.read().splitlines()
            except:
                print('\033[31m' + ' For some reason the required file was not found. \nSo the Brute DNS will be shut down' + '\033[0;0m')
                print('\n' + '-'*59 + '\n')
                time.sleep(10)
            for subdo in subdos:
                try:
                    target = ('{}.{}'.format(subdo, self.host))
                    results = dns.resolver.resolve(target, self.type_in)
                    for result in results:
                        print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(target, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass
        else:
            print('\033[31m' + 'Command not compatible' + '\033[0;0m')
            time.sleep(10)
            sys.exit(1)
    pass