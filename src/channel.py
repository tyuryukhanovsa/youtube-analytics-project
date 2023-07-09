from googleapiclient.discovery import build
import os
import json

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        """
        self.__channel_id = channel_id
        youtube = self.get_service()
        dict_of_chanel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        data_of_channel = dict_of_chanel["items"][0]

        self.title = data_of_channel['snippet']['title']
        self.description = data_of_channel['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriberCount = int(data_of_channel['statistics']['subscriberCount'])
        self.video_count = int(data_of_channel['statistics']['videoCount'])
        self.viewCount = int(data_of_channel['statistics']['viewCount'])

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Получает данные по API ключу"""
        youtube = self.get_service()
        dict_to_print = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def __str__(self):
        return f'{self.title}({self.url})'  # возвращает None

    def __add__(self, other):
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other):
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other):
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other):
        return self.subscriberCount == other.subscriberCount

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API"""
        return cls.youtube

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
