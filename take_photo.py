from time import sleep
from picamera import PiCamera

# Ask user to input their first and last names
first = input("Please type your first name and then press Enter: ")
last = input("Please type your last name and then press Enter: ")

# Get a reference to the Raspberry Pi camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview()

# Camera warm-up time
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
 
# Remove any characters in first and last variables that are not letters
for c in first:
    if c == "-" or c == "_":
        continue
    if c.isalpha() == False:
        first = first.replace(c, '')

for c in last:
    if c == "-" or c == "_":
        continue
    if c.isalpha() == False:
        last = last.replace(c, '')

# Save file as firstName_lastName.jpg, all lowercase
filename = first.lower() + "_" + last.lower() + ".jpg"

# Save image to the same directory as this program
# facerec_on_raspberry_pi should now recognize the added person
camera.capture(filename)
