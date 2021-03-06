# Election_Analysis

## Overview of Elections:

The purpose of this election audit analysis is to discover the results of an election for a U.S. congressional precinct in Colorado. A python script has been created using the panda’s library to determine the outcomes of the election without requiring severe manual work to populate the results. The outcome includes finding out the winning candidate, the total votes, breakdown of votes for each candidate, percentage of each candidate, voter turnout for each county, percentage of votes from each county, and the county with the highest turnout. These insights will then be passed to the Colorado Board of Election Commission to make results official and receive their desired election summary results.

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

 The image below is what the txt file "election_analysis.txt" outputs when the PyPollChallenge.py script is run.
 
 ![image](https://user-images.githubusercontent.com/96553992/150611851-ed19e4d5-5ba5-4e92-b02f-e968a0089769.png)


## Election-Audit Summary

Although this script was used for a specific Colorado precinct election, the use of the script built does not just stop there. With some modifications, and a data source containing similar data such as the ballot ID number, the place they are voting from, and the person they voted for, the script can be used. This would be done primarily by changing the name of the variables or creating another list/dictionary in the script to match what the data contains. The following are two examples of how this script could be modified to serve a different purpose and determine election results.

### Example 1 
The first example of how this script could be modified to serve a different purpose would be to determine the winner of an election not held in the same voting platform. Instead of having data for the different city’s voters are from, there could be data from how they voted. Examples of voting platforms being in person, call center, official online forum vote, and so on. There could be another dictionary and list added to hold the information of voting platform. Then by creating or renaming the city variables, the elections results could be populated. This would allow for a similar breakdown of percentage of voting method, the total turnout, the most used voting platform, and the winning candidate of the election. Furthermore, the scripts could help the election commission decide what voting platforms to use going forward and what platforms can be retired. All based on the most popular voting mechanism. It would make the set-up of voting platforms easier, and voters would find that process more to their liking.

### Example 2
Another way this script could be used would be for other elections that the Colorado election commission oversees. Similarly, a condensed CSV file with all the election data would be provided for the script to run properly. The script could even be used for a bigger election such as the election of the governor. Instead of county breakdown, a city breakdown could provide in the csv file. Therefore, would just require changing the name of variable names from county to city and renaming the dictionary and list for county. One top of that, the ballot ID and the candidate they voted for would need to be provided in the data file. This would lead to results of what cities certain candidates won, the voter turnout for each city, percentage of total votes for each candidate, and the winner of the governor election. A city election with more at stake and a greater number of voters would be an optimal scenario for the script to be used.

### Recommendation
The examples mentioned above are just a few ways this python script could be altered so that time and money could be saved due to less resources required to create a whole new script or process. Keeping in mind that modifications and the proper data is required, the possibilities are endless. I strongly recommended leveraging the script to analyze future elections that the Colorado Election Commission conducts.

