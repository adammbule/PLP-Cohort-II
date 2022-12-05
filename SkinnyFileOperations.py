#Perform file operations in python e.g open/close files read/write
#python in cmd
f = open("Test.txt")
f
f = open("Test.txt", 'w')
f = open("Test.txt", mode='r', encoding='UTF-8')
f.close()
with open("Test.txt", 'w', encoding='utf-8') as f:
    f.write("Text testing\n")
    f.write("This is my second try.Wow!!\n")
    f.write("She makes me so happy like coffee!!")
f = open("Test.txt", 'r', encoding='utf-8')
f.read(5)
f.read(10)
f.read()

#Lambda function same as def function 
# Research on use cases of both functions
greet_user = lambda : print("Hello Mbule")
greet_user() #call the function

#lambdafunction with an argument
list_num = [1,2,3,4,5,6,7,8,9]
filt = list(filter(lambda x: x%2==0, list_num))

print(filt)