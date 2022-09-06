# Getting Dependencies
import instaloader
from instaloader import Profile 

instance = instaloader.Instaloader()

#login or load session
user = 'vickyvinish98@gmail.com'
password = '3blue1brown'

instance.login(user, password)

# Fetching fullname of the profile:
profile = Profile.from_username(instance.context, username='vikkyvigneshhh')
# print(profile.full_name)

# Getting the followers of the profile:
# for followee in profile.get_followers():
#     print(followee.username)

# Getting followees of a sepcific user_account:
for follower in profile.get_followers():
    if follower.username == 'srikanthmadanagopal':
        follow_list = []
        count = 0
        for followee in follower.get_followees():
            follow_list.append(followee.username)
            with open('srikanth_follow_list.txt', 'a+') as f:
                f.write(follow_list[count])
                f.write('\n')
                count += 1
        print(f'Total number of people Srikanth follows is {len(follow_list)}')
        print("Mission Accomplished")