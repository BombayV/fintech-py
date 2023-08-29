birthstones = {
    "january": "Garnet",
    "february": "Amethyst",
    "march": "Bloodstone",
    "april": "Sapphire",
    "may": "Agate",
    "june": "Emerald",
    "july": "Onyx",
    "august": "Carnelian",
    "september": "Peridot",
    "october": "Beryl",
    "november": "Topaz",
    "december": "Ruby"
}


def get_birthstone(month):
    # Check if the month is only numbers
    if month.isdigit():
        if int(month) < 1 or int(month) > 12:
            return False
        return list(birthstones.values())[int(month) - 1]

    if month.lower().strip(' \t\n\r') not in birthstones:
        return False
    return birthstones[month.lower().strip(' \t\n\r')]
