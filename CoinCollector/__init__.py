# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pygame
import sys
import random

# 画面のサイズ
SCREEN = pygame.Rect(0, 0, 800, 600)

# プレーヤー
class Player(pygame.sprite.Sprite):
    def __init__(self, filename, size):
        super().__init__()
        # 画像を読み込む
        image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey((0,0,0))
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()

# コイン
class Coin(pygame.sprite.Sprite):
    def __init__(self, filename, size):
        super().__init__()
        # 画像を読み込む
        image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey((0,0,0))
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置をランダムに決める
        self.rect.centerx = random.randint(100, 700)
        self.rect.centery = random.randint(100, 500)

def main() -> None:
    # 初期化
    pygame.init()
    # 画面のサイズを設定する
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Coin Collector Game")
    # すべてのスプライトをまとめる
    all_sprites = pygame.sprite.Group()
    # プレーヤー・コインを作る
    player = Player("img/player.png", [100, 100])
    coin = Coin("img/coin.png", [80,80])
    # グループに追加する
    all_sprites.add(player)
    all_sprites.add(coin)
    # グループを描画
    all_sprites.draw(screen)
    while True:
        # 終了させる
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

