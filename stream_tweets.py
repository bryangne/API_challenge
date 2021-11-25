# !pip install python-twitter
import twitter
from api_key import api
import json

def main():
    filt = input('Enter a word to search for: ')
    lang = input('Enter which language to search in: ')
    output = input('Enter a name for the output: ')
    with open(output, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        stream = api.GetStreamFilter(track=filt, languages=lang)
        for line in stream:
#             print(line)
            f.write(json.dumps(line))
            f.write('\n')

if __name__ == "__main__":
    main()