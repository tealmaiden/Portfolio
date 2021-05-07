
input("Press Enter to continue. Enter answers when prompted...")

name=input('What is your name? ')

input('You are out in a field scanning for 4 leaf clovers.')
input('You see a bunny in the distance wearing a bowtie carrying an empty basket.')
input('Clearly it\'s the Easter Bunny hiding eggs for Easter!')
input('''You go up excitedly. "Hello, my name is '''+ name+ '''. Would you tell me
    where I can find some Easter eggs?"''')
input('''Like most bunnies, he scurries away as you approach, and like
    most people, you pointlessly chase after him.''')
input('''You reach into a patch of toadstools he escaped into and eventually
    feel something like a shoe.''')
input('"Oof, waaat ye chucker dat for?! Gie it back wud yer?"')
input('"What."')
input('It\'s not the small creature you were expecting, but perhaps one equally elusive.')


repeat=True
while repeat==True:
    ans=input('Give the leprechaun back his shoe? (y/n) ')
    if ans.lower()=='y':
        input('"Here\'s your shoe. Can you give me some gold in return?"')
        input('"I\'m a wee broke roi nigh... Dat hare owes me nicker. And \'e\'s a wee shy."')
        input('"But oi can \'elp yer fend an Easter egg fer each riddle yer answer correctly."')
        repeat=False
    elif ans.lower()=='n':
        input('"I\'ll give you your shoe if you take me to your pot of gold."')
        input('"I\'m a wee broke roi nigh... Dat hare owes me nicker. And \'e\'s a wee shy."')
        input('"But oi can \'elp yer fend an Easter egg fer each riddle yer answer correctly."')
        repeat=False
    else:
        print('try again')
        repeat=True #[loop through the conditional]
        

repeat=True
while repeat==True:
    ans2=input('Answer the riddles? (y/n) ')
    if ans2.lower()=='y':
        input('"Sure, I\'m pretty good at riddles."')
        repeat=False
    elif ans2.lower()=='n':
        input('"I think I\'ll keep your shoe."')
        input('"Oi\m a leprechaun. Oi tink Oi can make another shoe."')
    else:
        print('try again') #[loop through the conditional]

riddles=0

repeat=True
while repeat==True:
    ans3=input('''"Where does de Easter Bunny go ter ayte breakfast?
    Tis a restaurant." (enter answer) ''')
    if ans3.lower()=='ihop' or ans3.lower()=='the ihop':
        input('"Dat\'s roiii! Let\'s go dere."')
        riddles+=1
        print('"Yer answered', riddles, 'net riddles and \'av', riddles, 'future eggs."')
        input()
        repeat=False
    elif ans3==(''):
        input('"Waaat? Didn\'t catch dat." (press enter to try again)')
        repeat=True
    else:
        input('"Naw, google it."') #[loop through the conditional]
        riddles-=1
        print('"Yer answered', riddles, 'net riddles. Yer lost an egg."')
        input()
        repeat=True
        
input('''At the IHOP, your new friend, O\'Doodles, asks you to order for him.
    This is what he tells you to order...''')

repeat=True
while repeat==True:
    ans4=input('''"A white chamber whar golden treasures \'ide. You must break in ter git inside."
    What do you order O\'Doodles? (enter answer) ''')
    if ans4.lower()=='egg' or ans4.lower()=='eggs' or ans4.lower()=='an egg':
        input('"Aayyye!!! Gran\' job. Let\'s ayte."')
        riddles+=1
        print('"Yer answered', riddles, 'net riddles and \'av', riddles, 'future eggs."')
        input()
        repeat=False
    elif 'scrambled' in ans4.lower() or 'hardboiled' in ans4.lower() or 'sunny' in ans4.lower() \
         or 'poached' in ans4.lower() or 'mcmuffin' in ans4.lower() or 'easter' in ans4.lower() \
         or 'yolk' in ans4.lower():
        input('"Aye, close. Troi again." (press enter)')
        repeat=True
    elif ans4==(''):
        input('"Waaat? Didn\'t catch dat." (press enter to try again)')
        repeat=True
    else:
        input('"Naw, troi again." (press enter)') #[loop through the conditional]
        riddles-=1
        print('"Yer answered', riddles, 'net riddles. Yer lost an egg."')
        input()
        repeat=True

input('You both agree you had a hearty meal and perhaps a few too many pancakes.')
input('''To aid digestion, you set out to the park to roll down some hills.
    On the way there, O\'Doodles gives you a third riddle...''')
      
repeat=True
while repeat==True:
    ans5=input('''"Oi'm eaten by bunny an' make a gran' 'onney.
    I grow al' over because Oi am a ..." (enter answer) ''')
    if ans5.lower()=='clover':
        input('"Gran\' so yer did it!"')
        riddles+=1
        print('"Yer answered', riddles, 'net riddles and \'av', riddles, 'future eggs."')
        input()
        repeat=False
    elif ans5==(''):
        input('"Waaat? Didn\'t catch dat." (press enter to try again)')
        repeat=True
    else:
        input('"Naw, troi again." (press enter)') #[loop through the conditional]
        riddles-=1
        print('"Yer answered', riddles, 'net riddles. Yer lost an egg."')
        input()
        repeat=True

input('''After all that rolling in the grass, your hair could use a touch up.
    You and O\'Doodles go to the salon to refresh your hairstyles.''')
input('In the chair you receive your fourth riddle...')

repeat=True
while repeat==True:
    ans6=input('''What does the Easter Bunny use to keep his fur neat?
    (enter answer) ''')
    if ans6.lower()=='hare brush' or  ans6.lower()=='hare-brush' or ans6.lower()=='a hare-brush'\
       or ans6.lower()=='a hare brush':
        input('"Smart yer are!"')
        riddles+=1
        print('"Yer answered', riddles, 'net riddles and \'av', riddles, 'future eggs."')
        input()
        repeat=False
    elif ans6==(''):
        input('"Waaat? Didn\'t catch dat." (press enter to try again)')
        repeat=True
    else:
        input('"Naw, google it." (press enter)') #[loop through the conditional]
        riddles-=1
        print('"Yer answered', riddles, 'net riddles. Yer lost an egg."')
        input()
        repeat=True        

if riddles==4:
    input('"Since yer answered 4 net riddles, Oi\'ll show yer whar 4 easter eggs are \'idden.')
    input('''"As a bonus for gettin\' al\' 4 answers in a row, yer git a 4 leaf clover.
    \'appy Easter!"''')
    input('You gained 4 Easter eggs and 1 lucky clover.')
    
if riddles==3:
    input('"Since yer answered 3 net riddles, Oi\'ll show yer whar 3 easter eggs are \'idden.')
    input('As a bonus, yer git a 3 leaf clover. \'appy Easter!"')
    input('You gained 3 Easter eggs and 1 shamrock.')
    
if 0<=riddles<=2:
    print('''"Since yer answered''', riddles, '''net riddles, Oi'll show yer whar''', riddles,
          '''easter eggs are 'idden. 'appy Easter!"''')
    input()
    print('You gained', riddles, 'Easter eggs.')
    input()

if riddles==0:
    input('...and 1 enemy.')

if riddles < 0:
    print('''"Since yer answered''', riddles, '''net riddles, yer owe me''', abs(riddles),
          '''Easter eggs. 'appy Easter!"''')
    input()
    print('You lost', abs(riddles), 'Easter eggs and gained 1 enemy.')
    input()

if 1<=riddles<=4:
    input('Since yer good at this, I \'ave a bonus riddle for yer before yer go.')
    repeat=True
    while repeat==True:
        ans7=input('''Waaat kind o' ending does de Easter Bunny loike best?
    (enter answer) ''')
        if 'hoppy' in ans7.lower():
            input('"Yup! Yer gained 1 friend."')
            repeat=False
        elif ans7==(''):
            input('"Waaat? Didn\'t catch dat." (press enter to try again)')
            repeat=True
        else:
            input('"Naw, google it." (press enter)')
