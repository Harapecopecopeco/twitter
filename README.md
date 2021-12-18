# twitter

Twitter APIを叩いて遊ぶ。

すべてはここから。

Twitter: [@panicyusuke](https://twitter.com/panicyusuke)
> なぜ僕のツイートが伸びないか考えた結果次の仮説が導きだされた。  
ツイートは面白いのだがつぶやく時間とフォロワーのツイッターを見ている時間とマッチしていない。  
つまり、みんながよく見ている時間につぶやけばバズる。  
> この仮説を検証するにはフォロワーがTwitterを見ている時間がいつなのかを特定して、    
> そのタイミングに合わせて投稿すればよいということ。  
んじゃあそれってどうやるのさ？って話だけど  
> Twitter APIを使って僕のフォロワーの投稿時間、  
> いいね時間を吸い出して分析すればいい。  
Tweepyは4年前自然言語処理でたくさん触ったので自信はある。  
さあ、検証していくう

## Twitter API for Python

### Setup 

#### Python virtual environment

```shell

python3 -m venv venv
source venv/bin/activate

```

#### 1. Create `requirements.txt`

`requirements.txt`
```text:requirements.txt

twitter
python-dotenv
dash
pandas
pylint
django
flask_cors
requests_oauthlib
requests
oauthlib

```

#### 2. Create `.env` for secret twitter token

Create the .env file in the root directory.

`.env`
```ENV

CONSUMER_KEY=YourConsumerToken
CONSUMER_SECRET_KEY=YourConsumerSecret
ACCESS_TOKEN=YourAccessToken
ACCESS_TOKEN_SECRET=YourSecretToken

```

### API Doc

## Usage

`working tree`
```shell

>> pwd
/home/harapeco/go/src/github.com/Harapecopecopeco/twitter/

>> cd twitter
>> tree
.
├── __init__.py
├── __pycache__
│   └── twiiter_client.cpython-39.pyc
├── error
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── errors.cpython-39.pyc
│   │   └── query.cpython-39.pyc
│   ├── errors.py
│   ├── http.py
│   └── query.py
├── main.py
├── output.json
└── twiiter_client.py


```

### Get Tweets by screen name

screen_name をTwitterのIDに書き換え、root ディレクトリで実行

`Command Line`
```shell
>> python main.py 
```

cf. 

`main.py`
```python:main.py

from twiiter_client import TwitterClient
from datetime import date
from pprint import pprint

today = date.today()

screen_name = "shoku_pan_pan"
request_count = 5
client = TwitterClient(dt=today, screen_name=screen_name)

# Get Tweets by user ids
query = client.tweets(count=request_count)
pprint(query)

```