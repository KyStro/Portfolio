#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:30:21 2019

@author: Kyle
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''
Gets all games 1966-2018
'''
def get_vegas_data():
    file = "vegas_odds.csv"
    df = pd.read_csv(file, usecols=["schedule_date", "team_home","score_home","score_away","team_away"])
    return df.iloc[:12411,:]


def get_all_teams():
    file = "nfl_teams.csv"
    df = pd.read_csv(file)
    teams = df["team_name"]
    return teams


def make_team_dict(teams):
    dic = {}
    for t in teams:
        if t not in dic:
            dic[t] = [0,0]
    return dic


def update_win_pct(dic, df):
    for i in df.index:
        home = df.iloc[i].team_home
        home_score = df.iloc[i].score_home
        away = df.iloc[i].team_away
        away_score = df.iloc[i].score_away
        win, loss = get_winner_loser(home,home_score,away_score,away)
        if win != None or loss != None:
            dic[win][0] += 1
            dic[win][1] += 1
            dic[loss][1] += 1
    for team in dic:
        dic[team] = dic[team][0]/dic[team][1]
        
        
def remove_old_teams(dic):
    old = ['Phoenix Cardinals','St. Louis Cardinals','Baltimore Colts','San Diego Chargers',
           'St. Louis Rams','Boston Patriots','Los Angeles Raiders','Houston Oilers','Tennessee Oilers']
    for key in old:
        del dic[key]
        

def get_top_10_winning(dic):
    teams = sorted(dic,key=dic.get)
    return teams[-10:]



def make_graph_1(dic, top_10):
    x = np.arange(len(top_10))
    top_10_pct = [dic[t]*100 for t in top_10]

    plt.barh(x, top_10_pct, align='center', alpha=1, tick_label=top_10,
             color=['r','indigo','darkviolet','c','orange','midnightblue','crimson','yellow','silver','deepskyblue'])
    plt.title('Top 10 Most Winningest Teams in the NFL (1966-2018)')
    plt.xlim(0, 100)
    plt.xlabel('Win Percentage (% Out of 100)', labelpad=15)
    plt.show()
    

def get_winner_loser(home,home_score,away_score,away):
    if home_score == away_score:
        return None, None
    elif home_score > away_score:
        return home, away
    return away, home

def main():
    vegas = get_vegas_data()
    teams = get_all_teams()
    team_dict = make_team_dict(teams)
    update_win_pct(team_dict, vegas)
    remove_old_teams(team_dict)
    top_10 = get_top_10_winning(team_dict)
    make_graph_1(team_dict, top_10)
    
main()