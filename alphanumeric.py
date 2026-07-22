def alpha_only(word):
	for i in word:
		if not i.isalpha():
			word.pop(word.index(i))
	return f"The alpha only string is {"".join(word)}"




def main():
	s = list(input("Enter a word: "))
	print(alpha_only(s))

main()