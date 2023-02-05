# -*- coding: utf-8 -*-
"""Coin Collector Game

時間切れのクラス
"""
#!/usr/bin/env python3
import pygame
from . import settings, game


class Over(pygame.sprite.Sprite):
    """時間切れ表示

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.OVER_SIZE)
        # ゲームの参照
        self.game = game
        # 時間切れの描画
        self.draw()

    def draw(self) -> None:
        """描画

        """
        # スコアの表示形式を設定する
        self.image = self.sysfont.render(settings.OVER_TEXT, True, settings.OVER_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 中央に表示する
        self.rect.centerx = self.game.screen_rect.centerx
        self.rect.centery = self.game.screen_rect.centery
