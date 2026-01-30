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
```bash
git clone [https://github.com/你的用戶名/your-lyric-player.git](https://github.com/你的用戶名/your-lyric-player.git)
cd your-lyric-player