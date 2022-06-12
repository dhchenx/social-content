from social_content.weibo import *
'''
    Evaluate sentiment scores based on Weibo user's emoji list
'''
# 1. Chinese comment text
comment="那不也是新能源？如果真想要新能源指标，至于摇号那么久么[中国赞]"
# clean text
comment_cleaned=clean_weibo_text(comment)

# 2. load a list of all possible emojis
happy_emoji,neutral_emoji,sad_emoji=create_emoji_list()

# 3. extract an emoji list in the comment text
list_comment_emoji=extract_emoji(comment)
print("Emoji list:",list_comment_emoji)

# 4. evaluate emoji sentiment based on emoji dictionary and
happy,sad,neutral=sentiment_emoji(happy_emoji,neutral_emoji,sad_emoji,list_comment_emoji)
print(f"Sentiment preference:{happy}\t{sad}\t{neutral}")

# 5. evaluate a combined sentiment, two types of sentiment
avg_sentiment_real,avg_sentiment_grade = get_avg_sentiment_with_all(text=comment_cleaned,list_emoji=list_comment_emoji)
print("Average sentiment by continual value:",avg_sentiment_real)
print("Average sentiment by discrete value: ",avg_sentiment_grade)



