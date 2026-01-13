import random
from platform import platform
import platform


print(platform.machine())
print(platform.architecture())

if platform.system() == "Windows".lower():
	print("Using Windows paths")
elif platform.system() == "Darwin":
	print("Running on macOS")
else:
	print("Likely Linux or Unix")


print("platform.system() is : ", platform.system())
print("platform.python_implementation() is : ", platform.python_implementation())
print("platform.pythin_version is : ", platform.python_version())





