# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pygame
from . import settings


class Over(pygame.sprite.Sprite):
    """時間切れ表示

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.OVER_SIZE)
        # ゲームの参照
        self.game = game
        # スコアの表示形式を設定する
        self.image = self.sysfont.render(settings.OVER_TEXT, True, settings.OVER_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 中央に表示する
        self.rect.centerx = self.game.screen_rect.centerx
        self.rect.centery = self.game.screen_rect.centery
