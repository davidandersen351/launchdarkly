# launchdarkly test code
#
# this is a Python3 script used to test an LD feature flag called use-simple-average. 
# The flag determines which algorithm is used to compute a score based on 
# 3 inputted numbers.
#
# The code is documented but at a high level it:
#
# 1. Creates an instance of the LD client
# 2. Sets the value of a test user in the LD platform
# 3. Based on the user and feature flag name, calls the LD client and gets the value of the flag (true or false)
# 4. Defines a function that computes one of two score variations based on the feature flag (true = average, false = cubic)
# 5. Asks for 3 numbers of input from the command line
# 6. Calls the scoring function with the 3 inputted values
# 7. Displays the score, the calc method used, and if the feature is on or off
# 8. Shuts down the LD client

