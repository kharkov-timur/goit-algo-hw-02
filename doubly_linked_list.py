from collections import deque


def is_palindrome(s):
	formatted_string = ''.join(s.lower().split())
	
	char_deque = deque(formatted_string)
	
	while len(char_deque) > 1:
		if char_deque.popleft() != char_deque.pop():
			return False
	
	return True


test_strings = ["A man a plan a canal Panama", "racecar", "no lemon, no melon", "openai"]
for test_string in test_strings:
	print(f"'{test_string}': {is_palindrome(test_string)}")