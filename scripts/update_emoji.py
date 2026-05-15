import datetime
import zoneinfo
import re
import os
import requests
import json

def get_emoji_data(day_index):
    # Official Unicode/CLDR ordered JSON
    url = "https://unpkg.com/unicode-emoji-json/data-ordered-emoji.json"
    meta_url = "https://unpkg.com/unicode-emoji-json/data-by-emoji.json"
    
    # Critical: Use a User-Agent so the CDN doesn't block the GitHub Action runner
    headers = {'User-Agent': 'GitHubAction-EmojiUpdate-Bot'}

    try:
        all_emojis = requests.get(url, headers=headers, timeout=10).json()
        meta_data = requests.get(meta_url, headers=headers, timeout=10).json()

        # Your specific offset logic
        start_offset = 564
        index = (start_offset + (day_index - 1)) % len(all_emojis)
        selected_char = all_emojis[index]
        
        name = meta_data.get(selected_char, {}).get('name', 'Unknown')
        return selected_char, name.title()

    except Exception as e:
        print(f"Error: {e}")
        return "✨", "Sparkles" # Fallback emoji

def update_readme():
    now = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Bangkok"))
    day_of_year = int(now.strftime("%j"))
    date_str = now.strftime("%d %B %Y")

    char, name = get_emoji_data(day_of_year)
    
    display_text = (
        f"<!-- EMOJI_CLOCK_START -->\n"
        f"### 🗓️ Today is {date_str}\n"
        f"# {char}\n"
        f"**Daily Emoji:** {name}  \n"
        f"**Day of the Year:** {day_of_year} / 365  \n"
        f"<!-- EMOJI_CLOCK_END -->"
    )

    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("<!-- EMOJI_CLOCK_START -->\n<!-- EMOJI_CLOCK_END -->")

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(r"<!-- EMOJI_CLOCK_START -->.*?<!-- EMOJI_CLOCK_END -->", 
                         display_text, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()