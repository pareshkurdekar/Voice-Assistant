import json
import urllib.request, urllib.parse, urllib.error

url = 'https://api.dictionaryapi.dev/api/v2/entries/'
lang_code = 'en'
word = 'new'
final_url = url + lang_code + '/' + word
print(final_url)
fh = urllib.request.urlopen(final_url).read().decode()
data = json.loads(fh)
#print(json.dumps(data, indent =2))
#print(data[0]["meanings"][0]["definitions"][0]["definition"])
definition = data[0]["meanings"][0]["definitions"][0]["definition"]
print(definition)
meaning_len =  len(data[0]["meanings"][0]["definitions"][0]["synonyms"])
meaning = data[0]["meanings"][0]["definitions"][0]["synonyms"][0:2]
print(meaning)
