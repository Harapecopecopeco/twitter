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

### Requirements


`requirements.txt`
```text:requirements.txt

twitter

```

### API Doc

旧Tweepy: https://docs.tweepy.org/en/v3.5.0/api.html
新Twitter: 