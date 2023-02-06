# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import random
import pygame
from . import settings


class Coin(pygame.sprite.Sprite):
    """コイン

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # ゲームの参照
        self.game = game
        # サイズに合わせる
        self.image = game.coin_image
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
        # 有効化
        self.valid = True

    def update(self):
        """画面の更新

        """
        # 透明化
        if self.game.coin_valid:
            self.image.set_alpha()
        else:
            self.image.set_alpha(127)
        # 重力での移動
        self.rect.move_ip(int(self.velocity_x), int(self.velocity_y))
        # 重力で加速させる
        self.velocity_y += settings.GRAVITY
        # 左右に衝突した時の処理
        if self.rect.left < self.game.screen_rect.left or self.rect.right > self.game.screen_rect.right:
            self.velocity_x = - self.velocity_x
        # 下に衝突したときの処理
        if self.rect.bottom > self.game.screen_rect.bottom:
            self.kill()
