
iss=["STOP","ADD","SUB","MULTI","MOVER","MOVEM","COMB","BC","DIV","READ","PRINT"]
ad=["END","START","ORIGIN","EQU","LTORG"]
rg=["R1","R2","R3"]
dl=["DS","DC"]
cc=["EQ","LT","GT","LE","GE","NE"]
final=[]
with open('a') as f:
    contents=f.readLines()
for i in contents:
    for j in i.split(" "):
        if j in iss:
            index=iss.index(j)
            final.append([j,"IS",index,"1"])
        if j in ad:
            index=ad.index(j)
            final.append([j,"AD",index,"-"])
        if j in dl:
            index=dl.index(j)
            final.append([j,"DL",index,"-"])
        if j in rg:
            index=rg.index(j)
            final.append([j,"RG",index,"-"])
        if j in cc:
            index=cc.index(j)
            final.append([j,"CC",index,"-"])
for k in final:
    print(k)
            

      
a.txt

JOHN    START  200
        MOVER  R1 , ='3'  200
        MOVEM  R1 , X     201
L1      MOVER  R2 , ='2'  202
        LTORG             203
X       DS     1          204
        END
