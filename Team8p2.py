import random

def c1happy():
    happy = random.normalvariate(10, 8)
    return happy

def c2happy():
    happy = random.normalvariate(15, 6)
    return happy

def c3happy():
    happy = random.normalvariate(12, 5)
    return happy

def exploitOnly():
    happinessList = []
    happinessList.append(c1happy())
    happinessList.append(c2happy())
    happinessList.append(c3happy())

    highNum = happinessList[0]
    for i in happinessList:
        if i > highNum:
            highNum = i

    if highNum == happinessList[0]:
        for i in range(297):
            happinessList.append(c1happy())

    elif highNum == happinessList[1]:
        for i in range(297):
            happinessList.append(c2happy())

    elif highNum == happinessList[2]:
        for i in range(297):
            happinessList.append(c3happy())

    return sum(happinessList)

def exploreOnly():
    happinessList = []

    for i in range(100):
        happinessList.append(c1happy())

    for i in range(100):
        happinessList.append(c2happy())

    for i in range(100):
        happinessList.append(c3happy())

    return sum(happinessList)

def eGreedy():
    happinessList = []
    c1 = []
    c2 = []
    c3 = []
    e = 10

    happinessList.append(c1happy())
    c1.append(c1happy())
    happinessList.append(c2happy())
    c2.append(c2happy())
    happinessList.append(c3happy())
    c3.append(c3happy())

    for i in range(300):
        r = random.random()*100
        if r < e:
            cafe = random.randint(1, 3)

            if cafe == 1:
                happinessList.append(c1happy())
                c1.append(c1happy())

            elif cafe == 2:
                happinessList.append(c2happy())
                c2.append(c2happy())

            elif cafe == 3:
                happinessList.append(c3happy())
                c3.append(c3happy())

        else:
            c1avg = sum(c1) / len(c1)
            c2avg = sum(c2) / len(c2)
            c3avg = sum(c3) / len(c3)

            if c1avg > c2avg and c1avg > c3avg:
                happinessList.append(c1happy())
                c1.append(c1happy())

            elif c2avg > c1avg and c2avg > c3avg:
                happinessList.append(c2happy())
                c2.append(c2happy())

            elif c3avg > c1avg and c3avg > c2avg:
                happinessList.append(c3happy())
                c3.append(c3happy())

    print(sum(happinessList))


def simulation(t, e):
    optimumTotal = c2happy() * t
    exploitOnlyExpectedH = exploitOnly(t)
    exploreOnlyExpectedH = exploreOnly(t)
    eGreedyExpectedH = eGreedy(t, e)
    exploreAverage = exploreOnly(t) / t
    exploitAverage = exploitOnly(t) / t
    eGreedyAverage = eGreedy(t, e) / t
    exploitOnlyRegret = optimumTotal - exploitOnly(t)
    exploreOnlyRegret = optimumTotal - exploreOnly(t)
    eGreedyRegret = optimumTotal - eGreedy(t, e)
    exploitaveregret = exploitOnlyRegret / t
    exploreaveregret = exploreOnlyRegret / t
    eGreedyaveregret = eGreedyRegret / t
    hello = ("optimum total:", optimumTotal, "exploit Only Expected Regret:", exploitOnlyRegret, "explore Only Expected Regret:",
            exploreOnlyRegret, "eGreedy Expected Regret:", eGreedyRegret, "exploitOnly expected Happiness",
            exploitOnlyExpectedH, "exploreOnly Expected Happiness", exploreOnlyExpectedH,
            "eGreedy Expected Happiness:", eGreedyExpectedH, "exploit Only average:", exploreAverage,
             "exploit only average:", exploitAverage, "eGreedy average:", eGreedyAverage, "exploit Only average regret:",
             exploitaveregret, "explore only average regret:", exploreaveregret, "eGreedy average regret:",
             eGreedyaveregret)
    return hello

t = 10000
e = 10
print(simulation(t, e))
