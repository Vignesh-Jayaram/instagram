# Getting Dependencies
import instaloader
from instaloader import Profile 

instance = instaloader.Instaloader()

#login or load session
user = 'user_mail'
password = 'password'

instance.login(user, password)

# Fetching fullname of the profile:
profile = Profile.from_username(instance.context, username='username')# username of the profile
print(f"The full name of the profile is {profile.full_name}")

# Returns all the username of the profile's followers:
for follower in profile.get_followers():
    print(follower.username)

# Getting followees of a sepcific user_account:
for follower in profile.get_followers():
    if follower.username == 'srikanthmadanagopal':
        # Creating and adding follower usernames to a list
        follow_list = []
        count = 0
        for followee in follower.get_followees():
            follow_list.append(followee.username)
            # Writing username to a text file
            with open('srikanth_follow_list.txt', 'a+') as f:
                f.write(follow_list[count])
                f.write('\n')
                count += 1
        print(f'Total number of people Srikanth follows is {len(follow_list)}')