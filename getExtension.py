import sys

# The first argument is always the script's name, so set the second argument as
# the filename.
filename = sys.argv[1]

# Find the first period and take everything after it to be the extension. First
# period in case there are multiple in the extension (e.g., foo.log.backup)
extension = filename[filename.find("."):]
print(extension)
