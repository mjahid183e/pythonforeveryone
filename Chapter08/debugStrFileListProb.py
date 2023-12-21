#Debugging a file, where actually stored sequence of strigs. And debug the file using strings and lists data structures 
hfile = open('mbox-short.txt')

for line in hfile:
    line = line.rstrip()
    #We are printing lines to make sure what's the problem actually is. And this is actually msg for debugging
    print('Line:', line)

    #We can use the Gardian pattern also for lines:
    #if line == '' : continue #Or we may check for: if len(line) < 1: continue

    genList = line.split()
    print('Words:',genList) #This is a msg for debugging the problem 
    #To protect from the tracebacking, we used the following Gardian pattern (This is called Short circuit evaluaton) 
    if len(genList) < 3: #if we see less than 3 words, we are goring to skip it, to make the Gardian a bit stronger
        continue
    if genList[0] != 'From': #We can even use the Gardian in a compound statement: if len(genList) < 3 or genList[0] != 'From' : 
        print('Ignore') #This is a msg for debugging the problem 
        continue
    print(genList[3])