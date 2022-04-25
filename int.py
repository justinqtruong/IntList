

def nameCheck(): 

    lobby = open("lobby.txt", "r") #Lobby Text file copied from league lobby
    LobbyNames = lobby.readlines() #read line by line    

    for name in LobbyNames: #name is whole line      
        intList = open("Int List.txt", "r") #int List
        runItDown = intList.readlines()

        for inter in runItDown: #compare name to every name in intlist
            if name.strip() == inter.strip():
                print("Run it Down on {}".format(inter.strip())) #sprint it
        
        intList.seek(0)
        
        
        


    lobby.close()
    intList.seek(0)







