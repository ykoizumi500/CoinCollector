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
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スコアの設定
        self.score = 0
        # スコアの描画
        self.draw()

    def draw(self) -> None:
        """描画

        """
        # スコアの表示形式を設定する
        self.image = self.sysfont.render("{:0>5d}".format(self.score), True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()

    def add_score(self, score: int) -> None:
        """スコアの追加

        Args:
            score (int): 加える得点
        """
        # スコアを加える
        self.score += score
        # スコアの描画
        self.draw()

    def get_score(self) -> int:
        """スコアの取得

        """
        return self.score
