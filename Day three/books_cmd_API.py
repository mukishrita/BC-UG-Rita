import requests, sys

def get_book(search):
	r = requests.get('https://www.googleapis.com/books/v1/volumes?q='+search)
	return r.text

if __name__ == '__main__':
	args = sys.argv[1:]
	help_note = "Enter arguments in the format -a <author> or -t <title> or -i <isbn>"
	if not args or len(args) > 2:
		print help_note
	else:
		if args[0] == '-a':
			print get_book('inauthor:'+args[1])
		elif args[0] == '-i':
			print get_book('isbn:'+args[1])
		elif args[0] == '-t':
			print get_book('intitle:'+args[1])
		elif args[0] == '-h':
			print help_note
		else:
			print help_note