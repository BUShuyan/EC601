# EC601

[reference code for twitter API](https://www.askpython.com/python/examples/extracting-tweets-using-twitter-api)

The project.py is to test NLP API, it will shows the sentiment based on the sentence you input.

The test sentences and results in terminal are as following:

please input your words/sentence:you get nothing

Text: you get nothing

Sentiment: -0.800000011920929, 0.800000011920929

(base) zhangshuyan@iwas-MacBook-Air NLP % python NLP.py

please input your words/sentence:you get everything

Text: you get everything

Sentiment: 0.8999999761581421, 0.8999999761581421

(base) zhangshuyan@iwas-MacBook-Air NLP % python NLP.py

please input your words/sentence:The weather is terrible

Text: The weather is terrible

Sentiment: -0.699999988079071, 0.699999988079071

(base) zhangshuyan@iwas-MacBook-Air NLP % python NLP.py

please input your words/sentence:you are handsome

Text: you are handsome

Sentiment: 0.8999999761581421, 0.8999999761581421

# User story

From twitter API, we can find local trend and immediate tweets related to some topic. From the information gathered and filtered by program using Twitter API, google NLP API could be used to analyze the sentiment and attitude of people from their likes, retweet, and comment. This is the main function of the program. User stories can be analyzed from following views.
I want to build a community for people who have similar thoughts through this program. MVP are only tweeters because they post tweets and show their attitude towards something.

* Tweeter:
    * People who want to announce or show their attitude towards some topic or incidents could use this program to analyze the trend and obtain the positive and negative attitude of it, also they could see the reasons and thoughts behind the sentiment. If you want to come up with an objective idea or summary, you will need to use this program rather than just post your own tweets.
    * People who have already post their tweets also can analyze the sentiment of other from analyzing the likes/dislikes, retweets and comments using this program. The result could be regarded as the sentiment of people towards this tweet. There are many tweeters care about it, such as stars, celebrities and even official announcers.
    * From the sentiment and attitude of the same topic, it is easy to find people who holds similar thoughts. This information could be utilized to build a community for people who have similar thoughts to communicate and know each other. The topic could be an album, a masterpiece, some photos. Therefore, they could make more friends on this social media to talk about the things they are all concerned about.

* Module design
    * The whole analyzer could be separated into gathering part, sentiment part, classification part and building part.
    * The gathering part is to obtain the tweets and any information related to some topic on the Twitter.
    * The sentiment part is to analyze the sentiment and other attitude towards the topic or incident. 
    * The classification part is to sort people who hold different ideas into different groups and arrange the people who hold the similar one into consistent group.
    * Building part plays an organizer role in this analyzer.  The group formed in the last part is the prototype of community. Then, build the community from the prototype and incorporate the group who hold similar idea into a larger community.
