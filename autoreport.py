from lcu_driver import Connector
from time import sleep

# AutoReport Script by Dracea Lucian

connector = Connector()
friendList = []


@connector.ready
async def connect(connection):
    temp = await connection.request('get', '/lol-chat/v1/me')
    temp = await temp.json()
    friendList.append(temp['summonerId'])

    temp = await connection.request('get', '/lol-chat/v1/friends')
    temp = await temp.json()
    for friend in temp:
        friendList.append(friend['summonerId'])

    temp = await connection.request('get', '/lol-end-of-game/v1/eog-stats-block')
    temp = await temp.json()
    gameID = temp['gameId']
    teams = temp['teams']
    for team in teams:
        for player in team['players']:
            if player['summonerId'] not in friendList:
                _report = {
                    "offenderPuuid": player['puuid'],
                    "offenderSummonerId": player['summonerId'],
                    "gameId": gameID,
                    "categories": ['NEGATIVE ATTITUDE', 'VERBAL ABUSE', 'LEAVING THE GAME / AFK', 'INTENTIONAL FEEDING', 'HATE SPEECH', 'CHEATING', 'OFFENSIVE OR INAPPRIOPRIATE NAME'],
                    "comment": " "
                }
                temp = await connection.request('post', '/lol-end-of-game/v2/player-reports', data=_report)
                temp = await temp.json()
                print("Reported", player['summonerName'], '\n')
            else:
                print("Skipped friend", player['summonerName'], '\n')


connector.start()
sleep(5)
