def main():
	user_in = input("Enter a string of letters:  ").lower()
	vowels_list = 'aeiou'
	countChar(user_in, vowels_list)

def countChar(user_in, vowels_list):
	vowels = len([char for char in user_in if char in vowels_list])
	print('Your input has', vowels, 'vowels.')
	print('Your input has', len(user_in)-vowels, 'consonants.')
	print('Your input has', len(user_in), 'total chars.')

main()
