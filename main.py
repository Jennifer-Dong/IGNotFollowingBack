import re                                                                                                           #import requests module

with open("C:/Users/jennd/Desktop/Work/Projects/IGNotFollowingBack/IGNotFollowingBack/followers.html") as file:     #open your followers.html file
    for line in file:                                                                                               #go through each line in followers.html
            followers = re.findall('https://www.instagram.com/[^"]+', line)                                         #in followers, add all strings that start with https://www.instagram.com/ and continues until it reaches a "

with open("C:/Users/jennd/Desktop/Work/Projects/IGNotFollowingBack/IGNotFollowingBack/following.html") as file:     #open your following.html file
    for line in file:                                                                                               #go through each line in following.html
            following = re.findall('https://www.instagram.com/[^"]+', line)                                         #in following, add all strings that start with https://www.instagram.com/ and continues until it reaches a "

uh_oh = []                                                                                                          #uh-oh will hold a list of people that you follow, but don't follow you back
what = []                                                                                                           #what will hold a list of people that you don't follow, but they follow you

for i in following:                                                                                                 #go through every item in following
    if i not in followers:                                                                                          #go through every item in followers
        uh_oh.append(i)                                                                                             #add every follow that isn't following you to uh-oh
for i in followers:                                                                                                 #go through every item in follower
    if i not in following:                                                                                          #go through every item in following
        what.append(i)                                                                                              #add every follower that you aren't following to what

print('Not Following You, But You Follow Them')                                                                     #return the results
for i in range(len(uh_oh)):
    print(i+1, uh_oh[i])
print('\n\nFollowing You, But You Don\'t Follow Them')
for i in range(len(what)):
    print(i+1, what[i])

