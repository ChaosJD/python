import pssh.clients
from pssh.clients import ParallelSSHClient

# Variables
HOSTNAME=
USER=
PASSWORD=
PORT=

hosts = [HOSTNAME]
client = ParallelSSHClient(hosts, user=USER, password=PASSWORD, port=PORT)

# Here are the commands
cmd = """
export DISPLAY=":0.0"
xdotool click 3
"""

# Here run the commands
shells = client.open_shell()
client.run_shell_commands(shells, cmd)
client.join_shells(shells)

