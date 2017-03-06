def getReadableTimeBetween(first, last):
    # A helper function to make a readable string between two times
    timeBetween = int(last - first)
    weeks = int(timeBetween / 604800)
    days = int((timeBetween - (weeks * 604800)) / 86400)
    hours = int((timeBetween - (days * 86400 + weeks * 604800)) / 3600)
    minutes = int((timeBetween - (hours * 3600 + days * 86400 + weeks * 604800)) / 60)
    seconds = int(timeBetween - (minutes * 60 + hours * 3600 + days * 86400 + weeks * 604800))
    msg = ""

    if weeks > 0:
        if weeks == 1:
            msg = '{}{} week, '.format(msg, str(weeks))
        else:
            msg = '{}{} weeks, '.format(msg, str(weeks))
    if days > 0:
        if days == 1:
            msg = '{}{} day, '.format(msg, str(days))
        else:
            msg = '{}{} days, '.format(msg, str(days))
    if hours > 0:
        if hours == 1:
            msg = '{}{} hour, '.format(msg, str(hours))
        else:
            msg = '{}{} hours, '.format(msg, str(hours))
    if minutes > 0:
        if minutes == 1:
            msg = '{}{} minute, '.format(msg, str(minutes))
        else:
            msg = '{}{} minutes, '.format(msg, str(minutes))
    if seconds > 0:
        if seconds == 1:
            msg = '{}{} second, '.format(msg, str(seconds))
        else:
            msg = '{}{} seconds, '.format(msg, str(seconds))

    if not msg:
        return "0 seconds"
    else:
        return msg[:-2]

#=======================================================================================================================

import plugin
import command
import message
import main
import time

def onInit(plugin):
    #create the basics of our plugin
    xkcd_plugin = plugin.plugin.plugin()
    xkcd_plugin.plugin = plugin
    xkcd_plugin.name = 'uptime'

    #now to register commands
    xkcd_command = command.command()
    xkcd_command.plugin = plugin
    xkcd_command.name = 'uptime'

    #add our commands to the plugin
    xkcd_plugin.commands = [] #this line is for some reason needed or stuff will break
    xkcd_plugin.commands.append(xkcd_command)

    return xkcd_plugin

def onCommand(message_in):
    if message_in.command == 'uptime':
        currentTime = int(time.time())
        timeString = getReadableTimeBetween(main.startTime, currentTime)
        msg = 'I\'ve been up for *{}*.'.format(timeString)
        return message.create(body=msg)