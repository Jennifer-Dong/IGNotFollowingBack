import re

with open("C:/Users/jennd/Desktop/Work/Projects/IGNotFollowingBack/IGNotFollowingBack/followers.html") as file:
    for line in file:
            followers = re.findall('https://www.instagram.com/[^"]+', line)

with open("C:/Users/jennd/Desktop/Work/Projects/IGNotFollowingBack/IGNotFollowingBack/following.html") as file:
    for line in file:
            following = re.findall('https://www.instagram.com/[^"]+', line)

uh_oh = []
what = []

for i in following:
    if i not in followers:
        uh_oh.append(i)
for i in followers:
    if i not in following:
        what.append(i)

print('Not Following You, But You Follow Them')
for i in range(len(uh_oh)):
    print(i+1, uh_oh[i])
print('\n\nFollowing You, But You Don\'t Follow Them')
for i in range(len(what)):
    print(i+1, what[i])

