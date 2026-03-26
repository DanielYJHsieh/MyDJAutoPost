import subprocess
from datetime import datetime, timezone, timedelta


def write_datetime_to_file():
    """將當天日期時間寫入 action2_test.txt"""
    # 使用台灣時間 (UTC+8)
    tw_tz = timezone(timedelta(hours=8))
    now = datetime.now(tw_tz)
    date_str = now.strftime("%Y/%m/%d %H:%M:%S")

    with open("action2_test.txt", "w", encoding="utf-8") as f:
        f.write(date_str + "\n")

    print(f"✅ 已寫入日期時間：{date_str}")
    return date_str


def auto_commit():
    """自動 commit 變更"""
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
    subprocess.run(["git", "add", "action2_test.txt"], check=True)
    subprocess.run(["git", "commit", "-m", "自動更新日期時間"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ 已自動 commit 並 push！")


if __name__ == "__main__":
    write_datetime_to_file()
    auto_commit()
