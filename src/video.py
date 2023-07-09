from src.channel import Channel


class Video:
    def __init__(self, video_id):
        youtube = Channel.get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_id = video_id
        self.name = video_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/watch?v=" + video_id
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.name


class PLVideo(Video):

    def __init__(self, video_id, playlist):
        super().__init__(video_id)
        self.playlist = playlist
