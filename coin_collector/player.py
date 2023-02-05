# -*- coding: utf-8 -*-
"""Coin Collector Game

プレーヤのクラス
"""
#!/usr/bin/env python3
import pygame
from . import settings


class Player(pygame.sprite.Sprite):
    """プレーヤー

    """
    # 移動する速度
    speed = 10

    def __init__(self, image, size, game):
        super().__init__(self.containers)
        # 画像を読み込む
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 移動できる範囲の計算
        left = settings.PLAYER_X_RANGE[0]
        right = settings.PLAYER_Y_RANGE[0]
        height = settings.PLAYER_X_RANGE[1] - settings.PLAYER_X_RANGE[0]
        width = settings.PLAYER_Y_RANGE[1] - settings.PLAYER_Y_RANGE[0]
        # 移動できる範囲の設定
        self.range = pygame.Rect(left, right, height, width)
        # ゲームの参照
        self.game = game

    def move(self, right: int, down: int) -> None:
        """プレーヤを移動させる。

        Args:
            right (int): 右に移動させる距離
            down (int): 下に移動させる距離
        """
        # プレーヤーを移動させる
        self.rect.move_ip(right * self.speed, down * self.speed)
        # 外枠に衝突した時の処理
        self.rect = self.rect.clamp(self.range)
        # コインに衝突したときの処理
        coin_collide = pygame.sprite.spritecollide(self, self.game.coin_sprites, True)
        for coin in coin_collide:
            if coin.valid:
                # スコアを加える
                self.game.score.add_score(settings.COIN_SCORE)
                # 残り時間を加える
                self.game.time.add_time(settings.COIN_TIME)
                # 効果音を鳴らす
                self.game.coin_sound.play()
