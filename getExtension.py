import sys

# The first argument is always the script's name, so set the second argument as
# the filename.
filename = sys.argv[1]

# Extract the filename without the $PWD by slicing from the last "/" to the
# end. (This is to prevent hidden folders from being part of the 'extensin.')
# Then, find the first period and take everything after it to be the extension.
# First period in case there are multiple in the extension (e.g.,
# foo.log.backup
# TODO: deal with hidden files
filename = filename[filename.rfind("/"):]
extension = filename[filename.find("."):]
print(extension)
