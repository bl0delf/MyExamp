file1=open("/home/alex/MyExamp/1.log","r")
file2=open("/home/alex/MyExamp/ERRORs.log","w")
pid=str(input("Input ERROR PID : "))
pid=pid+"|"
filepid=open("/home/alex/MyExamp/PID.log","w")
temp = ""

for i in file1:
    if i.find("ERROR") != -1 and i.find("DEBUG") == -1 :
        file2.write(i)
        temp += i
        temp += "|"
    if i.find(pid) != -1 :
        filepid.write(i)
eq=temp.split("|")
del temp
eq=list(eq)
file6=open("/home/alex/MyExamp/file6.log","w")
count=0;
temp = ""
for i in eq:
    if i.find("ERROR")!=-1:
        file6.write(i)
        file6.write(eq[count+2])
        file6.write("\n")
        count+=1


        
file1.close; file2.close; filepid.close; file6.close
