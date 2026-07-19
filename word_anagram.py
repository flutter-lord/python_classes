def is_anagram(str1, str2):
	list_str1 = []
	list_str2 = []
	for i in str1:
		list_str1.append(i)

	for j in str2:
		list_str2.append(j)

	list_str1.sort()
	list_str2.sort()

	if list_str1 == list_str2:
		print(f"{str1} and {str2} are anagrams")

	else:
		print(f"{str1} and {str2} are not anagrams")
def main():
	s1 = input("Enter first string: ")
	s2 = input("Enter second string: ")
	is_anagram(s1, s2)
main()