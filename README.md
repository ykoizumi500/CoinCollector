CoinCollecterはコインを獲得するゲームです。

# 環境

- python 3.10

# インストール

```bash:インストール
git clone https://github.com/ykoizumi500/CoinCollector.git
cd CoinCollector
python -m pip install -r requirements.txt
```

# 使い方

```bash:実行
python -m coin_collector
```

## ゲーム開始画面

![ゲーム開始画面](docs/start_screen.png)

スペースキーでゲームを始めます。

## ゲーム中画面

![ゲーム中画面](docs/play_screen.png)

ゲーム中は矢印キーで移動できます。
コインを獲得すると、残り時間と得点が増えます。
岩に衝突すると、残り時間と得点が減ります。
残り時間は右上に、得点は左上に表示されます。
エスケープキーで終了します。
また、残り時間が０になると終了します。

## ゲーム終了画面

![ゲーム終了画面](docs/over_screen.png)

時間切れになるとこの画面になります。
エンターキーで再開します。

# 使用画像

画像は
[パブリックドメインQ](https://publicdomainq.net/)
から引用しました。
