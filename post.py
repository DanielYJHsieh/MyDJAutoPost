import os
import google.generativeai as genai
import requests


def generate_content():
    """使用 Gemini AI 產生 Facebook 貼文內容"""
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = """
    你是一個社群媒體小編。
    請幫我寫一篇適合 Facebook 粉絲專頁的短文（150字以內）。
    主題：今天的科技新知或生活小技巧。
    風格：輕鬆、親切、帶一點 emoji。
    最後加上 2-3 個 hashtag。
    只要輸出貼文內容，不要加任何前綴說明。
    """

    response = model.generate_content(prompt)
    return response.text


def post_to_facebook(content):
    """將內容發佈到 Facebook 粉絲專頁"""
    page_id = os.environ["FB_PAGE_ID"]
    access_token = os.environ["FB_PAGE_ACCESS_TOKEN"]

    url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
    response = requests.post(url, data={
        "message": content,
        "access_token": access_token
    })

    if response.status_code == 200:
        post_id = response.json().get("id")
        print(f"✅ 發文成功！Post ID: {post_id}")
    else:
        try:
            error = response.json().get("error", {})
            print(f"❌ 發文失敗：代碼 {error.get('code')} - {error.get('message')}")
        except Exception:
            print(f"❌ 發文失敗：{response.text}")
        exit(1)


if __name__ == "__main__":
    print("🤖 正在使用 Gemini AI 產生文章...")
    content = generate_content()
    print(f"📝 產生的文章：\n{content}\n")

    print("📤 正在發佈到 Facebook...")
    post_to_facebook(content)
