""" 設定ファイル

"""
# 画面のタイトル
TITLE = "Coin Collector Game"
# 時間切れのテキスト
OVER_TEXT = "GAME OVER"

# フレームレート
FRAME_RATE = 100
# スコア表示のサイズ
SCORE_SIZE = 50
# スコア表示の色
SCORE_COLOR = [0, 0, 0]
# 時間切れ表示の大きさ
OVER_SIZE = 100
# 時間切れ表示の色
OVER_COLOR = [0, 0, 255]

# 制限時間(フレーム)
TIME_LIMIT = 6000

# データの場所
DATA = "data"

# 背景の画像ファイル
BACKGROUND_IMAGE = "background.jpg"
# コインの画像ファイル
COIN_IMAGE = "coin.png"
# コイン獲得するときの効果音
COIN_SOUND = "coin.wav"
# コインの落下頻度
COIN_PERIOD = 50

# コイン獲得したときのスコア
COIN_SCORE = 10
# コイン獲得したときの獲得時間(フレーム)
COIN_TIME = 40

# 時計の音
CLOCK_SOUND = "clock.wav"

# プレーヤーの画像ファイル
PLAYER_IMAGE = "player.png"

# 画面のサイズ
SCREEN_SIZE = [800, 600]
# コインの大きさ
COIN_SIZE = [80, 80]
# プレーヤーの大きさ
PLAYER_SIZE = [100, 100]

# プレーヤーの移動範囲
PLAYER_X_RANGE = [0, 800]
PLAYER_Y_RANGE = [400, 600]
# プレーヤーの初期位置
PLAYER_X = 400
PLAYER_Y = 500

# 重力の大きさ
GRAVITY = 0.5

# コインの打ち上げ範囲
COIN_X_RANGE = [400, 450]
COIN_Y_RANGE = [100, 250]
# コインの打ち上げの速さ
COIN_VELOCITY_X_RANGE = [-20, 20]
COIN_VELOCITY_Y_RANGE = [-15, -10]
