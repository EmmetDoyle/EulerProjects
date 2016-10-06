res = 0

last = 0
current = 0
next = 1

while next < 4000000:
	last = current
	current = next
	next = last + current
	
	if current % 2 == 0:
		res += current

print (res)
