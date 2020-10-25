import serial
import time
arduinoData = serial.Serial('com6',9600)
arduinoData.timeout = 1

while True:
	led = input('Enter your colour choice:').strip()
	if led == 'done':
		print('finished program')
		break
	arduinoData.write(led.encode())
	time.sleep(0.5)
	print(arduinoData.readline().decode('ascii'))
arduinoData.close()
	



