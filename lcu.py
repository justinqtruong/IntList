import json
from lcu_driver import Connector
from int import *
connector = Connector()
#credit https://www.youtube.com/watch?v=crKTr5EwwNM
#Devin Phillips Youtube Guide "Python Coding with League of Legebds Client(LCU)"

async def champSelect(connection):
    champSelect = await connection.request('get', '/lol-champ-select/v1/session')
    if champSelect.status != 200:
        pass
    else:
        champSelectData = json.loads(await champSelect.read())
        #print(champSelectData['myTeam'][0]['summonerId'])
        teamSize = len(champSelectData['myTeam'])
        lobby = open("lobby.txt", "w") #Lobby Text file copied from league lobby
        for i in range(teamSize):
            pog =  await connection.request('get', '/lol-summoner/v1/summoners/'+ str(champSelectData['myTeam'][i]['summonerId']))
            huge = json.loads(await pog.read())
            lobby.write(huge['displayName'] + "\n")          
        lobby.close()
        nameCheck()
            
           


@connector.ready
async def connect(connection):
    print("connected to league")
@connector.close
async def disconnect(connection):
    print("disconnected to league")
    quit()

@connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def updated(connection,event):
    await champSelect(connection)
@connector.ws.register('/lol-pre-end-ofgame/v1/currentSequenceEvent', event_types=('UPDATE',))        
async def endGame(connection,event):
    print()
    end = await connection.request('get', 'lol-pre-end-of-game/v1/currentSequenceEvent')
    end = json.loads(await end.read())
    print(end)
#live code
connector.start()

