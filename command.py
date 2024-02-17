import mysql.connector

mydb = mysql.connector.connect(
  host="184.179.169.45",
  user="elo_weaker",
  password="weakerPassword",
  database="eloMachine"
)

mycursor = mydb.cursor()

def eloCalculation(player1elo,player2elo,winner):
  Ea = 1 / (1 + 10 ** ((player2elo - player1elo) / 400))
  Eb = 1 / (1 + 10 ** ((player1elo - player2elo) / 400))

  #Set player1's k
  if(player1elo < 2100):
    Ka = 32
  elif(player1elo >= 2100 and player1elo < 2400):
    Ka = 24
  else:
    Ka = 16
  #Set player2's k
  if(player2elo < 2100):
    Kb = 32
  elif(player2elo >= 2100 and player2elo < 2400):
    Kb = 24
  else:
    Kb = 16

  player1newelo = player1elo + Ka * (winner%2 - Ea)
  player2newelo = player2elo + Kb * ((winner+1)%2  - Eb)

  return(int(round(player1newelo)),int(round(player2newelo)))


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

def createMatch(player1, player2, winner):
  pass

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
