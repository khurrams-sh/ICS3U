def getFileName():
    fName=input("Enter file name: ")
    if (fName==""):
        fName="friends.txt"
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName
fileName=getFileName()
fin=open(fileName,"r")
while True:
    line=fin.readline()
    if line=="":
        break
    print(line.strip())
fin.close()

