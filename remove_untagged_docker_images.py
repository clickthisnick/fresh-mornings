'''
Command To Run: python3 remove_untagged_docker_images.py
What does it do: Removes untagged docker images
If you run docker images you might see a bunch that are <none> this takes up space and eventually you will run out on your vm
Example:
* 11 * * * /usr/local/bin/python3 /Users/nick/devops/devops/sdlc/remove_untagged_docker_images.py
* 14 * * * /usr/local/bin/python3 /Users/nick/devops/devops/sdlc/remove_untagged_docker_images.py
'''

import subprocess

def execute_command(command):
    ''' Executes the command '''
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    return output[0].decode()

# Restart computer
execute_command('docker rmi $(docker images | grep "^<none>" | awk "{print $3}")')
