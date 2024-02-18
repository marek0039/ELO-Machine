//created by Marek Niemyjski
//copied from Geeks for Geeks
//https://www.geeksforgeeks.org/create-a-responsive-navbar-using-reactjs/

import React from 'react';

const Rules = () => {
  return (
    <body>
    <div
      style={{
        display: 'flex',
        justifyContent: 'centre',
        alignItems: 'centre',
        height: '100vh'
      }}
    >
    <h1>Carpetball Rules</h1>
    </div>
    <h3>Requirements</h3>
      <p>
        1. Carpetball Table (12' - 16' long). <br>
        2. Billiard Table Ball Set minus 8 ball. <br>
        3. 2 Players <br>
      </p>
      <h3>Setup</h3>
      <p>
        1. The players separate the billiard balls into solids and stripes and sets aside the cue ball. Each player takes one set. <br>
        2. Each player chooses a side of the table and then places their balls in any assortment as long as they are all in between their pit and the halfway mark (gap in the felt). <br>
        3. Players then select a player to go first and whoever is first, takes the cue ball (See House rules for deciding who goes first). <br>
        4. Each player then stands behind their respective pits and the first player begins. <br>
      </p>
      <h3>Objective</h3>
      <p>
        1. Knock all of your opponents billiard balls into their pit before all of your's get knocked out. <br>
      </p>
      <h3>Procedure</h3>
      <p>
        1. The player with the cue ball either rolls or throws it (lightly) towards the opponents balls. <br>
            1a. If the active player knocks any of their own balls past the halfway point, they are counted as out and placed in the respective player's pit. <br>
            1b. If the active player knocks any of their opponents balls past the halfway point, they are still in play. <br>
            1c. The active player may only roll/throw from behind their pit. They may lean forwards but their feet must be behind the pit while going. <br>
        2. Players take turns throwing the cue ball back and forth until one player knocks all of their opponents balls into their pit. <br>
        3. Once one player knocks all balls, the opposing player enters "Sudden Death". <br>
        4. While in "Sudden Death", the remaining player attempts to roll/throw the cue ball and knock the remaining balls into their opponents pit. <br>
            4a. For each attempt, the player must knock at least one ball into the pit. <br>
            4b. If the player successfully knocks out all remaining balls, the game is a draw and is replayed again with one less ball. <br>
      </p>
      <h3>House Rules</h3>
      <p>
        1. To decide who goes first, the player who has played Carpetball the most recently goes second. <br>
            1a. If both players played against each other recently, then the winner of the last match goes second. <br>
        2. In a draw scenario (Sudden Death), the player who knocked all of their opponents balls first goes first. <br>
      </p>
      </body>
  );
};

export default Rules;