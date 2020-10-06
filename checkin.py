import requests
from urllib import parse
import os
requests.packages.urllib3.disable_warnings()

session=requests.session()
site=os.environ["SITE"]
user_name=os.environ["PSWD"]
user_pswd=os.environ["NAME"]

#通信测试:
headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4230.1 Safari/537.36"}
response=session.get(site,headers=headers, verify=False)
print("访问"+site+"返回状态码:"+str(response.status_code))
if response.status_code !=200:
    print("返回状态码有误，终止脚本")
    exit()
#登录账号:
headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4230.1 Safari/537.36",
        "referer": site}
response=session.get(site+"/index/login/", headers=headers, verify=False)
if response.status_code == 404:
    print("此网站返回404状态码，可能没有启用伪静态，不被此脚本支持")
    exit()
elif response.status_code != 200:
    print("网站返回状态码不正确:"+str(response.status_code))
    exit()

print("成功访问登录地址,开始尝试登陆...")

post_data={"swapname": user_name,
           "swappass": user_pswd}

response=session.post(site+"/index/login/?referer=",headers=headers, verify=False, data=post_data)
print("当前地址:"+parse.unquote(response.url))
if response.status_code == 404:
    print("此网站返回404状态码，可能没有启用伪静态，不被此脚本支持")
    exit()
elif response.status_code != 200 and response.status_code != 302:
    print("网站返回状态码不正确:"+str(response.status_code))
    exit()

print("登录返回状态码"+str(response.status_code))
#登录成功，开始签到:
headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4230.1 Safari/537.36",
        "referer": site}
response=session.get(site+"/user/?", headers=headers, verify=False)

headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4230.1 Safari/537.36",
        "referer": site+"/user/?"}
response=session.get(site+"/user/pay/?",headers=headers, verify=False)
if response.status_code !=200:
    print("返回的HTTP状态码不为200:"+str(response.status_code))
    exit()
print("成功访问网站充值界面")
headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4230.1 Safari/537.36",
        "referer": site+"/user/pay/?"}
response=session.get(site+"/plugin/qiandao",headers=headers, verify=False)
print("已尝试签到")
print(response.status_code)
print("当前URL(如果发生了错误，URL中会出现一个error参数):")
print(parse.unquote(response.url))
