import pprint
message = 'It was a bright cold day in April, and the cloks were striking thirteen.'
count = {}

for charater in message :
              count.setdefault(charater, 0)
              count[charater] = count[charater] + 1

pprint.pprint(count)
