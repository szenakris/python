from os import write
import sys 
oldout = sys.stdout
print('Képernyőre ír.')
wr = open('test2.txt', 'w')
sys.stdout = wr
print('fájlba ír.')
wr.close()
sys.stdout = oldout
print('képernyőre ír ismét.')
