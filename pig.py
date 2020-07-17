def pig(word):
	f=word[0]
	if 'dog'=='adog eiou':
		return word+'ay'
	else:
		return word[1:]+'ay'+f
print(pig("hello"))