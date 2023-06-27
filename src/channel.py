from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.subscriberCount = None
        self.video_count = None
        self.viewCount = None

    @property
    def channel_id(self):
        return self.__channel_id

    def get_info(self) -> None:
        """Получает данные по API ключу"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        dict_to_print = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        # print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
        data_of_channel = dict_to_print['items'][0]

        self.title = data_of_channel['snippet']['title']
        self.description = data_of_channel['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriberCount = int(data_of_channel['statistics']['subscriberCount'])
        self.video_count = int(data_of_channel['statistics']['videoCount'])
        self.viewCount = int(data_of_channel['statistics']['viewCount'])

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        data = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "video_count": self.video_count,
            "viewCount": self.viewCount
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
