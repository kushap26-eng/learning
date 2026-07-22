# 1) Normalize a sentence
# sentence = "   Hello     World   "
# normalised = " ".join(sentence.strip().lower().split())
# print("Original:",sentence)
# print("Normalised:",normalised)


# 2) Capitalize each word (without .title())
# sentence = "this is python"
# words = sentence.split()
# capitalized_words = []
# for word in words:
#     capitalized_words.append(word.capitalize())
# result = " ".join(capitalized_words)
# print("Capitalized Sentence: ",result)

# Second Method
# sentence = "This is Python"
# result = " ".join(word.capitalize() for word in sentence.split())
# print("Capitalize Sentence: ",result)


#3) Remove punctuation from string
# using .replace() multiple lines
# text = "hello!! world??"
# text = text.replace("!","")
# text = text.replace("?","")
# print("Result:",text)

# using .isalpha() and .join()
# text = "hello!!! world??"
# result= "".join(char for char in text if char.isalpha() or char.isspace())
# print("Result:",result)


#4) Extract only digits from string
# text = "a1b2c3"
# digit = "".join(char for char in text if char.isdigit())
# print("Digit:",digit)


#5) Extract only alphabets
# text = "Hello123"
# alpha = "".join(char for char in text if char.isalpha())
# print("Alpha: ",alpha)


#6) Reverse words in a sentence
# sentence = "I love Music"
# words = sentence.split()
# reversed_words = words[::-1]
# result = " ".join(reversed_words)
# print("Reversed Sentence: ",result)


#7) Remove duplicate words
# sentence = "this is is text text"
# words = sentence.split()
# unique_words = []
# for word in words:
#     if word not in unique_words:
#         unique_words.append(word)
# result = " ".join(unique_words)
# print("After removing duplicates: ",result)




#8) Check if email is valid (basic)
# email = "kushap26@gmail.com"
# if email.count("@") == 1 and email.endswith(".com") and email.find("@") > 0:
#     print("True")
# else:
#     print("False")


#9) Mask a phone number
# phone = "9852598252"
# masked = phone[:3] + "*" * 5 + phone[-2:]
# print("Phone number: ",masked)


#10) Convert sentence to snake_case
# sentence = "This is Python"
# snake_case = "_".join(sentence.lower().split())
# print("Snake Case:",snake_case)


#11) Remove first and last character of each word
# sentence = "Hello World"
# words = sentence.split()
# result = " ".join(word[1:-1] for word in words)
# print("Result",result)


#12) Find longest word
# sentence = "I love python programming"
# word = sentence.split()
# longest_words = max(word,key=len)
# print("Longest words = ",longest_words)

#13) Count words ignoring punctuation
# using .replace() and .split()
# sentence = "Hello, world! Python is great."
# sentence = sentence.replace(",","")
# sentence = sentence.replace("!","")
# sentence = sentence.replace(".","")
# words = sentence.split()
# print("Word Count:",len(words))


# using .isalpha() and .split()
# sentence = "Hello, world! Python is great"
# cleaned = "".join(char if char.isalpha() or char.isspace() else "" for char in sentence)
# words = cleaned.split()
# print("Word count:",len(words))


#14)Check if sentence is palindrome (ignore spaces)
# sentence = "nurses run"
# text = sentence.replace(" ","")
# if text == text[::-1]:
#     print("True")
# else:
#     print("False")


#15) Toggle case manually
# text = "hello"
# print("".join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in text))