from difflib import SequenceMatcher

text1 = input('Ener the first sentence: ')
text2 = input('Ener the second sentence: ')

sequenceScore =SequenceMatcher(None, text1, text2).ratio()
print(f'Both are {sequenceScore*100} % similar')