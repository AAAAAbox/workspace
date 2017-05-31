def binaryToDecimal(binaryString):
	decimalValue = 0
	for i in range(len(binaryString)):
		ch = binaryString[i]
		if ch == '0' or ch == '1':
			decimalValue = decimalValue * 2 + binCharToDecimal(ch)
		else:
			return None

	return decimalValue

def binCharToDecimal(ch):
	return ord(ch) - ord('0')

def main():
	bin = input('Enter a bin number: ').strip()

	decimal = binaryToDecimal(bin)
	if decimal == None:
		print('Incorrect Bin number')
	else:
		print('The decimal number for', bin,
			'is', decimal)

main()