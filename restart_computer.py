'''
Command To Run: python3 restart_computer.py
What does it do: Restarts your computer
Run this one minute after you run kill_all_processes.py
Example:
Set up System Preferences Energy Saving to wake up computer at 5:59
0 6 * * * /usr/local/bin/python3 /Users/nick/devops/devops/sdlc/kill_all_processes.py
1 6 * * * /usr/local/bin/python3 /Users/nick/devops/devops/sdlc/restart_computer.py
'''

import subprocess

def execute_command(command):
    ''' Executes the command '''
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    return output[0].decode()

# Restart computer
execute_command('osascript -e \'tell app "System Events" to restart\'')
