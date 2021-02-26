

def swaping():
    a=open(r"D:\PYTHONPROGRAMMING\C98\file1.txt",'r')
    data_a=a.read()
    print(data_a)

    b=open(r"D:\PYTHONPROGRAMMING\C98\file2.txt",'r')
    data_b=b.read()
    print(data_b)

    with open(r"D:\PYTHONPROGRAMMING\C98\file1.txt",'w') as a:
        a.write(data_b)
    print("new",data_a)

swaping()
