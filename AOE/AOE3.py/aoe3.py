class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        print(f"Logging in as {self.username}")
    
    def post(self, content):
        print(f"{self.username} posted: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers=0):
        super().__init__(username, password)
        self.number_of_followers = followers
    
    def share_story(self, content):
        print(f"{self.username} shared a story: {content}")
        print(f"Viewable by {self.number_of_followers} followers")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets=0):
        super().__init__(username, password)
        self.number_of_tweets = tweets
    
    def tweet(self, content):
        self.number_of_tweets += 1
        print(f"{self.username} tweeted: {content}")
        print(f"Total tweets: {self.number_of_tweets}")

# Test the implementations
instagram = InstagramAccount("photo_lover", "pass123", 1000)
twitter = TwitterAccount("tweet_master", "pass456", 500)

# Test Instagram features
instagram.login()
instagram.post("Check out my new photo!")
instagram.share_story("At the beach!")

# Test Twitter features
twitter.login()
twitter.post("Regular post")
twitter.tweet("Hello Twitter!")
twitter.tweet("Another tweet!")
