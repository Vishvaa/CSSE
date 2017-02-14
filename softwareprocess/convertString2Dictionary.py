import urllib
class convertt():
    def convertString2Dictionary(self, inputString = ""):
        Key = ''
        value = ''
        Dict = {}
        i = 0
        Flagg = False
        if inputString == "":
            Dict = {'error':'true'}
        else:
            if inputString[0].isalpha() and inputString[1] != '%':
                lenght = len(inputString)
                while i < lenght:
                    if inputString[i] == '%':
                        if inputString[i]== '%' and inputString[i+1] == '2' and inputString[i+2] == '0':
                            if inputString[i+3] == '%' or inputString[i-3] == '%':
                                i += 3
                            else:
                                Dict = {'error':'true.'}
                                break

                        elif inputString[i]== '%' and inputString[i+1] == '2' and inputString[i+2] == 'C':
                            i += 3
                            if Flagg == False:
                                Dict = {'error':'true'}
                                break
                            if inputString[i].isalpha() and inputString[i+1] != '%':
                                if Flagg == True:
                                    if i < lenght:
                                        if Key in Dict or "_" in value:
                                            Dict = {'error':'true'}
                                            Flagg = False
                                            break
                                        else:
                                            Dict[Key] = value
                                            Flagg = False
                                            Key = ''
                                            value = ''
                                    else:
                                        Dict = {'error':'true'}
                                        Flagg = False
                                        break
                            else:
                                Dict = {'error':'true'}
                                Flagg = False
                                break
                        elif inputString[i]== '%' and inputString[i+1] == '3' and inputString[i+2] == 'D':
                            i +=3
                            Flagg = True
                        else:
                            Dict = {'error':'true'}
                            break

                    else:
                        if Flagg == False:
                            Key += inputString[i]
                            i += 1

                        if Flagg == True:
                            value += inputString[i]
                            i += 1

                if Flagg == False:
                    Dict = {'error':'true'}
                elif value == "" or Key == "":
                    Dict = {'error':'true'}
                else:
                    if Key in Dict or "_" in value:
                        Dict = {'error':'true'}
                    else:
                        Dict[Key] = value
            else:
                Dict = {'error':'true'}

        return Dict


