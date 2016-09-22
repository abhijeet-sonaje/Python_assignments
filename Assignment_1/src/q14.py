print("( 1 , 1 )")
posi = [1]
posj = [1]
flag = []
temp = True
for i in range(1,4):
    #print("i:",i)
    for j in range(1,4):
        #print("j:",j)
        for k in range(0,len(posi)):
            flag.append(0)
        for p in  range(0,len(posi)):
            print("p:",p,posi,posj)
            if (posj[p] != j) and ((j-posj[p]) != (i-posi[p])) and (posi[p] != i):
                flag[p] = 1;
                print("p:",p,"flag:",flag[p])
            for z in flag:
                if z == 0:
                    temp = False
            if temp == True:
                print("(",i,",",j,")")
                posi.append(i)
                posj.append(j)
