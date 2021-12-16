class app_tracking:

    def __init__(self,name):
        self.name=name

    def warningsfun(self):
        print("Displaying All The Apps That are Overused\n")
        for k,v in data[self.name].items():
            if(v>45):
                print(k,end=" ")
        print("\n")
        menu()



def viewdata():
    for k,v in data.items():
        print(k,v)

    print("\n")
    menu()

