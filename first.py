
from selenium import webdriver
import time
from userinfo import *


dataDict = get_userinfo("user1.txt")
list=[]
for item in dataDict:
     zd = {}
     username=item['username']
     password=item['password']
     title=item["title"]
     content=item["content"]
     bankuai=item["bankuai"]
     title1=item["title1"]
     content1=item["content1"]
     bankuai1=item['bankuai1']
     zd['username']=username
     zd['password']=password
     zd['title']=title
     zd['bankuai']=bankuai
     zd['content']=content
     zd['title1']=title1
     zd['bankuai1']=bankuai1
     zd['content1']=content1
     list.append(zd)

for item in list:
    username1=item['username']
    password1=item['password']
    title1=item['title']
    bankuai1=item['bankuai']
    content1=item['content']
    title2=item['title1']
    bankuai2=item['bankuai1']
    content2=item['content1']
    bs = webdriver.Firefox()
    bs.get("http://localhost/phpwind/")
    login_btn=bs.find_element_by_id("J_sidebar_login");
    login_btn.click();
    username=bs.find_element_by_id("J_u_login_username")
    password=bs.find_element_by_id("J_u_login_password")
    login_btn1=bs.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div/dl[4]/dd/button")

    username.send_keys(username1)
    password.send_keys(password1)
    login_btn1.click()
    time.sleep(4)
    login_post=bs.find_elements_by_class_name("header_post")[0]
    time.sleep(4)

    login_post.click()
    # label=bs.find_element_by_xpath("/html/body/div/header/div/div[3]/div[3]/div[1]/ul/li")
    time.sleep(2)
    label=bs.find_element_by_css_selector(".J_cate_item")
    time.sleep(2)
    label.click()

    if bankuai1=="NBA":

            bs.find_element_by_xpath("/html/body/div/header/div/div[3]/div[3]/div[2]/ul/li[2]").click()

    else:

            bs.find_element_by_xpath("/html/body/div/header/div/div[3]/div[3]/div[2]/ul/li[3]").click()


    queding=bs.find_element_by_xpath("//*[@id='J_head_forum_sub']")
    queding.click()

    biaoti=bs.find_element_by_xpath("//*[@id='J_atc_title']")
    biaoti.send_keys(title1)
    bs.switch_to.frame(bs.find_element_by_tag_name("iframe"))
    content=bs.find_element_by_xpath("/html/body")
    content.send_keys(content1)
    bs.switch_to.default_content()
    bt=bs.find_element_by_xpath("//*[@id='J_post_sub']")
    bt.click()
    time.sleep(9)
    try:
        kit=bs.find_element_by_xpath('//*[@id="J_post_sub"]')
        with open("dubbo.txt", "a") as f:
            f.write("username:" + username1 + "   mode:" + bankuai1 + "   title" + title1 + "   content" + content1 + "   Fail"+"\n")
            f.close()
        bs.find_element_by_xpath("/html/body/div/header/div/div[1]/a/img").click()
        em=bs.switch_to_alert()
        em.accept()
    except:
        with open("dubbo.txt", "a") as f:
            f.write("username:"+username1+"    mode:"+bankuai1+"    title"+title1+"     content"+content1+"   Pass"+"\n")
            f.close()



    time.sleep(4)
    login_post = bs.find_elements_by_class_name("header_post")[0]
    time.sleep(4)

    login_post.click()
    label=bs.find_element_by_xpath("/html/body/div/header/div/div[3]/div[3]/div[1]/ul/li")


    time.sleep(2)
    label.click()
    mk1 = bs.find_element_by_xpath("/html/body/div/header/div/div[3]/div[3]/div[2]/ul/li[3]")
    mk1.click()
    queding = bs.find_element_by_xpath("//*[@id='J_head_forum_sub']")
    queding.click()

    biaoti = bs.find_element_by_xpath("//*[@id='J_atc_title']")

    biaoti.send_keys(title2)
    bs.switch_to.frame(bs.find_element_by_tag_name("iframe"))
    content = bs.find_element_by_xpath("/html/body")
    content.send_keys(content2)
    bs.switch_to.default_content()
    bt = bs.find_element_by_xpath("//*[@id='J_post_sub']")
    bt.click()
    time.sleep(6)
    try:
       kit1=bs.find_element_by_xpath('//*[@id="J_post_sub"]')
       with open("dubbo.txt", "a") as f:
           f.write(
               "username:" + username1 + "   mode:" + bankuai2 + "   title" + title1 + "   content" + content1 + "   Fail" + "\n")
       bs.find_element_by_xpath("/html/body/div/header/div/div[1]/a/img").click()
       em = bs.switch_to_alert()
       em.accept()
    except:
        with open("dubbo.txt", "a") as f:
            f.write("username:" + username1 + "     mode:" + bankuai2 + "    title" + title1 + "   content" + content1 + "    Pass"+"\n")




