# -*- coding: utf-8 -*-
"""Coin Collector Game

コインのクラス
"""
#!/usr/bin/env python3
import random
import pygame
from . import settings, game


class Coin(pygame.sprite.Sprite):
    """コイン

    """

    def __init__(self, image, size, game):
        super().__init__(self.containers)
        # サイズに合わせる
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置をランダムに決める
        self.rect.centerx = random.uniform(*settings.COIN_X_RANGE)
        self.rect.centery = random.uniform(*settings.COIN_Y_RANGE)
        # コインの速度をランダムに決める
        self.velocity_x = random.uniform(*settings.COIN_VELOCITY_X_RANGE)
        self.velocity_y = random.uniform(*settings.COIN_VELOCITY_Y_RANGE)
        # ゲームの参照
        self.game = game

    def update(self):
        """画面の更新

        """
        # 重力での移動
        self.rect.move_ip(int(self.velocity_x), int(self.velocity_y))
        # 重力で加速させる
        self.velocity_y += settings.GRAVITY
        # 左右に衝突した時の処理
        if self.rect.left < self.game.screen_rect.left or self.rect.right > self.game.screen_rect.right:
            self.velocity_x = - self.velocity_x
        if self.rect.bottom > self.game.screen_rect.bottom:
            self.kill()
