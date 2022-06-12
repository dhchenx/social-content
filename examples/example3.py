from social_content.twitter import *

text='''
#CatBoy called #SafeCatGirl !
https://t.co/CZgF6SJ2RQ
https://t.co/pay2uVyvxL
https://t.co/WeUom7jtEr
#BSCGems #BSCGem #NFT #NFTs #GameFi #ElonMusk #altcoins #bitcoin  
#crypto #ethereum #btc #altcoin #Binance #ripple 
#ETH #shiba #MXS #BNB #dogecoin #Metaverse #BSC #DeFi https://t.co/CHhdHVBuDe https://t.co/fMhOYH1rlO
'''

text=remove_hashtag_mention(text)
text=remove_urls(text)

print(text.strip())