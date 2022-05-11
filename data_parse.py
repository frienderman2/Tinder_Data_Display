# Callaghan Donnelly
# Quick n dirty json parser for Tinder data, there are a ton of optimizations that can be made,
# but they're not necessary for the scope of this project
# uses a tinker / Graphics main page that runs in the background and can launch each different needed graph or open pictures


# PUT THE FULL PATH TO YOUR data.json FILE HERE
fullPath = 'data.json'


import json
from json import *
# have to install numpy bc matplotlib uses numpy arrays for shaped lists (fml)
import numpy as np
import graphics
from graphics import *
import matplotlib.pyplot as myWindow
# set the default window size to something larger
myWindow.rcParams['figure.figsize'] = [12.0, 8.0]


# return all keys from a given dictionary
def getKeys(dict):
    return [*dict]


# test function to practice matplotlib
def plotTest():
    xDat = [1, 2, 3]
    yDat = [4, 2, 1]
    myWindow.plot(xDat, yDat)
    myWindow.xlabel('X Axis')
    myWindow.ylabel('Y Axis')
    myWindow.title('Title')
    myWindow.show()


def plotData(accList, useDict, useCatagory, useNum):
    yDat = []
    dateList = accList[useNum]
    # for each date in the list of opens, grab the value from the dictionary for that date
    for num in dateList:
        try:
            yDat.append(useDict[useCatagory][num])

        except KeyError as e:
            print(num)

    xDat = np.arange(len(yDat))
    myWindow.plot(xDat, yDat)
    # TODO: Variablize the axis labels and title based on what was passed in for useNum
    if (useNum == 0):
        myWindow.xlabel('Date')
        myWindow.ylabel('Opens')
        myWindow.title('Number of times app was opened per day')

    elif (useNum == 1):
        myWindow.xlabel('Date')
        myWindow.ylabel('Likes Sent')
        myWindow.title('Number of likes sent per day')

    elif (useNum == 2):
        myWindow.xlabel('Date')
        myWindow.ylabel('Dislikes')
        myWindow.title('Number of dislikes sent per day')

    elif (useNum == 3):
        myWindow.xlabel('Date')
        myWindow.ylabel('Superlikes')
        myWindow.title('Number of Superlikes sent per day')

    elif (useNum == 4):
        myWindow.xlabel('Date')
        myWindow.ylabel('Matches')
        myWindow.title('Number of matches per day')

    elif (useNum == 5):
        myWindow.xlabel('Date')
        myWindow.ylabel('Messages Sent')
        myWindow.title('Number of messages sent per day')

    elif (useNum == 6):
        myWindow.xlabel('Date')
        myWindow.ylabel('Messages received')
        myWindow.title('Number of messages received per day')

    else:
        myWindow.xlabel('Date')
        myWindow.ylabel('??')
        myWindow.title('??')

    # turn the x axis labels so they're readable
    # TODO: change the xDat to actual dates instead of the stupid number dash thing
    myWindow.xticks(xDat, accList[useNum], rotation=90)
    myWindow.show()


def readData():
    dataStore = {}
    with open(fullPath, 'r+') as jfile:
        dataStore = json.loads(jfile.read())

    return dataStore


# take in the dictionary, and the desired sub category and returns the subList and the accumulator list
def parseCat(dataDict, subCatName):
    subList = []
    if subCatName == 'act':
        # each sub-category that makes up the Usage category
        subList = ['app_opens', 'swipes_likes', 'swipes_passes', 'superlikes', 'matches', 'messages_sent', 'messages_received', 'advertising_id', 'idfa']
        useData = myDataDict['Usage']

    elif subCatName == 'user':
        # each sub-category that makes up the User category
        subList = ['active_time', 'age_filter_max', 'age_filter_min', 'bio', 'birth_date', 'city', 'coords', 'create_date', 'email', 'full_name', 'gender', 'gender_filter', 'interested_in', 'ip_address', 'name', 'pos', 'client_registration_info', 'phone_id', 'user_interests']
        useData = myDataDict['User']

    else:
        subList = []
        useData = {}

    # for each sub-category to usage, get the keys (dates) and add those dates to an accumulator list
    accumulatorList = []
    for category in subList:
        keyList = getKeys(useData[category])
        accumulatorList.append(keyList)

    return(subList, accumulatorList)


def drawButtons(win):
    # thing = Rectangle(xPnt, yPnt)
    btnExit = Rectangle(Point(770, 510), Point(850, 560))
    btnExit.setFill('black')
    lblExit = Text(Point(810, 535), 'Exit')
    lblExit.setTextColor('red')
    lblExit.setSize(26)
    btnExit.draw(win)
    lblExit.draw(win)

    btnGraphUser = Rectangle(Point(100, 110), Point(240, 160))
    btnGraphUser.setFill('grey')
    lblGraphUser = Text(Point(170, 135), 'Daily Use Data')
    lblGraphUser.setSize(20)
    btnGraphUser.draw(win)
    lblGraphUser.draw(win)

    btnGraphLikes = Rectangle(Point(100, 210), Point(240, 260))
    btnGraphLikes.setFill('grey')
    lblGraphLikes = Text(Point(170, 235), 'Daily Likes Sent')
    lblGraphLikes.setSize(18)
    btnGraphLikes.draw(win)
    lblGraphLikes.draw(win)

    btnGraphDislikes = Rectangle(Point(100, 310), Point(240, 360))
    btnGraphDislikes.setFill('grey')
    lblGraphDislikes = Text(Point(170, 335), 'Daily Dislikes Sent')
    lblGraphDislikes.setSize(16)
    btnGraphDislikes.draw(win)
    lblGraphDislikes.draw(win)

    btnGraphSuplikes = Rectangle(Point(100, 410), Point(240, 460))
    btnGraphSuplikes.setFill('grey')
    lblGraphSuplikes = Text(Point(170, 435), 'Daily Superlikes Sent')
    lblGraphSuplikes.setSize(15)
    btnGraphSuplikes.draw(win)
    lblGraphSuplikes.draw(win)

    btnGraphMatches = Rectangle(Point(300, 110), Point(440, 160))
    btnGraphMatches.setFill('grey')
    lblGraphMatches = Text(Point(370, 135), 'Daily Matches')
    lblGraphMatches.setSize(15)
    btnGraphMatches.draw(win)
    lblGraphMatches.draw(win)

    btnShowMessages = Rectangle(Point(300, 210), Point(440, 260))
    btnShowMessages.setFill('grey')
    lblShowMessages = Text(Point(370, 235), 'Show Messages')
    lblShowMessages.setSize(18)
    btnShowMessages.draw(win)
    lblShowMessages.draw(win)

    # basics of drawing a picture
    # assuming the image is 200 x 200
    # centerPoint = Point(100, 100)
    # imStr = '0.jpeg'
    # imHold = Image(centerPoint, imStr)
    # imHold.draw(win)

def parseAge(date):
    splitHalf = date.split('T')
    numSplit = splitHalf[0].split('-')
    year = numSplit[0]
    month = numSplit[1]
    day = numSplit[2]
    # TODO: Not all alignments will be perfect, as I only designed it my my information originally
    # fix the months for readability
    if month == '01':
        month = 'January'

    elif month == '02':
        month = 'February'

    elif month == '03':
        month = 'March'

    elif month == '04':
        month = 'April'

    elif month == '05':
        month = 'May'

    elif month == '06':
        month = 'June'

    elif month == '07':
        month = 'July'

    elif month == '08':
        month = 'August'

    elif month == '09':
        month = 'September'

    elif month == '10':
        month = 'October'

    elif month == '11':
        month = 'November'

    elif month == '12':
        month = 'December'

    # now fix the days
    # yes I know there is a cool string manipulation way to do this so it only takes like 3 conditionals,
    # but once again this was originally made for my data only, so that was one particular date,
    # and I don't feel like putting that kind of effort in now bc im hungry
    if day == '1':
        day = '1st'

    elif day == '2':
        day = '2nd'

    elif day == '3':
        day = '3rd'

    elif day == '21':
        day = '21st'

    elif day == '22':
        day = '22nd'

    elif day == '23':
        day = '23rd'

    elif day == '31':
        day = '31st'

    else:
        day = day + 'th'

    setStr = f'{month} {day} {year}'
    return setStr


def printUserData(win, userDict):
    lblNamePrompt = Text(Point(580, 135), 'Name: ')
    lblNamePrompt.setSize(22)
    lblNamePrompt.draw(win)
    name = userDict['name']
    lblNameText = Text(Point(650, 136), name)
    lblNameText.setSize(20)
    lblNameText.draw(win)

    lblAgePrompt = Text(Point(570, 175), 'Age: ')
    lblAgePrompt.setSize(22)
    lblAgePrompt.draw(win)
    age = userDict['birth_date']
    bDay = parseAge(age)
    lblAgeText = Text(Point(730, 176), bDay)
    lblAgeText.setSize(20)
    lblAgeText.draw(win)

    lblPhonePrompt = Text(Point(623, 215), 'Phone Number: ')
    lblPhonePrompt.setSize(22)
    lblPhonePrompt.draw(win)
    number = userDict['phone_id']
    # remove a phone number for privacy
    # number = number.replace('0', "*")
    lblPhoneText = Text(Point(770, 216), number)
    lblPhoneText.setSize(20)
    lblPhoneText.draw(win)

    lblAgePrompt = Text(Point(560, 255), 'IP: ')
    lblAgePrompt.setSize(22)
    lblAgePrompt.draw(win)
    ip = userDict['ip_address']
    reg = userDict['client_registration_info']
    plat = reg['platform']
    plat = plat.upper()
    stackStr = f'{ip} (on {plat})'
    lblAgeText = Text(Point(700, 255), stackStr)
    lblAgeText.setSize(20)
    lblAgeText.draw(win)

    lblLocPrompt = Text(Point(540, 300), 'Last Known Location: ')
    lblLocPrompt.setSize(22)
    lblLocPrompt.draw(win)
    pos = userDict['pos']
    posTime = pos['at']
    posLat = pos['lat']
    posLong = pos['lon']
    fullStr = f'Lat = {posLat}, Long = {posLong}'
    lblLocText = Text(Point(770, 300), fullStr)
    lblLocText.setSize(20)
    lblLocText.draw(win)
    timStr = f'on {posTime}'
    lblTimText = Text(Point(740, 325), timStr)
    lblTimText.setSize(20)
    lblTimText.draw(win)


if __name__ == '__main__':
    win = GraphWin('DATA-ing Apps', 900, 600)
    drawButtons(win)
    myDataDict = readData()

    # parse both Tuples now so they don't have to be repeatedly parsed on each button press
    # give act (short for activity) for the Usage OR give user for the user data
    activityTuple = parseCat(myDataDict, 'act')
    subListActivity = activityTuple[0]
    accListActivity = activityTuple[1]

    # TODO: fix whatever is broken in this
    #userTuple = parseCat(myDataDict, 'user')
    #subListUser = userTuple[0]
    #accListUser = userTuple[1]

    # each top level category that composes the dict
    # indexList = ['Messages', 'Purchases', 'Usage', 'User', 'Photos']
    activityData = myDataDict['Usage']
    userData = myDataDict['User']

    printUserData(win, userData)

    clickExit = False
    while not clickExit:
        click = win.checkMouse()
        if click is not None:
            xCord = click.getX()
            yCord = click.getY()

            # if the user clicks the exit button
            if (770 <= xCord <= 850):
                if (510 <= yCord <= 560):
                    clickExit = True
                    break

            if (100 <= xCord <= 240):
                if (110 <= yCord <= 160):
                    # when the graph daily opens is clicked
                    plotData(accListActivity, activityData, subListActivity[0], 0)

                elif (210 <= yCord <= 260):
                    # when the graph likes sent button is clicked
                    plotData(accListActivity, activityData, subListActivity[1], 1)

                elif (310 <= yCord <= 360):
                    # when the graph dislikes sent button is clicked
                    plotData(accListActivity, activityData, subListActivity[2], 2)

                elif (410 <= yCord <= 460):
                    # when the graph superlikes sent button is clicked
                    plotData(accListActivity, activityData, subListActivity[3], 3)

            elif(300 <= xCord <= 440):
                if (110 <= yCord <= 160):
                    # when the graph matches is clicked
                    plotData(accListActivity, activityData, subListActivity[4], 4)

                if (210 <= yCord <= 260):
                    # when show messages is clicked
                    smallWin = GraphWin("Every Message Ever Sent", 400, 400)
                    lblGraphMatches = Text(Point(200, 200), 'LOL, not showing these, but they\'re in the data.')
                    lblGraphMatches.setSize(18)
                    lblGraphMatches.draw(smallWin)
