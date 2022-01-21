# Election_Analysis

## Overview of Elections:

The purpose of this election audit analysis is to discover the results of an election for a U.S. congressional precinct in Colorado. A python script has been created using the panda’s library to determine the outcomes of the election without requiring several manual work to populate the results. The outcome includes finding out the winning candidate, the total votes, breakdown of votes for each candidate, percentage of each candidate, vote turnout for each county, percentage of votes from each county, and the county with the highest turnout. These insights will then be passed to the Colorado Board of Election Commission to make results official and receive their desired election data request.

## Election-Audit Results:

### Below is a summary of the results of the election.

The "PyPollChallenge.py" file gives the output for the questions below to be answered.

* How many votes were cast in this congressional election? 
  * 369,711 votes
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * Jefferson: 10.5% with 38,855 votes
  * Denver: 82.8% with 306,055 votes
  * Arapahoe: 6.7% with 24,801 votes
* Which county had the largest number of votes? 
  * Denver
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  * Charles Casper Stockham has 23.0% of total votes with 85,213 votes
  * Diana DeGette has 73.8% of total votes with 272,892 votes
  * Raymon Anthony Doane has 3.1% of total votes with 11,606 votes
  
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  * Dian DeGette won the election 73.81% of total votes. She received a total of 272,892 votes.

 The image below is what the txt file "election_Analysis.txt" outputs when the PyPollChallenge.py script is run.
 
 ![image](https://user-images.githubusercontent.com/96553992/150611851-ed19e4d5-5ba5-4e92-b02f-e968a0089769.png)


## Election-Audit Summary

Although this script was used for a Colorado election, the use of the script built does not just stop there. With some modifications, and dating containing similar data such as name of voter, the place they are voting from, and the person they voted for, the script can be used. The following are two examples of how this script could be modified to serve a different purpose and determine election results.

### Example 1 
The first example of how this script could be modified to serve a different purpose would be to determine the winner of an election not held in the same voting platform. Instead of having data for the different city’s voters are from, there could be data from how they voted. Examples of voting platforms being via email, Google Doc, forum vote, and so on. There could be another dictionaries, lists, and variable names could be replaced to hold the voting data platform. This would allow for a similar breakdown of percentage of voting method, the total turnout, what platform was most used to vote, and the winning candidate of the election. Furthermore, the scripts could help the election commission decide what voting platforms to use going forward and what platforms can be retired. All based on the most popular voting mechanism. It would make the set-up of voting platform easier, and voters would find that process smoother.

### Example 2
Another way this script could be used would for other elections that the Colorado election commission oversees. Similarly, a condensed CSV file with all the election data would be provided for the script to run properly. The script could even be used for a bigger election such as the election of the governor. Instead of county breakdown, a city breakdown could provide in the csv file. One top of that, the ballot ID and the candidate they voted for would be provided in the data file. This would lead to results of what cities certain candidates won, the voter turnout for each city, percentage of total votes for each candidate, and the winner of the governor election. 

The examples mentioned above are just a few ways this python script could be altered so that time and money could be saved in gathering more resources to create a whole new script or process. The possibilities are endless, I strongly recommended leveraging the script to fulfill future elections the Colorado Election Commission will hold.

