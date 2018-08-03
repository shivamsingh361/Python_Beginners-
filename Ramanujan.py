def Ramanujan_no(min ,max):
    dict1,dict2 = {},{}
    res = []
    min,max = int(abs(min) ** (1/3)) ,int(abs(max) ** (1/3))
    for i in range(min, max):
        dict1[i] = i**3 
    for i in range(min, max+1):
        for j in range(i,max+1):
            x = (i**3) + (j**3)
            if x not in res:
                res.append(x)
                dict2[x] = (i,j)
            else:
                print(x,'=',dict2[x][0],dict2[x][1],'=',i,j)


if __name__ == '__main__':
    Ramanujan_no(int(input("Enter minimum range:")),int(input("Enter max range:")))