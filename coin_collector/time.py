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

    def __init__(self, screen):
        super().__init__(self.containers)
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スクリーンの参照
        self.screen = screen

    def draw(self) -> None:
        """描画

        """
        # スコアの表示形式を設定する
        self.image = self.sysfont.render("{:.2f} s".format(self.time / settings.FRAME_RATE), True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置を右にする
        self.rect.right = self.screen.right

    def add_time(self, time: int) -> None:
        """残り時間の追加

        Args:
            time (int): 加える時間
        """
        # 時間を加える
        self.time += time
        # 時間の描画
        self.draw()
        return self.time > 0

    def set_time(self, time: int) -> None:
        """時間を設定する

        """
        # 時間を設定する
        self.time = time
        # 時間の描画
        self.draw()
