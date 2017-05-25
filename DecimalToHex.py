def decimalTohex(decimalValue):
	hex = ' '

	while decimalValue != 0:
		hexValue = decimalValue % 16
		hex = toHexchar(hexValue) + hex
		decimalValue = decimalValue // 16

	return hex

def toHexchar(hexValue):
	if 0 <= hexValue <= 9:
		return chr(hexValue + ord('0'))
	else:
		return chr(hexValue - 10 + ord('A'))

def main():
	decimalValue = eval(input('Enter a decimal number: '))

	print('The hex number for decimal', 
		decimalValue, 'is', decimalTohex(decimalValue))

main()