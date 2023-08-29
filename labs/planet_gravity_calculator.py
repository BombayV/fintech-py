import math

PLANET_GRAVITIES = {
    "mercury": 3.7,
    "venus": 8.87,
    "earth": 9.8,
    "mars": 3.711,
    "jupiter": 24.79,
    "saturn": 10.44,
    "uranus": 8.69,
    "neptune": 11.15
}

COLORS = {
    "PURPLE": '\033[95m',
    "NORMAL": '\033[0m',
    "WARNING": '\033[93m',
    "SUCCESS": '\033[92m'
}


def time_calculator(gravity, height):
    return round(math.sqrt((2 * height) / gravity), 2)


def distance_calculator(speed, time):
    return round((speed * time), 2)


def angle_distance_calculator(speed, time, angle):
    return round((speed * time) * math.cos(angle * (math.pi / 180)), 2)


print(
    f"{COLORS['PURPLE']}Welcome to the Planet Gravity Calculator {COLORS['NORMAL']}\n"
)

userPlanet = ""
userHeight = 0
userSpeed = 0
userAngle = 0
userContinue = None

while True:
    if userContinue == "both" or userContinue == "planet" or not userContinue:
        userPlanet = input("Enter the planet you're on: ").lower()
        while userPlanet not in PLANET_GRAVITIES:
            userPlanet = input(
                f"{COLORS['WARNING']}Planet not found. {COLORS['NORMAL']}Enter a real planet: "
            ).lower()
        userPlanet = PLANET_GRAVITIES[userPlanet]

    if userContinue == "both" or userContinue == "data" or not userContinue:
        userHeight = input(
            "Enter the current distance from the surface of the planet (m): "
        )

        while not userHeight.isnumeric():
            userHeight = input(
                f"{COLORS['WARNING']}Invalid height. {COLORS['NORMAL']}Enter a proper number: "
            ).lower()

        userSpeed = input("Enter horizontal speed (m/s): ")
        while not userSpeed.isnumeric():
            userSpeed = input(
                f"{COLORS['WARNING']}Invalid speed. {COLORS['NORMAL']}Enter a proper number: "
            ).lower()

        userAngle = input("Enter launch angle (degrees): ")
        while not userAngle.isnumeric():
            userAngle = input(
                f"{COLORS['WARNING']}Invalid angle. {COLORS['NORMAL']}Enter a proper angle number: "
            ).lower()

    time = time_calculator(userPlanet, float(userHeight))
    distance = distance_calculator(float(userSpeed), time)
    angleDistance = angle_distance_calculator(float(userSpeed), time, float(userAngle))

    print(f"\nYour time is {COLORS['SUCCESS']}{time}s{COLORS['NORMAL']}")
    print(f"Your distance is {COLORS['SUCCESS']}{distance}m/s{COLORS['NORMAL']}")
    print(
        f"Your distance at {COLORS['PURPLE']}{userAngle} deg{COLORS['NORMAL']} is {COLORS['SUCCESS']}{angleDistance}m{COLORS['NORMAL']}"
    )

    userContinue = input(f"{COLORS['WARNING']}Would you like to change the planet, data, both, or quit?\n{COLORS['NORMAL']}")
    if userContinue == "quit":
        break