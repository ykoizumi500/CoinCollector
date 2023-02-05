# -*- coding: utf-8 -*-
"""Coin Collector Game

スコアのクラス
"""
#!/usr/bin/env python3
import pygame
from . import settings


class Score(pygame.sprite.Sprite):
    """スコア表示

    """
    def __init__(self):
        super().__init__(self.containers)
        # スコアを初期化する
        self.score = 0
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スコアの表示形式を設定する
        self.image = self.sysfont.render("{:0>5d}".format(self.score), True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
