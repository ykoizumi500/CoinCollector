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

    def __init__(self, game):
        super().__init__(self.containers)
        # ゲームの参照
        self.game = game
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スコアの表示
        self.image = None
        self.rect = None

    def update(self):
        """画面の更新

        """
        # スコアの表示形式を設定する
        self.image = self.sysfont.render(f"{self.score:05d}", True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
