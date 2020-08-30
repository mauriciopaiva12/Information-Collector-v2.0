#------ IMPORT LIBRARIES ------#

import time
import sys

#------------#

#------ GLOBAL VARIABLES ------#

from portscan import PORTSCAN
from dnsbrute import DNSBRUTE

#------------#

#------ PRESENTATION ------#

print('\n' + '-'*53 + '\n' + '-'*11 + 'Automated information collector' + '-'*11 + '\n' + '-'*24 + 'V:2.0' + '-'*24 + '\n')
print(' - For more information about the application, read the attachment "README.txt" ')
print('\n' + '-'*59 + '\n')

#------------#

#------ INITIAL DECISION ------#

question1 = input(' Do you want to use the full program or just portscan?[F/p]: ')
print('\n' + '-'*59 + '\n')

#------------#

target = str(input('Target: '))
print('\n' + '-'*24 + '\n')
if(question1 == 'P' or question1 == 'p'):
    question2 = str(input(' Do you want to use standard ports or all ports?[P/a]: '))
    print('\n' + '-'*24 + '\n')
    if(question2 == 'A' or question2 == 'a'):
        ps = PORTSCAN(target, 'all')
        ps.running_scan()
    else:
        ps = PORTSCAN(target, 'pattern')
        ps.running_scan()
else:
    wlist = input('Small, medium or large word-list?[S/m/l]: ')
    print('\n' + '-'*59 + '\n')
    type_in = str(input('[A/AAAA/MX/NS/TXT]: '))
    print('\n' + '-'*59 + '\n')
    if(wlist == 'M' or wlist == 'm'):
        db = DNSBRUTE(target, 'medium', type_in)
        db.running()
    elif(wlist == 'L' or wlist == 'l'):
        db = DNSBRUTE(target, 'large', type_in)
        db.running()
    else:
        db = DNSBRUTE(target, 'small', type_in)
        db.running()
    
    ps = PORTSCAN(target, 'pattern')
    ps.running_scan()