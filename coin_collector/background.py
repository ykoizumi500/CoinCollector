# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pygame


class Background(pygame.sprite.Sprite):
    """背景

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # サイズに合わせる
        self.image = game.background_image
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
