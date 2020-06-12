

def eggs (someParameter):
    someParameter.append('Hello')
	
spam = [1,2,3]
eggs(spam) #will alter the original list
print (spam)

