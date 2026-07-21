def lockers_status():

	is_closed = True
	locker = [is_closed] * 100
	students = list(range(1, 101))

	for i in students:
		for j in range(i, len(students) + 1, i):
			locker[j- 1] = not locker[j - 1]


	print(f"Closed lockers is : {locker.count(is_closed)}")
	print(f"Open lockers is : {locker.count(not is_closed)}")


def main():
	lockers_status()
main()