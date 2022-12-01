#Perform file operations in python e.g open/close files read/write
#python in cmd
f = open("Test.txt")
f
f = open("Test.txt", 'w')
f = open("Test.txt", mode='r', encoding='UTF-8')
f.close()
with open("Test.txt", 'w', encoding='utf-8') as f:
    f.write("Text testing\n")