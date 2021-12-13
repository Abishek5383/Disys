photos={"camera":10,"watsapp images":25,"canva":1,"screenshots":100}
photos["B612"]=10
photos["sweetsnap"]=7
photos["snapseed"]=5       
photos["candycamera"]=9
photos["bloom camera"]=5
print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
