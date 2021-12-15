app_details = {"Watsapp":"2hrs","Facebook":"1hr","Instagram":"3hrs","Snapchat":"1 hr","Amazon":"1 hr","Music":"3 hrs"}

print(app_details)

   
class apps:
    def __init__(self):
        self.number=int(input("Enter No.of.apps:"))

        for i in range(self.number):
            self.app=input("Enter app Name :")
            self.amthrs=int(input("Enter amount of hours used:"))
            key=self.app
            value=self.amthrs
            app_details[key]=value
        main()

    def displayapps(self):
        print(app_details)
        
       
   
def install_app():
    app=input("Enter app Name:")
    amthrs=input("Enter amount of hours used:")
    app_details[app]=amthrs
    main()


    
def uninstall():
    app=input("Enter the App Name:")
    app_details.pop(app)
    main()


def display_all(app_details):

    if not app_details:
        print("List is empty: []")
    else:
        print(apps)
        
def quit():
    print("Exit")


#Main function



def main():

    print("1. Install a new app")
    print("2. Uninstall an app")
    print("3. Display all apps")
    print("4. Exit ")
    ch=int(input("Enter your choice:"))

    if(ch==1):
        install_app()
    elif(ch==2):
        uninstall()
    elif(ch==3):
        display_all(app_details)
    else:
        exit()



ab=apps()
fb.displayapps()
main()
