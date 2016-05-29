'''
Command To Run: python3 kill_all_processes.py
What does it do: Closes all applications
Run this one minute before the restart_computer.py
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

def search_and_kill_processes(name):
    ''' Returns the command to search and force kill apps by name '''
    return 'ps aux | grep -i ' + name + ' | awk {\'print $2\'} | xargs kill -9'

APPS_SEARCH_AND_FORCE_KILL = ['chrome', 'firefox', 'burp', 'atom', 'sublime', 'intellij',
                              'cyberduck', 'mail', 'finder', 'pages', 'calendar',
                              'keynote', 'numbers', 'slack', 'skitch', 'sequel', 'textedit',
                              'vlc'
                             ]

## Always do this last
APPS_SEARCH_AND_FORCE_KILL.append('terminal')

for app in APPS_SEARCH_AND_FORCE_KILL:
    kill_command = search_and_kill_processes(app)
    execute_command(kill_command)
