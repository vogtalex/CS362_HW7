def leapYearChecker(year):
	leapYear = False
	if ((year % 4) == 0):
		leapYear = True
	if (leapYear == True):
		return "Yes"
