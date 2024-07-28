def calculateDay(missions, limit):
    dayMissions = []
    necessaryDay = 1
    for _, item in enumerate(missions):
        if (isDayMissionValid(dayMissions, item, limit)):
            dayMissions.append(item)
        else:
            necessaryDay += 1
            dayMissions = [item]
    return necessaryDay

def isDayMissionValid(passedMissions, mission, limit):
    temp = list(passedMissions)
    temp.append(mission)
    if len(temp) <= 1:
        return True
    temp.sort()
    return temp[-1] - temp[0] <= limit

input = [1,12,10,4,5,2]
print(calculateDay(input, 2))