# Split function breaks a string into parts and produces a list of strings. We think of these as words.
# We can access a particular word or loop through all the words
name = 'My name is Md. Jahidul Islam'
gen_list = name.split()
print('Newly generated list form the string is:',gen_list, 'And the length of the list is:', len(gen_list))
# Printing the words individually 
for word in gen_list:
    print(word)

# We can specify what delimiter character to use in the spliting like ;, \n, and etc.
line = 'I;study;at;North South University'
gen_list1 = line.split(';')
print('Newly generated list form the string 2:',gen_list1, 'And the length of the list is:', len(gen_list1))
# Printing the words individually 
for word in gen_list1:
    print(word)

# An example using file
fhand = open('Jahid1.txt')
for itr_var in fhand:
    itr_var = itr_var.rstrip()
    if not itr_var.startswith('Please'):
        continue
    newList = itr_var.split()
print('New created list:',newList)
