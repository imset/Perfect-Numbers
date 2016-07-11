import sys
def perfCheck(arg1, arg2):
	numChk = 0
	if arg1.lower() == 'check':
		numChk = int(arg2)
	elif arg1.lower() == 'iterate':
		numChk = 2
	else:
		print("Argument ", arg1, " is not valid.")
		return
	loopStop = 'false'	
	while numChk <= int(arg2) and loopStop == 'false':
		factorList = []
		factorChk = 1
		while factorChk < numChk:
			if numChk % factorChk == 0:
				factorList.append(factorChk)
			factorChk += 1
		factorSum = sum(factorList)
		if factorChk == factorSum:
			print(str(numChk) + " is perfect!")
		else:
			print(str(numChk) + " is not perfect!")
		
		if arg1.lower() == 'check':
			loopStop = 'True'
		else:
			numChk += 1
	return perfCheck
	
if __name__ == '__main__':
   perfCheck(sys.argv[1], sys.argv[2])