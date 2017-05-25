def decimalToBinary(decimalValue):
	Bin = ''

	while decimalValue != 0:
		BinValue = decimalValue % 2
		Bin = toBinChar(BinValue) + Bin
		decimalValue = decimalValue // 2

	return Bin

def toBinChar(BinValue):
	return chr(BinValue + ord('0'))

def main():
	decimalValue = eval(input('Enter a decimal number: '))

	print('The Bin number for decimal', decimalValue,
		'is', decimalToBinary(decimalValue))

main()