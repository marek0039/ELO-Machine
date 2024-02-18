//created by Marek Niemyjski
//copied from Geeks for Geeks
//https://www.geeksforgeeks.org/create-a-responsive-navbar-using-reactjs/

import React from 'react';

const Home = () => {
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
      <h1>Welcome to the Carpetball ELO Machine</h1>
    </div>
      <h6> Created By: Marek Niemyjski </h6>
      <h6> Contributed By: Nick Arredondo, Michael Ross, Jackie Dworaczyk, Matthew Merrill </h6>
      <h3> {"\n"}{"\n"}Carpetball Basics </h3>
      <p>
        Carpetball is a game which uses a unique table made of wood with a felt carpet on the inside surfaces.
        Table sizes can vary, but the table used at Marek's house is 2 feet wide, 12 feet long, and 3 feet, 7.5 inches tall.
        Inside the table there is a 7 inch drop down, which is the game's playspace.
        At each of the table there is an additional 3 inch pit where the felt carpet creates a hammock-like structure. <br>
        The game uses a standard billiard table ball set minus the 8 ball.
      </p>
    </body>
  );
};

export default Home;