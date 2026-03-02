# MyDJAutoPost 🤖📱

使用 Google Gemini AI 自動產生文章內容，並透過 GitHub Actions 定時發佈到 Facebook 粉絲專頁。

## 功能

- 🤖 使用 Gemini AI 自動產生貼文內容
- 📅 每天台灣時間 09:00 自動發文
- 🔧 支援手動觸發測試
- 🔒 使用 GitHub Secrets 安全管理金鑰

## 設定步驟

### 1. 取得 Gemini API Key

前往 [Google AI Studio](https://aistudio.google.com/apikey) 取得 API Key。

### 2. 取得 Facebook Page Access Token

1. 到 [Facebook Developers](https://developers.facebook.com/) 建立應用程式
2. 使用 [Graph API Explorer](https://developers.facebook.com/tools/explorer/) 取得 Page Access Token
3. 將短期 Token 轉換為永久 Token

### 3. 設定 GitHub Secrets

在 repo 的 **Settings → Secrets and variables → Actions** 新增：

| Secret Name | 說明 |
|---|---|
| `GEMINI_API_KEY` | Google Gemini API Key |
| `FB_PAGE_ID` | Facebook 粉絲專頁 ID |
| `FB_PAGE_ACCESS_TOKEN` | Facebook 永久 Page Access Token |

### 4. 測試

到 **Actions** 分頁，選擇 **Auto Post to Facebook**，點擊 **Run workflow** 手動觸發測試。

## 自訂發文主題

編輯 `post.py` 中的 `prompt` 變數來修改 AI 產生文章的主題和風格。

## 修改發文頻率

編輯 `.github/workflows/fb-post.yml` 中的 `cron` 表達式：

| Cron 表達式 | 說明 |
|---|---|
| `0 1 * * *` | 每天台灣時間 09:00 |
| `0 1 * * 1` | 每週一台灣時間 09:00 |
| `0 1,7 * * *` | 每天台灣時間 09:00 和 15:00 |
