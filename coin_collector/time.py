# -*- coding: utf-8 -*-
"""Coin Collector Game

残り時間のクラス
"""
#!/usr/bin/env python3
import pygame
from . import settings


class Time(pygame.sprite.Sprite):
    """残り時間表示

    """
    def __init__(self, game):
        super().__init__(self.containers)
        # ゲームの参照
        self.game = game
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # 残り時間の表示
        self.image = None
        self.rect = None
        # 音の有無
        self.sound = False

    def update(self):
        """画面の更新

        """
        # 1秒おきに
        if self.sound and self.time % settings.FRAME_RATE == 0:
            # 効果音をさせる
            self.game.clock_sound.play()
        # スコアの表示形式を設定する
        self.image = self.sysfont.render(f"{self.time / settings.FRAME_RATE:>0.02f} s", True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置を右にする
        self.rect.right = self.game.screen_rect.right
