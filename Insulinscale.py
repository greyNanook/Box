print """
Insulin Sliding Scale Program
based on values provided by 
The University of Pittsburg Medical Center. (2003)
This program is not affiliated with UPMC. 
"""

def start():
	print "Are you currently ill with an infection or being treated with steroids?"
	
	highdose = raw_input("> ")
	
	if highdose == "yes":
		high_dose()
	elif highdose == "no":
		average_dosecheckpoint()
	else:
		print "Please respond with a lower case yes or no."
		start()	
		

def high_dose():
	print "What is your blood glucose concentration?"
	
	glucose = raw_input("> ")
	glucose = int(glucose)
		
	if glucose < 85: 
		print "You are low, do not give yourself insulin. Initiate Hypoglycemia Protocol!"
		exit (0)
	elif glucose < 130:
		print "Your blood sugars are in a normal range, do not give yourself any insulin."
		exit (0)
	elif glucose < 180:
		print "You need to give yourself 8 units of insulin and recheck your blood sugars in 1 to 2 hours."
		exit (0)
	elif glucose < 240:
		print "You need to give yourself 12 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 300:
		print "You need to give yourself 16 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)	
	elif glucose < 350:
		print "You need to give yourself 20 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 400:
		print "You need to give yourself 24 units of insulin and recheck your blood sugars in 30 minutes."
		exit (0)
	elif glucose >= 400:
		print "You need to give yourself 28 units of insulin. Check your urine ketone levels, contact your primary care physician, and recheck your blood sugars in 30 minutes."
		exit (0)			


def average_dosecheckpoint():	
	print "Are you considered thin or elderly?"
	
	dosecheckpoint = raw_input("> ")
	
	if dosecheckpoint == "yes":
		thin_dose()
	elif dosecheckpoint == "no":
		average_dose()
	else:
		print "Please respond with a lower case yes or no."
		average_dosecheckpoint()	


def average_dose():
	print "What is your blood glucose concentration?"
	
	glucose = raw_input("> ")
	glucose = int(glucose)
		
	if glucose < 85: 
		print "You are low, do not give yourself insulin. Initiate Hypoglycemia Protocol!"
		exit (0)
	elif glucose < 130:
		print "Your blood sugars are in a normal range, do not give yourself any insulin."
		exit (0)
	elif glucose < 180:
		print "You need to give yourself 4 units of insulin and recheck your blood sugars in 1 to 2 hours."
		exit (0)
	elif glucose < 240:
		print "You need to give yourself 8 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 300:
		print "You need to give yourself 10 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)	
	elif glucose < 350:
		print "You need to give yourself 12 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 400:
		print "You need to give yourself 16 units of insulin and recheck your blood sugars in 30 minutes."
		exit (0)
	elif glucose >= 400:
		print "You need to give yourself 20 units of insulin. Check your urine ketone levels, contact your primary care physician, and recheck your blood sugars in 30 minutes."
		exit (0)			


def thin_dose():
	print "What is your blood glucose concentration?"
	
	glucose = raw_input("> ")
	glucose = int(glucose)
		
	if glucose < 85: 
		print "You are low, do not give yourself insulin. Initiate Hypoglycemia Protocol!"
		exit (0)
	elif glucose < 130:
		print "Your blood sugars are in a normal range, do not give yourself any insulin."
		exit (0)
	elif glucose < 180:
		print "You need to give yourself 2 units of insulin and recheck your blood sugars in 1 to 2 hours."
		exit (0)
	elif glucose < 240:
		print "You need to give yourself 4 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 300:
		print "You need to give yourself 6 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)	
	elif glucose < 350:
		print "You need to give yourself 8 units of insulin and recheck your blood sugars in 30 minutes to 1 hour."
		exit (0)
	elif glucose < 400:
		print "You need to give yourself 10 units of insulin and recheck your blood sugars in 30 minutes."
		exit (0)
	elif glucose >= 400:
		print "You need to give yourself 12 units of insulin. Check your urine ketone levels, contact your primary care physician, and recheck your blood sugars in 30 minutes."
		exit (0)			

start()