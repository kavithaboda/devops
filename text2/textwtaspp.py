# importing the module
import pywhatkit
# using Exception Handling to avoid
# unprecedented errors
try:
    pywhatkit.sendwhatmsg("+917730949541","Hello",22,28)
    print("Successfully Sent!")
except:
    print("An Unexpected Error!")