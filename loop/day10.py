# users=[
#     {"name":"ram","gender":"male","status":True},
#     {"name":"hari","gender":"male","status":False},
#     {"name":"sita","gender":"female","status":True},
#     {"name":"gita","gender":"female","status":False},
#     {"name":"gopal","gender":"male","status":True},
# ]

# total_user=len(users)
# total_male=0
# total_female=0
# total_active_user=0
# total_inactive_user=0
# total_active_male=0
# total_inactive_male=0
# total_active_female=0
# total_inactive_female=0
# for user in users:
#     if user['gender']=='male':
#         total_male+=1
        
#     else:
#         total_female+=1
        
#     if user['status']=='true':
#         total_active_user+=1
#     else:
#         total_inactive_user+=1
    
        
# print("total users:", total_user)
# print("total active users:" ,total_active_user)
# print("total inactive users", total_inactive_user)



# courses=[
#     {"title":"python","price":"20000"},
#     {"title":"java","price":"18000"},
#     {"title":"php","price":"15000"},
# ]

# name = input("Enter course name:")
# is_found=False
# course_details="";
# for cs in courses:
#     if name == cs['title']:
#         course_details=cs["title"]+" "+ cs["price"]
#         is_found=True
        

# if is_found:
#     print(course_details)
# else:
#     print("Course not found " + name)

sectionA=['ram','sita','kamala']
sectionB=['para','dong','hari']

print(sectionA)
print(sectionB)


temp = sectionA[0]
sectionA[0] = sectionB[-1]
sectionB[-1] = temp

temp = sectionA[1]
sectionA[1] = sectionB[1]
sectionB[1] = temp

temp = sectionA[-1]
sectionA[-1] = sectionB [1]
sectionB[1] = temp

print("\n")
print(sectionA)
print(sectionB)