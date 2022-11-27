def LCS_DP_CB(x,y):
    print(f"X = \"{x}\" Y = \'{y}\'")
    height=6+len(x)
    index=0
    r=len(x)
    c=len(y)
    lcs=""
    a = [["0"]* (len(y)+1) for _ in range(len(x)+1)]
    for row in range(1, len(x) + 1):
        for col in range(1, len(y) + 1):
            if x[row-1]==y[col-1]:
                k=a[row - 1][col - 1].split()[-1]
                a[row][col]= r"\ "+str(1+int(k))
            else:
                if int(a[row][col-1].split()[-1])>int(a[row-1][col].split()[-1]):
                    a[row][col] = "< "+str(a[row][col-1].split()[-1])
                else:
                    a[row][col] = "^ "+str(a[row-1][col].split()[-1])
    length = a[-1][-1].split()[-1]
    while (r>0 and c>0):
        e=a[r][c].split()
        if e[0]=="^":
            r-=1
        elif e[0]=="<":
            c-=1
        else:
            r-=1
            c-=1
            lcs += x[r]

    for i in range(height):
        if i==0 or i==3 or i==height-1:
            print("---"*(len(y)+6))
        elif i==1:
            print(" "*6+"|"+" "*7+"   ".join(str(i+1) for i in range(len(y))))
        elif i==2:
            print(" " * 6 + "|" + " " * 3+"Y"+" "*3 + "   ".join(str(i) for i in y))
        elif i==4:
            print(" " * 4 + "X |" + " " * 3+"   ".join(str(i) for i in a[0]))
        else:
            print(f"{index+1}"+" " * 3 + f"{x[index]} |" + " " * 3 + " ".join(str(i) for i in a[index+1]))
            index+=1



    print(f"Length of the Longest Common Subsequence is : {length}")
    print(f"Longest Common Subsequence of \"{x}\" and \"{y}\" is \"{lcs[::-1]}\"")

with open('LCS1.txt',"r") as f:
    flag=1
    for line in f.readlines():
        line = line.split(",")
        print(f"{flag}.")
        print(f"============================================================\n{line[0],line[1][:-1]}\n============================================================")
        LCS_DP_CB(line[0],line[1][:-1])
        print("==============================================================\n\n\n")
        flag+=1
