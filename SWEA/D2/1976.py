

T = int(input())

for i in range(T):
	time_list = list(map(int, input().split()))
	hour = time_list[0] + time_list[2]
	minute = time_list[1] + time_list[3]
	ans = []

	if hour > 12:
		hour -= 12
	
	# minute 합이 60이상이 되면 hour가 1증가해야한다. 
	if minute > 59:
		minute -= 60
		hour += 1

	print('#{} {} {}'.format(i+1, hour, minute))
