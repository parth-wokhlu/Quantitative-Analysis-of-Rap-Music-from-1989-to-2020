# Initializes the months that have each different length (either 28, 30, 31) in MM format
monthsWith30 = ["04", "09", "11", "06"]
monthsWith31 = ["01", "03", "05", "07", "08", "10", "12"]
monthsWith28 = ["02"]


class DateControl:

    def __init__(self):
        self.year = "1989"
        self.month = "01"
        self.day = "01"

    # Returns the date in a format that the billboard.py api can understand
    def getDate(self):
        return self.year + "-" + self.month + "-" + self.day

    # Advances the date one week ahead, adjusting the year, month, and day variables as necessary
    def nextWeek(self):
        dayInt = int(self.day)
        dayInt += 7
        self.day = self.convertToString(dayInt)
        if self.month in monthsWith31:
            if dayInt > 31:
                temp = int(self.month)
                temp += 1
                self.month = self.convertToString(temp)
                self.day = self.convertToString(dayInt - 31)

        elif self.month in monthsWith30:
            if dayInt > 30:
                temp = int(self.month)
                temp += 1
                self.month = self.convertToString(temp)
                self.day = self.convertToString(dayInt - 30)

        elif self.month in monthsWith28:
            if dayInt > 28:
                temp = int(self.month)
                temp += 1
                self.month = self.convertToString(temp)
                self.day = self.convertToString(dayInt - 28)

        if self.month == "13":
            self.month = "01"
            temp = int(self.year)
            temp += 1
            self.year = str(temp)

    # Converts a day or month in integer format to a DD or MM format
    def convertToString(self, month):
        if month < 10:
            return "0" + str(month)
        else:
            return str(month)
