'''# return human readable duration (4 kyu).py

Your task in order to complete this Kata is to write a function which formats a duration, 
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. 
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


'''

######################################################### MY
import math

def format_duration(seconds=0):
    result = []
    years = math.floor(seconds / 31536000)
    days =  math.floor((seconds-(years*31536000)) / 86400)
    hours =  math.floor((seconds-(years*31536000)-(days*86400)) / 3600)
    minutes =  math.floor((seconds-(years*31536000)-(days*86400)-(hours*3600)) / 60)
    sex = math.floor((seconds-(years*31536000)-(days*86400)-(hours*3600)-(minutes*60)))

    def get_suffix(the_digit):
        return "s" if the_digit != 1 else ""

    if seconds <= 0:
        return "now"

    if years > 0:
        years = f"{years} year{get_suffix(years)}"
        result.append(years)

    if days > 0 and len(result) >= 1:
        days = f", {days} day{get_suffix(days)}"
        result.append(days)
    elif days > 0:
         days = f"{days} day{get_suffix(days)}"
         result.append(days)       


    if hours > 0 and len(result) >= 1:
        hours = f", {hours} hour{get_suffix(hours)}"
        result.append(hours)       
    elif hours > 0:
         hours = f"{hours} hour{get_suffix(hours)}"
         result.append(hours)         


    if minutes > 0 and len(result) >= 1:
        minutes = f", {minutes} minute{get_suffix(minutes)}"
        result.append(minutes)  
    elif minutes > 0:
         minutes = f"{minutes} minute{get_suffix(minutes)}"  
         result.append(minutes)     


    if sex > 0 and len(result) >= 1:
        sex = f", {sex} second{get_suffix(sex)}"
        result.append(sex)
    elif sex > 0:
        sex = f"{sex} second{get_suffix(sex)}"  
        result.append(sex)     

    result[-1] = result[-1].replace(","," and")
    return "".join(result)


######################################################### BEST PRACTICE && CLEVER

# times = [("year", 365 * 24 * 60 * 60), 
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]


######################################################### CLEVER

# def format_duration(seconds):
#     if seconds == 0: return "now"
#     units = ( (31536000, "year"  ), 
#               (   86400, "day"   ),
#               (    3600, "hour"  ),
#               (      60, "minute"),
#               (       1, "second") )
#     ts, t = [], seconds
#     for unit in units:
#         u, t = divmod(t, unit[0])
#         ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
#     return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]

#########################################################

print(format_duration(61))