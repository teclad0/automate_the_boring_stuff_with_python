message = 'It was a bright cold day in april and the clocks were striking thirteen'
count = {}
for character in message:
    count.setdefault(character,0)#ensures that the key is in the count 
    count[character] = count[character]+1


print(count)

