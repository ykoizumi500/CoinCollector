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

    def __init__(self, image, size, coin, score, time):
        super().__init__(self.containers)
        # 画像を読み込む
        self.image = pygame.transform.scale(image, size)
        # 外縁を消す
        self.image.set_colorkey([0, 0, 0])
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # スクリーンの参照
        self.range = pygame.Rect(settings.PLAYER_MIN, settings.PLAYER_RANGE)
        # コインの参照
        self.coin = coin
        # スコアの参照
        self.score = score
        # 残り時間の参照
        self.time = time
        # 位置を決める
        self.rect.centerx = settings.PLAYER_X
        self.rect.centery = settings.PLAYER_Y


    def move(self, right: int, down: int) -> None:
        """プレーヤを移動させる。

        Args:
            right (int): 右に移動させる距離
            down (int): 下に移動させる距離
        """
        # プレーヤーを移動させる
        self.rect.move_ip(right * self.speed, down * self.speed)
        # 外枠に衝突した時の処理
        self.rect = self.rect.clamp(self.range)
        # コインに衝突したときの処理
        if pygame.sprite.spritecollide(self, self.coin, True):
            # スコアを加える
            self.score.add_score(settings.COIN_SCORE)
            # 残り時間を加える
            self.time.add_time(settings.COIN_TIME)
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
        self.rect.centerx = random.randint(*settings.COIN_X_RANGE)
        self.rect.centery = random.randint(*settings.COIN_Y_RANGE)
        # コインの速度をランダムに決める
        self.velocity_x = random.randint(*settings.COIN_VELOCITY_X_RANGE)
        self.velocity_y = random.randint(*settings.COIN_VELOCITY_Y_RANGE)
        # スクリーンの参照
        self.screen = screen

    def update(self):
        """画面の更新

        """
        # 重力での移動
        self.rect.move_ip(int(self.velocity_x), int(self.velocity_y))
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


class Score(pygame.sprite.Sprite):
    """スコア表示

    """

    def __init__(self, screen):
        super().__init__(self.containers)
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スコアの設定
        self.score = 0
        # スクリーンの参照
        self.screen = screen
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


class Time(pygame.sprite.Sprite):
    """残り時間表示

    """

    def __init__(self, screen, time):
        super().__init__(self.containers)
        # フォントの設定
        self.sysfont = pygame.font.SysFont(None, settings.SCORE_SIZE)
        # スクリーンの参照
        self.screen = screen
        # 残り時間の設定
        self.time = time
        # 時間の描画
        self.draw()


    def draw(self) -> None:
        """描画

        """
        # スコアの表示形式を設定する
        self.image = self.sysfont.render("{:.2f}".format(self.time / settings.FRAME_RATE), True, settings.SCORE_COLOR)
        # Rect（四角）オブジェクトも生成しておく
        self.rect = self.image.get_rect()
        # 位置を右にする
        self.rect.right = self.screen.right

    def add_time(self, time: int) -> bool:
        """残り時間の追加

        Args:
            time (int): 加える時間
        """
        # 時間を加える
        self.time += time
        # 時間の描画
        self.draw()
        return self.time > 0

    def set_time(self, time: int) -> None:
        """時間を設定する

        """
        # 時間を設定する
        self.time = time
        # 時間の描画
        self.draw()


class Game:
    """ ゲーム

    """
    def __init__(self):
        # 初期化
        pygame.init()
        # 画面のサイズを設定する
        self.screen = pygame.display.set_mode(settings.SCREEN_SIZE)
        self.screen_rect = pygame.Rect([0, 0], settings.SCREEN_SIZE)
        pygame.display.set_caption(settings.TITLE)
        # スプライトでまとめる
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.coin_sprites = pygame.sprite.Group()
        Player.containers = self.all_sprites
        Coin.containers = self.coin_sprites, self.all_sprites
        Background.containers = self.all_sprites
        Score.containers = self.all_sprites
        Time.containers = self.all_sprites
        # データを読み込む
        self.load_data()
        # 背景を作る
        Background(self.background_image, settings.SCREEN_SIZE)
        # プレーヤーがコインを獲得するときの効果音を設定する
        Player.coin_sound = self.coin_sound
        # スコア表示を作る
        self.score = Score(self.screen_rect)
        # 時間表示を作る
        self.time = Time(self.screen_rect, settings.TIME_LIMIT)
        # プレーヤーを作る
        self.player = Player(self.player_image, settings.PLAYER_SIZE, self.coin_sprites, self.score, self.time)
        # クロック
        self.clock = pygame.time.Clock()
        # コインの周期のカウント
        self.coin_period = 0

    def play(self) -> int:
        """ ゲームループ

        """
        while True:
            # フレームレートの設定
            self.clock.tick(settings.FRAME_RATE)
            # スプライトを更新
            self.all_sprites.update()
            dirty = self.all_sprites.draw(self.screen)
            # 画面更新
            pygame.display.update(dirty)
            for event in pygame.event.get():
                # 閉じるボタンが押されたら
                if event.type == pygame.QUIT:
                    # 終了させる
                    return self.over()
            # キー操作の情報を受け取る
            keystate = pygame.key.get_pressed()
            # 右方向に移動する距離
            right = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
            # 下方向に移動する距離
            down = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
            # 移動させる
            self.player.move(right, down)
            # コインを出現させる時になったら
            if self.coin_period == settings.COIN_PERIOD:
                # コインを増やす
                self.add_coin()
                # コインの周期のカウントをリセットする
                self.coin_period = 0
            # コインの周期のカウントする
            self.coin_period += 1
            # 時間を減らして時間切れでないなら
            if not self.time.add_time(-1):
                return self.over()

    def over(self) -> int:
        # 残り時間をリセットする
        self.time.set_time(0)
        return self.score.get_score()

    def load_data(self) -> None:
        """ 画像を読み込む

        """
        self.background_image = pygame.image.load(os.path.join(settings.DATA, settings.BACKGROUND_IMAGE)).convert()
        self.coin_image = pygame.image.load(os.path.join(settings.DATA, settings.COIN_IMAGE)).convert()
        self.player_image = pygame.image.load(os.path.join(settings.DATA, settings.PLAYER_IMAGE)).convert()
        self.coin_sound = pygame.mixer.Sound(os.path.join(settings.DATA, settings.COIN_SOUND))

    def add_coin(self) -> None:
        """コインを増やす

        """
        # コインを作る
        coin = Coin(self.coin_image, settings.COIN_SIZE, self.screen_rect)
        # コインをグループに追加する
        self.coin_sprites.add(coin)


def main():
    """メイン

    """
    game = Game()
    # プレイを始める
    game.play()
