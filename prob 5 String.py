cnp=str(input("Introduceti CNP-ul:"))
nr=0
x=len(cnp)
if (len(cnp)<13)or(len(cnp)>13):
    print("Este gresit")
elif len(cnp)==13:
    for i in cnp:
        if (48<=ord(i)) and (ord(i)<=57):
            nr+=1
        if nr==13:
            print("CNP-ul este corect")
        else:
            print("CNP-ul nu este corect")
