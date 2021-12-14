Contacts=[{"firstname":"abishek","lastname":"thakur","mobile":8248603107},
          {"firstname":"ak","lastname":"Disys","mobile":9962508398},
          {"firstname":"aarthi","lastname":"mam","mobile":9025975784},
          {"firstname":"venkatesh","lastname":"Sir","mobile":9900367097}]

#print(Contacts)
class Mobile_Contacts:
    def __init__(self,serial_number):
        self.serialnumber=serial_number

    def show(self):
        if self.serialnumber==1:
            firstname=input("enter firstname")
            lastname=input("enter lastname")
            mobile=input("enter number")
            print(obj.savecontacts(firstname,lastname,mobile))
    
        elif self.serialnumber==2:
            b=input("enter your firstname")
            print(obj.deletecontacts(b))

        elif self.serialnumber==3:
            first_name=input("enter your name")

            print(obj.searchcontacts(first_name))
        print(Contacts)
            

    def savecontacts(self,firstname,lastname,mobile):
        self.firstname=firstname
        self.lastname=lastname
        self.mobile=mobile
        phone_contact=str(self.mobile)
        
        
        if type(self.firstname)==str and type(self.lastname)==str and type(phone_contact)==str :
            if (len(self.firstname)<=10) and (len(self.lastname) <=10) and (len(phone_contact) == 10):
                Contacts.append({"firstname":self.firstname,"lastname":self.lastname,"mobile":int(phone_contact)})
                return "your contact is saved"
            else:
                raise ValueError("invalid")
        else:
            raise TypeError("invalid")

    def deletecontacts(self,Firstname):
        for i in Contacts:
            if i['firstname']==Firstname :
                i.clear()
                print("your contact is deleted")
                
    def searchcontacts(self,first_name):
        search=[]
        for i in Contacts:
            if i['firstname']==first_name:
                search.append(i)
                print(search)
        


    
print("****CONTACTS****")
print(" 1.Save 2.Delete 3.search contact ")
Firstname=int(input("enter serial number"))
obj=Mobile_Contacts(Firstname)
obj.show()







    
