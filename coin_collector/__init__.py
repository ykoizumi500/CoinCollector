"""Coin Collector Game

コイン収集ゲーム
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import random
import os
import pygame

# 画面のサイズ
SCREEN = pygame.Rect(0, 0, 800, 600)


# プレーヤー
class Player(pygame.sprite.Sprite):
    """プレーヤー

    """
    # 移動する速度
    speed = 10

    def __init__(self, filename, size):
        super().__init__(self.containers)
        # 画像を読み込む
        image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()

    def move(self, right, down) -> None:
        """プレーヤを移動させる。

        Args:
            right (int): 右に移動させる距離
            down (int): 下に移動させる距離
        """
        # プレーヤーを移動させる
        self.rect.move_ip(right * self.speed, down * self.speed)
        # 衝突時の処理
        self.rect = self.rect.clamp(SCREEN)


# コイン
class Coin(pygame.sprite.Sprite):
    """
        コイン
    """
    def __init__(self, filename, size):
        super().__init__(self.containers)
        # 画像を読み込む
        image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置をランダムに決める
        self.rect.centerx = random.randint(100, 700)
        self.rect.centery = random.randint(100, 500)


def main() -> None:
    """ゲームの開始

    ゲームを開始します。
    """
    # 初期化
    pygame.init()
    # 画面のサイズを設定する
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("Coin Collector Game")
    # スプライトでまとめる
    all_sprites = pygame.sprite.RenderUpdates()
    coin_sprites = pygame.sprite.Group()
    Player.containers = all_sprites
    Coin.containers = coin_sprites, all_sprites
    # プレーヤーを作る
    player = Player(os.path.join("img", "player.png"), [100, 100])
    # 3回繰り返す
    for _ in range(3):
        # コインを作る
        coin = Coin(os.path.join("img", "coin.png"), [80, 80])
        # コインをグループに追加する
        coin_sprites.add(coin)
    # クロック
    clock = pygame.time.Clock()
    while True:
        # フレームレートの設定
        clock.tick(60)
        # スプライトを更新
        all_sprites.update()
        screen.fill([0, 0, 0])
        dirty = all_sprites.draw(screen)
        # 画面更新
        pygame.display.update(dirty)
        for event in pygame.event.get():
            # 閉じるボタンが押されたら
            if event.type == pygame.QUIT:
                # 終了させる
                sys.exit()
        # キー操作の情報を受け取る
        keystate = pygame.key.get_pressed()
        # 右方向に移動する距離
        right = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        # 下方向に移動する距離
        down = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
        # 移動させる
        player.move(right, down)
