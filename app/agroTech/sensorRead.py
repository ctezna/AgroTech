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
            if len(readings) > 24:
                sensors = False
                temp = readings[2:7]
                hum = readings[9:14]
                ph = readings[16:20]
                gndHum = readings[22:27]
        except:
            pass

    ser.close()
    val = [temp,hum,ph,gndHum]
    return val
