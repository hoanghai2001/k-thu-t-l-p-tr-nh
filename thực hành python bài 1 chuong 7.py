input_file=open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    While(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input _file.close()
