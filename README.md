ELO Machine:
This will be a website that will have the following webpages
1. Leaderboards
   1. Will be able to display the current rankings sorted by ELO throughout all time.
   2. Will be able to display the current rankings sorted by ELO for the current season
   3. Will be able to display the rankings of past seasons
   4. Each leaderboard will contain the following info: 
      Player first name, Player last name, Player age, Timeframe ELO, Timeframe wins, and Timeframe losses.
2. Rules
   1. Will have a explanation of the rules of carpetball
   2. Will also describe season rules and rewards
3. Enter Matches
   1. User will be able to select two players via two dropdowns
      1. User will optionally will be able to create a player here using a popup window.
   2. After selecting two players, the user will be set the following options: Affect ELO, Single or Multiple Matches
   3. If user selected single match then pictures of the two players will appear. 
      The user can click on one of the two pictures. After clicking a popup window to confirm. 
      If the user selected an ELO affecting match it will then show the updated ELO's and rankings for that season.
      1. If a player does not have a profile picture a button will appear underneath to upload a picture.
      2. If a player does have a picture then a button will appear underneath to edit the picture.
   4. If user selected multiple matches then two text boxes will be in between the two player pictures.
      The user can then enter the wins for each player in the respective text box.
      After entering the match info the user can click a button to submit matches.
      The user will be prompted with the same confirmation window as described in part iii.
      1. The buttons described under part iii. for the pictures still appear.
4. Tournament Brackets
   1. User will be able to create tournaments brackets
   2. When creating a bracket the user will select the following options:
      Number of Players (numbers divisible by 4 starting at 4 up to 32), Single or Double Elimination, 
      Number of Games in a Series (Best of 1, 3, 5, 7), Final Series is longer (best of 1 becomes best of 3, 3 becomes 5, 5 becomes 7, 7 unaffected),
      Affect ELO, random or set seeding, use total or seasonal ELO.
   3. After selecting the options, user will need to select the players.
      1. There will be a button to create new players.
         1. After creating a new player there will be a button to create another new player.
         2. New players will automatically be added to the list
      2. There will be a button next to each players name to remove.
      3. Once sufficient number of players have been selected the user will be able to click a button labeled begin bracket.
   4. Once bracket is begun players will be seeding based on the option selected
      1. If set, then four "divisions" will be created with selected ELO in mind. Top 4 players will be placed in their own division.
         Process is repeated for the next four until every player is in a division. 
         The division is then used for placement in one quarter of the bracket.
      2. If random, then players will be randomly set in their location.
   5. After the bracket has been created, then at thee top of the page will display the current matchup and 
      the user will be able to enter the match information the same way as done on the "Enter Matches" Page
   6. Underneath entering the match information will be display of the current bracket.
   7. After the user enters a match information the website will automatically show the next match.
   8. Process is repeated until bracket is completed


Other Notes:
The website will be created using React with a Python Backend.
The website will be hosted by Github.
There will be a database server hosted on a personal machine.
When loading any page besides the rules page, it will test the connection to the database and if unsuccessful, 
then the page will display an error message and thats it.
The database will be accessed by the website via API calls.

There will also be a script stored in the repository which will have developer functionality. 
This is where the following features will be stored:
* Ability to start a season
* Ability to end a season
* Ability to reset a season
* Ability to remove a player from the database
* Ability to undo a player's last match (Will undo ELO changes)
* Ability to test each functionality. 

All features will be executable via CLI.


