import serial

def getReadings(serialPort):
    try:
        ser = serial.Serial(serialPort, 9600, timeout=1)
    except:
        try:
            ser = serial.Serial(serialPort, 9600, timeout=1)
        except:
            return('ERROR: SERIAL CONNECTION')

    sensors = True
    while sensors:
        try:
            readings = ser.readline()
            if len(readings) == 29:
                sensors = False
                temp = readings[2:7]
                hum = readings[9:15]
                ph = readings[17:21]
                gndHum = readings[23:29]
        except:
            pass

    ser.close()
    val = [temp,hum,ph,gndHum]
    return val
