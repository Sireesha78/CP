# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	x = 0
	b = (b1-b2)
	m = (m2-m1)
	if(b!=0 and m!=0):
		x = b // m
	y1 = m1 * x + b1
	y2 = m2 * x + b2
	if(x>1 and y1 > 1 and y2>1):
		return x
	else: 
		return None
