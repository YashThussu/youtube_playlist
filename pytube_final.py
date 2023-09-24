import pytube

def playlist_length(url:str):
    """calculates total time of a youtube video or playlist 

    Args:
        url (str): takes vurl of playlist or video
    """

    time=0
    n=0
    error=0  # in seconds
    
    try:
        
        p1=pytube.Playlist(url)
        for video in p1:
            video_obj=pytube.YouTube(video) 
            time+=video_obj.length
            print(video_obj.length//60,'mins ',video_obj.length%60,'secs' )
            n+=1
            # print(video_obj.length%60)
        
        hrs=time//3600
        mins=(time%3600)//60
        secs=(time%60)
        error=n

        return f'{hrs}hrs {mins}mins {secs}secs, max_error: +{error}secs'
    except:
        
        return 'cannot parse url'

url1='https://www.youtube.com/playlist?list=PLwLSw1_eDZl2sqKBwA6XyV_3It6SXVfy9'
url2='https://www.youtube.com/playlist?list=PLeo1K3hjS3uu0N_0W6giDXzZIcB07Ng_F'

print(playlist_length(url2))
