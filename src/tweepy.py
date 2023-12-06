# keys
api_key = '1MVFftXceUfhExRkSqSpXhy6C'
api_secret_key = "IZb1jbpENLiRqjOVt2vgEhR3jen2CO2RIobZh7E2cACsU95vA5"
bearer_tokem = 'AAAAAAAAAAAAAAAAAAAAAKwkbwEAAAAAI%2BLe3sh6dNEIGF9JCIL5U%2BpCCeY%3DmJgV6Opqm8Km8XNcf04llAVRvKD98SPvtWaZNwvweo09dmM834'
access_token = "1517584070154272768-EvlYEM0uP8LUaup9GTxQqWbTulegc9"
access_token_secret = 'BsMD78683Qb2IY5XJRv1ijRx8pxzNtenCJV83pEKvn8KO'

# Tweepy data extraction

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)