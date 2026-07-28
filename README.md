# BBQ pricing calculator

## Overview
This program is designed to calculate the price to charge a customer for barbecue catering for one or two meats. Using variables such as cost per pound, portion per person, it calculates the total cost for the customer and the required raw weight. It then calculates the sides and stores them all into a database

## Features
- Meat types include pork, chicken, and brisket
- Estimates cooked off percentage to ensure proper raw weight
- Validates user input
- Supports one or two meat types
- Side types include mac and cheese, green beans, baked beans, and cole slaw
- Stores orders into a database with a unique order number
- Orders can be looked up later

# Version History

# Version 1

## Features
- Meat types include pork, chicken, and brisket
- Control portion sizes if two meats
- An internal data layer to separate the meat data from the calculations
- Estimates cooked off percentage to ensure proper raw weight
- Validates user input
- Supports one or two meat types
- Adds markup percentage to the total supplier cost

## What I learned
- Improved syntax and formatting
- Changing code to reduce redundancy
- Separating data access from business logic
- Building the program with future changes in mind

## Future improvements
- Save quotes in a database
- Add sides
- Separate the function groups into different files for readability

# Version 2
## New Features
- can now take both meats and sides
- changed order structure 
- seperated program into multiple files

## What I learned
-how to debug code more carfuly
-breaking down what i need to do into multiple steps
-how to better organize my output to be clearer
-gained a better understanding of how for loops work and how they differ from java
-how to prevent data loss and how it occurs
## Future improvements 
-save orders into a database
-Give every order a unique order number 
-have it save to be able to look up orders later
-eliminate some redundancies that finishing version 2 made 
-look into combining the sides and meats dictionary into one

# Version 3
## New Features
- introduced database support 
- new order structure is now stored in database instead of a dictionary
- got rid of the dictionaries entierly everything is now stored inside of the database
- order lookup
- Pricing model updated to match the real business
- Simplified calculations after customer feedback
## What I learned
- Reducing redundant information in a database by making relationship tables
- I learned that the software should adapt to the business process, not the other way around. After reviewing real orders with the client, we discovered that the pricing model should use a fixed price per pound for each meat, and that the separate 'both meats' calculation wasn't actually part of their workflow. Updating the software to match the real process made the program simpler and more accurate.
- Building the software is just half of the job; making sure it meets business needs is also extremely important
- How SQLite differs from SQL 
- Why it is important when starting to build a program to build it to be updatable
- Learned how to design a relational database using primary keys, foreign keys, and relationship tables to model real-world data.
## Future improvements
- make into a website using javascript and html
- add buttons on the website to add/remove a meat or side and one to change the values in the meats or sides

