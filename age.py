driving = input (' have you driven a car?')
if driving != 'yes' and driving != 'no':
	print ('only yes or no allowed')
	raise SystemExit #trig program ends if input format is not correct

age = input ('how old are you?')
age = int (age)
if driving == 'yes':
	if age >= 18:
		print ('pass')
	else:
		print ('you are not allowed to drive')
elif driving == 'no':
	if age >= 18:
		print ('why not get a driving license')
	else:
		print ('that is fine, just wait a couple of years')
