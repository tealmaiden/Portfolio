# Analyzing Mobile App Data

The purpose of this project is to analyze profitable apps to generate revenue for an imaginary app-building company. The revenue is ad-based and depends on user engagement from English-speaking audiences.

The data to be analyzed comes from the [Apple Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) and [Google Play store](https://dq-content.s3.amazonaws.com/350/googleplaystore.csv) in csv files that can be downloaded at the linked sources. The following code extracts data from these files to create list of list datasets.


```python
def get_data(file):
    the_file = open(file)
    from csv import reader
    read_file = reader(the_file)
    apps_data = list(read_file)
    return apps_data

appledata = get_data('AppleStore.csv')
googledata = get_data('googleplaystore.csv')
```

This function returns specified rows of a data set, which can be reused to observe slices of data:


```python
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
```

Column headers are removed and saved separately below to make the dataset easier to work with later.


```python
explore_data(appledata, 0, 2) #16 columns
explore_data(googledata, 0, 2) #13 columns
appleheader = appledata[0]
del appledata[0]
googleheader = googledata[0]
del googledata[0]
```

    ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']
    
    
    ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']
    
    
    ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
    
    
    ['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']
    
    


## Data cleaning

When a dataset has errors, duplicates or other unwanted data, it can be cleaned by removing the rows of problematic data. For example, it is known that one of the rows of Google App Store data is missing an entry, which shifts the columns. This is deleted below.


```python
print(googleheader, "\n")

explore_data(googledata, 10471, 10472) #normal data
explore_data(googledata, 10472, 10473) #wrong data, missing Category
```

    ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'] 
    
    ['Xposed Wi-Fi-Pwd', 'PERSONALIZATION', '3.5', '1042', '404k', '100,000+', 'Free', '0', 'Everyone', 'Personalization', 'August 5, 2014', '3.0.0', '4.0.3 and up']
    
    
    ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
    
    



```python
del googledata[10472]
```

## Removing duplicates

Duplicates in the Google data are identified below. The set with the most reviews will be kept in favor of others so that newer reviews won't be left out.


```python
googleduplicates = []
googleuniques = []

for app in googledata:
    name = app[0]
    if name not in googleuniques:
        googleuniques.append(name)
    else:
        googleduplicates.append(name)
```


```python
#print(googleuniques)
print('Examples of duplicates', googleduplicates[0:3])
print('Expected Length: ', len(googleuniques))
print('Length duplicates: ', len(googleduplicates))
print('Expected Length: ', len(googledata)-1181)

```

    Examples of duplicates ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business']
    Expected Length:  9659
    Length duplicates:  1181
    Expected Length:  9659



```python
reviewsmax = {}

def get_names_max_reviews(dataset):
    for app in googledata:
        name = app[0]
        nreviews = float(app[3])
        if name in reviewsmax and nreviews>reviewsmax[name]:
            reviewsmax[name] = nreviews
        elif name not in reviewsmax:
            reviewsmax[name] = nreviews

get_names_max_reviews(googledata)
print('Length of apps with highest number of reviews: ', len(reviewsmax))

googleclean = []
alreadyadded = []

def clean_dataset_max_reviews(dataset):
    for app in googledata:
        name = app[0]
        nreviews = float(app[3])
        if nreviews==reviewsmax[name] and name not in alreadyadded:
            googleclean.append(app)
            alreadyadded.append(name)

clean_dataset_max_reviews(googledata)
print('Length cleaned data: ', len(alreadyadded))
```

    Length of apps with highest number of reviews:  9659
    Length cleaned data:  9659


## Isolating English-speaking apps
The Apple Store data doesn't have duplicates, but both sets have non-English-speaking apps, which are not useful for the goal of this analysis and will be removed below.


```python
def is_English(checkstring):
    countFilteredChars = 0
    for letter in checkstring:
        if ord(letter)>127:
            countFilteredChars+=1
        if countFilteredChars>=3:
            return False
    return True

print('Testing function:')
print(is_English('Instagram'))
print(is_English('çˆ±å¥‡è‰ºPPS -ã€Šæ¬¢ä¹é¢‚2ã€‹ç”µè§†å‰§çƒ­æ’­'))
print(is_English('Docs To Goâ„¢ Free Office Suite'))
print(is_English('Instachat ðŸ˜œ'))

def English_filter(dataset, header, namecol):
    newset = []
    index = header.index(namecol)
    for app in dataset:
        name = app[index]
        if is_English(name):
            newset.append(app)
    return newset
            
googleEnglish = English_filter(googleclean, googleheader, 'App')
print('Length google data - no duplicates English: ', len(googleEnglish))
appleEnglish = English_filter(appledata, appleheader, 'track_name') 
print('Length apple data - no duplicates English: ', len(appleEnglish))
#print(appleEnglish)
print(is_English('UCæµè§ˆå™¨HD'))
```

    Testing function:
    True
    False
    True
    True
    Length google data - no duplicates English:  9597
    Length apple data - no duplicates English:  6155
    False


## Isolating free apps
We are only interested in free apps, so those are isolated here.


```python
def get_free_apps(dataset, header, pricecol):
    priceindex = header.index(pricecol)
    freeapps = []    
    for app in dataset:
        price = (app[priceindex]).lower()
        if price == 'free' or price == '0' or price == '0.0':
            freeapps.append(app)
    return freeapps

freegoogle = get_free_apps(googleEnglish, googleheader, 'Price')
freeapple = get_free_apps(appleEnglish, appleheader, 'price')

print("Length free Google: ", len(freegoogle))
print("Length free Apple: ", len(freeapple))  
```

    Length free Google:  8848
    Length free Apple:  3203


## Further context and strategy
The app is planned to be made available on both the Apple Store and Google Play because our revenue is based on the number of users engaging with the app. Broader platform availability allows for the app to reach more people.

The strategy for validating and releasing the app is as follows:
1. Build a minimal Android version of the app, and add it to Google Play.
2. If the app has a good response from users, we develop it further.
3. If the app is profitable after six months, we build an iOS version of the app and add it to the App Store.

To be successful, we need to find app profiles that will be successful in both markets. This will require analysis of popular types of apps based on genre, ratings, and other metrics.

## Building frequency tables
The following functions build and display a frequency table for values in a given column of a dataset.


```python
def freq_table(dataset, header, colname):
    index = header.index(colname)
    ftable = {}    
    for app in dataset:
        colval = app[index]
        if colval not in ftable:
            ftable[colval]=1
        else:
            ftable[colval]+=1
    sumf = sum(ftable.values()) #sum over values in frequency table
    for key in ftable:
        #ftable[key]="{:.2f}".format(ftable[key]/sumf*100) #show as a percentage formatted to 2 dec places
        ftable[key]=ftable[key]/sumf*100
    return ftable

#Allows for displaying sorted results:
def display_table(table):    
    #table = freq_table(dataset, header, colname)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key) #convert dictionary to tuple with value first, key second
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
        
print('Freq table for apple prime_genre: \n')
applegenrefreq = freq_table(freeapple, appleheader, 'prime_genre')
display_table(applegenrefreq)
```

    Freq table for apple prime_genre: 
    
    Games : 58.25788323446769
    Entertainment : 7.836403371838902
    Photo & Video : 4.995316890415236
    Education : 3.6840462066812365
    Social Networking : 3.3093974399000934
    Shopping : 2.5913206369029034
    Utilities : 2.466437714642523
    Sports : 2.1542304089915705
    Music : 2.0605682172962845
    Health & Fitness : 2.0293474867311896
    Productivity : 1.7483609116453322
    Lifestyle : 1.5610365282547611
    News : 1.3424914142990947
    Travel : 1.248829222603809
    Finance : 1.0927255697783327
    Weather : 0.8741804558226661
    Food & Drink : 0.8117389946924758
    Reference : 0.5307524196066188
    Business : 0.5307524196066188
    Book : 0.3746487667811427
    Navigation : 0.18732438339057134
    Medical : 0.18732438339057134
    Catalogs : 0.1248829222603809


## Average apple ratings by genre

The above code can be used to find the average number of ratings per genre of a dataset. This will be used to help make a genre recommendation for an Apple Store app below.


```python
def avgnumratings(dataset, header, genrecolname, ratingsctcolname):
    freqtable = freq_table(dataset, header, genrecolname)
    dictionary={}
    for genre in freqtable:
        total = 0
        lengenre = 0
        genreindex = header.index(genrecolname)
        ratingsindex = header.index(ratingsctcolname)
        for app in dataset:           
            genreapp = app[genreindex]            
            if genreapp==genre:
                ratingct = float(app[ratingsindex])
                total+=ratingct
                lengenre+=1
        avgnumratings=total/lengenre
        dictionary[genre]=avgnumratings
    return dictionary
```


```python
applenumratingsdict=avgnumratings(freeapple, appleheader, 'prime_genre', 'rating_count_tot')
display_table(applenumratingsdict)
```

    Navigation : 86090.33333333333
    Reference : 79350.4705882353
    Social Networking : 71548.34905660378
    Music : 57326.530303030304
    Weather : 52279.892857142855
    Book : 46384.916666666664
    Food & Drink : 33333.92307692308
    Finance : 32367.02857142857
    Photo & Video : 28441.54375
    Travel : 28243.8
    Shopping : 27230.734939759037
    Health & Fitness : 23298.015384615384
    Sports : 23008.898550724636
    Games : 22886.36709539121
    News : 21248.023255813954
    Productivity : 21028.410714285714
    Utilities : 19156.493670886077
    Lifestyle : 16815.48
    Entertainment : 14195.358565737051
    Business : 7491.117647058823
    Education : 7003.983050847458
    Catalogs : 4004.0
    Medical : 612.0


## Recomendation for Apple Store app
It appears navigation apps have the highest average number of ratings. Genres with few single apps that have high numbers of ratings and few total apps may skew the results. Navigation is dominated by Waze and Google Maps, with very few other apps. However it appears genres lower down the list have many monoliths as well, such as Music and Social Networking with rating numbers in the millions for Pandora and Facebook. The app with the max number of ratings in reference is for the Bible, which is also relatively high, but to a lesser extent. I would recommend either **Social Networking** or doing a different kind of analysis to draw a recommendation for the Apple Store because using the average alone doesn't seem to be very useful with such a large spread. Many of the apps with the most use in non-social categories seem to have elements of social intent to them: Waze, Google Maps (reviews), Dictionary.com (communication), Google Translator, the Bible (religion). Also, Social Networking is a relatively much larger category, which can bring down the average while also signaling demand in that area.


```python
def display_genre_dict(dataset, genrename, header, namecol, genrecol, ratingsctcol):
    nameindex=header.index(namecol)
    genreindex=header.index(genrecol)
    ratingsctindex=header.index(ratingsctcol)
    dictionary={}
    for app in dataset:
        name=app[nameindex]
        ratingsct=app[ratingsctindex]
        if app[genreindex]==genrename:
            dictionary[name]=float(ratingsct)
    display_dictionary(dictionary)
```


```python
print('nav app counts')
display_genre_dict(freeapple, 'Navigation', appleheader, 'track_name', 'prime_genre', 'rating_count_tot')
```

    nav app counts
    Waze - GPS Navigation, Maps & Real-time Traffic : 345046.0
    Google Maps - Navigation & Transit : 154911.0
    GeocachingÂ® : 12811.0
    CoPilot GPS â€“ Car Navigation & Offline Maps : 3582.0
    ImmobilienScout24: Real Estate Search in Germany : 187.0
    Railway Route Search : 5.0



```python
print('reference app counts')
display_genre_dict(freeapple, 'Reference', appleheader, 'track_name', 'prime_genre', 'rating_count_tot')
```

    reference app counts
    Bible : 985920.0
    Dictionary.com Dictionary & Thesaurus : 200047.0
    Dictionary.com Dictionary & Thesaurus for iPad : 54175.0
    Google Translate : 26786.0
    Muslim Pro: Ramadan 2017 Prayer Times, Azan, Quran : 18418.0
    New Furniture Mods - Pocket Wiki & Game Tools for Minecraft PC Edition : 17588.0
    Merriam-Webster Dictionary : 16849.0
    Night Sky : 12122.0
    City Maps for Minecraft PE - The Best Maps for Minecraft Pocket Edition (MCPE) : 8535.0
    LUCKY BLOCK MOD â„¢ for Minecraft PC Edition - The Best Pocket Wiki & Mods Installer Tools : 4693.0
    GUNS MODS for Minecraft PC Edition - Mods Tools : 1497.0
    Guides for PokÃ©mon GO - Pokemon GO News and Cheats : 826.0
    WWDC : 762.0
    Horror Maps for Minecraft PE - Download The Scariest Maps for Minecraft Pocket Edition (MCPE) Free : 718.0
    VPN Express : 14.0
    Real Bike Traffic Rider Virtual Reality Glasses : 8.0
    Jishokun-Japanese English Dictionary & Translator : 0.0



```python
print('social app counts')
display_genre_dict(freeapple, 'Social Networking', appleheader, 'track_name', 'prime_genre', 'rating_count_tot')
```

    social app counts
    Facebook : 2974676.0
    Pinterest : 1061624.0
    Skype for iPhone : 373519.0
    Messenger : 351466.0
    Tumblr : 334293.0
    WhatsApp Messenger : 287589.0
    Kik : 260965.0
    ooVoo â€“ Free Video Call, Text and Voice : 177501.0
    TextNow - Unlimited Text + Calls : 164963.0
    Viber Messenger â€“ Text & Call : 164249.0
    Followers - Social Analytics For Instagram : 112778.0
    MeetMe - Chat and Meet New People : 97072.0
    We Heart It - Fashion, wallpapers, quotes, tattoos : 90414.0
    InsTrack for Instagram - Analytics Plus More : 85535.0
    Tango - Free Video Call, Voice and Chat : 75412.0
    LinkedIn : 71856.0
    Matchâ„¢ - #1 Dating App. : 60659.0
    Skype for iPad : 60163.0
    POF - Best Dating App for Conversations : 52642.0
    Timehop : 49510.0
    Find My Family, Friends & iPhone - Life360 Locator : 43877.0
    Whisper - Share, Express, Meet : 39819.0
    Hangouts : 36404.0
    LINE PLAY - Your Avatar World : 34677.0
    WeChat : 34584.0
    Badoo - Meet New People, Chat, Socialize. : 34428.0
    Followers + for Instagram - Follower Analytics : 28633.0
    GroupMe : 28260.0
    Marco Polo Video Walkie Talkie : 27662.0
    Miitomo : 23965.0
    SimSimi : 23530.0
    Grindr - Gay and same sex guys chat, meet and date : 23201.0
    Wishbone - Compare Anything : 20649.0
    imo video calls and chat : 18841.0
    After School - Funny Anonymous School News : 18482.0
    Quick Reposter - Repost, Regram and Reshare Photos : 17694.0
    Weibo HD : 16772.0
    Repost for Instagram : 15185.0
    Live.me â€“ Live Video Chat & Make Friends Nearby : 14724.0
    Nextdoor : 14402.0
    Followers Analytics for Instagram - InstaReport : 13914.0
    YouNow: Live Stream Video Chat : 12079.0
    FollowMeter for Instagram - Followers Tracking : 11976.0
    LINE : 11437.0
    eHarmonyâ„¢ Dating App - Meet Singles : 11124.0
    Discord - Chat for Gamers : 9152.0
    QQ : 9109.0
    Telegram Messenger : 7573.0
    Weibo : 7265.0
    Periscope - Live Video Streaming Around the World : 6062.0
    Chat for Whatsapp - iPad Version : 5060.0
    QQ HD : 5058.0
    Followers Analysis Tool For Instagram App Free : 4253.0
    live.ly - live video streaming : 4145.0
    Houseparty - Group Video Chat : 3991.0
    SOMA Messenger : 3232.0
    Monkey : 3060.0
    Down To Lunch : 2535.0
    Flinch - Video Chat Staring Contest : 2134.0
    Highrise - Your Avatar Community : 2011.0
    LOVOO - Dating Chat : 1985.0
    PlayStationÂ®Messages : 1918.0
    BOO! - Video chat camera with filters & stickers : 1805.0
    Qzone : 1649.0
    Chatous - Chat with new people : 1609.0
    Kiwi - Q&A : 1538.0
    GhostCodes - a discovery app for Snapchat : 1313.0
    Jodel : 1193.0
    FireChat : 1037.0
    Google Duo - simple video calling : 1033.0
    Fiesta by Tango - Chat & Meet New People : 885.0
    Google Allo â€” smart messaging : 862.0
    Peach â€” share vividly : 727.0
    Hey! VINA - Where Women Meet New Friends : 719.0
    Battlefieldâ„¢ Companion : 689.0
    All Devices for WhatsApp - Messenger for iPad : 682.0
    Chat for Pokemon Go - GoChat : 500.0
    IAmNaughty â€“ Dating App to Meet New People Online : 463.0
    Qzone HD : 458.0
    Zenly - Locate your friends in realtime : 427.0
    League of Legends Friends : 420.0
    è±†ç“£ : 407.0
    Candid - Speak Your Mind Freely : 398.0
    çŸ¥ä¹Ž : 397.0
    Selfeo : 366.0
    Fake-A-Location Free â„¢ : 354.0
    Popcorn Buzz - Free Group Calls : 281.0
    Fam â€” Group video calling for iMessage : 279.0
    QQ International : 274.0
    Ameba : 269.0
    SoundCloud Pulse: for creators : 240.0
    Tantan : 235.0
    Cougar Dating & Life Style App for Mature Women : 213.0
    Rawr Messenger - Dab your chat : 180.0
    WhenToPost: Best Time to Post Photos for Instagram : 158.0
    Inkeâ€”Broadcast an amazing life : 147.0
    Mustknow - anonymous video Q&A : 53.0
    CTFxCmoji : 39.0
    Lobi : 36.0
    Chain: Collaborate On MyVideo Story/Group Video : 35.0
    botman - Real time video chat : 7.0
    niconico ch : 0.0
    bit-tube - Live Stream Video Chat : 0.0
    MATCH ON LINE chat : 0.0
    LINE BLOG : 0.0
    BestieBox : 0.0


## Finding a recommendation for Google Play market
For Google Play, we will look at the number of installs per Category.


```python
print ('Freq table for google category: \n')
freqgooglecategory = freq_table(freegoogle, googleheader, 'Category')
display_table(freqgooglecategory)
```

    Freq table for google category: 
    
    FAMILY : 18.942133815551536
    GAME : 9.697106690777577
    TOOLS : 8.453887884267631
    BUSINESS : 4.599909584086799
    PRODUCTIVITY : 3.899186256781193
    LIFESTYLE : 3.887884267631103
    FINANCE : 3.7070524412296564
    MEDICAL : 3.5375226039783
    SPORTS : 3.390596745027125
    PERSONALIZATION : 3.322784810126582
    COMMUNICATION : 3.2323688969258586
    HEALTH_AND_FITNESS : 3.0854430379746836
    PHOTOGRAPHY : 2.949819168173599
    NEWS_AND_MAGAZINES : 2.802893309222423
    SOCIAL : 2.667269439421338
    TRAVEL_AND_LOCAL : 2.3395117540687163
    SHOPPING : 2.2490958408679926
    BOOKS_AND_REFERENCE : 2.1360759493670884
    DATING : 1.8648282097649187
    VIDEO_PLAYERS : 1.7970162748643763
    MAPS_AND_NAVIGATION : 1.3901446654611211
    FOOD_AND_DRINK : 1.2432188065099457
    EDUCATION : 1.164104882459313
    ENTERTAINMENT : 0.9606690777576853
    LIBRARIES_AND_DEMO : 0.9380650994575045
    AUTO_AND_VEHICLES : 0.9267631103074141
    HOUSE_AND_HOME : 0.8024412296564195
    WEATHER : 0.7911392405063291
    EVENTS : 0.7120253164556962
    PARENTING : 0.6555153707052441
    ART_AND_DESIGN : 0.6442133815551537
    COMICS : 0.6103074141048824
    BEAUTY : 0.599005424954792



```python
def avginstalls(dataset, header, categcolname, installscolname):
    freqtable = freq_table(dataset, header, categcolname)
    dictionary={}
    for category in freqtable:
        total = 0
        lencateg = 0
        categindex = header.index(categcolname)
        installsindex = header.index(installscolname)
        for app in dataset:           
            categapp = app[categindex]            
            if categapp==category:
                rawinstalls = app[installsindex]
                cleaninstalls=rawinstalls.replace('+', '')
                cleaninstalls=cleaninstalls.replace(',', '')
                installs = float(cleaninstalls)
                total+=installs
                lencateg+=1
        avginstalls=total/lencateg
        dictionary[category]=avginstalls
    return dictionary

googleavginstalls = avginstalls(freegoogle, googleheader, 'Category', 'Installs')
print('Avg number of installs per category: \n')
display_table(googleavginstalls)
```

    Avg number of installs per category: 
    
    COMMUNICATION : 38590581.08741259
    VIDEO_PLAYERS : 24727872.452830188
    SOCIAL : 23253652.127118643
    PHOTOGRAPHY : 17840110.40229885
    PRODUCTIVITY : 16787331.344927534
    GAME : 15544014.51048951
    TRAVEL_AND_LOCAL : 13984077.710144928
    ENTERTAINMENT : 11640705.88235294
    TOOLS : 10830251.970588235
    NEWS_AND_MAGAZINES : 9549178.467741935
    BOOKS_AND_REFERENCE : 8814199.78835979
    SHOPPING : 7036877.311557789
    PERSONALIZATION : 5201482.6122448975
    WEATHER : 5145550.285714285
    HEALTH_AND_FITNESS : 4188821.9853479853
    MAPS_AND_NAVIGATION : 4049274.6341463416
    FAMILY : 3695641.8198090694
    SPORTS : 3650602.276666667
    ART_AND_DESIGN : 1986335.0877192982
    FOOD_AND_DRINK : 1924897.7363636363
    EDUCATION : 1833495.145631068
    BUSINESS : 1712290.1474201474
    LIFESTYLE : 1446158.2238372094
    FINANCE : 1387692.475609756
    HOUSE_AND_HOME : 1360598.042253521
    DATING : 854028.8303030303
    COMICS : 832613.8888888889
    AUTO_AND_VEHICLES : 647317.8170731707
    LIBRARIES_AND_DEMO : 638503.734939759
    PARENTING : 542603.6206896552
    BEAUTY : 513151.88679245283
    EVENTS : 253542.22222222222
    MEDICAL : 120550.61980830671


## Google Play recommendation
The app category with the highest number of installs is Communication, and that is what I would recommend for the Google Play market. On the surface, there doesn't appear to be potential for much skewing of data in this case, and Communication is marginally different from another top category, Social.


```python
def display_categ_dict(dataset, categname, header, namecol, categcol, installscol):
    nameindex=header.index(namecol)
    categindex=header.index(categcol)
    installsindex=header.index(installscol)
    dictionary={}
    for app in dataset:        
        if app[categindex]==categname:
            name=app[nameindex]
            rawinstalls = app[installsindex]
            cleaninstalls=rawinstalls.replace('+', '')
            cleaninstalls=cleaninstalls.replace(',', '')
            installs = float(cleaninstalls)
            dictionary[name]=installs
    display_dictionary(dictionary)
```


```python
display_categ_dict(freegoogle, 'COMMUNICATION', googleheader, 'App', 'Category', 'Installs')
```

    WhatsApp Messenger : 1000000000.0
    Skype - free IM & video calls : 1000000000.0
    Messenger â€“ Text and Video Chat for Free : 1000000000.0
    Hangouts : 1000000000.0
    Google Chrome: Fast & Secure : 1000000000.0
    Gmail : 1000000000.0
    imo free video calls and chat : 500000000.0
    Viber Messenger : 500000000.0
    UC Browser - Fast Download Private & Secure : 500000000.0
    LINE: Free Calls & Messages : 500000000.0
    Google Duo - High Quality Video Calls : 500000000.0
    imo beta free calls and text : 100000000.0
    Yahoo Mail â€“ Stay Organized : 100000000.0
    Who : 100000000.0
    WeChat : 100000000.0
    UC Browser Mini -Tiny Fast Private & Secure : 100000000.0
    Truecaller: Caller ID, SMS spam blocking & Dialer : 100000000.0
    Telegram : 100000000.0
    Opera Mini - fast web browser : 100000000.0
    Opera Browser: Fast and Secure : 100000000.0
    Messenger Lite: Free Calls & Messages : 100000000.0
    Kik : 100000000.0
    KakaoTalk: Free Calls & Text : 100000000.0
    GO SMS Pro - Messenger, Free Themes, Emoji : 100000000.0
    Firefox Browser fast & private : 100000000.0
    BBM - Free Calls & Messages : 100000000.0
    Android Messages : 100000000.0
    free video calls and chat : 50000000.0
    Zalo â€“ Video Call : 50000000.0
    Mail.Ru - Email App : 50000000.0
    Dolphin Browser - Fast, Private & AdblockðŸ¬ : 50000000.0
    Contacts : 50000000.0
    CM Browser - Ad Blocker , Fast Download , Privacy : 50000000.0
    Azar : 50000000.0
    myMail â€“ Email for Hotmail, Gmail and Outlook Mail : 10000000.0
    chomp SMS : 10000000.0
    ZenUI Dialer & Contacts : 10000000.0
    Xperia Linkâ„¢ : 10000000.0
    Whoscall - Caller ID & Block : 10000000.0
    WhatsCall Free Global Phone Call App & Cheap Calls : 10000000.0
    WhatsApp Business : 10000000.0
    WEB.DE Mail : 10000000.0
    Voxer Walkie Talkie Messenger : 10000000.0
    TouchPal Keyboard - Fun Emoji & Android Keyboard : 10000000.0
    Text SMS : 10000000.0
    Talkray - Free Calls & Texts : 10000000.0
    Talkatone: Free Texts, Calls & Phone Number : 10000000.0
    Puffin Web Browser : 10000000.0
    Psiphon Pro - The Internet Freedom VPN : 10000000.0
    Portable Wi-Fi hotspot : 10000000.0
    Orfox: Tor Browser for Android : 10000000.0
    Opera Mini browser beta : 10000000.0
    Omlet Chat : 10000000.0
    Mr. Number-Block calls & spam : 10000000.0
    Messenger for SMS : 10000000.0
    MegaFon Dashboard : 10000000.0
    ICQ â€” Video Calls & Chat Messenger : 10000000.0
    Hiya - Caller ID & Block : 10000000.0
    Hangouts Dialer - Call Phones : 10000000.0
    GroupMe : 10000000.0
    Google Voice : 10000000.0
    Google Allo : 10000000.0
    Glide - Video Chat Messenger : 10000000.0
    GO Notifier : 10000000.0
    GMX Mail : 10000000.0
    Free WiFi Connect : 10000000.0
    Free Adblocker Browser - Adblock & Popup Blocker : 10000000.0
    ExDialer - Dialer & Contacts : 10000000.0
    Discord - Chat for Gamers : 10000000.0
    DU Browserâ€”Browse fast & fun : 10000000.0
    Cricket Visual Voicemail : 10000000.0
    Contacts+ : 10000000.0
    Calls Blacklist - Call Blocker : 10000000.0
    CallApp: Caller ID, Blocker & Phone Call Recorder : 10000000.0
    Browser 4G : 10000000.0
    Adblock Browser for Android : 10000000.0
    AT&T Visual Voicemail : 10000000.0
    Your Freedom VPN Client : 5000000.0
    Web Browser & Explorer : 5000000.0
    Sync.ME â€“ Caller ID & Block : 5000000.0
    Skype Lite - Free Video Call & Chat : 5000000.0
    My Vodacom SA : 5000000.0
    My Tele2 : 5000000.0
    Microsoft Edge : 5000000.0
    K-9 Mail : 5000000.0
    JusTalk - Free Video Calls and Fun Video Chat : 5000000.0
    Full Screen Caller ID : 5000000.0
    Ear Agent: Super Hearing : 5000000.0
    Daum Mail - Next Mail : 5000000.0
    Chrome Dev : 5000000.0
    Calls & Text by Mo+ : 5000000.0
    Caller ID & Call Block - DU Caller : 5000000.0
    Call Free â€“ Free Call : 5000000.0
    Call Control - Call Blocker : 5000000.0
    CM Transfer - Share any files with friends nearby : 5000000.0
    CIA - Caller ID & Call Blocker : 5000000.0
    Brave Browser: Fast AdBlocker : 5000000.0
    Bluetooth Auto Connect : 5000000.0
    AT&T Call Protect : 5000000.0
    mysms SMS Text Messaging Sync : 1000000.0
    mail.com mail : 1000000.0
    Wi-Fi Auto-connect : 1000000.0
    Web Browser for Android : 1000000.0
    WeFi - Free Fast WiFi Connect & Find Wi-Fi Map : 1000000.0
    Vonage MobileÂ® Call Video Text : 1000000.0
    Virtual Walkie Talkie : 1000000.0
    Video Caller Id : 1000000.0
    True Contact - Real Caller ID : 1000000.0
    TracFone My Account : 1000000.0
    Tiny Call Confirm : 1000000.0
    Should I Answer? : 1000000.0
    Seznam.cz : 1000000.0
    Safest Call Blocker : 1000000.0
    SW-100.tch by Callstel : 1000000.0
    RocketDial Dialer & Contacts : 1000000.0
    PHONE for Google Voice & GTalk : 1000000.0
    Ninesky Browser : 1000000.0
    Newton Mail - Email App for Gmail, Outlook, IMAP : 1000000.0
    My magenta : 1000000.0
    My Vodafone (GR) : 1000000.0
    Messaging+ SMS, MMS Free : 1000000.0
    Lite for Facebook Messenger : 1000000.0
    InBrowser - Incognito Browsing : 1000000.0
    Ghostery Privacy Browser : 1000000.0
    Firefox Focus: The privacy browser : 1000000.0
    Email TypeApp - Mail App : 1000000.0
    DW Contacts & Phone & Dialer : 1000000.0
    ClanPlay: Community and Tools for Gamers : 1000000.0
    Caller ID + : 1000000.0
    Call Blocker - Blacklist, SMS Blocker : 1000000.0
    CB Radio Chat - for friends! : 1000000.0
    Burner - Free Phone Number : 1000000.0
    BBMoji - Your personalized BBM Stickers : 1000000.0
    AntennaPict Î² : 1000000.0
    All Email Providers : 1000000.0
    Adblock Plus for Samsung Internet - Browse safe. : 1000000.0
    AW - free video calls and chat : 1000000.0
    AT&T Messages for Tablet : 1000000.0
    2ndLine - Second Phone Number : 1000000.0
    Web Browser : 500000.0
    U - Webinars, Meetings & Messenger : 500000.0
    TownWiFi | Wi-Fi Everywhere : 500000.0
    Talkie - Wi-Fi Calling, Chats, File Sharing : 500000.0
    SolMail - All-in-One email app : 500000.0
    LokLok: Draw on a Lock Screen : 500000.0
    Lightning Web Browser : 500000.0
    FreedomPop Messaging Phone/SIM : 500000.0
    BD Data Plan (3G & 4G) : 500000.0
    WiFi Access Point (hotspot) : 100000.0
    T-Mobile DIGITS : 100000.0
    QRZ Assistant : 100000.0
    Portable Wi-Fi hotspot Free : 100000.0
    PlacarTv Futebol Ao Vivo : 100000.0
    Morse Code Reader : 100000.0
    M star Dialer : 100000.0
    K-@ Mail - Email App : 100000.0
    Goodbox - Mega App : 100000.0
    Everbridge : 100000.0
    Channel 19 : 100000.0
    CB On Mobile : 100000.0
    Baby Monitor AV : 100000.0
    BT MeetMe with Dolby Voice : 100000.0
    Antillean Gold Telegram (original version) : 100000.0
    AZ Browser. Private & Download : 100000.0
    X Browser : 50000.0
    N-Com Wizard : 50000.0
    My BF App : 50000.0
    IZ2UUF Morse Koch CW : 50000.0
    HipChat - beta version : 50000.0
    Free Wi-fi HotspoT : 50000.0
    BT Messenger : 50000.0
    BD Internet Packages (Updated) : 50000.0
    AudioBT: BT audio GPS/SMS/Text : 50000.0
    3G DZ Configuration : 50000.0
    m:go BiH : 10000.0
    [verify-U] VideoIdent : 10000.0
    Ring : 10000.0
    Pocket Prefix Plus : 10000.0
    Mail1Click - Secure Mail : 10000.0
    Jazz Wi-Fi : 10000.0
    Inbox.eu : 10000.0
    Ham Radio Prefixes : 10000.0
    Feel Performer : 10000.0
    Eg Call : 10000.0
    EZ Wifi Notification : 10000.0
    Deaf World DW : 10000.0
    DMR BrandMeister Tool : 10000.0
    ClanHQ : 10000.0
    BT One Phone Mobile App : 10000.0
    BF Browser by Betfilter - Stop Gambling Today! : 10000.0
    BD Dialer : 10000.0
    Ad Blocker Turbo - Adblocker Browser : 10000.0
    Access Point Names : 10000.0
    /u/app : 10000.0
    retteMi.ch : 5000.0
    mail.co.uk Mail : 5000.0
    love sms good morning : 5000.0
    Sat-Fi : 5000.0
    Mircules DX Cluster Lite : 5000.0
    Learn Morse Code - G0HYN Learn Morse : 5000.0
    K-9 Material (unofficial) : 5000.0
    Ham DX Cluster & Spots Finder : 5000.0
    DM for WhatsApp : 5000.0
    DM Talk New : 5000.0
    Council Voting Calculator : 5000.0
    CS Browser Beta : 5000.0
    BT One Voice mobile access : 5000.0
    BD Live Call : 5000.0
    AK Phone : 5000.0
    AG Contacts, Lite edition : 5000.0
    cluster.dk : 1000.0
    Sat-Fi Voice : 1000.0
    SMS Sender - sluzba.cz : 1000.0
    ReadyOp DT : 1000.0
    FO AIRBUS TLSE : 1000.0
    FC Browser - Focus Privacy Browser : 1000.0
    EU Council : 1000.0
    DM Tracker : 1000.0
    Call Blocker & Blacklist : 1000.0
    CS Customizer : 1000.0
    CS Browser | #1 & BEST BROWSER : 1000.0
    CQ-Mobile : 1000.0
    BlueDV AMBE : 1000.0
    BQ Partners : 1000.0
    BN MALLORCA Radio : 1000.0
    BK Chat : 1000.0
    BH Mail : 1000.0
    AV Phone : 1000.0
    AU Call Blocker - Block Unwanted Calls Texts 2018 : 1000.0
    Traffic signs BD : 500.0
    RÃ¡dio Sol Nascente DF : 500.0
    Have your say on Europe : 500.0
    ES-1 : 500.0
    CW BLE Peripheral Simulator : 500.0
    CQ-Alert : 500.0
    Best Auto Call Recorder Free : 500.0
    ATC Unico BS : 500.0
    tournaments and more.aj.2 : 100.0
    chat dz : 100.0
    [EF]ShoutBox : 100.0
    Programi podrÅ¡ke EU : 100.0
    MARKET FO : 100.0
    Katalogen.ax : 100.0
    FP Connect : 100.0
    FO STELIA MÃ©aulte : 100.0
    FO SODEXO : 100.0
    FO RCBT : 100.0
    FO PSA Sept-Fons : 100.0
    FO OP St-Nazaire : 100.0
    FO Interim : 100.0
    FO AIRBUS Nantes : 100.0
    EP RSS Reader : 100.0
    EHiN-FH conferenceapp : 100.0
    DG Card : 100.0
    Cy Messenger : 100.0
    Carpooling FH Hagenberg : 100.0
    CW Bluetooth SPP : 100.0
    CJ DVD Rentals : 100.0
    CJ Browser - Fast & Private : 100.0
    CF Chat: Connecting Friends : 100.0
    C W Browser : 100.0
    Bee'ah Employee App : 100.0
    BV : 100.0
    Amadeus GR & CY : 100.0
    Aj.Petra : 100.0
    Hyundai CX Conference : 50.0
    DK TEL Dialer : 50.0
    Cb browser : 50.0
    BS-Mobile : 50.0
    AC-BL : 50.0
    ei : 10.0
    Oklahoma Ag Co-op Council : 10.0
    FP Live : 10.0
    FNH Payment Info : 10.0
    FN Web Radio : 10.0
    Ek IRA : 10.0
    EO Mumbai : 10.0
    EJ messenger : 10.0
    DM - The Offical Messaging App : 10.0
    DK Browser : 10.0
    CK Call NEW : 10.0
    Best Browser BD social networking : 10.0
    BJ - Confidential : 10.0
    Test Server SMS FA : 5.0
    Of the wall Arapaho bk : 5.0
    BA SALES : 1.0



```python
display_categ_dict(freegoogle, 'VIDEO_PLAYERS', googleheader, 'App', 'Category', 'Installs')
```

    YouTube : 1000000000.0
    Google Play Movies & TV : 1000000000.0
    MX Player : 500000000.0
    VivaVideo - Video Editor & Photo Movie : 100000000.0
    VideoShow-Video Editor, Video Maker, Beauty Camera : 100000000.0
    VLC for Android : 100000000.0
    Motorola Gallery : 100000000.0
    Motorola FM Radio : 100000000.0
    Dubsmash : 100000000.0
    Vote for : 50000000.0
    Vigo Video : 50000000.0
    VMate : 50000000.0
    Samsung Video Library : 50000000.0
    Ringdroid : 50000000.0
    MiniMovie - Free Video and Slideshow Editor : 50000000.0
    LIKE â€“ Magic Video Maker & Community : 50000000.0
    KineMaster â€“ Pro Video Editor : 50000000.0
    HD Video Downloader : 2018 Best video mate : 50000000.0
    DU Recorder â€“ Screen Recorder, Video Editor, Live : 50000000.0
    video player for android : 10000000.0
    iMediaShare â€“ Photos & Music : 10000000.0
    YouTube Studio : 10000000.0
    Video Player All Format : 10000000.0
    Video Downloader - for Instagram Repost App : 10000000.0
    Video Downloader : 10000000.0
    Ustream : 10000000.0
    Quik â€“ Free Video Editor for photos, clips, music : 10000000.0
    PowerDirector Video Editor App: 4K, Slow Mo & More : 10000000.0
    Omlet Arcade - Stream, Meet, Play : 10000000.0
    Naruto Shippuden - Watch Free! : 10000000.0
    Music - Mp3 Player : 10000000.0
    Mobizen Screen Recorder for SAMSUNG : 10000000.0
    Magisto Video Editor & Maker : 10000000.0
    Inst Download - Video & Photo : 10000000.0
    HTC Service ï¼ DLNA : 10000000.0
    HTC Gallery : 10000000.0
    FrostWire: Torrent Downloader & Music Player : 10000000.0
    FilmoraGo - Free Video Editor : 10000000.0
    Code : 10000000.0
    Cartoon Network App : 10000000.0
    BitTorrentÂ®- Torrent Downloads : 10000000.0
    BSPlayer FREE : 10000000.0
    All Video Downloader : 10000000.0
    AfreecaTV : 10000000.0
    AZ Screen Recorder - No Root : 10000000.0
    YouCut - Video Editor & Video Maker, No Watermark : 5000000.0
    WiFi Baby Monitor - NannyCam : 5000000.0
    Video Editor : 5000000.0
    HTC Serviceâ€”Video Player : 5000000.0
    Droid Zap by Motorola : 5000000.0
    Adobe Premiere Clip : 5000000.0
    ActionDirector Video Editor - Edit Videos Fast : 5000000.0
    video player : 1000000.0
    iSmart DV : 1000000.0
    iPlayIT for YouTube VR Player : 1000000.0
    XX HD Video downloader-Free Video Downloader : 1000000.0
    Vuze Torrent Downloader : 1000000.0
    Video.Guru - Video Maker : 1000000.0
    Video Status : 1000000.0
    Video Editor,Crop Video,Movie Video,Music,Effects : 1000000.0
    VidPlay : 1000000.0
    VUE: video editor & camcorder : 1000000.0
    VPlayer : 1000000.0
    Tencent Video - Supporting the whole network : 1000000.0
    SVT Play : 1000000.0
    Play Tube : 1000000.0
    OnePlus Gallery : 1000000.0
    OBJECTIVE : 1000000.0
    Multiple Videos at Same Time : 1000000.0
    Mobizen Screen Recorder for LG - Record, Capture : 1000000.0
    Iqiyi (for tablet) : 1000000.0
    HD Video Player : 1000000.0
    HD Video Download for Facebook : 1000000.0
    HD Movie Video Player : 1000000.0
    G Guide Program Guide (SOFTBANK EMOBILE WILLCOM version) : 1000000.0
    Funny videos for whatsapp : 1000000.0
    EZCast â€“ Cast Media to TV : 1000000.0
    DU Privacy-hide appsã€smsã€file : 1000000.0
    DS video : 1000000.0
    DS photo : 1000000.0
    BluTV : 1000000.0
    BSPlayer ARMv7 VFP CPU support : 1000000.0
    AndStream - Streaming Download : 1000000.0
    All Video Downloader 2018 : 1000000.0
    AX Player -Nougat Video Player : 1000000.0
    Video Player All Format for Android : 500000.0
    GoPlus Cam : 500000.0
    DR TV : 500000.0
    CJ VLC HD Remote (+ Stream) : 500000.0
    amazer - Global Kpop Video Community : 100000.0
    Video Downloader for FB : Video Download with Link : 100000.0
    Sketch 'n' go : 100000.0
    Nero AirBurn : 100000.0
    GoAction : 100000.0
    Free TV series : 100000.0
    Ez Screen Recorder (no ad) : 100000.0
    EZ Web Video Cast | Chromecast : 100000.0
    ES Audio Player ( Shortcut ) : 100000.0
    BGCN TV : 100000.0
    AW Screen Recorder No Root : 100000.0
    AB Repeat Player : 100000.0
    dv Prompter : 50000.0
    bgtime.tv : 50000.0
    ES-IPTV : 50000.0
    BR Series : 50000.0
    AX Video Player : 50000.0
    ACTIVEON CX & CX GOLD : 50000.0
    ek tuhi : 10000.0
    W Box VMS : 10000.0
    MelifeCam-M : 10000.0
    HD VideoDownlaoder For Fb : XXVideo Downloader : 10000.0
    HD Video Player (wmv,avi,mp4,flv,av,mpg,mkv)2017 : 10000.0
    EZ-SEE : 10000.0
    EZ Usenet for EasynewsÂ® : 10000.0
    EZ TV Player : 10000.0
    EML UPnP-AV Control Point : 10000.0
    Downvids Helper - One touch DW : 10000.0
    DG Video Editor : 10000.0
    DG UPnP Player Free : 10000.0
    Casper Ssinema : 10000.0
    BS player remote : 10000.0
    BK News Channel : 10000.0
    W Box VMS HD : 5000.0
    Videos downloader for Facebook:fast fb video saver : 5000.0
    Q-See Plus : 5000.0
    M-Sight Pro : 5000.0
    HD Video Player - Video & MP3 Player | AV Player | : 5000.0
    Furrion ES Control : 5000.0
    EF Sidekick : 5000.0
    DZ Popup Video Player : 5000.0
    DV Lottery Photo : 5000.0
    BR Video Player : 5000.0
    BG video - floating video - background video : 5000.0
    Ay : 5000.0
    A-B repeater : 5000.0
    4K VIDEO PLAYER ULTRA HD : 5000.0
    Music for Youtube - Tube Music BG, Red+ : 1000.0
    Movie Downloader Torrent : Az Torrent : 1000.0
    EZ game screen recorder with audio 1080P : 1000.0
    CINE BR : 1000.0
    BZ Langenthaler Tagblatt : 1000.0
    BC iptv player : 1000.0
    Ay Sabz Gunbad Waly : 1000.0
    AV-IPTV : 1000.0
    YourTube Video Views BG : 500.0
    Video Wallpaper Show : 500.0
    DG Screen Recorder : 500.0
    CX Monthly Tech News : 500.0
    CJ Camcorder : 500.0
    A-Z Screen Recorder - : 500.0
    List iptv FR : 100.0
    EC MANAGER : 100.0
    Bx-WiFi-GI : 100.0
    Bc Vod : 100.0
    BG MUSIC PLAYER - MUSIC PLAYER : 100.0
    AK Lodi Films : 100.0
    AJ Player : 100.0
    CI Stream : 10.0
    Art of F J Taylor : 10.0



```python
display_categ_dict(freegoogle, 'SOCIAL', googleheader, 'App', 'Category', 'Installs')
```

    Instagram : 1000000000.0
    Google+ : 1000000000.0
    Facebook : 1000000000.0
    Snapchat : 500000000.0
    Facebook Lite : 500000000.0
    VK : 100000000.0
    Tumblr : 100000000.0
    Tik Tok - including musical.ly : 100000000.0
    Tango - Live Video Broadcast : 100000000.0
    Pinterest : 100000000.0
    LinkedIn : 100000000.0
    Badoo - Free Chat & Dating App : 100000000.0
    BIGO LIVE - Live Stream : 100000000.0
    ooVoo Video Calls, Messaging & Stories : 50000000.0
    Zello PTT Walkie Talkie : 50000000.0
    SKOUT - Meet, Chat, Go Live : 50000000.0
    POF Free Dating App : 50000000.0
    MeetMe: Chat & Meet New People : 50000000.0
    textPlus: Free Text & Calls : 10000000.0
    magicApp Calling & Messaging : 10000000.0
    YouNow: Live Stream Video Chat : 10000000.0
    We Heart It : 10000000.0
    Waplog - Free Chat, Dating App, Meet Singles : 10000000.0
    TextNow - free text + calls : 10000000.0
    Text free - Free Text + Call : 10000000.0
    Text Me: Text Free, Call Free, Second Phone Number : 10000000.0
    Tapatalk - 100,000+ Forums : 10000000.0
    Tagged - Meet, Chat & Dating : 10000000.0
    SayHi Chat, Meet New People : 10000000.0
    Quora : 10000000.0
    Phone Tracker : Family Locator : 10000000.0
    Periscope - Live Video : 10000000.0
    Path : 10000000.0
    Mico- Stranger Chat Random video Chat, Live, Meet : 10000000.0
    Messenger Messenger : 10000000.0
    Messenger : 10000000.0
    Messages, Text and Video Chat for Messenger : 10000000.0
    LiveMe - Video chat, new friends, and make money : 10000000.0
    Legend - Animate Text in Video : 10000000.0
    LOVOO : 10000000.0
    Kate Mobile for VK : 10000000.0
    Jaumo Dating, Flirt & Live Video : 10000000.0
    HTC Social Plugin - Facebook : 10000000.0
    Grindr - Gay chat : 10000000.0
    Free phone calls, free texting SMS on free number : 10000000.0
    Find My Friends : 10000000.0
    Dating App, Flirt & Chat : W-Match : 10000000.0
    Amino: Communities and Chats : 10000000.0
    Who Viewed My Facebook Profile - Stalkers Visitors : 5000000.0
    Whisper : 5000000.0
    Web Browser & Fast Explorer : 5000000.0
    VidStatus app - Status Videos & Status Downloader : 5000000.0
    Timehop : 5000000.0
    Text Free: WiFi Calling App : 5000000.0
    Telegram X : 5000000.0
    SPARK - Live random video chat & meet new people : 5000000.0
    Nextdoor - Local neighborhood news & classifieds : 5000000.0
    Meetup : 5000000.0
    Meet â€“ Talk to Strangers Using Random Video Chat : 5000000.0
    Instachat ðŸ˜œ : 5000000.0
    Hornet - Gay Social Network : 5000000.0
    Hide Something - Photo, Video : 5000000.0
    HOLLA Live: Meet New People via Random Video Chat : 5000000.0
    FunForMobile Ringtones & Chat : 5000000.0
    Frim: get new friends on local chat rooms : 5000000.0
    Fame Boom for Real Followers, Likes : 5000000.0
    Blogger : 5000000.0
    ðŸ’˜ WhatsLov: Smileys of love, stickers and GIF : 1000000.0
    pixiv : 1000000.0
    Wishbone - Compare Anything : 1000000.0
    VMate Lite - Funny Short Videos Social Network : 1000000.0
    U LIVE â€“ Video Chat & Stream : 1000000.0
    TwitCasting Live : 1000000.0
    The Messenger App : 1000000.0
    Stickers for Facebook : 1000000.0
    Snaappy â€“ 3D fun AR core communication platform : 1000000.0
    Moment : 1000000.0
    MobilePatrol Public Safety App : 1000000.0
    Messenger Pro : 1000000.0
    Love Sticker : 1000000.0
    Love Images : 1000000.0
    Lesbian Chat & Dating - SPICY : 1000000.0
    Jodel - The Hyperlocal App : 1000000.0
    GUYZ - Gay Chat & Gay Dating : 1000000.0
    Frontback - Social Photos : 1000000.0
    Friendly for Facebook : 1000000.0
    Free Messages, Video, Chat,Text for Messenger Plus : 1000000.0
    FollowMeter for Instagram : 1000000.0
    Fiesta by Tango - Find, Meet and Make New Friends : 1000000.0
    Faster for Facebook Lite : 1000000.0
    Family GPS tracker KidControl + GPS by SMS Locator : 1000000.0
    Facebook Local : 1000000.0
    Facebook Creator : 1000000.0
    EZ Video Download for Facebook : 1000000.0
    Couple - Relationship App : 1000000.0
    Banjo : 1000000.0
    BOO! - Next Generation Messenger : 1000000.0
    B-Messenger Video Chat : 1000000.0
    All Social Networks : 1000000.0
    +Download 4 Instagram Twitter : 1000000.0
    Web Browser ( Fast & Secure Web Explorer) : 500000.0
    Verdad o Reto : 500000.0
    Swift for Facebook Lite : 500000.0
    Stream - Live Video Community : 500000.0
    Qeek for Instagram - Zoom profile insta DP : 500000.0
    Puffin for Facebook : 500000.0
    Profile Tracker - Who Viewed My Facebook Profile : 500000.0
    Pink Color for Facebook : 500000.0
    Mirrativ: Live Stream Any App : 500000.0
    Greeting Cards & Wishes : 500000.0
    Gayvox - Gay Lesbian Bi Dating : 500000.0
    Fake Chat (Direct Message) : 500000.0
    Daddyhunt: Gay Dating : 500000.0
    Bloglovin' : 500000.0
    uCiC- Videos and Photos on demand : 100000.0
    YAY - TBH : 100000.0
    What U See : 100000.0
    The Video Messenger App : 100000.0
    Social network all in one 2018 : 100000.0
    See U - Random video chat, video chat : 100000.0
    Phoenix - Facebook & Messenger : 100000.0
    Patook - make platonic friends : 100000.0
    Meet U - Get Friends for Snapchat, Kik & Instagram : 100000.0
    MB Notifications for FB (Free) : 100000.0
    KPOP Amino for K-Pop Entertainment : 100000.0
    KDRAMA Amino for K-Drama Fans : 100000.0
    FutureNet your social app : 100000.0
    Fr Daoud Lamei : 100000.0
    Faster Social for Facebook : 100000.0
    Dr. B.R.Ambedkar : 100000.0
    Dr B R Ambedkar (Jai Bhim) : 100000.0
    Dating.dk : 100000.0
    DP and Status for WhatsApp 2018 : 100000.0
    Chat For Strangers - Video Chat : 100000.0
    Blogaway for Android (Blogger) : 100000.0
    Undertale AU Amino : 50000.0
    Rande.cz : 50000.0
    Hashtags For Likes.co : 50000.0
    Golden telegram : 50000.0
    FCB Connect - FC Barcelona : 50000.0
    Equestria Amino for MLP : 50000.0
    EXO-L Amino for EXO Fans : 50000.0
    CP Dialer : 50000.0
    BT Dating -Find your match, help cupid, be social : 50000.0
    Anime et Manga Amino en FranÃ§ais : 50000.0
    Unlimited Group Links - Whatsapp, FB, Telegram : 10000.0
    U-Report : 10000.0
    Stickers for Imo, fb, whatsapp : 10000.0
    Share G - Images Sharing - Wallpapers App : 10000.0
    Mini for Facebook lite : 10000.0
    Mali J : 10000.0
    Lite Messenger for Facebook Lite : 10000.0
    Jamaa Amino for Animal Jam : 10000.0
    Ek Maratha : 10000.0
    Eddsworld Amino : 10000.0
    Digi-TV.ch : 10000.0
    Daily Murli Saar Widget : 10000.0
    DM Me - Chat : 10000.0
    Cyprus Police : 10000.0
    Best DP and Status : 10000.0
    BT Communicator : 10000.0
    BK Traffic Control cum Chart : 10000.0
    Au Pair : 10000.0
    funny Image Comments for FB : 5000.0
    TNEB Bill Online Payment (Tamil) : 5000.0
    TN e Sevai TN EB Bill Patta Citta EC Birth All Hub : 5000.0
    Profile Pictures and DP for Whatsapp : 5000.0
    Instant DP Downloader for Instagram : 5000.0
    Dp for Facebook : 5000.0
    Dp For Whatsapp : 5000.0
    DP Display Pictures Life Quotes Motivational GM : 5000.0
    DM for IG ðŸ˜˜ - Image & Video Saver for Instagram : 5000.0
    DB Event App : 5000.0
    Check Your Visitors on FB ? : 5000.0
    signÃ¡ly.cz : 1000.0
    eChallan Andhra Pradesh (AP) : 1000.0
    Zdravei.BG : 1000.0
    V Bucks ProTips New : 1000.0
    TN EC Online New : 1000.0
    Students.ch : 1000.0
    Sabka Malik Ek Sai : 1000.0
    Noticias DF : 1000.0
    Media Sosial TNI AU : 1000.0
    Join R, Community Engagement : 1000.0
    H letter images : 1000.0
    European Solidarity Corps : 1000.0
    DW Streaming : 1000.0
    DC Comics Amino : 1000.0
    CG Districts : 1000.0
    Black Social : 1000.0
    BR Chat Bot : 1000.0
    BGKontakti Vienna BG Kontakti : 1000.0
    BGKontakti Bayern BG Kontakti : 1000.0
    BG LINKED (BGLINKED) : 1000.0
    Auto DM for Twitter ðŸ”¥ : 1000.0
    Alarm.fo â€“ choose your info : 1000.0
    iCard BD Plus : 500.0
    Downloader plus for FB : 500.0
    DK Murali : 500.0
    DF BugMeNot : 500.0
    Br Browser : 500.0
    BGKontakti London BG Kontakti : 500.0
    i-share AF/KLM (AFKL ishare) : 100.0
    TN Patta /Chitta /EC New : 100.0
    Rejoin Your Ex : 100.0
    Naruto & Boruto FR : 100.0
    Myjob@BM : 100.0
    Movement BE : 100.0
    Message AI - Write Better Messages (Free) : 100.0
    GirlTalk.dk : 100.0
    Frases Cristianas de Esperanza y Fe : 100.0
    Evasion.bz : 100.0
    Eternal Light AG : 100.0
    DiscÃ­pulos em BH : 100.0
    DV Statistics : 100.0
    DM Storage (for twitter) : 100.0
    CJ Gospel Hour : 100.0
    Alumni BJ : 100.0
    UP EB Bill Payment & Details : 50.0
    FB Advanced Search : 50.0
    EG Way Life : 50.0
    Coupe AdhÃ©mar EY 2017 : 50.0
    quran-DZ : 10.0
    bm-Events : 10.0
    Reisedealz.eu : 10.0
    Otto DM : 10.0
    News Dz : 10.0
    Hum Ek Hain 2.02 : 10.0
    EO RAIPUR : 10.0
    DN Blog : 10.0
    BA 3 Banjarmasin : 10.0
    CB Heroes : 5.0
    C.P. CERVANTES (TOBARRA) : 5.0
    BH Connect : 1.0
    Amleen Ey : 1.0
    Pekalongan CJ : 0.0

