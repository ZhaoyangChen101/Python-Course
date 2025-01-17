# Create a program that allows a user to choose one of
# up to 9 times zones from a menu. You can choose any zones
# you want from the all_timezones list.

# The program will then display the time in that timezone, as
# well as local time and UTC time.

# Entering 0 as the choice will quit the program.

# Display the dates and times in a format suitable for the use
# of your program to understand, and include the timezone name
# when displaying the chosen time.

import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Japan",
                   '6': "Pacific/Tahiti",
                   '7': "Europe/London",
                   '8': "US/Hawaii",
                   '9': "Zulu",
                   }
#
# print("Please choose a time zone (or 0 to quit): ")
# for place in sorted(available_zones):
#     print("\t{}. {}".format(place, available_zones[place]))

choice = "-"
while choice != '0':
    # choice = input()

    # if choice == '0':
    #     break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime("%A %x %X %z"), world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime("%A %x %X")))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
        print()

    print("Please choose a time zone (or 0 to quit): ")
    for place in sorted(available_zones):
        print("\t{}. {}".format(place, available_zones[place]))
    choice = input()

else:
    print("You have quit!")
