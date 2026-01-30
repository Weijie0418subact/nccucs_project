import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor, QPalette
import pygame

class LyricsPlayer(QWidget):
    def __init__(self, lyrics_data):
        super().__init__()
        self.lyrics_data = lyrics_data
        self.init_ui()
        
        # 初始化音頻
        pygame.mixer.init()
        pygame.mixer.music.load("song.mp3") # 請確保目錄下有這檔案
        pygame.mixer.music.play()

        # 定時器：每 10 毫秒檢查一次進度
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_lyrics)
        self.timer.start(10)

    def init_ui(self):
        self.setWindowTitle("Python Dynamic Lyrics Player")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #121212;") # 深色主題

        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.container = QWidget()
        self.container_layout = QVBoxLayout()

        self.word_labels = []
        
        # 建立歌詞標籤
        for item in self.lyrics_data:
            label = QLabel(item['word'])
            label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
            label.setStyleSheet("color: #444444;") # 預設灰色
            self.container_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
            self.word_labels.append(label)

        self.container.setLayout(self.container_layout)
        self.scroll_area.setWidget(self.container)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

    def update_lyrics(self):
        # 獲取當前音樂播放時間（秒）
        current_time = pygame.mixer.music.get_pos() / 1000.0

        for i, item in enumerate(self.lyrics_data):
            # 邏輯：如果當前時間落在單字的開始與結束之間
            if item['start'] <= current_time <= item['end']:
                self.word_labels[i].setStyleSheet("color: #FFFFFF;") # 正在唱：白色
                # 自動捲動到當前單字位置
                self.scroll_area.ensureWidgetVisible(self.word_labels[i])
            elif current_time > item['end']:
                self.word_labels[i].setStyleSheet("color: #AAAAAA;") # 唱過了：淺灰

if __name__ == "__main__":
    # 範例測試資料
    sample_lyrics = [
        {"start": 1.0, "end": 1.5, "word": "Hello"},
        {"start": 1.6, "end": 2.2, "word": "this"},
        {"start": 2.3, "end": 2.8, "word": "is"},
        {"start": 2.9, "end": 3.5, "word": "Apple"},
        {"start": 3.6, "end": 4.2, "word": "Music"},
        {"start": 4.3, "end": 5.0, "word": "Style!"},
    ]

    app = QApplication(sys.argv)
    player = LyricsPlayer(sample_lyrics)
    player.show()
    sys.exit(app.exec())