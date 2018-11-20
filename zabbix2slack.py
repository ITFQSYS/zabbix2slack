#!/usr/bin/env python3

import requests
import json
import sys

url='Type Slack Webhook URL'

# クォーテーションを取り除く
subject=sys.argv[2].replace('\'','')
text=sys.argv[3].replace('\'','')

if subject.find('Problem') > -1:
    character=':face_vomiting:'
    text='@channel\n'+text
elif subject.find('Resolved') > -1:
    character=':smile:'
else:
    character=':neutral_face:'

requests.post(url, data = json.dumps({
    'text': text, # 投稿するテキスト
    'username': u'Zabbix', # 投稿のユーザー名
    'icon_emoji': character, # 投稿のプロフィール画像に入れる絵文字
    'link_names': 1, # メンションを有効にする
}))
