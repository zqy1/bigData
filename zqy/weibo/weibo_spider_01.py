#-*-coding:utf8-*-

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver


user_id = 1863847262
cookie = {"Cookie": "_T_WM=bd35cb79d2140c573ed561b4d0b270d6; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https%3A%2F%2Flogin.sina.com.cn%2Fsso%2Flogin.php%3Furl%3Dhttps%3A%2F%2Fm.weibo.cn%2F%26_rand%3D1503407847.1495%26gateway%3D1%26service%3Dsinawap%26entry%3Dsinawap%26useticket%3D1%26returntype%3DMETA%26sudaref%3D%26_client_version%3D0.6.26; ALF=1506003943; SCF=AvPXTMRfNW1mv904vFEBVxirF3VVmm4FBSjn960HrTIbMbKlkfQaFns898dDOMq3gMYVjNxrYAotNxeQP8LwFJI.; SUB=_2A250mE63DeRhGeBN6FsX8yvPzT-IHXVUY1L_rDV6PUJbktANLXLFkW0LaoqSfTkGtNCva2epglJOVMPWTQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W52-A-NWNlDdsHY4aFoq2_Y5JpX5o2p5NHD95Qce0e4Soefe0q0Ws4Dqc_xi--Xi-zRiKn4i--Ri-2NiKnEi--ciKL8iKnpi--ci-82i-20i--NiKLWiKnXi--RiKn0i-2pi--fi-82iK.7i--fi-2Xi-2Ni--fiKysiK.X; SUHB=0bt8klccqFf1Zr; SSOLoginState=1503411943; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076031863847262"}

# url = 'http://weibo.cn/u/%d'%user_id
# url2 = 'https://m.weibo.cn/status/4141760094094304'
url3 = 'https://m.weibo.cn/status/4138566579839305'
# html = requests.get(url2, cookies = cookie).text
# soup = BeautifulSoup(html, 'lxml')
# print(soup)

driver = webdriver.Chrome()
# driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
driver.get(url3)



# name = driver.find_element_by_class_name('m-text-cut').text
# push_time = driver.find_element_by_class_name('time').text
# device = driver.find_element_by_class_name('from').text
# weibo_text = driver.find_element_by_class_name('weibo-text').text
# reproduced_num = driver.find_element_by_class_name('m-font m-font-forward').text
# comment_num = driver.find_element_by_class_name('m-font m-font-comment').text
# favor_num = driver.find_element_by_class_name('m-icon m-icon-like').text
# brief_introduction = '链接网址: ' + url3 + '\n' + '用户名: '+ name + '\n' + '用户设备: '+ device + '用户名: '+ name + '\n' +\
#     '发布时间： ' + push_time + '\n' + '微博内容: '+ weibo_text + '\n' + '转载数: ' + reproduced_num + '\n' +\
#                      '评论数: ' + comment_num + '\n'+ '点赞数: '+ favor_num + '\n'

# with open('sina_comment_data_append.csv', 'at') as f:
#     f.write(brief_introduction)
i = 0
while i < 20:
    # 将页面滚动条拖到底部
    driver.execute_script("document .body .scrollTop = 1000000")
    time.sleep(1)
    i += 1

# 抓取用户名，评论时间，点赞数，评论内容
for i in driver.find_elements_by_class_name('comment-item'):
    # content = i.text
    username = i.find_element_by_class_name('comment-user-name').text
    comment_time = i.find_element_by_class_name('comment-time').text
    comment_dz_num = i.find_element_by_class_name('comment-dz-num').text
    comment_con = i.find_element_by_class_name('comment-con').text
    content = username + ', ' + comment_time + ', ' + comment_dz_num + ', ' + comment_con + '\n'
    print(content)
    with open('sina_comment_data4.csv', 'at') as s:
        s.write(content)

driver.close()
