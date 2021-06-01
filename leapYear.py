def leapYearChecker(year):
	leapYear = False
	if ((year % 4) == 0):
		leapYear = True
		if ((year % 100) == 0):
			leapYear = False
			if ((year % 400) == 0):
				leapYear = True
	if (leapYear == True):
		return "Yes"
	if (leapYear == False):
		return "No"
