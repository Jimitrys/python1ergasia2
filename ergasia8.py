# -*-coding:utf-8-*-
import tweepy
from tweepy import OAuthHandler
import os
import sys
#για επαναληψη του προγράμματος
play = True
while play == True:
    
    def load_api():

        consumer_key = 'Ezfthtgor0eq8pwPg91i1b8PU'
        consumer_secret = 'XL3aCkrJikAh45kcNXCWJnAACvpd3rvqCsNdytBerVRW6J4PEG'
        access_token = '3305179066-1JVhQULTVie9K4sqKaqejJgqdMf9iTOMOIdj7lm'
        access_secret = 'duliEuCdOFZjLmbxvKC6kbKFKx7PB4uKcq9gfUrhADUVf'
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return tweepy.API(auth)

    class TweetCount():
        #μετράει τα τουιτς του πρωτου λογαριασμου (θα δοθεί αργότερα)
        def tweets(self, tweets1):
            sum1 = 0
            for tweet in tweets1:
                sum1 += len(tweet.text.split())
            return sum1
        #μετράει τα τουιτς του δεύτερου λογαριασμου (θα δοθεί αργότερα)
        def tweets(self, tweets2):
            sum2 = 0
            for tweet in tweets2:
                sum2 += len(tweet.text.split())
            return sum2

    def main():

        api = load_api()

        #για τον πρώτο λογ. και τους φολλοουερς
        twitter_user1 = raw_input("Δώστε τον πρώτο λογαριασμό του τουίτερ: ")
        tweets1 = api.user_timeline(screen_name=twitter_user1, count=10)
        user1 = api.get_user(twitter_user1)
        followers1 = int(user1.followers_count)

        #για τον δευτερο λογαριασμο και τους φολλοουερς
        twitter_user2 = raw_input("Δώστε τον δεύτερο λογαριασμό του τουίτερ: ")
        tweets2 = api.user_timeline(screen_name=twitter_user2, count=10)
        user2 = api.get_user(twitter_user2)
        followers2 = int(user2.followers_count)

        #παίρνει απο την κλάση TweetCount τα αποτελεσματα
        count1 = TweetCount().tweets(tweets1)
        print "\nΟι Followers του χρήστη", twitter_user1, "είναι", followers1, " και ο αριθμός λέξεων των 10 τελευταίων του tweets είναι", count1

        count2 = TweetCount().tweets(tweets2)
        print "\nΟι Followers του χρήστη", twitter_user2, "είναι", followers2, " και ο αριθμός λέξεων των 10 τελευταίων του tweets είναι", count2

        #Κανει το γινομενο, συγκρίνει και εμφανίζει το αποτελεσμα
        if (followers2 * count2) > (followers1 * count1):
            print "\n\nΤο μεγαλύτερο γινόμενο λέξεων επι Followers εχει ο χρήστης", twitter_user2, "με γινόμενο ", (followers2 * count2)
        elif (followers2 * count2) < (followers1 * count1):
            print "\n\nΤο μεγαλύτερο γινόμενο λέξεων επι Followers εχει ο χρήστης", twitter_user1, "με γινόμενο ", (followers1 * count1)
        else:
            print "\n\nΚαι οι δύο λογαριασμοί έχουν το ίδιο γινόμενο λέξεων επι followers."

    main()
    #για επανάληψη η παύση του προγράμματος
    stop = raw_input("Πατήστε R για επανάληψη ή X για έξοδο: ").capitalize()
    if stop == "R":
        play = True
    elif stop == "X":
        play = False
if stop == "X":
        print("Αντίο.")
        sys.exit(-1)
