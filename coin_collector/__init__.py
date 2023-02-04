# -*- coding: utf-8 -*-
"""Coin Collector Game

コイン収集ゲーム
"""
#!/usr/bin/env python3
import sys
import random
import os
import pygame
from . import settings


class Player(pygame.sprite.Sprite):
    """プレーヤー

    """
    # 移動する速度
    speed = 10

    def __init__(self, image, size, screen, coin):
        super().__init__(self.containers)
        # 画像を読み込む
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # スクリーンの参照
        self.screen = screen
        # コインの参照
        self.coin = coin

    def move(self, right, down) -> None:
        """プレーヤを移動させる。

        Args:
            right (int): 右に移動させる距離
            down (int): 下に移動させる距離
        """
        # プレーヤーを移動させる
        self.rect.move_ip(right * self.speed, down * self.speed)
        # 外枠に衝突した時の処理
        self.rect = self.rect.clamp(self.screen)
        # コインに衝突したときの処理
        if pygame.sprite.spritecollide(self, self.coin, True):
            # 効果音を鳴らす
            self.coin_sound.play()


class Coin(pygame.sprite.Sprite):
    """コイン

    """

    def __init__(self, image, size, screen):
        super().__init__(self.containers)
        # サイズに合わせる
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置をランダムに決める
        self.rect.centerx = random.randint(0, screen.width)
        self.rect.top = random.randint(0, screen.height)
        # コインの速度をランダムに決める
        self.velocity_x = random.randint(*settings.VELOCITY_X_RANGE)
        self.velocity_y = random.randint(*settings.VELOCITY_Y_RANGE)
        # スクリーンの参照
        self.screen = screen

    def update(self):
        """画面の更新

        """
        # 重力での移動
        self.rect.move_ip(self.velocity_x, self.velocity_y)
        # 重力で加速させる
        self.velocity_y += settings.GRAVITY
        # 左右に衝突した時の処理
        if self.rect.left < self.screen.left or self.rect.right > self.screen.right:
            self.velocity_x = - self.velocity_x
        if self.rect.bottom > self.screen.bottom:
            self.kill()


class Background(pygame.sprite.Sprite):
    """背景

    """

    def __init__(self, image, size):
        super().__init__(self.containers)
        # サイズに合わせる
        self.image = pygame.transform.scale(image, size)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()


def main() -> None:
    """ゲームの開始

    ゲームを開始します。
    """
    # 初期化
    pygame.init()
    # 画面のサイズを設定する
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    screen_rect = pygame.Rect([0, 0], settings.SCREEN_SIZE)
    pygame.display.set_caption(settings.TITLE)
    # スプライトでまとめる
    all_sprites = pygame.sprite.RenderUpdates()
    coin_sprites = pygame.sprite.Group()
    Player.containers = all_sprites
    Coin.containers = coin_sprites, all_sprites
    Background.containers = all_sprites
    # 画像を読み込む
    background_image = pygame.image.load(os.path.join(settings.DATA, settings.BACKGROUND_IMAGE)).convert()
    coin_image = pygame.image.load(os.path.join(settings.DATA, settings.COIN_IMAGE)).convert()
    player_image = pygame.image.load(os.path.join(settings.DATA, settings.PLAYER_IMAGE)).convert()
    # 背景を作る
    Background(background_image, settings.SCREEN_SIZE)
    # プレーヤーを作る
    player = Player(player_image, settings.PLAYER_SIZE, screen_rect, coin_sprites)
    # プレーヤーがコインを獲得するときの効果音を取得する
    Player.coin_sound = pygame.mixer.Sound(os.path.join(settings.DATA, settings.COIN_SOUND))
    # クロック
    clock = pygame.time.Clock()
    # ゲームループ
    while True:
        # フレームレートの設定
        clock.tick(settings.FRAME_RATE)
        # スプライトを更新
        all_sprites.update()
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
        # コインを作る
        coin = Coin(coin_image, settings.COIN_SIZE, screen_rect)
        # コインをグループに追加する
        coin_sprites.add(coin)
