#!/usr/bin/env python
# coding: utf-8

# In[84]:


import requests

url_reg = "http://10.61.64.26:8000/authentication/register/"
url_new_token = "http://10.61.64.26:8000/authentication/token/"
#TC1 & TC2
olga = {'username': 'Olga','password': '1234'}
nick = {'username': 'Nick','password': '1234'}
mary = {'username': 'Mary','password': '1234'}
nestor = {'username': 'Nestor','password': '1234'}

user_list = [olga, nick, mary, nestor]
json_response = dict()
for i in user_list:
    store = requests.post(url_new_token, data = i)
    store = store.json()
    json_response[i['username']] = store
print(json_response)


# In[14]:


#TC3
url_post = "http://10.61.64.26:8000/v1/Post/"
olga_response = requests.get(url_post)
olga_response = olga_response.json()
print(olga_response)


# In[85]:


#Grab tokens
olga_token = json_response['Olga']['access_token']
nick_token = json_response['Nick']['access_token']
mary_token = json_response['Mary']['access_token']
nestor_token = json_response['Nestor']['access_token']


# In[157]:


#TC4 Olga creates a Post record with expiration time using her token
post_url = 'http://10.61.64.26:8000/v1/Post/'

headers_tc4 = {'Authorization': 'Bearer '+ str(olga_token)}

record_tc4 = {'title':'Tesla Daily',
          'topic':'tech',
          'message_body':'Tesla Rulz in today news',
          'expiration_time':'2021-05-20 10:20',
          'author':'42', #Olga is under number 42 in the user list
          'status':'live'
         }
olga_tc_4 = requests.post(post_url, headers=headers_tc4, data=record_tc4)
print(olga_tc_4.json())


# In[158]:


#TC5 Nick creates a Post record with expiration time using her token
headers_tc5 = {'Authorization': 'Bearer '+ str(nick_token)}

record_tc5 = {'title':'SpaceX Daily',
          'topic':'tech',
          'message_body':'SpaceX launched Starship SN16',
          'expiration_time':'2021-05-20 10:20',
          'author':'43', #Nick is under number 43 in the user list
          'status':'live'
         }
nick_tc_5 = requests.post(post_url, headers=headers_tc5, data=record_tc5)
print(nick_tc_5.json())


# In[159]:


#TC6 Mary creates a Post record with expiration time using her token
headers_tc6 = {'Authorization': 'Bearer '+ str(mary_token)}

record_tc6 = {'title':'NeuraLink Weekly',
          'topic':'tech',
          'message_body':'Neuralink releases a video of Monkey playing Ping Pong using its brain',
          'expiration_time':'2021-05-20 10:20',
          'author':'44', #Mary is under number 44 in the user list
          'status':'live'
         }
mary_tc_6 = requests.post(post_url, headers=headers_tc6, data=record_tc6)
print(mary_tc_6.json())


# In[162]:


#TC7 Nick and Olga browse all the available posts in the Tech topic, there should be three posts available with zero likes, zero dislikes and without any comments.
posts_query_url = 'http://10.61.64.26:8000/v1/Post/?topic=tech' #query filter did not not work properly so used loop here


headers_tc7 = {'Authorization': 'Bearer '+ str(nick_token)}
response_tc7 = requests.get(posts_query_url, headers=headers_tc7)

count=int()
for post_item in response_tc7.json(): #query filter did not not work properly so used loop here
    if post_item['topic'] =='tech':
        count+=1
        print(post_item)
    else:
        break
print("Number of posts: " + str(count))


# In[165]:


#TC7 Nick and Olga browse all the available posts in the Tech topic, there should be three posts available with zero likes,
headers_tc7 = {'Authorization': 'Bearer '+ str(olga_token)}
response_tc7 = requests.get(post_url, headers=headers_tc7)

count=int()
for post_item in response_tc7.json(): #query filter did not not work properly so used loop here  
    if post_item['topic'] =='tech':
        count+=1
        print(post_item)
    else:
        break
print("Number of posts: " + str(count))


# In[196]:


#TC7 there should be three posts available with zero likes and comments
likes_query_url = 'http://10.61.64.26:8000/v1/Likes/?post='
comments_query_url = 'http://10.61.64.26:8000/v1/Comment/?post='

headers_tc7 = {'Authorization': 'Bearer '+ str(nick_token)}

post_ids = [3,4,5]
for i in post_ids:
    response = requests.get(comments_query_url + str(i), headers=headers_tc7)
    print(response.json())


# In[198]:


#TC8 Nick likes Mary's post in the tech topic
likes_url = 'http://10.61.64.26:8000/v1/Likes/'
headers_tc8 = {'Authorization': 'Bearer '+ str(nick_token)}

record_tc8 = {'like_or_dislike':'like',
          'post':'5', #Mary's post is under primary key number 5 - Neuralink Weekly
          'author':'43', #Nick is under number 43 in the user list
         }
nick_tc_8 = requests.post(likes_url, headers=headers_tc8, data=record_tc8)
print(nick_tc_8.json())


# In[199]:


#TC8 Olga likes Mary's post in the tech topic
likes_url = 'http://10.61.64.26:8000/v1/Likes/'
headers_tc8 = {'Authorization': 'Bearer '+ str(olga_token)}

record_tc8 = {'like_or_dislike':'like',
          'post':'5', #Mary's post is under primary key number 5 - Neuralink Weekly
          'author':'42', #Olga is under number 42 in the user list
         }
olga_tc_8 = requests.post(likes_url, headers=headers_tc8, data=record_tc8)
print(olga_tc_8.json())


# In[202]:


#TC9 Nestor “likes” Nick’s post, and “dislikes” Mary’s post in the Tech topic.
headers_tc8 = {'Authorization': 'Bearer '+ str(nestor_token)}

record_tc8 = {'like_or_dislike':'like',
          'post':'4',#Nick's post is under number 4 - SpaceX Daily
          'author':'43', #Nick is under number 43 in the user list
         }
nick_tc_8 = requests.post(likes_url, headers=headers_tc8, data=record_tc8)
print(nick_tc_8.json())


# In[200]:


#TC9 Nestor “likes” Nick’s post, and “dislikes” Mary’s post in the Tech topic.
headers_tc8 = {'Authorization': 'Bearer '+ str(nestor_token)}

record_tc8 = {'like_or_dislike':'dislike',
          'post':'5',#Mary's post is under number 5 - Neuralink Weekly
          'author':'45', #Nestor is under number 43 in the user list
         }
nick_tc_8 = requests.post(likes_url, headers=headers_tc8, data=record_tc8)
print(nick_tc_8.json())


# In[ ]:


#TC9 Nestor “likes” Nick’s post, and “dislikes” Mary’s post in the Tech topic.
headers_tc8 = {'Authorization': 'Bearer '+ str(nestor_token)}

record_tc8 = {'like_or_dislike':'dislike',
          'post':'11',#Mary's post is under number 11
          'author':'45', #Nestor is under number 43 in the user list
         }
nick_tc_8 = requests.post(likes_url, headers=headers_tc8, data=record_tc8)
print(nick_tc_8.json())


# In[237]:


#TC10 Nick browses all posts in Tech topic, he can see Mary's post likes/dislikes and comments attributes

likes_query_url = 'http://10.61.64.26:8000/v1/Likes/?post='

headers_tc10 = {'Authorization': 'Bearer '+ str(nick_token)}

post_ids = [3,4,5]
for i in post_ids:
    response = requests.get(likes_query_url + str(i), headers=headers_tc10)
    print("Comments for post: "+ str(i) + str(response.json()))


# In[215]:


for item in response.json():
    print(str(item['like_or_dislike']) + " for post PK num:" + str(item['post']))


# In[236]:


comments_query_url = 'http://10.61.64.26:8000/v1/Comment/?post='

headers_tc10 = {'Authorization': 'Bearer '+ str(nick_token)}

post_ids = [3,4,5]
for i in post_ids:
    response = requests.get(comments_query_url + str(i), headers=headers_tc10)
    print("Comments for post: "+ str(i) + str(response.json()))


# In[224]:


#TC11 Mary likes her post in the Tech topic. This call should be unsuccessful, as in Piazza a post owner cannot like their own messages
headers_tc11 = {'Authorization': 'Bearer '+ str(mary_token)}

record_tc11 = {'like_or_dislike':'like',
          'post':'5',#Mary's post is under number 5
          'author':'44', #Mary is under number 44 in the user list
         }
mary_tc_11 = requests.post(likes_url, headers=headers_tc11, data=record_tc11)
print(mary_tc_11.json())


# In[225]:


#TC12 Nick and Olga comment for Mary’s post in the Tech topic in a round-robin fashion (one after the other adding at least 2 comments each)
comment_url = 'http://10.61.64.26:8000/v1/Comment/'

#Nick and Olga's tokens
headers_1 = {'Authorization': 'Bearer '+ str(nick_token)}
headers_2 = {'Authorization': 'Bearer '+ str(olga_token)}

#comment records to insert
record1 = {'comment':'this is very educational', 'author': '43', 'post':'5'}
record2 = {'comment':'this is fun', 'author': '43', 'post':'5'}
record3 = {'comment':'YOLO', 'author': '42', 'post':'5'}
record4 = {'comment':'HODL', 'author': '42', 'post':'5'}

result_nick1 = requests.post(comment_url, headers=headers_1, data=record1)
result_olga1 = requests.post(comment_url, headers=headers_2, data=record3)
result_nick2 = requests.post(comment_url, headers=headers_1, data=record2)
result_olga2 = requests.post(comment_url, headers=headers_2, data=record4)

comb_results = [result_nick1, result_olga1, result_nick2, result_olga2]
for i in comb_results:
    print(i.json())


# In[226]:


#TC13 Nick browses all the available posts in the Tech topic; at this stage he can see the number of likes and dislikes of each post and the comments made.

posts_query_url = 'http://10.61.64.26:8000/v1/Post/?topic=tech'

headers_tc13 = {'Authorization': 'Bearer '+ str(nick_token)}

nick_tc_13 = requests.get(posts_query_url, headers=headers_tc13)
print(nick_tc_13.json())
print("Number of posts: " + str(len(nick_tc_13.json())))


# In[234]:


#TC13 show likes of posts
likes_query_url = 'http://10.61.64.26:8000/v1/Likes/?post='

headers_tc10 = {'Authorization': 'Bearer '+ str(nick_token)}

post_ids = [3,4,5]
for i in post_ids:
    response = requests.get(likes_query_url + str(i), headers=headers_tc10)
    print("Likes for post: "+ str(i) + str(response.json()))


# In[232]:


#TC13 show comments of posts
comments_query_url = 'http://10.61.64.26:8000/v1/Comment/?post='

headers_tc10 = {'Authorization': 'Bearer '+ str(nick_token)}

post_ids = [3,4,5]
for i in post_ids:
    response = requests.get(comments_query_url + str(i), headers=headers_tc10)
    print("Comments for post: "+ str(i) + str(response.json()))


# In[238]:


#TC14 Nestor posts a message in the Health topic with an expiration time using her token

headers_tc14 = {'Authorization': 'Bearer '+ str(nestor_token)}

record_tc14 = {'title':'Sports nutrition',
          'topic':'health',
          'message_body':'Vitamin C is essential to human body',
          'expiration_time':'2021-05-20 10:20',
          'author':'45', #Nestor is under number 45 in the user list
          'status':'live'
         }
nestor_tc_14 = requests.post(post_url, headers=headers_tc14, data=record_tc14)
print(nestor_tc_14.json())


# In[239]:


#TC15 Mary browses all the available posts in the Tech topic; at this stage he can see the number of likes and dislikes of each post and the comments made.

posts_query_url = 'http://10.61.64.26:8000/v1/Post/?topic='

topic = "health"

headers_tc15 = {'Authorization': 'Bearer '+ str(mary_token)}

mary_tc_15 = requests.get(posts_query_url + topic, headers=headers_tc15)
print(mary_tc_15.json())
print("Number of posts: " + str(len(mary_tc_15.json())))


# In[240]:


#TC16 Mary posts a comment in the Nestor’s message in the Health topic
headers_tc16 = {'Authorization': 'Bearer '+ str(mary_token)}

record_tc16 = {'num_comments':'1',
          'comment':'This post is incredible',
          'author':'44', #May is under Pk number 44
          'post':'6', #Nestor's post is under number Pk number 6
         }
nick_tc_16 = requests.post(comment_url, headers=headers_tc16, data=record_tc16)
print(nick_tc_16.json())


# In[241]:


#TC17 Mary dislikes Nestor’s message in the Health topic after the end of post expiration time. This should fail.
headers_tc17 = {'Authorization': 'Bearer '+ str(mary_token)}

record_tc17 = {'like_or_dislike':'dislike',
          'post':'6',#NEstor's post is under number 6
          'author':'44', #Mary's is under number 43 in the user list
         }
mary_tc_17 = requests.post(likes_url, headers=headers_tc17, data=record_tc17)
print(mary_tc_17.json())


# In[242]:


#TC18 Nestor browses all the messages in the Health topic. There should be only post (his own) with one comment (Mary’s).
posts_query_url = 'http://10.61.64.26:8000/v1/Post/?topic=health'

headers_tc15 = {'Authorization': 'Bearer '+ str(nestor_token)}

mary_tc_15 = requests.get(posts_query_url, headers=headers_tc15)
print(mary_tc_15.json())
print("Number of posts: " + str(len(mary_tc_15.json())))


# In[249]:


#TC18 show comments of post
comments_query_url = 'http://10.61.64.26:8000/v1/Comment/?post=6'

headers_tc18 = {'Authorization': 'Bearer '+ str(nick_token)}

response = requests.get(comments_query_url, headers=headers_tc18)
print("Comments for Nestor's post:" + str(response.json()))


# In[250]:


#TC19 Nick browses all the expired messages in the Sport topic. These should be empty

posts_query_url = 'http://10.61.64.26:8000/v1/Post/?topic='

topic = "sport"

headers_tc19 = {'Authorization': 'Bearer '+ str(nick_token)}

nick_tc_19 = requests.get(posts_query_url + topic, headers=headers_tc19)
print(nick_tc_19.json())
print("Number of posts: " + str(len(nick_tc_19.json())))


# In[ ]:


#TC 20. Nestor queries for an active post having the highest interest (maximum sum of likes and dislikes) in the Tech topic. This should be Mary’s post

