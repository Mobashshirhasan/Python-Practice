# f = open('myfile.txt', 'r')

# text = f.read()
# print(text)
# f.close()



# f = open('myfile3.txt', 'a')  #this wll open files for appending only
# f.write(' Hello, form India ')
# f.close()



# f = open('myfile2.txt', 'w')    #this will open files for writing onluy and creates a new file if doesn't exist.
# text = f.read()
# print(text)
# f.close()





# f = open('myfile2.txt', 'x')    #this will creates a files and gives an error if the file is already exists.
# text = f.read()
# print(text)
# f.close()



with open('myfile.txt', 'a') as f:
    f.write("hey i am inside your file")