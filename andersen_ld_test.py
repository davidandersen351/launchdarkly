
#simple Python3 code to demonstrate the use of LaunchDarkly feature flags

#import the LaunchDarkly client 
import ldclient
from ldclient.config import Config

#create instance of LaunchDarkly client using Test Env key
ldclient.set_config(Config("sdk-1c869509-b2b1-47d6-8fa2-827e08db955f"))
ld_client = ldclient.get()

#set value of user - in a dynamic execution this would be set on the fly
user = {
  "key": "UNIQUE IDENTIFIER",
  "firstName": "Bob",
  "lastName": "Loblaw",
  "custom": {
    "groups": "beta_testers"
  }
}

#set the feature flag value (t/F) based on the flag ID and user name. 
show_feature = ld_client.variation("use-simple-average",user, False)


# Score Calculating Function
# using the "use-simple-average" feature flag to determine the algo
def compute_score(r1,r2,r3):

	if show_feature:
  		return (r1 + r2 + r3) / 3
	else:
  		return (r1 + r2 + r3)**3 /6


print (" ")
print (" ")
print (" ")
# Get the 3 values needed to compute a final score
round1 = int(input("Enter score 1: "))
round2 = int(input("Enter score 2: "))
round3 = int(input("Enter score 3: "))

#call the score function 
score=round(compute_score(round1,round2,round3))


# Display the result and which score feature was used
print (" ")
print (" ")
print (" ")
print ("*******************************")
print ("The final score is: ", score )
print ("*******************************")
if show_feature:
	print("used average (feature on)")
else:
	print("used cubic (feature off)")
print (" ")
print (" ")
print (" ")

#shut down the LaunchDarkly client
ldclient.get().close()