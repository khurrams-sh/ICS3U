fileName=input("Enter file name: ")
if (fileName==""):
    fileName="friends.txt"
if (fileName.endswith(".txt")==False):
    fileName+=".txt"
fout=open(fileName,"w")
while True:
    print("Enter a friend's name:")
    name=input("-> ")
    if (name=="STOP"):
        break
    fout.write(name+"\n")
fout.close()
