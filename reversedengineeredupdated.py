import requests
import time
import json
import os
import csv


def get_next_cursor(response: dict):
    if response is None:
        return 'DAABCgABGLCr8Yv__9YKAAIYo9wzgRsg9ggAAwAAAAIAAA'
    for item in response['data']['user']['result']['timeline_v2']['timeline']['instructions']:
        if item['type'] == 'TimelineAddEntries':
            for entry in item['entries']:
                pass
            cursor = item['entries'][-1]['content']['value']
            return cursor



cookies = {
    'guest_id_marketing': 'v1%3A170521912648258381',
    'guest_id_ads': 'v1%3A170521912648258381',
    'guest_id': 'v1%3A170521912648258381',
    '_ga': 'GA1.2.1471807406.1712950739',
    'g_state': '{"i_l":0}',
    'kdt': 'FCnDlHA4vXJxwDUa0uKsRzCO5K30ZXNPxnn2XF5l',
    'auth_token': '26fb20a0c0905bb1bd65776da80bd3af0f4402dd',
    'ct0': '2c5c0ebda19df9e2700e348ecfad288315808de9756b175e51e03984c1542c67e96b86d9c9e712ed35f37e08decd0c0f84102c74fa1771f1a829589293fe1face1ad1f7dd7a2a768753b4fc93ac5bce0',
    'twid': 'u%3D1594396750063800323',
    'lang': 'en',
    '_gid': 'GA1.2.1090050302.1713108516',
    'personalization_id': '"v1_ZIID+K74JUXOb2sWW+5Rbw=="',
}
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': 'guest_id_marketing=v1%3A170521912648258381; guest_id_ads=v1%3A170521912648258381; guest_id=v1%3A170521912648258381; _ga=GA1.2.1471807406.1712950739; g_state={"i_l":0}; kdt=FCnDlHA4vXJxwDUa0uKsRzCO5K30ZXNPxnn2XF5l; auth_token=26fb20a0c0905bb1bd65776da80bd3af0f4402dd; ct0=2c5c0ebda19df9e2700e348ecfad288315808de9756b175e51e03984c1542c67e96b86d9c9e712ed35f37e08decd0c0f84102c74fa1771f1a829589293fe1face1ad1f7dd7a2a768753b4fc93ac5bce0; twid=u%3D1594396750063800323; lang=en; _gid=GA1.2.1090050302.1713108516; personalization_id="v1_ZIID+K74JUXOb2sWW+5Rbw=="',
    'referer': 'https://twitter.com/marc_louvion/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-client-transaction-id': '6nLrhUWS+zcUGck6K6lCzsd8zLpF/WMQfmjt+Vr1ZOHTDBTGr8wRzxkSoHrahCeJUyF4JuslQ94VzgUnmhV5QOEfp6986Q',
    'x-client-uuid': '20fad734-1072-47f9-a153-8ea2a3279062',
    'x-csrf-token': '2c5c0ebda19df9e2700e348ecfad288315808de9756b175e51e03984c1542c67e96b86d9c9e712ed35f37e08decd0c0f84102c74fa1771f1a829589293fe1face1ad1f7dd7a2a768753b4fc93ac5bce0',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

response = None
i = 0
while True:
    try:
        i += 1

        cursor = get_next_cursor(response)
        params = {
            'variables': '{"userId":"111425302","count":20,"cursor":"' + cursor + '","includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}',
            'features': '{"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
            'fieldToggles': '{"withArticlePlainText":false}',
        }

        response = requests.get(
            'https://twitter.com/i/api/graphql/piUHOePH_uDdwbD9GkquJA/UserTweets',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        print(response.status_code, i, i*20)
        response = response.json()

        if not os.path.exists('responses'):
            os.makedirs('responses')

        with open(f'responses/{i}.json', 'w') as f:
            json.dump(response, f)

        time.sleep(2)
    except json.decoder.JSONDecodeError:
        print('The script has scraped max. possible amount of tweets.')
        break

files = os.listdir('responses')

listoftweetresp = []

for i in range(len(files)):
    with open(f'responses/{i+1}.json', 'r') as file:
        data = json.load(file)
        publishedtimefirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
        descfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
        likesfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['favorite_count']
        repostsfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['retweet_count']
        viewsfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['views']['count']
        repliesfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['reply_count']
        bookmarksfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['bookmark_count']
        tweeturlfirst = 'https://x.com/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'] + '/status/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['rest_id']
        contenturlfirst = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entry']['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][0]['media_url_https']
        dictoftweetresp = {
            'publishedtime': f'{publishedtimefirst}',
            'desc': f'{descfirst}',
            'likes': f'{likesfirst}',
            'reposts': f'{repostsfirst}',
            'views': f'{viewsfirst}',
            'replies': f'{repliesfirst}',
            'bookmarks': f'{bookmarksfirst}',
            'tweeturl': f'{tweeturlfirst}',
            'contenturl': f'{contenturlfirst}'
        }
        listoftweetresp.append(dictoftweetresp)
    for j in range(20):
        try:
            publishedtime = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
        except KeyError:
            try:
                publishedtime = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['created_at']
            except KeyError:
                publishedtime = None
                pass
        except IndexError:
            break
        try:
            desc = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
            if 'ą' in str(desc) or 'ę' in str(desc):
                desc = None
                continue
        except KeyError:
            try:
                desc = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
                if 'ą' in str(desc) or 'ę' in str(desc):
                    desc = None
                    continue
            except KeyError:
                continue
        except IndexError:
            break
        try:
            likes = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['favorite_count']
        except:
            try:
                likes = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['favorite_count']
            except KeyError:
                likes = None
                pass
        try:
            reposts = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['retweet_count']
        except KeyError:
            try:
                reposts = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['retweet_count']
            except KeyError:
                reposts = None
                pass
        except IndexError:
            break
        try:
            views = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['views']['count']
        except KeyError:
            try:
                views = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['views']['count']
            except KeyError:
                views = None
                pass
        try:
            replies = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['reply_count']
        except KeyError:
            try:
                replies = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['reply_count']
            except KeyError:
                replies = None
                pass
        try:
            bookmarks = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['bookmark_count']
        except KeyError:
            try:
                bookmarks = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['bookmark_count']
            except KeyError:
                bookmarks = None
                pass
        try:
            tweeturl = 'https://x.com/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'] + '/status/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['rest_id']
        except KeyError:
            try:
                tweeturl = 'https://x.com/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'] + '/status/' + data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['rest_id']
            except KeyError:
                tweeturl = None
                pass
        try:
            contenturl = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][0]['media_url_https']
        except KeyError:
            try:
                contenturl = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][j]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][0]['media_url_https']
            except KeyError:
                contenturl = None
                pass
        dictoftweetresp = {
        'publishedtime': f'{publishedtime}',
        'desc': f'{desc}',
        'likes': f'{likes}',
        'reposts': f'{reposts}',
        'views': f'{views}',
        'replies': f'{replies}',
        'bookmarks': f'{bookmarks}',
        'tweeturl': f'{tweeturl}',
        'contenturl': f'{contenturl}'
        }
        listoftweetresp.append(dictoftweetresp)





outputfile = 'outputresp.csv'

keys = listoftweetresp[0].keys()

with open(outputfile, 'w', newline='', encoding='utf-8') as file:
    dict_writer = csv.DictWriter(file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(listoftweetresp)
