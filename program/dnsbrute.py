import sys
import dns.resolver
import time

a = 1

small = '../w_lists/Filenames_or_Directories_Common.wordlist'
medium = '../w_lists/Filenames_or_Directories_Extra.wordlist'
big = '../w_lists/Filenames_or_Directories_All.wordlist'

class DNSBRUTE():
    def __init__(self, host, wlist, type_in):
        self.host = host
        self.wlist = wlist
        self.type_in = type_in
    pass

    def running_dbscan(self):

        global a
        global small
        global medium
        global big

        
        if(self.wlist == 'M' or self.wlist == 'm'):
            wordlist = medium
        elif(self.wlist == 'L' or self.wlist == 'l'):
            wordlist = big
        else:
            wordlist = small

        try:
            arq = open(wordlist)
            subdo = arq.read().splitlines()
        except:
            print('\033[31m' + ' For some reason the required file was not found. \nSo DNS Brute will be shut down' + '\033[0;0m')
            print('\n' + '-'*59 + '\n')
            time.sleep(5)
            sys.exit(1)

        if(1 == 1):
            for subdomain in subdo:
                try:
                    target = ('{}.{}'.format(subdomain, self.host))
                    results = dns.resolver.resolve((target, self.type_in))
                    for result in results:
                        print('\033[32m' + 'Target: ' + '\033[0;0m' + '{} <----> IP: {} <====> {}'.format(target, result, self.type_in))
                        print('\n' + '-'*24 + '\n')
                except:
                    a += a
                pass