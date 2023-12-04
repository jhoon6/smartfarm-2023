import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    try:
        data1 = ser.readline()
        decoded_data1 = data1.decode('utf-8')
        data2 = ser.readline()
        decoded_data2 = data2.decode('utf-8')
        data3 = ser.readline()
        decoded_data3 = data3.decode('utf-8')

        serial_input = decoded_data1 + decoded_data2 + decoded_data3
        
        lines = serial_input.split('\n')
        parsed_values = {}

        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip() 
                if key == "gh": key = "ground_humi"
                if key == "h": key = "humi"
                if key == "t": key = "temp"
                value_str = parts[1].strip()

                if value_str.lower() == 'nan':
                    value = float('nan')
                else:
                    value = float(value_str)

                parsed_values[key] = value

        print(parsed_values)

    except KeyboardInterrupt:
        ser.close()

