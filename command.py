import mysql.connector
import datetime

mydb = mysql.connector.connect(
	host="184.179.169.45",
	user="elo_weaker",
	password="weakerPassword",
	database="eloMachine"
)

mycursor = mydb.cursor()

def eloCalculation(player1Elo, player2Elo, winner):
	Ea = 1 / (1 + 10 ** ((player2Elo - player1Elo) / 400))
	Eb = 1 / (1 + 10 ** ((player1Elo - player2Elo) / 400))

  	#Set player1's k
	if(player1Elo < 2100):
		Ka = 32
	elif(player1Elo >= 2100 and player1Elo < 2400):
		Ka = 24
	else:
		Ka = 16
  	#Set player2's k
	if(player2Elo < 2100):
		Kb = 32
	elif(player2Elo >= 2100 and player2Elo < 2400):
		Kb = 24
	else:
		Kb = 16

	player1NewElo = int(round(player1Elo + Ka * (winner%2 - Ea)))
	player2NewElo = int(round(player2Elo + Kb * ((winner+1)%2  - Eb)))

	if(player1NewElo < 0 and player2NewElo < 0):
		return(0, 0)
	elif(player1NewElo < 0):
		return(0, player2NewElo)
	elif(player2NewElo < 0):
		return(player1NewElo, 0)
	else: 
		return(player1NewElo, player2NewElo)

def startSeason():
	#Get current season
	sql = "SELECT seasonID FROM seasonCount WHERE active = 1"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	#End the previous season
	sql = ("UPDATE seasonCount SET active = 0, endedOn = CURDATE() WHERE seasonID = %s" % str(myresult[0][0]))
	print(sql)
	mycursor.execute(sql)

	#Create new season
	sql = ("INSERT INTO seasonCount VALUES(%s,CURDATE(),NULL,1)" % str((myresult[0][0]+1)))
	mycursor.execute(sql)
	#Commit the changes
	mydb.commit()

def createMatch(player1, player2, winner): #for this to work, update season database ELO to elo. add boolean active season to season database
	sql = "SELECT elo FROM total WHERE playerID = {}" .format(player1)
	mycursor.execute(sql)
	player1AllTimeElo = mycursor.fetchall() 

	sql = "SELECT elo FROM total WHERE playerID = {}" .format(player2)
	mycursor.execute(sql)
	player2AllTimeElo = mycursor.fetchall()

	sql = "SELECT elo FROM seasons WHERE playerID = {} AND activeSeason = true" .format(player1)
	mycursor.execute(sql) 
	player1SeasonElo = mycursor.fetchall()

	sql = "SELLECT elo FROM seasons WHERE playerID = {} AND activeSeason = true" .format(player2)
	mycursor.execute(sql)
	player2SeasonElo = mycursor.fetchall()

	newPlayer1AllTimeElo, newPlayer2AllTimeElo = eloCalculation(player1AllTimeElo, player2AllTimeElo, winner)
	newPlayer1SeasonElo, newPlayer2SeasonElo = eloCalculation(player1SeasonElo, player2SeasonElo, winner)

	sql = "SELECT season FROM seasons WHERE activeSeason = true"
	mycursor.execute(sql) 
	seasonNum = mycursor.fetchall()

	someDT = datetime.now()
	dateAndTime = someDT.strftime('%Y-%m-%d %H:%M:%S')

	sql = "INSERT INTO matches VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})" .format(seasonNum, dateAndTime, player1, player2, winner, player1SeasonElo, newPlayer1SeasonElo, newPlayer1SeasonElo, newPlayer2SeasonElo)
	sql = "INSERT INTO matches VALUES (-1, {}, {}, {}, {}, {}, {}, {}, {})" .format(dateAndTime, player1, player2, winner, player1AllTimeElo, newPlayer1AllTimeElo, player2AllTimeElo, newPlayer2AllTimeElo)

	sql = "UPDATE total SET elo = {} WHERE playerID = {}" .format(newPlayer1AllTimeElo, player1)
	mycursor.execute(sql)

	sql = "UPDATE total SET elo = {} WHERE playerID = {}" .format(newPlayer2AllTimeElo, player2)
	mycursor.execute(sql)

	sql = "UPDATE seasons SET elo = {} WHERE playerID = {} AND activeSeason = true" .format(newPlayer1SeasonElo, player1)
	mycursor.execute(sql) 
	
	sql = "UPDATE seasons SET elo = {} WHERE playerID = {} AND activeSeason = true" .format(newPlayer2SeasonElo, player2)
	mycursor.execute(sql)

	mydb.commit()

	return(newPlayer1AllTimeElo, newPlayer2AllTimeElo, newPlayer1SeasonElo, newPlayer2SeasonElo)

	#assumptions made; 
	#	two different players are selected 
	#	winner is 1 or 2
	# 	both players exist 

"""
print("Before Season Start --------------------------------------------")
mycursor.execute("SELECT * FROM seasonCount")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("Run Season Start --------------------------------------------")
startSeason()


mycursor.execute("SELECT * FROM seasonCount")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
"""
test = eloCalculation(1600,1400,1)
print("Player 1 new elo: " + str(test[0]) + " Player 2 new elo: " + str(test[1]))
mycursor.close()
