# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pygame
import sys
import random

# 画面のサイズ
SCREEN = pygame.Rect(0, 0, 800, 600)

def main() -> None:
    # 初期化
    pygame.init()
    # 画面のサイズを設定する
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Coin Collector Game")
    # 画像を読み込む
    player_image = pygame.image.load("img/player.png")
    coin_image = pygame.image.load("img/coin.png")
    # 画像のサイズを指定する
    player_image = pygame.transform.scale(player_image, [100, 100])
    coin_image = pygame.transform.scale(coin_image, [80, 80])
    # Rect（四角）オブジェクトも生成しておく
    player_rect = player_image.get_rect()
    coin_rect = coin_image.get_rect()
    # コインの位置をランダムに決める
    coin_rect.centerx = random.randint(100, 700)
    coin_rect.centery = random.randint(100, 500)
    # コインとプレイヤーを描画。
    screen.blit(coin_image, coin_rect)
    screen.blit(player_image, player_rect)
    while True:
        # 終了させる
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

