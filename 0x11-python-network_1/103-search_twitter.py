#!/usr/bin/python3
"""Takes in three strings and sends a Tweet search to the Twitter API"""

import requests
import sys
import base64

if __name__ == "__main__":

    key = '{}:{}'.format(sys.argv[1], sys.argv[2]).encode('ascii')
    encoded_key = base64.b64encode(key)
    encoded_key = encoded_key.decode('ascii')
    response = requests.post('https://api.twitter.com/oauth2/token',
                             headers={
                                'Authorization': 'Basic {}'
                                .format(encoded_key),
                                'Content-Type':
                                'application/x-www-form-urlencoded;charset=\
                                    UTF-8'
                             },
                             data={
                                'grant_type': 'client_credentials'
                             })
    token = response.json()['access_token']
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json',
                            headers={
                                'Authorization': 'Bearer {}'.format(token)
                            },
                            params={
                                'q': sys.argv[3],
                                'result_type': 'recent',
                                'count': 5
                            })
    tweets = response.json()
    for tweet in tweets['statuses']:
        print("[{}] {} by {}".format(tweet.get('id_str'),
                                     tweet.get('text'),
                                     tweet.get('user').get('name')))
