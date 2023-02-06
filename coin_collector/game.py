# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import os
import pygame
from . import settings, over, background, score, time, player, coin


class Game:
    """ ゲーム

    """
    def __init__(self):
        # 初期化する
        pygame.init()
        # 画面のサイズを設定する
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.screen_rect = pygame.Rect([0, 0], settings.SCREEN_SIZE)
        pygame.display.set_caption(settings.TITLE)
        # グループでまとめる
        self.all = pygame.sprite.RenderUpdates()
        self.coin_group = pygame.sprite.Group()
        self.over_group = pygame.sprite.Group()
        player.Player.containers = self.all
        coin.Coin.containers = self.coin_group, self.all
        background.Background.containers = self.all
        over.Over.containers = self.over_group, self.all
        score.Score.containers = self.all
        time.Time.containers = self.all
        # データを読み込む
        self.load_data()
        # 背景を作る
        self.background = background.Background(self)
        # ゲームオーバーを作らない
        self.over = None
        # スコア表示を作る
        self.score = score.Score(self)
        # 時間表示を作る
        self.time = time.Time(self)
        # プレーヤーを作る
        self.player = player.Player(self)
        # 背景をグループに加える
        self.all.add(self.background)
        # スコア表示をグループに加える
        self.all.add(self.score)
        # 時間表示をグループに加える
        self.all.add(self.time)
        # プレーヤーをグループに加える
        self.all.add(self.player)
        # クロック
        self.clock = pygame.time.Clock()
        # コインの周期のカウントの初期化
        self.coin_period = 0

    def update(self) -> None:
        """画面の更新

        """
        # フレームレートの設定
        self.clock.tick(settings.FRAME_RATE)
        # スプライトを更新
        self.all.update()
        dirty = self.all.draw(self.screen)
        # 画面更新
        pygame.display.update(dirty)

    def start(self) -> None:
        """ゲーム開始画面

        """
        # コインを有効化
        self.coin_valid = True
        # 位置を決める
        self.player.rect.centerx = settings.PLAYER_X
        self.player.rect.centery = settings.PLAYER_Y
        # 時間
        self.time.time = settings.TIME_LIMIT
        # スコアの初期化
        self.score.score = 0
        # コインの周期のカウントの初期化
        self.coin_period = 0
        # ゲームオーバを消す
        for sprite in self.over_group.sprites():
            sprite.kill()
        while True:
            # 画面の更新
            self.update()
            for event in pygame.event.get():
                # 閉じるボタンが押されたら
                if event.type == pygame.QUIT:
                    # 終了させる
                    sys.exit()
            # キー操作の情報を受け取る
            keystate = pygame.key.get_pressed()
            # スペースが押されたら
            if keystate[pygame.K_SPACE]:
                # ゲームを始める
                self.play()

    def play(self) -> None:
        """ ゲームループ

        """
        # 時計を始める
        self.time.sound = True
        while self.time.time > 0:
            # 画面の更新
            self.update()
            for event in pygame.event.get():
                # 閉じるボタンが押されたら
                if event.type == pygame.QUIT:
                    # 終了させる
                    sys.exit()
            # キー操作の情報を受け取る
            keystate = pygame.key.get_pressed()
            # エスケープが押されたら
            if keystate[pygame.K_ESCAPE]:
                self.game_over()
            # 右方向に移動する距離
            right = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
            # 下方向に移動する距離
            down = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
            # 移動させる
            self.player.move(right, down)
            # コインを出現させる時になったら
            if self.coin_period == settings.COIN_PERIOD:
                # コインを増やす
                self.add_coin()
                # コインの周期のカウントをリセットする
                self.coin_period = 0
            # コインの周期のカウントする
            self.coin_period += 1
            # 時間を減らす
            self.time.time -= 1
        # ゲームオーバー
        self.game_over()

    def game_over(self) -> None:
        """ゲームオーバー
        ゲームオーバーの表示をする
        """
        # 残り時間をリセットする
        self.time.sound = False
        self.time.time = 0
        # コインの無効化
        self.coin_valid = False
        # 時間切れ表示をする
        self.over = over.Over(self)
        # 時間切れ表示をグループに加える
        self.all.add(self.over)
        self.over_group.add(self.over)
        while True:
            # 画面の更新
            self.update()
            for event in pygame.event.get():
                # 閉じるボタンが押されたら
                if event.type == pygame.QUIT:
                    # 終了させる
                    sys.exit()
            # キー操作の情報を受け取る
            keystate = pygame.key.get_pressed()
            # エンターが押されたら
            if keystate[pygame.K_RETURN]:
                # ゲーム再開する
                self.start()


    def load_data(self) -> None:
        """ 画像・音声を読み込む

        """
        # ファイルからデータを読み込む
        self.background_image = pygame.image.load(os.path.join(settings.DATA, settings.BACKGROUND_IMAGE)).convert()
        self.coin_image = pygame.image.load(os.path.join(settings.DATA, settings.COIN_IMAGE)).convert()
        self.player_image = pygame.image.load(os.path.join(settings.DATA, settings.PLAYER_IMAGE)).convert()
        self.coin_sound = pygame.mixer.Sound(os.path.join(settings.DATA, settings.COIN_SOUND))
        self.clock_sound = pygame.mixer.Sound(os.path.join(settings.DATA, settings.CLOCK_SOUND))
        # 大きさを変える
        self.background_image = pygame.transform.scale(self.background_image, settings.SCREEN_SIZE)
        self.coin_image = pygame.transform.scale(self.coin_image, settings.COIN_SIZE)
        self.player_image = pygame.transform.scale(self.player_image, settings.PLAYER_SIZE)

    def add_coin(self) -> None:
        """コインを増やす

        """
        # コインを作る
        my_coin = coin.Coin(self)
        # コインをグループに加える
        self.all.add(my_coin)
        self.coin_group.add(my_coin)
