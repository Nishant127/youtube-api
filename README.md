# Youtube-API
![yt](https://i.postimg.cc/KzV1Td4s/Whats-App-Image-2022-08-28-at-6-17-09-PM.jpg)

## 💻 Development

### Requirements:

- Python >= 3.8 🐍
- Postgres 🐘

### 👨‍💻 Project Setup: 

- Clone this repository
- Setup the .env file.
- Enter the shell by typing `$ docker build .`
- Build the docker compose `$ docker-compose build`
- Run the `$ docker-compose up` command to start the service.
- And then run migrations `$ docker-compose exec web python manage.py migrate`
- Also create the super user `$ docker-compose exec web python manage.py createsuperuser`

### 🔐 Environment variables: 

- Create file `.env` inside `youtube-api` directory
- Copy contents from `.env.example` file and paste it in the `.env` file you just created.
- After copying the contents, edit the `SECRET_KEY`.
  - You can generate SECRET_KEY using `get_random_secret_key` method.
  - Run `$ django-admin shell` in the terminal.
  - Enter `$ from django.core.management.utils import get_random_secret_key ` to import the method.
  - And then enter `$ secret_key = get_random_secret_key()` to generate the secret key.
  - You can now use the generated value as our SECRET_KEY.


# Functionality
- Youtube API is used to fetch latest videos for a predefined query.
- Server call the YouTube API continuously in background (async) with some interval (say 10 seconds)
- The latest videos are stored in the database.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A search API to search the stored videos using their title and description.
- Support for supplying multiple API keys so that if quota is exhausted on one, automatically the next available key is used.

# Note
- Atleast one Youtube API key should be added in the database using the endpoint `http://localhost:8000/youtube/api-key/` to fetch and save the video details. 


# API Enpoints
### 1. API to add Youtube API Key in the database.
#### *Post request will add Youtube API key in the database*
```
http://127.0.0.1:8000/youtube/api-key/
```
- **Body**
```json
{
    "api_key":"AIzaSyC5iiJjJzX_MAYsss5f3TTZzTvC4"
}
```
- **Response**
```json
"API key added successfully"
```
### 2. API to get stored youtube videos.
#### *Get API will return paginated JSON response in descending order of the published datetime.*

``` 
http://127.0.0.1:8000/youtube/videos/
```
- *Response*
```json
{
    "count": 191,
    "next": "http://localhost:8000/youtube/videos/?page=2",
    "previous": null,
    "results": [
        {
            "id": 186,
            "created_at": "2022-08-27T20:55:32.488414Z",
            "updated_at": "2022-08-27T20:55:32.488440Z",
            "video_id": "AGpg0Z5pH0Y",
            "title": "Team india dancing #viral #shorts #video #cricket #india #team",
            "description": "",
            "thumbnail": {
                "high": {
                    "url": "https://i.ytimg.com/vi/AGpg0Z5pH0Y/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/AGpg0Z5pH0Y/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/AGpg0Z5pH0Y/default.jpg",
                    "width": 120,
                    "height": 90
                }
            },
            "published_at": "2022-08-27T20:54:48Z"
        },
        {
            "id": 185,
            "created_at": "2022-08-27T20:55:32.482348Z",
            "updated_at": "2022-08-27T20:55:32.482378Z",
            "video_id": "-kaCsjpzvRA",
            "title": "AB De Villiers Batting#shorts #cricket #cricketshorts #icct20worldcup #abdevilliers #abdevillier",
            "description": "",
            "thumbnail": {
                "high": {
                    "url": "https://i.ytimg.com/vi/-kaCsjpzvRA/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/-kaCsjpzvRA/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/-kaCsjpzvRA/default.jpg",
                    "width": 120,
                    "height": 90
                }
            },
            "published_at": "2022-08-27T20:54:03Z"
        },
        {
            "id": 194,
            "created_at": "2022-08-27T20:55:53.599784Z",
            "updated_at": "2022-08-27T20:55:53.599806Z",
            "video_id": "dWeXChuo8Bw",
            "title": "Afghanistan Won The Match || Asia Cup 2022 || SMN Cricket",
            "description": "Afghanistan Beat Sri Lanka By 8 Wickets. #AfghanistanVsSriLanka #AFGvsSL #AsiaCup2022 #SMNSports #SharkMediaNetwork ...",
            "thumbnail": {
                "high": {
                    "url": "https://i.ytimg.com/vi/dWeXChuo8Bw/hqdefault.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/dWeXChuo8Bw/mqdefault.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/dWeXChuo8Bw/default.jpg",
                    "width": 120,
                    "height": 90
                }
            },
            "published_at": "2022-08-27T20:52:14Z"
        }
    ]
}
```
### 3. API to search the stored videos using their title and description.
#### Get request with query param eg:`search=virat` will return response related to the search query.
```
http://127.0.0.1:8000/youtube/search/
```
- **Response**
```json
[
    {
        "id": 77,
        "created_at": "2022-08-27T11:18:27.003009Z",
        "updated_at": "2022-08-27T11:18:27.003019Z",
        "video_id": "KVfW5EJjhEo",
        "title": "How To Bowl Googly ? #shorts #cricket #viral #viratkohli #msdhoni #rohitsharma #abdevilliers",
        "description": "",
        "thumbnail": {
            "high": {
                "url": "https://i.ytimg.com/vi/KVfW5EJjhEo/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/KVfW5EJjhEo/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "default": {
                "url": "https://i.ytimg.com/vi/KVfW5EJjhEo/default.jpg",
                "width": 120,
                "height": 90
            }
        },
        "published_at": "2022-08-27T11:15:14Z"
    },
    {
        "id": 82,
        "created_at": "2022-08-27T11:18:48.066040Z",
        "updated_at": "2022-08-27T11:18:48.066083Z",
        "video_id": "K-aLd3kssXs",
        "title": "VIRAT KOHLI 😵 2016 IN  RCB♥️  TEAM /#short /#status /#viratkohli /#rcb /#trending /#cricket /#goat",
        "description": "",
        "thumbnail": {
            "high": {
                "url": "https://i.ytimg.com/vi/K-aLd3kssXs/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/K-aLd3kssXs/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "default": {
                "url": "https://i.ytimg.com/vi/K-aLd3kssXs/default.jpg",
                "width": 120,
                "height": 90
            }
        },
        "published_at": "2022-08-27T11:17:25Z"
    },
    {
        "id": 85,
        "created_at": "2022-08-27T11:19:31.498063Z",
        "updated_at": "2022-08-27T11:19:31.498095Z",
        "video_id": "EoeVKQI-a3Y",
        "title": "Virat Kohali से क्यो डरता है इतना ज्यादा पाकिस्तान 💪 || #shorts #cricket",
        "description": "",
        "thumbnail": {
            "high": {
                "url": "https://i.ytimg.com/vi/EoeVKQI-a3Y/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/EoeVKQI-a3Y/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "default": {
                "url": "https://i.ytimg.com/vi/EoeVKQI-a3Y/default.jpg",
                "width": 120,
                "height": 90
            }
        },
        "published_at": "2022-08-27T11:17:58Z"
    },
    {
        "id": 86,
        "created_at": "2022-08-27T15:11:26.119701Z",
        "updated_at": "2022-08-27T15:11:26.119728Z",
        "video_id": "szW8K3S8DW8",
        "title": "Babar vs Kohli Challenge  ⚡💫🤯 #cricket #shorts #viral #trending #trending #babarazam #viratkohli",
        "description": "BABAR AZAM VS VIRAT KOHLI CHALLENGE #cricket #babarazam #viratkohli #babarvskohli #challenge #babar #kohli ...",
        "thumbnail": {
            "high": {
                "url": "https://i.ytimg.com/vi/szW8K3S8DW8/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/szW8K3S8DW8/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "default": {
                "url": "https://i.ytimg.com/vi/szW8K3S8DW8/default.jpg",
                "width": 120,
                "height": 90
            }
        },
        "published_at": "2022-08-27T15:09:26Z"
    },


]
```
