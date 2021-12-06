'''---------------------------------------------
CSC535-FA2021
Data Mining
Final Group Project

Maria's deliverables: 
The top 6 best performing players per position based on game statistics 
Positions: Pitcher, Catcher, 1B, 2B, 3B, Short stop, Right fielder, Left fielder, Center fielder and Designated Hitter

Column names in the "full_roster.csv" file
Name,Age,Country,B,T,Ht,Wt,DoB,Yrs,G,GS,Batting,Defense,P,C,1B,2B,3B,SS,LF,CF,RF,OF,DH,PH,PR,WAR,Status

Column names in the "team_batting.csv" file
Rank,Position,Name,Age,Games,PA,AB,Runs,Hits,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB
------------------------------------------------'''

import pandas as pd
import numpy as np

def get_data(fileName):
    df = pd.read_csv(fileName)
    return df

#preprocessing the full_roster.csv file
def preprocess_roster(df):
    roster = df.drop(['Country', 'Ht', 'Wt', 'DoB', 'Yrs', 'WAR', 'Status'], axis=1)
    print(roster)
    return roster


#preprocessing the team_batting.csv file
def preprocess_batting(df):
    # batting = df.drop(['Country', 'Ht', 'Wt', 'DoB', 'Yrs', 'WAR', 'Status'], axis=1)
    ranks = pd.DataFrame(df.iloc[:, 0:4])
    data = pd.DataFrame(df.iloc[:, 2:])

    return 0

def main():

    batting_file = "team_batting.csv"
    roster_file = "full_roster.csv"

    batting_df = get_data(batting_file)
    roster_df = get_data(roster_file)
    
    preprocess_roster(roster_df)
    preprocess_batting(batting_df)

main()