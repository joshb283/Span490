

             # print(type(video_stickers))
            # json_object = json.dumps(video_dict, indent = 4) 
            # print(json_object)
            # temp = 1
            # for key in video_dict.keys():
            #     print(key + "\n")
            # break
            # for sticker in video_dict['stickersOnItem']:
            #     video_stickersOnItem += str(sticker["stickerText"]).strip("\n") + " "

                #     out_file.write(video_data)
            # if flag == 0:
            #     print(video_dict["music"])
            #     flag = 1
                # video_data = video.bytes()
                # with open("output/outtest"+str(flag)+".mp4", "wb") as out_file:
                #     out_file.write(video_data)
            # json_object = json.dumps(video_dict, indent = 4) 
            # print(json_object)
            # print("\n\n\n\n")
            
                # if(flag == 0):
                #     for key in comment_dict:
                #         print(key)
                #         print("\n")
                #     flag = 1
                # json_object = json.dumps(comment_dict, indent = 4) 
                # print(json_object)
                # print("\n\n\n\n")
    # tag = api.hashtag(name="spanglish")
    # print(tag.info())
    # g = open("output/tiktokout.csv", "w")
    # flag = 0
    # fp = open('output/tiktokdict.json', 'w')
    
    # for video in tag.videos():
    #     g.write(str(video.author.username))
    #     g.write(",")
    #     g.write(str(video.id))
    #     g.write(",")
    #     s = "https://www.tiktok.com/@"+str(video.author.username)+"/video/"+str(video.id)
    #     g.write(s)
    #     g.write(",")
        
    #     #print(video.author)
    #     json.dump(video.as_dict, fp)
    #     #print("\n")
    #     #print(video.hashtags)
    #     #print(video.id)
    #     for hasht in video.hashtags:
    #         g.write("#")
    #         g.write(str(hasht.name))
    #         g.write(" ")
    #     g.write("\n")
    #     #can save it 
    #     # if(flag < 100):
    #     #     video = api.video(id=video.id)
    #     #     video_data = video.bytes()
    #     #     with open("output/out"+str(flag)+".mp4", "wb") as out_file:
    #     #         out_file.write(video_data)
    #     #     flag += 1
    # g.close()
    # fp.close()


# with TikTokApi() as api:
#     tiktok_video_id = 7107272719166901550
#     video = api.video(id=tiktok_video_id)

#     for comment in video.comments():
#         print(comment.text)