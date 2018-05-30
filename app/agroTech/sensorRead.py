import serial

def getReadings(serialPort):
    try:
        ser = serial.Serial(serialPort, 9600, timeout=1)
    except:
        try:
            ser = serial.Serial(serialPort, 9600, timeout=1)
        except:
            return('ERROR: SERIAL CONNECTION')

    readings = ser.readline()
    while len(readings) < 18:
        readings = ser.readline()
    temp = -404
    hum = -1
    ph = -1
    for i in range(2,len(readings)+1):
        if i == 7:
            temp = readings[2:i]
            temp = temp.decode("utf-8")
        if i == 14:
            hum = readings[9:i]
            hum = hum.decode("utf-8")
        if i == 20:
            ph = readings[16:i]
            ph = ph.decode("utf-8")

    if temp != -404 and hum != -1 and ph != -1:
        val = [temp,hum,ph]
        return val
    else:
        val = [-404,-1,-1]
        return val
