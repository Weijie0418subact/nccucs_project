# 🎵 Python Scrolling Lyric Player (滾動逐字歌詞播放器)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

這是一個基於 Python 開發的**輕量化歌詞播放器**，支援滾動效果與逐字高亮顯示。適合用於個人音樂練習、KTV 模擬或是作為桌面小工具。

---

## ✨ 核心亮點

* **逐字同步 (Karaoke Style)：** 精確解析 LRC 擴充格式，達成逐字高亮。
* **平滑滾動：** 歌詞隨音軌進度自動位移，確保當前句子始終處於視覺中心。
* **自定義界面：** 支援調整字體大小、高亮顏色及背景透明度。
* **跨平台支援：** 只要有 Python 環境，無論 Windows、macOS 或 Linux 皆可運行。

---

## ⚙️ 運作邏輯

本專案的核心在於將音訊的時間戳（Timestamp）與歌詞內容進行即時比對與渲染。



1.  **解析 (Parsing)：** 讀取 `.lrc` 檔案，提取 `[mm:ss.xx]` 時間標籤。
2.  **同步 (Sync)：** 使用 `pygame.mixer` 或 `time` 模組獲取當前播放秒數。
3.  **渲染 (Rendering)：** 根據當前時間 $t$ 計算歌詞在螢幕上的偏移量 $y = f(t)$ 並刷新畫面。

---

## 🛠 安裝步驟

### 1. 複製本專案
2. 安裝依賴庫
建議使用虛擬環境，並安裝必要函式庫（以 Pygame 為例）：

Bash
pip install pygame
3. 準備檔案
確保你的音樂檔 (.mp3) 與歌詞檔 (.lrc) 檔名一致並放在同個資料夾：

song.mp3

song.lrc

🚀 快速上手
執行主程式並載入你的音樂：

Bash
python main.py --file "assets/my_song.mp3"
📂 專案結構
Plaintext
.
├── main.py              # 主程式進入點
├── core/
│   ├── parser.py        # 歌詞解析邏輯
│   └── player.py        # 音訊控制與同步
├── ui/
│   └── renderer.py      # UI 渲染與滾動動畫
└── assets/              # 存放音樂與字體檔案
📝 授權協議 (License)
本專案採用 MIT License。你可以自由地使用、修改並分發此程式碼。

🤝 貢獻指南
歡迎任何形式的貢獻！如果你有新的想法（如：桌面懸浮窗、網路歌詞自動搜尋），請隨時提交 Issue 或 Pull Request。

小提醒： 如果遇到歌詞編碼錯誤（亂碼），請檢查 .lrc 檔案是否為 UTF-8 編碼。```bash
git clone [https://github.com/你的用戶名/your-lyric-player.git](https://github.com/你的用戶名/your-lyric-player.git)
cd your-lyric-player
