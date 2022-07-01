import re #REGULAR EXPRESSION
sentence = "wheel of fortune" #space is included in indexing. If 15 characters, last is index no.16
# sentence = "wheel of fortune"
hidden_sentence = re.sub("\w", '-', sentence) # /w look for any alphanumeric character, includes _
print('Guess the phrase :', hidden_sentence)
# while loop to keep asking for the letter and print out the phrase

while hidden_sentence != sentence:
 letter = input("Give me a letter: ")
 for index in range(len(sentence)): # indexing always need len so it counts for u
  if letter == sentence[index]:
   hidden_sentence = hidden_sentence[:index]+letter+hidden_sentence[index+1:]
 print("Guess the phrase: ", hidden_sentence)
print("Yay, you've got it right")
