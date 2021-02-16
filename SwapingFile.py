

def swaping():
    a=open("file1.txt",'r')
    data_a=a.read()
    print(data_a)

    b=open("file2.txt",'r')
    data_b=b.read()
    print(data_b)
    a.write(data_b)

    with open("file1.txt",'w') as a:
        a.write(data_b)
    print("new",data_a)


swaping()
