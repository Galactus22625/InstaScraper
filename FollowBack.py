def FollowBack(follower, following):
    file = open(follower, "r")
    followers = file.readlines()
    file.close()

    file = open(following, "r")
    followings = file.readlines()
    file.close

    notfollowback = [person.removesuffix('\n') for person in followings if person not in followers]
    print("These People Do Not Follow You Back:")
    for person in notfollowback:
        print(person)
    print("there are " + str(len(notfollowback)) + " people")

if __name__ == "__main__":
    followerfile = input("Follower File Name:  ")
    followingfile = input("Following File Name: ")
    FollowBack(followerfile,followingfile)
