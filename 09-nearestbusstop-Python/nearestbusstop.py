# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	# while(street>0):
	if(street%8==0):
		return street
	else:
		# return int(8 * round(float(street)/8) )
		a =street%8
		if(a<=4):
			a=(street//8)*8
		else:
			a=((street//8)*8)+8
		return a
