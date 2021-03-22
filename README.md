# An Analysis of the Election Results of a Colorado Precinct

<img src="analysis/Election_Results_Terminal.png" align="center" width="290" height="200" >

## Table of Contents
* [Project Overview PyPoll](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#project_overview_pypoll)
* [Resources](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#resources)
* [Summary](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#summary)
* [Project Overview PyPoll Challenge](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#project_overview_pypoll_challenge)
* [Challenge Resources](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#challenge_resources)
* [Election Audit Results](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#election_audit_results)
* [Election Audit Summary](https://github.com/rkaysen63/Election_Analysis/blob/master/README.md#election_audit_summary)

## Project Overview PyPoll
The Colorado Election Commission has requested assistance with an audit of the tabulated votes for a princinct in Colorado.  They have requested a report of the election results that include, the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and winner based on the popular vote.

This analysis is the precursor to the challenge assignment and was performed while learning the basics of the Python coding language. 

## Resources
Data Source: ![election_results.csv](https://github.com/rkaysen63/Election_Analysis/blob/main/Resources/election_results.csv)<br/>  
Software:  Python 3.8.5<br/>
Lesson Plan:  UTA-VIRT-DATA-PT-02-2021-U-B-TTH, Module 3

## Summary
* The Colorado princinct that was analyzed includes the following counties:
  * Arapahoe
  * Denver
  * Jefferson

* The candidates were:
  * Diana DeGette
  * Raymon Anthony Doane
  * Charles Casper Stockham

* The analysis of the election shows that of the total votes cast:
  * Diana DeGette received 73.8% of the vote (272,892 votes).
  * Raymon Anthony Doane received 3.1% of the vote (11,606 votes).
  * Charles Casper Stockham received 23.0% of the vote (85,213 votes).
 
* The winner of the election was:
  * Diana DeGette, who received 73.8% of the popular vote and 272,892 number of votes.

## Project Overview PyPoll Challenge
The Colorado Election Commission has requested assistance with an audit of the tabulated votes for a princinct in Colorado.  They have requested a report of the election results that include, the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and winner based on the popular vote. In addition, they have also requested the voter turnout for each county, the percentage of votes from each county out of the total count, and to identify the county with the highest turnout.

## Challenge Resources
Data Source: ![election_results.csv](https://github.com/rkaysen63/Election_Analysis/blob/main/Resources/election_results.csv)
Software:  Python 3.8.5
Lesson Plan:  UTA-VIRT-DATA-PT-02-2021-U-B-TTH, Module 3 Challenge and starter code file PyPoll_Challenge_starter_code.py

## Election Audit Results:
The Colorado princinct that was analyzed includes the following counties:
* Arapahoe
* Denver
* Jefferson

* The candidates were:
  * Diana DeGette
  * Raymon Anthony Doane
  * Charles Casper Stockham

* Total number of votes cast: 369,711

* The analysis of the election shows that of the total votes cast:
  * Diana DeGette received 73.8% of the vote (272,892 votes).
  * Raymon Anthony Doane received 3.1% of the vote (11,606 votes).
  * Charles Casper Stockham received 23.0% of the vote (85,213 votes).

* The winner of the election was:
  * Diana DeGette, who received 73.8% of the popular vote (272,892 votes).

* The results show that of the three counties in the precinct, Denver County had the largest turnout with 272,892 voters.

* The voter turnout by county is as follows:
  * Arapahoe County had 24,801 voters turn out to vote, equating to 6.7% of the precinct's total number of voters.
  * Denver County had 306,055 voters turned out to vote, equating  to 82.8% of the precinct's total number of voters.
  * Jefferson County had 38,855 voters turn out to vote, equating  to 10.5% of the precinct's total number of voters.

The results were written to a text file, ![election_results.txt](https://github.com/rkaysen63/Election_Analysis/blob/main/analysis/election_results.txt), and printed in the terminal, ![analysis/Election_Results_Terminal.png](https://github.com/rkaysen63/Election_Analysis/blob/main/analysis/analysis/Election_Results_Terminal.png)

## Election Audit Summary:

The results were gathered from the election_data.csv using a program written in Python.  This program may be used to analyze election data from other precincts or districts with very little modification because the code is fairly generic.  The exceptions are the path to retrieve the data and the path to store the output text file.

In order to use the script for other precincts:
1. Update the `file_to_load =` path in order to retrieve a new data file.
   * Per line 9 of PyPoll_Challenge_RK.py code:
   * The current file path to retrieve the data is: `file_to_load = os.path.join("Resources", "election_results.csv")`
   * Change the path ("Resources", "election_results.csv") to reflect the actual location of the new code.  This may be done in two ways: either replace the path and file name within the parentheses, or replace the code `os.path.join` with the direct path.  
   * To illustrate, please consider the following example file, folder and folder location relative to the program:
     * File name: district1_election_results.csv
     * Folder name:  all_districts
     * Location of folder "all_districts" is up a level in the folder structure from the PyPoll_Challenge_RK.py program.
   * File Path Example 1, uses `os.path.join`, but replaces the particulars of the path within the parentheses:
     * `file_to_load = os.path.join("..", "all_districts", "district1_election_results.csv")`
     * The new path indicates to the program to go up a level in the folder structure, select the "all_districts" folder and select "district1_election_results.csv" file from that folder.
   * File Path Example 2, uses the direct path method.
     * On line 9 of the code, delete everything after `file_to_load =`
     * Then, navigate to the desired file in Windows File Explorer.
     * Then, click once on the file.
     * While the file is selected/highlighted, press the shift key and right click on the file for the drop-down menu.  From the drop-down menu select "copy as path".
     * Paste the path after the equal sign on line 9 of the code.  It should look something like this: `file_to_load = "C:\Users\<user_name>\Documents\all_districts\district1_election_results.csv"`.
     * Then add a second forward slash to each forward slash so that it looks like this: `file_to_load = "C:\\<user_name>\\Documents\\all_districts\\district1_election_results.csv"`.
2. Change the `file_to_save =`path in order to save the new results in the desired folder and create a new text file with a descriptive name to prevent saving over the existing text file.  
   * Per line 11 of the PyPoll_Challenge_RK.py code:
   * The current file path to save the text file with the results is: `file_to_save = os.path.join("analysis", "election_results.txt")` 
   * Similarly, using the procedure described in the examples 1.1 and 1.2 above, change the name of the new text file (and the folder and folder location as well).
   * For example, for district1_election_results.csv data, perhaps the file path might be:
   * `file_to_save = os.path.join("analysis", "district1_results.txt")` 
   * The new file "district1_results.txt" would be created when the code is executed and placed in the "analysis" folder, which in this case is located in the same folder with the PyPoll_Challenge_RK.py program.



