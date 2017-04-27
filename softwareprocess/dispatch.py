import math
import os
import datetime
def obser2atl(con):
    con = str(con)
    if con.find("d") == False:
        con = "error"
        return con
    else:
        try:
            degnmin = con.split("d")
            global degree
            global minute
            degree = int(degnmin[0])
            minute = float(degnmin[1])
            minute = round(minute,1)
        except:
            con = 'error'
            return con
        if degree < 0 or degree > 90 or minute < 0.0 or minute > 60.0:
            con = "error"
            return con
        else:
            return con

def obser2atl2(con):
    degree = con.split('d')
    minute = float(degree[1])
    if int(degree[0]) != 0:
        if int(degree[0]) < 0:
            degree = int(degree[0]) - minute / 60
        else:
            degree = int(degree[0]) + minute / 60
    else:
        if degree[0][0] == '-':
            degree = - minute / 60
        else:
            degree = minute / 60
    return degree
def convert2String(con):
    nminute = str("{:.1f}".format((con - int(con)) * 60))
    nminute = nminute.split('.')
    inti = nminute[0].zfill(1)
    dec = nminute[1]
    nminute = inti + '.' + dec
    con = str(int(con)) + 'd' + nminute
    return con
def dispatch(values=None):
    dip = 0
    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if 'error' in values:
        del values['error']
        return values
    if (not('op' in values)):
        values['error'] = 'no op is specified'
        return values
                #Perform designated function
    if(values['op'] == 'adjust'):
        if ('observation' in values) and values['observation'] != "" and (not('altitude' in values)):
            tempaltitude = obser2atl(values['observation'])
            if tempaltitude != "error":
                if ('height' in values) and values['height'] != '':
                    try:
                        height = float(values['height'])
                    except:
                        values['error'] = 'Height is invalid'
                        return values
                    if height < 0:
                        values['error'] = 'Height is invalid'
                        return values
                else:
                    height = 0
                if ('pressure' in values) and values['pressure'] != '':
                    try:
                        pressure = int(values['pressure'])
                    except:
                        values['error'] = 'Pressure is invalid'
                        return values
                    if pressure < 100 or pressure > 1100:
                        values['error'] = 'Pressure is invalid'
                        return values
                else:
                    pressure = 1010
                if ('temperature' in values) and values['temperature'] != '':
                    try:
                        temperature = int(values['temperature'])
                    except:
                        values['error'] = 'Temperature is invalid'
                        return values
                    if temperature < -20 or temperature > 120:
                        values['error'] = 'Temperature is invalid'
                        return values
                else:
                    temperature = 72
                if ('horizon' in values) and values['horizon'] != '':
                    if values['horizon'] == 'natural' or values['horizon'] == 'artificial':
                        horizon = values['horizon']
                    else:
                        values['error'] = 'Horizon is invalid'
                        return values
                else:
                    horizon = "natural"
            else:
                values['error'] = 'Observation is invalid'
                return values
        else:
            values['error'] = 'Observation is missing'
            return values
        if(horizon == 'natural'):
            dip = ((-0.97 * math.sqrt(float(height)))/60)
        tempaltitude = (degree + minute / 60)
        temper = int(temperature)
        ref1 = (-0.00452 * float(pressure))
        ref2 = (273 + (temper - 32) * 5/9 )
        ref3 = math.tan(math.radians(tempaltitude))
        ref = ref1 / ref2 / ref3
        altitude = float(tempaltitude + dip + ref)
        values['altitude'] = convert2String(altitude)
        return values    #<-------------- replace this with your implementation

    elif(values['op'] == 'predict'):
        if 'lat' in values or 'long' in values:
            values['error'] = "Latitude or Longitude already Present"
            return values
        starsfile = os.path.join(os.path.dirname(__file__),'stars.txt')
        starbody = {}
        sbody = open(starsfile)
        for starb in sbody:
            star = starb
            star = star.split()
            starbody[str.lower(star[0])] = str(star[1]) + ' ' + str(star[2])
        sbody.close()
        try:
            starref = values['body']
            starref = str.lower(starref)
        except:
            values['error'] = "mandatory information is missing"
            return  values
        if 'date' in values and values['date'] != "":
            stardate = values['date']
        else:
            values['date'] = '2001-01-01'
            stardate = values['date']
        if 'time' in values and values['time'] != "":
            startime = values['time']
        else:
            values['time'] = '00:00:00'
            startime = values['time']
        if starref in starbody:
            starfull = starbody[starref]
            starfull = starfull.split()
            SHA = starfull[0]
            latitude = starfull[1]
        else:
            values['error'] = 'Star not in Stars File'
            return values
        RefYear = 2001
        try:
            stardate = stardate.split('-')
            ObserYear = int(stardate[0])
            ObserMonth = int(stardate[1])
            ObserDay = int(stardate[2])
        except:
            values['error'] = "Wrong Date"
            return values
        if 0 < ObserMonth > 12 or 0 < ObserDay > 31 or ObserYear < 2001:
            values['error'] = "Date is invalid"
            return values

        if ObserMonth == 2 or ObserMonth == 4 or ObserMonth == 6 or ObserMonth == 9 or ObserMonth == 11 and ObserDay == 31 :
            values['error'] = "Date is invalid"
            return values
        diff = ObserYear - RefYear
        leap = diff/4
        leap = int(leap)
        CumProg = diff * obser2atl2('-0d14.31667')
        totalProg = obser2atl2('0d59.0') * leap
        yearStart = datetime.date(ObserYear,1,1)
        yearNow = datetime.date(ObserYear,ObserMonth,ObserDay)
        diff = yearNow - yearStart
        diff = int(diff.days)
        try:
            startime = startime.split(':')
            if 0 < int(startime[0]) > 24 or 0 < int(startime[1]) > 59 or 0 < int(startime[2]) > 59:
                values['error'] = "Time is invalid"
                return values
        except:
            values['error'] = "Wrong Time Format"
            return values
        seconds = diff * 86400 + int(startime[0]) * 3600 + int(startime[1]) * 60 + int(startime[2])
        rotation = (seconds - int(seconds / 86164.1) * 86164.1) / 86164.1 * obser2atl2('360d0')
        GHA = CumProg + rotation + totalProg + obser2atl2('100d42.6')
        longitude = GHA + obser2atl2(SHA)
        longitude = longitude - (int(longitude / 360) * 360)
        longitude = longitude - 0.001
        values['lat'] = latitude
        values['long'] = convert2String(longitude)
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        try:
            LHA = obser2atl2(values['long']) + obser2atl2(values['assumedLong'])
            intermediateDistance = ((math.sin(math.radians(obser2atl2(values['lat']))) * math.sin(math.radians(obser2atl2(values['assumedLat'])))) + ( math.cos(math.radians(obser2atl2(values['lat']))) * math.cos(math.radians(obser2atl2(values['assumedLat']))) * math.cos(math.radians(LHA))))
            correctedAltitude = math.asin(intermediateDistance)
            correctedDistance = math.radians(obser2atl2(values['altitude'])) - correctedAltitude
            num = ((math.sin(math.radians(obser2atl2(values['lat']))) - (math.sin(math.radians(obser2atl2(values['assumedLat']))) * intermediateDistance )))
            dum = (math.cos(math.radians(obser2atl2(values['assumedLat']))) * math.cos(math.asin(intermediateDistance)))
            correctedAzimuth = math.acos(num / dum) * 180 / math.pi
            correctedDistance = int(correctedDistance * 180 / math.pi * 60)
            values['correctedDistance'] = str(correctedDistance)
            values['correctedAzimuth'] = convert2String(correctedAzimuth)
        except:
            values['error'] = "mandatory information is missing"
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
