from TikTokApi import TikTokApi
from datetime import datetime

def ExtractTikTok(queries, filename1, filename2, foldername,numvidsrequested, paired_with_tags):
    with TikTokApi() as api:
        #build list of all hashtags currently searching for
        tags = []
        for query in queries:
            tag = api.hashtag(name=query)
            tags.append(tag)
        #open files to write to and write headings
        mainfile = open(filename1, "w")
        commentsfile = open(filename2, "w")
        mainfile.write("my_id,url,video_id,video_author,hashtags,createtime,description,isAd,stickersOnItem,privateItem,commentCount,playCount,shareCount,searchQuery,isPairedWith,time_queried\n")
        commentsfile.write("my_id,comment_id,text,author,likecount,language,ReplyCommenttotal,createtime\n")

        curr_video_id = 0
        for tag in tags:
            for video in tag.videos(count=numvidsrequested):
                #define properties of the videos
                video_id = str(video.id)
                video_author = str(video.author.username)
                video_hashtags = ""
                for hashtag in video.hashtags:
                    video_hashtags += "#" +str(hashtag.name) + " "
                video_url = "https://www.tiktok.com/@"+str(video.author.username)+"/video/"+str(video.id)
                video_dict = video.as_dict
                video_createtime = str(video.create_time)
                video_description = str(video_dict["desc"]).replace(",", " ").replace("\n", " ")
                video_isAd = str(video_dict["isAd"])
                video_stickersOnItem = ""
                video_stickers = []
                try:
                    video_stickers = video_dict["stickersOnItem"]
                except:
                    video_stickers = []
                for sticker in video_stickers:
                    sticker1 = sticker["stickerText"]
                    for sticker2 in sticker1:
                        video_stickersOnItem += (str(sticker2.replace("\n"," ").replace("\t", " ").replace(","," "))) + " "
                stats_dict = video_dict["stats"]
                video_commentCount = stats_dict["commentCount"]
                video_playCount = stats_dict["playCount"]
                video_shareCount = stats_dict["shareCount"]
                video_privateItem = video_dict["privateItem"]
                #define searchterm
                searchquery = "#"+str(tag.name)
                #see if paired with any of paired
                paired_with = ""
                if(len(paired_with_tags) != 0):
                    for i in paired_with_tags:
                        if i in video_hashtags:
                            paired_with = "True"
                    if(paired_with != "True"):
                        paired_with = "False"
                #get currtime
                curr_time = str(datetime.now())
                curr_time = curr_time[:curr_time.index(".")]
                #write all of these defined properites to the main file 
                mainfile.write(str(curr_video_id)+","+video_url+","+str(video_id)+","+video_author+","+ video_hashtags+ "," + str(video_createtime)+ ","+video_description+","+str(video_isAd) +","+video_stickersOnItem + ","+str(video_privateItem)+","+str(video_commentCount)+","+str(video_playCount)+","+str(video_shareCount)+","+searchquery+","+paired_with+","+curr_time+"\n")
                #define properties for the comments
                
                try:
                    for comment in video.comments():
                        comment_id = comment.id
                        comment_text = str(comment.text).replace(",", " ").replace("\n", " ")
                        comment_author = comment.author.username
                        comment_likecount = comment.likes_count
                        comment_dict = comment.as_dict
                        comment_language = comment_dict["comment_language"]
                        comment_replycommenttotal = comment_dict["reply_comment_total"]
                        comment_createtime = comment_dict["create_time"]
                        #write all of these properies to the comment file one by one
                        commentsfile.write(str(curr_video_id)+","+str(comment_id)+","+str(comment_text)+","+str(comment_author)+","+str(comment_likecount)+","+str(comment_language)+","+str(comment_replycommenttotal)+","+str(comment_createtime)+"\n")
                except:
                    print("no comments on video "+str(curr_video_id))
                #get the actual tiktok video and save it
                video_data = video.bytes()
                with open(foldername+"/"+str(tag.name)+"_"+str(curr_video_id)+".mp4", "wb") as out_file:
                    out_file.write(video_data)
                curr_video_id += 1



#start of usability, 
args = input("Enter all hashtags separated by spaces (ex: nosabo nosabokids): ").split(" ")
for i in range(len(args)):
    if args[i][0]=="#" and len(args[i])>1:
        args[i] = args[i][1:]

if(len(args)==0):
    raise Exception("Provide at least one hashtag to use")
filename1 = input("Enter path and filename (.csv) for main output file (ex: output/nosabo.csv): ")
filename2 = input("Enter path and filename (.csv) for comments output file (ex: output/nosabocomments.csv): ")
foldername = input("Enter the path to the folder for the videos to be saved in (ex: output/nosabovids): ")
if(len(foldername) ==0):
    raise Exception("provide a valid folder name")
if(foldername[len(foldername)-1]=="/"):
    foldername  = foldername[:len(foldername)-1]
numvidsrequested = input("Enter the number of videos you want per hashtag (ex: 10): *THIS IS BROKEN RIGHT NOW* ")
try:
    numvidsrequested = int(numvidsrequested.strip())
except:
    raise Exception("invalid number of videos, please enter a number")
if(numvidsrequested < 0 and numvidsrequested > 500):
    raise Exception("not valid number of videos, negative or too many for current implementation")
paired_with_tags = input("enter the hashtag(s) separated by spaces that you want to see if the search term is paired with (ex: mexico mexicano): ").split(" ")

ExtractTikTok(args, filename1, filename2, foldername, numvidsrequested, paired_with_tags)