# module



# import datetime
# post_date='2023-01-01'
# post_date=datetime.datetime.strptime(post_date, "%Y-%m-%d")
# print(post_date)
# today=datetime.date.today()
# birthday=datetime.date(2000,3,31)
# print(today-birthday)
# import datetime
# today="2023-12-27"
# today=datetime.datetime.strptime(today,"%Y-%m-%d")
# # print(today)
# # today=datetime.datetime.today()
# jobs =[
#     {'title':"python developer","exp_date":"2020-01-01"},
#     {'title':"java developer","exp_date":"2024-01-01"},
#     {'title':"php developer","exp_date":"2022-01-01"},
#     {'title':"c++ developer","exp_date":"2021-01-01"},
#     {'title':"c# developer","exp_date":"2024-06-08"},
# ]
# for job in jobs:
#     title = job['title']
#     date = job["exp_date"]
#     date = datetime.datetime.strptime(date, "%Y-%m-%d")
    
#     if today >= date:
#         print(f"{title},Your job has expired.")
#     else:
#         print(f"{title},You have an ongoing job.")
    
# or



# import sys
# import os
# import glob
# file hanlding

import datetime
today = datetime.datetime.today()
print(today)
today = today.strftime('%Y-%m-%d')
todayMonth = datetime.datetime.strptime(today,"%Y-%m-%d").month
todayDay = datetime.datetime.strptime(today,"%Y-%m-%d").day


birthDate = "2002-12-27"
birthMonth = datetime.datetime.strptime(birthDate,"%Y-%m-%d").month
birthDay = datetime.datetime.strptime(birthDate,"%Y-%m-%d").day



if todayMonth==birthMonth:
    if todayDay == birthDay:
        print("Today is your birthday.")
    elif todayDay >= birthDay:
        print("Your birthday is gone.")
    else:
        print("Your birthday is coming")

elif todayMonth >= birthMonth:
    print("Your birthday is gone.")