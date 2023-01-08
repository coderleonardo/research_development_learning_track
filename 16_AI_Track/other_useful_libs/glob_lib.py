# The glob module finds all the pathnames matching a specified pattern according to the rules 
# used by the Unix shell, 
# although results are returned in arbitrary order.
import glob

# Return a possibly empty list of path names that match pathname
print(glob.glob("extra_other_useful_libs/*.txt"))

# https://docs.python.org/3/library/glob.html