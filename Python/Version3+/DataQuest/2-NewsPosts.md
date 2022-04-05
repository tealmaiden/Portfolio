# Exploring Hacker News Posts

The purpose of this guided project is to practice working with string manipulation, object-oriented Python, and dates and times by running data analyses on posts from Hacker News, a popular technology news forum, similar to reddit.


```python
#read in csv file and make into a list:
file = open('hacker_news.csv')
from csv import reader
read_file = reader(file)
hn = list(read_file)

#show first 5 rows:
for row in hn[0:4]:
    print(row)
```

    ['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at']
    ['12224879', 'Interactive Dynamic Video', 'http://www.interactivedynamicvideo.com/', '386', '52', 'ne0phyte', '8/4/2016 11:52']
    ['10975351', 'How to Use Open Source and Shut the Fuck Up at the Same Time', 'http://hueniverse.com/2016/01/26/how-to-use-open-source-and-shut-the-fuck-up-at-the-same-time/', '39', '10', 'josep2', '1/26/2016 19:30']
    ['11964716', "Florida DJs May Face Felony for April Fools' Water Joke", 'http://www.thewire.com/entertainment/2013/04/florida-djs-april-fools-water-joke/63798/', '2', '1', 'vezycash', '6/23/2016 22:20']



```python
#extract header:
header = hn[0]
hn=hn[1:]

#check:
print(header)
print('\n')
print(hn[0:4])

```

    ['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at']
    
    
    [['12224879', 'Interactive Dynamic Video', 'http://www.interactivedynamicvideo.com/', '386', '52', 'ne0phyte', '8/4/2016 11:52'], ['10975351', 'How to Use Open Source and Shut the Fuck Up at the Same Time', 'http://hueniverse.com/2016/01/26/how-to-use-open-source-and-shut-the-fuck-up-at-the-same-time/', '39', '10', 'josep2', '1/26/2016 19:30'], ['11964716', "Florida DJs May Face Felony for April Fools' Water Joke", 'http://www.thewire.com/entertainment/2013/04/florida-djs-april-fools-water-joke/63798/', '2', '1', 'vezycash', '6/23/2016 22:20'], ['11919867', 'Technology ventures: From Idea to Enterprise', 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429', '3', '1', 'hswarna', '6/17/2016 0:01']]


#### We are only interested in observing posts that begin with Ask HN or Show HN in the title.


```python
#separate posts into different lists based on the beginning of the title
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
#check:
print('ask posts: ' + str(len(ask_posts)))
print('show posts: ' + str(len(show_posts)))
print('other posts: ' + str(len(other_posts)))
```

    ask posts: 1744
    show posts: 1162
    other posts: 17194


#### Looking at calculations on number of comments for the different post types:


```python
#total comments and avg number of comments per ask post
total_ask_comments = 0

for row in ask_posts:
    num_comments = row[4]   
    num_comments = int(num_comments)
    total_ask_comments+=num_comments
        
avg_ask_comments = total_ask_comments/len(ask_posts)
print('avg number of ask comments: ' + str(avg_ask_comments))

#total comments and avg number of comments per show post
total_show_comments = 0

for row in show_posts:
    num_comments = int(row[4])
    total_show_comments+=num_comments

avg_show_comments = total_show_comments/len(show_posts)
print('avg number of show comments: ' + str(avg_show_comments))
```

    avg number of ask comments: 14.038417431192661
    avg number of show comments: 10.31669535283993


#### Since ask posts get more comments on average, we will focus more on these posts and see what times of day are more likely to attract comments.


```python
import datetime as dt
result_list = []

for row in ask_posts:
    created_at = row[6]    
    num_comments = int(row[4])
    pair = [created_at, num_comments]
    result_list.append(pair)
    
#print(result_list)
counts_by_hour = {} # num posts by hour
comments_by_hour = {}

for pair in result_list:
    time = pair[0]
    num_comments = pair[1]
    
    hour = dt.datetime.strptime(time, '%m/%d/%Y %H:%M')
    hour_str = hour.strftime('%H')
        
    if hour_str not in counts_by_hour:
        counts_by_hour[hour_str] = 1
        comments_by_hour[hour_str] = num_comments
    else:
        counts_by_hour[hour_str] += 1
        comments_by_hour[hour_str] += num_comments
        
print('counts by hour {hour, num posts}: ')
print(counts_by_hour)
print('comments by hour: {hour, num comments}')
print(comments_by_hour)
```

    counts by hour {hour, num posts}: 
    {'09': 45, '13': 85, '10': 59, '14': 107, '16': 108, '23': 68, '12': 73, '17': 100, '15': 116, '21': 109, '20': 80, '02': 58, '18': 109, '03': 54, '05': 46, '19': 110, '01': 60, '22': 71, '08': 48, '04': 47, '00': 55, '06': 44, '07': 34, '11': 58}
    comments by hour: {hour, num comments}
    {'09': 251, '13': 1253, '10': 793, '14': 1416, '16': 1814, '23': 543, '12': 687, '17': 1146, '15': 4477, '21': 1745, '20': 1722, '02': 1381, '18': 1439, '03': 421, '05': 464, '19': 1188, '01': 683, '22': 479, '08': 492, '04': 337, '00': 447, '06': 397, '07': 267, '11': 641}



```python
#average number of comments per post during each hour of the day
avg_by_hour = []

for hour in comments_by_hour:
    #print(comments_by_hour[hour])
    #print(counts_by_hour[hour])
    avg = comments_by_hour[hour]/counts_by_hour[hour]
    avg_by_hour.append([hour, avg])
print(avg_by_hour)
```

    [['09', 5.5777777777777775], ['13', 14.741176470588234], ['10', 13.440677966101696], ['14', 13.233644859813085], ['16', 16.796296296296298], ['23', 7.985294117647059], ['12', 9.41095890410959], ['17', 11.46], ['15', 38.5948275862069], ['21', 16.009174311926607], ['20', 21.525], ['02', 23.810344827586206], ['18', 13.20183486238532], ['03', 7.796296296296297], ['05', 10.08695652173913], ['19', 10.8], ['01', 11.383333333333333], ['22', 6.746478873239437], ['08', 10.25], ['04', 7.170212765957447], ['00', 8.127272727272727], ['06', 9.022727272727273], ['07', 7.852941176470588], ['11', 11.051724137931034]]


#### Identifying the hours with the highest averages:


```python
swap_avg_by_hour = []
for pair in avg_by_hour:
    hour = pair[0]
    avg = pair[1]
    swap_avg_by_hour.append([avg, hour])

print("inverted list: ")
print(swap_avg_by_hour)
print("\n")

#https://docs.python.org/3/howto/sorting.html#sortinghowto
sorted_swap = sorted(swap_avg_by_hour, key=None, reverse=True)

print("Top 5 hours for ask post comments: ")
for pair in sorted_swap[0:4]:
    hour = pair[1]
    hour = dt.datetime.strptime(hour, "%H")
    hour = hour.strftime("%H:%M")
    avg = pair[0]
    string = "{}: {:.2f} average comments per post".format(hour, avg)
    print(string)
    
```

    inverted list: 
    [[5.5777777777777775, '09'], [14.741176470588234, '13'], [13.440677966101696, '10'], [13.233644859813085, '14'], [16.796296296296298, '16'], [7.985294117647059, '23'], [9.41095890410959, '12'], [11.46, '17'], [38.5948275862069, '15'], [16.009174311926607, '21'], [21.525, '20'], [23.810344827586206, '02'], [13.20183486238532, '18'], [7.796296296296297, '03'], [10.08695652173913, '05'], [10.8, '19'], [11.383333333333333, '01'], [6.746478873239437, '22'], [10.25, '08'], [7.170212765957447, '04'], [8.127272727272727, '00'], [9.022727272727273, '06'], [7.852941176470588, '07'], [11.051724137931034, '11']]
    
    
    Top 5 hours for ask post comments: 
    15:00: 38.59 average comments per post
    02:00: 23.81 average comments per post
    20:00: 21.52 average comments per post
    16:00: 16.80 average comments per post

