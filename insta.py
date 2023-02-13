# Getting Dependencies
import instaloader
from instaloader import Profile 

instance = instaloader.Instaloader()

#login or load session
user = 'vikkyvigneshhh' # Replace your username here.
instance.interactive_login(user) # Enter the password in the terminal to login

# Fetching profile of the user:
profile = Profile.from_username(instance.context, user) # username of the profile


# Returns the profile's followers as a list:
def get_followers( profile ):
    return [ follower.username for follower in profile.get_followers()]

# Returns the profile's followees as a list:
def get_followees( profile ):
    return [ followee.usernmae for followee in profile.get_followees() ]


# Getting followings of a sepcific user_account:
def  get_followings_of_specific_account( profile, followee_name ):
    for followee in profile.get_followees():
        if followee.username == followee_name:
            following_list = []
            count = 0
            # Loop through and add followings to a text file.
            for followee in followee.get_followees():
                following_list.append(followee.username)
                with open(followee_name + '_followings_list.txt', 'a+') as f:
                    f.write(following_list[count])
                    f.write('\n')
                    count += 1


# working with saved_posts: (Function needs to be checked and updated)
def saved_posts( profile ):
    return profile.get_saved_posts()

if __name__ == "__main__":

    print(f" Hi {profile.full_name}!! ")
    print("\n")

    print(f" You follow { profile.followees } profiles")
    # print(get_followees( profile ))  // Uncomment this line if you want the list of following.
    
    print(f" { profile.followers } profiles follow you")
    # print(get_followers( profile )) // Uncomment this line if you want the list of followers.

    # To get followings of a sepcific user_account you follow:
    followee_name = 'srikanthmadanagopal' # Replace the with the required username 
    get_followings_of_specific_account( profile, followee_name )

    print(saved_posts( profile ))