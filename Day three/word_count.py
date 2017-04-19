def words(wordstring):
	wordlist = wordstring.split()
	worddict = {}
	for w in wordlist:
		if w.isdigit():
			w = int(w)
		if worddict.has_key(w):
			worddict[w] = worddict[w] + 1
		else:
			worddict[w] = 1
	return worddict

if __name__ == '__main__':
	print words('Olly 1 Olly 2 in come free')