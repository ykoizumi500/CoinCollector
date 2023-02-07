""" 設定ファイル

"""
# 文字
## 画面のタイトル
TITLE = "Coin Collector Game"
## 時間切れのテキスト
OVER_TEXT = "GAME OVER"

# スコア表示のサイズ
SCORE_SIZE = 50
# 時間切れ表示の大きさ
OVER_SIZE = 100

## スコア表示の色
SCORE_COLOR = [0, 0, 0]
# 時間切れ表示の色
OVER_COLOR = [0, 0, 255]

# 時間
## フレームレート
FRAME_RATE = 100
# 制限時間
TIME_LIMIT = 60 * FRAME_RATE
# コイン獲得したときの獲得時間
COIN_TIME = 0.2 * FRAME_RATE
# 岩に衝突したときの獲得時間
ROCK_TIME = -2.0 * COIN_TIME
# コインの落下頻度
COIN_PERIOD = int(1.1 * COIN_TIME) + 1
# 岩の落下頻度
ROCK_PERIOD = 2.0 * COIN_PERIOD

# スコア
## コイン獲得したときのスコア
COIN_SCORE = 300
## 岩に衝突したときのスコア
ROCK_SCORE = -700
## フレームごとの得点
FRAME_SCORE = 1

# 音声・画像データ
## データの場所
DATA = "data"
# 背景の画像ファイル
BACKGROUND_IMAGE = "background.jpg"
# プレーヤーの画像ファイル
PLAYER_IMAGE = "player.png"
# コインの画像ファイル
COIN_IMAGE = "coin.png"
# 岩の画像ファイル
ROCK_IMAGE = "rock.png"
# コイン獲得するときの効果音
COIN_SOUND = "coin.wav"
# 岩に衝突したときの効果音
ROCK_SOUND = "rock.wav"
# 時計の音
CLOCK_SOUND = "clock.wav"

# 大きさ
# 画面のサイズ
SCREEN_SIZE = [800, 600]
# プレーヤーの大きさ
PLAYER_SIZE = [100,] * 2
# コインの大きさ
COIN_SIZE = [80,] * 2
# コインの効果音の大きさ
COIN_SOUND_SIZE = 0.1
# 岩の大きさ
ROCK_SIZE = [70,] * 2
# 岩の効果音の大きさ
ROCK_SOUND_SIZE = 0.3
# 時計の効果音の大きさ
CLOCK_SOUND_SIZE = 0.05
# プレーヤーの移動範囲
PLAYER_X_RANGE = [0, 800]
PLAYER_Y_RANGE = [300, 600]
# プレーヤーの初期位置
PLAYER_X = 400
PLAYER_Y = 500
## 打ち上げ範囲
X_RANGE = [300, 500]
Y_RANGE = [100, 250]

# 速さ
## 重力の大きさ
GRAVITY = 30 / FRAME_RATE
## プレーヤーの速さ
PLAYER_SPEED = 1000 / FRAME_RATE
## 打ち上げの速さ
VELOCITY_X_RANGE = [-2000 / FRAME_RATE, 2000 / FRAME_RATE]
VELOCITY_Y_RANGE = [-1000 / FRAME_RATE, -500 / FRAME_RATE]
