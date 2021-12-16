import tracking
class menu(tracking.app_tracking):
    temp={}
    print("""
          1.Check For App Tracking Of a Person
          2.Add Your Data 
          3.View The Data
          4.Exit The App
          """)
    obj=int(input("Please Enter Your Choice:"))
    if(obj==1):
        name=input("Enter The Name Of The Person Whom You Want To Track?")
        obj=app_tracking(name)
        obj.warningsfun()
    elif(obj==2):
        na=input("Enter Your Name:")
        print("\n")
        noa=int(input("Enter The Number Of App Data You Want To Add?"))
        for i in range(noa):
            appname=input("Enter The App Name:")
            usage=int(input("Enter The Usage In Minutes:"))
            print("\n")
            temp[appname]=usage
        data[na]=temp
        menu()
    elif(obj==3):
        viewdata()
    elif(obj==4):
        print("Thank You For Using Digital Wellbeing")
        exit()
data={"jananiya":{"whatsapp":30,"snapchat":30,"Spotify":20,"facebook":20,"Youtube":60},
      "jina":{"Instagram":60,"Twitter":10,"Spotify":70,"Tunein":5,"Youtube":15}}



menu()
