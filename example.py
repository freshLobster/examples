def old_home():
	response=raw_input("what is 2+2")
	if int(response)<>4:
		return("haha, you are stupid")
	else:
		return("wow")

def double_age(age):
	age=age*2
	return(age)

a=raw_input("what is your age? ")
age = int(a)
if age <= 16:
	print age, " is too young"
	print "twice your age is ", double_age(age)

elif age > 100:
	print age, "is too old, go to an old peoples home"
	print old_home()

else:
	print age, " is over 16, cool"
print "done"
done=raw_input("bye!")