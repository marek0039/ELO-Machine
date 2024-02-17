//created by Marek Niemyjski
//copied from Geeks for Geeks
//https://www.geeksforgeeks.org/create-a-responsive-navbar-using-reactjs/

import React from "react";
import {
    Nav,
    NavLink,
    Bars,
    NavMenu,
} from "./NavBarElements";

const Navbar = () => {
    return (
        <>
            <Nav>
                <Bars />

                <NavMenu>
                    <NavLink to="/rules" >
                        Rules
                    </NavLink>
                    <NavLink to="/leaderboards" activeStyle>
                        Leaderboards
                    </NavLink>
                    <NavLink to="/matches" activeStyle>
                        Enter Matches
                    </NavLink>
                    <NavLink to="/bracket" activeStyle>
                        Create Tournament Bracket
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;