# Practicing this assignment: https://vincit.fi/risingstar/Vincit-Rising-Star-2021-Pre-assignment.pdf

## General:

● Both start and end dates should be included in a date range.

● A day’s price means the price at 00:00 UTC time (use price data from as close to midnight as
  possible as the day’s price, if you don’t have a datapoint from exactly midnight).
  
● Allow the user of your application to pass the start and end dates of the date range in some way,
  e.g. via input fields in a UI or as parameters to an API.
  
## TASK A: How many days is the longest bearish (downward) trend within a given date range?

● Definition of a downward trend shall be: “Price of day N is lower than price of day N-1”

● Expected output: The maximum amount of days bitcoin’s price was decreasing in a row.

## TASK B: Which date within a given date range had the highest trading volume?

● Expected output: The date with the highest trading volume and the volume on that day in
  euros.
  
## TASK C: The application should be able to tell for a given date range, the best day for buying bitcoin, 
and the best day for selling the bought bitcoin to maximize profits. If the price only decreases in the date range, 
your output should indicate that one should not buy (nor sell) bitcoin on any of the days.

● Expected output: A pair of days: The day to buy and the day to sell. In the case when one
should neither buy nor sell, return an indicative output of your choice.

## What we value:

● Clean code

● Ease of use — Either host your solution somewhere where it can be used immediately, or include
clear directions (e.g. in a README file) for running your solution.

● Simplicity — Minimize the use of external libraries and dependencies. We want to see how you
manage with a programming language of your choice, not how many packages you are able to
import. You are of course highly encouraged to use any conveniences or standard library utilities
that ship with your chosen language. It's also fine to build your solution around a single 3rd party
library or framework, if that adds value to your solution.

● Extensibility — Scrooge only wants these three features for now, but very likely wants to hire us
to add capabilities to the application after it has proved its value to him


