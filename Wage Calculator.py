try:
	hrs = float(raw_input("Enter Hours: "))
	pay = float(raw_input("Enter pay: "))
	overtime_pay_rate = 1.5
	if hrs < 40:
		print hrs * pay
	else:
		extra_hrs = hrs - 40 #5hours
		pay_for_extra_hour = pay * 1.5 #15.75
		overtime_pay = extra_hrs * pay_for_extra_hour #78.75
		normal_pay = 40 * pay #420
		print normal_pay + overtime_pay
except:
	print("Please enter a number");	