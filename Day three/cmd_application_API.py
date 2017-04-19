import pprint
import sys
from apiclient.discovery import build

api_key = sys.argv[1]
service = build('books', 'v1', developerKey=api_key)
request = service.volumes().list(source='public', q='android')
response = request.execute()
pprint.pprint(response)

print 'Found %d books:' % len(response['items'])
for book in response.get('items', []):
  print 'Title: %s, Authors: %s' % (
    book['volumeInfo']['title'],
    book['volumeInfo']['authors'])