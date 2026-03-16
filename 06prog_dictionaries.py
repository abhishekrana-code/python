# dictionaries are mutable
# dictionaries are created by using curly braces {} or by using the dict() function

monthConversions = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "april",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

print(monthConversions["mar"])
print(monthConversions.get("mar"))
