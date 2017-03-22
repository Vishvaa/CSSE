#from math import sqrt
import math
def obser2atl(con):
    con = str(con)
    if con.find("d") == False:
        con = "error"
        return con
    else:
        degnmin = con.split("d")
        global degree
        global minute
        degree = int(degnmin[0])
        minute = float(degnmin[1])
        minute = round(minute,1)
        # if degree < 0 or degree > 90 or minute < 0.0 or minute > 60.0:
        #     con = "error"
        #     return con
        # else:
        #     return con

def dispatch(values=None):
    dip = 0
    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op is specified'
        return values

    if values['observation'] != "":
        tempaltitude = obser2atl(values['observation'])

        if tempaltitude != "error":
            if ('height' in values) and values['height'] != '':
                height = values['height']
            else:
                height = 0

            if ('pressure' in values) and values['pressure'] != '':
                pressure = values['pressure']
            else:
                pressure = 1010

            if ('temperature' in values) and values['temperature'] != '':
                temperature = values['temperature']
            else:
                temperature = 72

            if ('horizon' in values):
                horizon = values['horizon']
            else:
                horizon = "naturall"

                #Perform designated function
            if(values['op'] == 'adjust'):
                if(horizon == 'natural'):
                    dip = ((-0.97 * math.sqrt(float(height)))/60)

                print horizon
                tempaltitude = (degree + minute / 60)
                temper = int(temperature)
                ref1 = (-0.00452 * float(pressure))
                ref2 = (273 + (temper - 32) * 5/9 )
                ref3 = math.tan(math.radians(tempaltitude))
                ref = ref1 / ref2 / ref3
                print  ref
                altitude = float(tempaltitude + dip + ref)
                nminute = str("{:.1f}".format((altitude - int(altitude)) * 60))
                nminute = nminute.split('.')
                inti = nminute[0].zfill(1)
                dec = nminute[1]
                nminute = inti + '.' + dec
                altitude = str(int(altitude)) + 'd' + nminute

                #
                #
                print dip
                print altitude

                values['altitude'] = altitude
                return values    #<-------------- replace this with your implementation
            elif(values['op'] == 'predict'):
                return values    #This calculation is stubbed out
            elif(values['op'] == 'correct'):
                return values    #This calculation is stubbed out
            elif(values['op'] == 'locate'):
                return values    #This calculation is stubbed out
            else:
                values['error'] = 'op is not a legal operation'
                return values
        else:
            values['error'] = 'observation value is invalid'
            return values



    else:
        values['error'] = 'observation is missing'
        return values
