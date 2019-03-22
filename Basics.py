#!/usr/bin/env python
# coding: utf-8

# # Exploring Hacker News
# 
# This project will explore "Ask HN" and "Show HN" posts. Do either of the posts receive more comments than the other? Do posts created at a certain time receive more comments than average? 

# In[1]:


import csv
opened_file = open('hacker_news.csv')
hn = list(csv.reader(opened_file))



# # Removing Headers from a List

# In[2]:


headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[:5])


# # Extracting Ask HN and Show HN Posts

# In[3]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    title = title.lower()
    if title.startswith('ask hn'):
        ask_posts.append(row)
    elif title.startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# # Calculate the Number of Comments for Ask HN and Show HN Posts

# In[4]:


total_ask_comments = 0
for row in ask_posts:
    num_comments = row[4]
    num_comments = int(num_comments)
    total_ask_comments += num_comments
    
avg_ask_comments = total_ask_comments / len(ask_posts)
print(avg_ask_comments)

total_show_comments = 0
for row in show_posts:
    num_comments = row[4]
    num_comments = int(num_comments)
    total_show_comments += num_comments
    
avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)



# "HN Ask" posts receive an average of 14 comments per post while "HN Show" posts" receive an average of 10.3 comments per post.
# 
# Since "HN Ask" posts receive the most comments, we'll focus our attentnion on those. Next, we'll analyze if a certain time of day is more likely to receive more comments. 
# 
# # Find the Amount of Ask Posts and Comments Created Per Hour

# In[5]:


import datetime as dt
result_list = []
for row in ask_posts:
    created_at = row[6]
    comments = row[4]
    comments = int(comments)
    result_list.append([created_at, comments])
    
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    hour = row[0]
    comment = row[1]
    comment = int(comment)
    hour_dt = dt.datetime.strptime(hour, "%m/%d/%Y %H:%M").strftime("%H")
    
    if hour_dt not in counts_by_hour:
        counts_by_hour[hour_dt] = 1
        comments_by_hour[hour_dt] = comment
    elif hour_dt in counts_by_hour:
        counts_by_hour[hour_dt] += 1
        comments_by_hour[hour_dt] += comment
        
print(counts_by_hour)
print(comments_by_hour)
    


# Next we will create a new list of lists containing two elements. The first element of the lists will be the hours posts were created. The second will be the average number of comments posts received at those hours.

# In[6]:


avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])
           
print(avg_by_hour)


# # Sort the List and Print the 5 Highest Values

# In[11]:


swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print("Top 5 Hours for Ask Posts Comments")


for avg, hr in sorted_swap[:5]:
    template = "{}: {:.2f} average comments per post"
    template = template.format(dt.datetime.strptime(hr, "%H").strftime("%H:%M"), avg)
    print(template)

    
    


# # Conclusion
# 
# According to this sample of data, the posts on Hacker News that get the most interaction are "Ask HN" posts. The best time to post them are 15:00 Eastern time, with an average of 38.59 comments for each post. 
# 
# "Show HN" was a close contender for a high number of comments on posts as well. "Show HN" averaged 10.31 comments per post while "Ask HN" averaged 14.03 comments per post. 

# In[ ]:




