import glob
# Get all photos in the same directory as this program
# Returns all files that end in .jpg
filenames = glob.glob('*.jpg')
print(filenames)
