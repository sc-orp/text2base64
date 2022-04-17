import base64, os

os.system('clear')
ask = input('[ + ] What do you want to do?\n1. encode a text to base64.\n2. decode a base64 to text.\n\n')

if ask == '1':
    a = input('[ + ] Alright, now tell me what text you want to convert.\n')
    b = a.encode("UTF-8")
    c = base64.b64encode(b)
    result = c.decode("UTF-8")
    print('[ + ] Here\'s your result: ' + result)
    exit()
    
elif ask == '2':
    a = input('[ + ] Alright, now tell me what base64 text you want to convert to normal text.\n')
    b = base64.b64decode(a)
    result = b.decode('UTF-8')
    print('[ + ] Here\'s your result: ' + result)
    
else:
    print('[ ! ] Please only use 1 (for encoding) or 2 (for decoding).')
    exit()
