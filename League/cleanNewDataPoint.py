def main():
    inFile = open('newDataPoint.csv', 'r')
    outFileX = open('newDataPoint_X.csv', 'w')
    outFileY = open('newDataPoint_Y.csv', 'w')
    
    
    for line in inFile:
        tokens = line.split(',')
        teamID = tokens[8].strip()
        teamID = int(teamID)
        if teamID == 100 or teamID == 200:              # Makes sure its pulling from team statistics not player statistics
            result = tokens[20].strip()                 # Win or Loss
            firstBlood = tokens[30].strip()             # Whether the team got First blood
            firstDrag = tokens[37].strip()              # First dragon of the game
            teamDrags = tokens[39].strip()              # Number of dragons taken by the team
            oppDrags = tokens[40].strip()               # Number of dragons taken by the enemy team
            herald = tokens[49].strip()                 # Whether the team got the Rift Herald
            firstTower = tokens[51].strip()             # Whether the team got the first tower
            firstToThreeTowers = tokens[54].strip()     # Whether the team was the first to 3 towers
            firstBaron = tokens[57].strip()             # Whether the team got the first baron
            teamBarons = tokens[59].strip()             # Number of barons taken by the team
            oppBarons = tokens[60].strip()              # Number of barons taken by the enemy
            damageToChamps = tokens[61].strip()         # Damage done to champions by the team
            dpm = tokens[62].strip()                    # Damage to champions by the team per minute
            wpm = tokens[66].strip()                    # Number of wards put down by the team per minute
            wcpm = tokens[69].strip()                   # Number of wards cleared by the team per minute
            gpm = tokens[75].strip()                    # Gold earned by the team per minute
            gd10 = tokens[85].strip()                   # Gold difference at 10 minutes
            gd15 = tokens[88].strip()                   # Gold difference at 15 minutes
            cspm = tokens[82].strip()                   # Creep Score by the team per minute
            csd15 = tokens[97].strip()                  # Creep Score difference at 15 minutes
            if firstBlood != "" and firstDrag !="" and teamDrags !="" and oppDrags !="" and herald !="" and firstTower !="" and firstToThreeTowers !="" and firstBaron != "" and teamBarons != "" and oppBarons != "" and damageToChamps !="" and dpm !=""  and wpm !="" and wcpm !="" and gpm !=""and gd10 !="" and gd15 !="" and cspm !="" and csd15 !="":
                outFileX.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(firstBlood, firstDrag, teamDrags, oppDrags, herald, firstTower, firstToThreeTowers, firstBaron, teamBarons, oppBarons, damageToChamps, dpm, wpm, wcpm, gpm, gd10, gd15, cspm, csd15))
                outFileY.write('{}\n'.format(result))
        
    outFileX.close()
    outFileY.close()

main()