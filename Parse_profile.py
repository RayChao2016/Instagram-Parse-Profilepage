import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time
import datetime
from datetime import timedelta


def daily_post1():
    print('start')
    for x in account_list: 
        time.sleep(2.0)
        user_link = "https://www.instagram.com/" + x

        doc = requests.get(user_link)
        soup = BeautifulSoup(doc.text, 'html.parser')

        #See if any errors
        type_p = soup.find("meta", property="og:type")
        
        if type_p :
        
            body = soup.find('body')
            script_tag = body.find('script')
            raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
            json_data=json.loads(raw_string)
            js=json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        
            follow_number = js['edge_followed_by']['count']
            user_x_id = js['id']
            ig_x_account = js['username']

            if not js['is_private']:
               
            #3 photos
                for y in range(3):
                    post_y_photo_id = js['edge_owner_to_timeline_media']['edges'][y]['node']['shortcode']

                    post_y_time = datetime.datetime.fromtimestamp(js['edge_owner_to_timeline_media']['edges'][y]['node']['taken_at_timestamp'])

                    post_y_like = js['edge_owner_to_timeline_media']['edges'][y]['node']['edge_liked_by']['count']

                    post_y_img = js['edge_owner_to_timeline_media']['edges'][y]['node']['display_url']
		
                    
            else:
                print('private, ' + ig_x_account)
                pass
                  
        else:
            print('not valid link, ' + x )
            pass
