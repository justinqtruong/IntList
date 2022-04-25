
def main():
    lobby = open("lobby.txt", "r") #Lobby Text file copied from league lobby
    LobbyNames = lobby.readlines() #read line by line
    extra = " joined the lobby" #part of string we want to cut off
    index = 0 #compare extra to lobby league string
    endMarker = 0 #index of where we want to cut string
    

    for name in LobbyNames: #name is whole line

        for i in range(len(name) - 1):
            if name[i] == extra[index]:
                index += 1
            else:
                index= 0
                endMarker = 0
            if index == 1:
                endMarker = i

        index = 0
        name = name[0:endMarker]         

        
        intList = open("Int List.txt", "r") #int List
        runItDown = intList.readlines()

        for inter in runItDown: #compare name to every name in intlist
            if name.strip() == inter.strip():
                print("Run it Down on {}".format(inter.strip())) #sprint it
        
        intList.seek(0)
        
        
        


    lobby.close()
    intList.seek(0)



if __name__=="__main__":
    main()




