#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""
Created on Mon Dec  2 19:22:02 2019

@author: Kyle
"""

def get_years_points():
    file = "vegas_odds.csv"
    df = pd.read_csv(file, usecols=["schedule_season","score_home","score_away"])
    return df.iloc[:12411,:]
    

def get_xy_years_pts(df):
    years = [n for n in range(1966,2019)]
    pts = []
    for year in years:
        mini_df = df.loc[df['schedule_season'] == year]
        total = mini_df.sum(skipna=True)['score_away'] + mini_df.sum(skipna=True)['score_home']
        pts.append(total/len(mini_df))
    return years, pts

def scatterplot(x, y):
    plt.scatter(x,y, marker='x', color='darkblue')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='crimson')
    plt.xlabel('Year', labelpad=15)
    plt.ylabel('Average Total Points Per Game', labelpad=15)
    plt.title('Average Total Points For a NFL Game vs. Year', pad=15)

def main():
    years_pts = get_years_points()
    x, y = get_xy_years_pts(years_pts)
    scatterplot(x, y)
    
main()
