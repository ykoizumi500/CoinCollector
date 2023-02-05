# -*- coding: utf-8 -*-
"""Coin Collector Game

ゲームのクラス
"""
#!/usr/bin/env python3
import os
import pygame
from . import settings, background, score, time, player, coin


class Game:
    """ ゲーム

    """
    def __init__(self):
        # 初期化
        pygame.init()
        # 画面のサイズを設定する
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.screen_rect = pygame.Rect([0, 0], settings.SCREEN_SIZE)
        pygame.display.set_caption(settings.TITLE)
        # スプライトでまとめる
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.coin_sprites = pygame.sprite.Group()
        player.Player.containers = self.all_sprites
        coin.Coin.containers = self.coin_sprites, self.all_sprites
        background.Background.containers = self.all_sprites
        score.Score.containers = self.all_sprites
        time.Time.containers = self.all_sprites
        # データを読み込む
        self.load_data()
        # 背景を作る
        background.Background(self.background_image, settings.SCREEN_SIZE)
        # スコア表示を作る
        self.score = score.Score()
        # 時間表示を作る
        self.time = time.Time(self.screen_rect, settings.TIME_LIMIT)
        # プレーヤーを作る
        self.player = player.Player(self.player_image, settings.PLAYER_SIZE, self)
        # クロック
        self.clock = pygame.time.Clock()
        # コインの周期のカウント
        self.coin_period = 0

    def play(self) -> int:
        """ ゲームループ

        """
        while True:
            # フレームレートの設定
            self.clock.tick(settings.FRAME_RATE)
            # スプライトを更新
            self.all_sprites.update()
            dirty = self.all_sprites.draw(self.screen)
            # 画面更新
            pygame.display.update(dirty)
            for event in pygame.event.get():
                # 閉じるボタンが押されたら
                if event.type == pygame.QUIT:
                    # 終了させる
                    return self.over()
            # キー操作の情報を受け取る
            keystate = pygame.key.get_pressed()
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
            # 時間を減らして時間切れでないなら
            if not self.time.add_time(-1):
                return self.over()

    def over(self) -> int:
        # 残り時間をリセットする
        self.time.set_time(0)
        return self.score.get_score()

    def load_data(self) -> None:
        """ 画像を読み込む

        """
        self.background_image = pygame.image.load(os.path.join(settings.DATA, settings.BACKGROUND_IMAGE)).convert()
        self.coin_image = pygame.image.load(os.path.join(settings.DATA, settings.COIN_IMAGE)).convert()
        self.player_image = pygame.image.load(os.path.join(settings.DATA, settings.PLAYER_IMAGE)).convert()
        self.coin_sound = pygame.mixer.Sound(os.path.join(settings.DATA, settings.COIN_SOUND))

    def add_coin(self) -> None:
        """コインを増やす

        """
        # コインを作る
        my_coin = coin.Coin(self.coin_image, settings.COIN_SIZE, self)
        # コインをグループに追加する
        self.coin_sprites.add(my_coin)
