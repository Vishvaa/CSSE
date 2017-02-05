import urllib
#print 'Helloooo'
class convertt():
    def convertString2Dictionary(self, inputString = ""):
        Key = ''
        i = 0
        print 'hello'
        if inputString[0].isalpha() and inputString[1] != '%':
            lenght = len(inputString)
            while i < lenght:
                if inputString[i] == '%':
                    break
                else:
                    Key += inputString[i]
                    i += 1
                    print Key
            print "correct"
            if inputString[i]== '%' and inputString[i+1] == '2' and inputString[i+2] == '0':
                pass
            if inputString[i]== '%' and inputString[i+1] == '2' and inputString[i+2] == 'C':
                pass
            if inputString[i]== '%' and inputString[i+1] == '3' and inputString[i+2] == 'D':
                pass

convertt = convertt()
val = convertt.convertString2Dictionary('vishv%aa')
