import os
import subprocess

def list_all_commands():
    """
    List all available commands
    """
    stream = os.popen('compgen -c')
    output = stream.read()
    commands = output.split('\n')
    return commands


def execute_command(command: str):
    """
    Execute a command
    """
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sp.communicate()
