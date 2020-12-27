import billboard
from DateControl import DateControl
import json

# Initialize the current year and current songs variables
# create the date object to handle changing the dates
date = DateControl()
currentYear = date.year
currentSongs = {}

# Parent while loop, runs until it the date becomes 12-24-2020
while date.year != "2020" or date.month != "12" or date.day != "24":

    # Get the chart for the week it is on and adds all songs and artists to the current songs dictionary
    # It skips repeats to ensure each song is only on the list once
    currentChart = billboard.ChartData('rap-song', date.getDate())
    for song in currentChart:
        if song not in currentSongs:
            currentSongs.update({song.title : song.artist})

    # Advances the date object one week
    date.nextWeek()

    # Checks to see if the date is 12-24-2020 or a the date object has advanced one year
    # If so, it updates the rapData.json file with all the data for the year which is in the currentSongs dictionary
    # It then reinitializes currentSongs and and currentYear
    if date.year == "2020" and date.month == "12" and date.day == "24"or date.year != currentYear:
        with open('rapData.json', 'r') as openfile:
            data = json.load(openfile)

        data.update({str(currentYear) : currentSongs})
        json_object = json.dumps(data, indent=4)

        with open("rapData.json", "w") as outfile:
            outfile.write(json_object)
        currentYear = date.year
        currentSongs = {}

    print(date.getDate())
