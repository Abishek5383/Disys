Swiggy=[{"hotelname":"Saravanabavan","location":"Adyar","recommendedfood":"Dosa","rating":"4.8"},
        {"hotelname":"Ananda bhavan","location":"Thiruvanmiyur","recommendedfood":"idly","rating":"4.7"},  #contacts=swiggy,Mobile_Contacts=Hotel_Nmaes
        {"hotelname":"Thalapakattu","location":"Porur","recommendedfood":"Chicken biriyani","rating":"5"},
        {"hotelname":"Aaifa Biriyani","location":"Thambaram","recommendedfood":"Mutton Gravy","rating":"4.7"},]


print(Swiggy)
class Hotel_Names:
    def __init__(self,serial_number):
        self.serialnumber=serial_number

    def show(self):
        if self.serialnumber==1:
            
            print(obj.searchhotels(location,recommendedfood,rating))
    
        elif self.serialnumber==2:
            print(obj.searchhotels(hotelname))

        elif self.serialnumber==3:
            

            print(obj.searchlocation(location))
        elif self.serialnumber==4:
            

            print(obj.searchrating(location))    
        print(hotel)
        
            

    def searchhotels(self,location,recommendedfood,rating):
        self.hotel_name=input("enter a hotel")
        self.loca_tion=location
        self.recommended_food=recommendedfood
        self.rati_ng=rating
        for i in Swiggy:
            if i["hotelname"]==self.hotel_name:
                print(i)
        
        
        
                
    def searchhotels(self,hotal_name):
        search=[]
        for i in Swiggy:
            if i['hotelname']==hotal_name:
                search.append(i)
                
        


    
print("Swiggy")
print(" 1.Search hotel names 2.Location 3.Recommended food 4.Rating ")
ser=int(input("enter serial number"))
obj=Hotel_Names(ser)
obj.show()










    

