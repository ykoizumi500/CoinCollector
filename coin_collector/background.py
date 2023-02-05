# -*- coding: utf-8 -*-
"""Coin Collector Game

背景のクラス
"""
#!/usr/bin/env python3
import pygame
from . import settings


class Background(pygame.sprite.Sprite):
    """背景

    """

    def __init__(self, game):
        super().__init__(self.containers)
        # サイズに合わせる
        self.image = game.background_image
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
