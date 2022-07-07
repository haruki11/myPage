'''
説明会やインターンに空席が出たかどうかをチェックしてLINEに通知するソフトウェア
マイページの利用規約でウェブスクレイピング技術を用いたアクセスは禁止されていないので法的にも問題ありません

下記の内容をバッチファイルで作成することで自動でN秒おきにチェックしてくれます。
:top

myPage.py
timeout N

goto top

'''

import time
import chromedriver_binary
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def send_line_notify(notification_message):
    line_notify_token = '{自分のline_notifyのtoken}'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def check(i): 
    driver.get(lis[i][1]) #マイページのログイン画面へ移動

    time.sleep(10)

    id_name = driver.find_element_by_name('id') 
    password = driver.find_element_by_name('password')

    id_name.send_keys(lis[i][3]) #idの入力
    password.send_keys(lis[i][4]) #パスワードの入力

    id_name.submit()
    url = lis[i][2] #説明会やインターンの予約画面へ移動

    
    time.sleep(10)

    driver.get(url)
    time.sleep(10)
    page = driver.page_source

    if "受付中" in page:
        send_line_notify(lis[i][0] + "　空席")
    else:
        send_line_notify(lis[i][0] + "　満席")


driver = webdriver.Chrome()  #WEBブラウザの起動
lis = [
    ['{会社名}', '{マイページのログイン画面のURL}', '{説明会やインターンの予約画面URL}', "{マイページのID}", "{マイページのパスワード}"],
    ['{会社名}', '{マイページのログイン画面のURL}', '{説明会やインターンの予約画面URL}', "{マイページのID}", "{マイページのパスワード}"]
    ] #何社でも同時に調べられる

for i in range(len(lis)):
    check(i)


driver.close()

