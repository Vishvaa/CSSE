from math import sqrt

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
        if degree < 0 or degree > 90 or minute < 0.0 or minute > 60.0:
            con = "error"
            return con
        else:
            return con

def dispatch(values=None):
    dip = 0
    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    if values['observation'] != "":
        tempaltitude = obser2atl(values['observation'])

        if tempaltitude != "error":
            #Perform designated function
            if(values['op'] == 'adjust'):
                if(values['horizon'] == 'natural'):
                    dip = ((-0.97 * sqrt(values['height']))/60)
                    temper = (values['temperature'] - 32 ) /9 / 5

                refraction = (-0.00452*values['pressure']/ (273))
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
