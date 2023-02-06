# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import random
import pygame
from . import settings


class Rock(pygame.sprite.Sprite):
    """岩

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # ゲームの参照
        self.game = game
        # サイズに合わせる
        self.image = game.rock_image
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置をランダムに決める
        self.rect.centerx = random.uniform(*settings.X_RANGE)
        self.rect.centery = random.uniform(*settings.Y_RANGE)
        # コインの速度をランダムに決める
        self.velocity_x = random.uniform(*settings.VELOCITY_X_RANGE)
        self.velocity_y = random.uniform(*settings.VELOCITY_Y_RANGE)
        # 有効・無効の設定
        self.valid = game.rock_valid

    def update(self):
        """画面の更新

        """
        # 透明化
        if self.valid:
            # 透明にしない
            self.image.set_alpha()
        else:
            # 少し透明にする
            self.image.set_alpha(127)
        # 重力での移動
        self.rect.move_ip(int(self.velocity_x), int(self.velocity_y))
        # 重力で加速させる
        self.velocity_y += settings.GRAVITY
        # 左右に衝突した時の処理
        if self.rect.left < self.game.screen_rect.left or self.rect.right > self.game.screen_rect.right:
            # 反射させる（反対向きに移動させる）
            self.velocity_x = - self.velocity_x
        # 下に衝突したときの処理
        if self.rect.bottom > self.game.screen_rect.bottom:
            # 消す
            self.kill()
