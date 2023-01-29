import pandas as pd
import random
import vlc
import time
####### This file is for suzuki violin daily pracese.
# Before using the code, you will need:
#to download and install vlc: https://www.videolan.org/vlc/
#In order to make it work for you, you will need to make the following changes:
# 1. Open Time_Suzuki_Violin_Book_1.xlsx or .csv
# 2. Find the ID for the song that you learned (learned_ID).
# For exp, if you just learned 'Lightly Row', change learned_ID = 1
# 3. You can then change the other parameters:

# Parameters to modify:
learned_ID = 15       # The ID of the last song that you learned. The ID for the first song Twinkle Variations is 0
speed_newsong=0.6 #The speed for the new song
rp_newsong=2 # How many times to play the new song
speed_oldsong=0.7 #The speed for the old song
num_song = 3 #The number of old song that you want to play besides the new song cat meow i love cats cat cat cat cat




# Open the list of song names and time label information
df= pd.read_csv('resources/Time_Suzuki_Violin_Book_1.csv', header=None)
lenth_song = '20:22'

####################Creat the df including Song Name with the Start and End Time #####################
df[['Start','Name']] = df[0].str.split(' ',1,expand = True)
df['End']=''
df['Duration'] =''
#df['Start'][15] = '15:48'

def time_to_hm(times):
       t00=time.strptime('00:00',('%M:%S'))
       tx=time.strptime(times,('%M:%S'))
       dif = time.mktime(tx) - time.mktime(t00)  # sec
       return (dif)



for i in df.index:
       df['Start'][i]=time_to_hm(df['Start'][i])
       df['End'][i-1] = df['Start'][i]-1

df['End'][i] = time_to_hm(lenth_song)
df['Duration'] =df['End']-df['Start']



############# Play Random Song ################


def play_song(song_ID):
       # media object
       media = vlc.Media("resources/Suzuki_Violin_Book_1.mp3")

       # creating vlc media player object
       media_player = vlc.MediaPlayer()
       # setting the speed of the video
       media_player.set_rate(speed)

       media_temp = media
       # media start and stop time
       print('Now Playing: ' + df['Name'][song_ID] + '   Speed: ' + str(speed))
       media_temp.add_option('start-time=' + str(df['Start'][song_ID]))
       media_temp.add_option('stop-time=' + str(df['End'][song_ID]))

       # setting media to the media player
       media_player.set_media(media_temp)

       # start playing video
       media_player.play()
       time.sleep(df['Duration'][song_ID]/speed+0)
       #media_player.stop()




randomlst = random.sample(range(0, learned_ID), num_song)
random_song_lst = [df['Name'][items] for items in randomlst]
print('Today Nolan is going to play the following '+str(num_song) +' songs:')
print(random_song_lst)
print('')

#Play the new song for three times`
speed=speed_newsong
for i in range(rp_newsong):
       print(i)
       play_song(learned_ID)

#Play random learned song for twice or twinkle for once
speed=speed_oldsong
for items in randomlst:
       print(items)
       #print(df['Name'][items])

       play_song(items)

       # if the song is not 'Twinkle Variance', play twice; Play once it is 'Twinkle'
       if items >0:
              play_song(items)


