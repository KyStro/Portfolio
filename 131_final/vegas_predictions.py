#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:44:50 2019

@author: Kyle
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_winner_loser(home,home_score,away_score,away):
    if home_score == away_score:
        return None, None
    elif home_score > away_score:
        return home, away
    return away, home

    
def get_vegas_data2():
    file = "vegas_odds.csv"
    df = pd.read_csv(file, usecols=["team_home","score_home","score_away","team_away", "team_favorite_id"])
    return df.iloc[:12411,:]

def get_vegas_actual(df):
    correct = 0
    wrong = 0
    tot = 0
    code_teams = map_code_to_teams()
    for row in df.index:
        win, loss = get_winner_loser(df.iloc[row,0],df.iloc[row,1],df.iloc[row,2],
                               df.iloc[row,3])
        if win == None or pd.isna(df.iloc[row,4]):
            continue
        winner_id = code_match(code_teams, win)
        if teams_match(winner_id, df.iloc[row,4]):
            correct += 1
        else:
            wrong += 1
        tot += 1
    return correct/tot * 100, wrong/tot * 100
    
    
def make_graph_2(c, w):
    y = [c,w]
    x = np.arange(len(y))
    plt.ylim(0, 100)
    plt.bar(x, y, align='center', alpha=1, width=0.7, tick_label=['Correct','Incorrect'],
            color=['green','red'])
    plt.xlabel('Prediction Outcome')
    plt.ylabel('Frequency (%)')
    plt.title('Vegas Favorite Prediction Outcomes for NFL Games (1979-2018)', pad=15)
    plt.show()

def map_code_to_teams():
    file = "nfl_teams.csv"
    df = pd.read_csv(file, usecols=[0,2])
    d = {}
    for row in df.index:
        code = df.iloc[row,1]
        team = df.iloc[row,0]
        if code not in d:
            d[code] = []
            d[code].append(team)
        else:
            d[code].append(team)
    return d

def code_match(dic, team):
    for key in dic.keys():
        for teams in dic[key]:
            if team in teams:
                return key
            
def teams_match(t,s):
    return t == s

def main():
    vegas2 = get_vegas_data2()
    correct, wrong = get_vegas_actual(vegas2)
    make_graph_2(correct,wrong)
    
main()