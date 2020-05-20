'''
File: bball.py
    Author: Kyle Strokes
    Purpose: Computes what conference has the highest winning %.
'''



'''In main a ConferenceSet object is called and for each line in the text
    file a Team object is made then adds the teams to a list then appends
    the list to a dictonary with the key being it's conference and the
    value being the team list and prints the best win ratio of all
    conferences.

    Parameters: None

    Returns: None

    Pre-conditions: file must be a readable file

    Post-conditions: conf_set must be an object of ConferenceSet class
                    and new_team must be object of the Team class'''
def main():
    file = open(input())
    conf_set = ConferenceSet()
    for line in file:
        new_team = Team(line)
        '''appending new_team to team list'''
        conf_set.add(new_team)
        '''setting team list as conference dict value'''
        conf_set.add(new_team.conf())
    if len(conf_set) > 0:
        #Invariant: the len of conf_set is greater than 0
        print(conf_set.best())
       


'''This is a Team class which splits the info about a certain
    team within a line
    
Parameters: a line of output from the file

Returns: name of the team, conference, win ratio and output
            statement

Pre-conditions: line must be a list of characters from the file with
                last two elements are ints

Post-conditions: The class splits the line into different functions
                 that return the required parts'''
class Team:
    def __init__(self, line):
        line = line.split()
        for i in range(len(line)-1,-1,-1):
            '''To get the last parentheses in the line
                which is the conference'''
            if line[i].endswith(')'):
                conf_e = i+1
            if line[i].startswith('('):
                conf_i = i
                conf = line[conf_i:conf_e]
                conf = ' '.join(conf)
                '''cuts off parentheses'''
                self._conf = conf[1:-1]
                name = line[:conf_i]
                self._name = ' '.join(name)
                break
            win = int(line[-2])
            lose = int(line[-1])
            self._win_ratio = win / (win + lose)
            
    def name(self):
        return self._name

    def conf(self):
        return self._conf

    def win_ratio(self):
        return self._win_ratio

    def __str__(self):
        return "{} : {}".format(self._name, self._win_ratio)



'''This is a Conference class that extracts information about
    a certain conference from the teams.conf

    Parameters: A team's conference

    Returns: conference's name, win average and also if its
            team is in teamlist

    Pre-conditons: conf is the team's conf

    Post-conditions: win ratio is the conferences average win
                    win ratio and name is it's name'''
class Conference:
    def __init__(self, conf):
        self._conf = conf
        self._team_list = []
        
    def __contains__(self, team):
        return team in self._team_list

    def name(self):
        return self._conf

    def add(self, team):
        self._team_list.append(team)

    def win_ratio_avg(self):
        avg = 0
        '''takes the teams win ratio from its conference and
            returns the avgerage win ratio'''
        for team in self.team_list:
            avg += self._team.win_ratio()
        return avg / len(self.team_list) 

    def __str__(self):
        return "{} : {}".format(self._conf, self._win_ratio_str)


'''ConferenceSet is a class that adds the team list to a dictonary
    value with the key being the conference for those teams

    Parameters: None

    Returns: Supposed the return the best win ratio of all conferences

    Pre-conditions: team has to be a list, conf_set is a dictonary

    Post-conditons: best is a list of conferences with best
                    win ratio'''

class ConferenceSet:
    def __init__(self):
        self._conf_set = {}

    def add(self, team):
        if not team.conf() in self._conf_set:
            self._conf_set[team.conf()] = []
            #invariant: len(conf_set[team.conf()]) == 0
            self._conf_set[team.conf()].append(team)
        else:
            self._conf_set[team.conf()].append(team)

                
    def best(self):
        for conf in self._conf_set:
            pass 


        

main()
