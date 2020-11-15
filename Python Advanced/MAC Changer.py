import subprocess

subprocess.run("ipconfig enol down", shell=True)
subprocess.run("ipconfig enol hw ether 00:11:22:33:44:55", shell=True)
subprocess.run("ipconfig enol up", shell=True)
subprocess.run("ipconfig")
