import os
import re
import datetime
import zoneinfo
import requests

def get_emoji_data(day_index):
    url = "https://unpkg.com/unicode-emoji-json/data-ordered-emoji.json"
    meta_url = "https://unpkg.com/unicode-emoji-json/data-by-emoji.json"
    
    # Critical: Use a User-Agent so the CDN doesn't block the GitHub Action runner
    headers = {'User-Agent': 'GitHubAction-EmojiUpdate-Bot'}

    try:
        all_emojis = requests.get(url, headers=headers, timeout=10).json()
        meta_data = requests.get(meta_url, headers=headers, timeout=10).json()

        # 1. Read the user's custom start offset from the environment variable
        # Default to 564 if the variable is missing or empty
        env_offset = os.environ.get("START_OFFSET", "564")
        
        # 2. Safety check: Ensure the input is actually a valid number
        if env_offset.isdigit():
            start_offset = int(env_offset)
        else:
            print(f"Warning: '{env_offset}' is not a valid number. Falling back to 564.")
            start_offset = 564

        print(f"Using starting offset index: {start_offset}")

        # 3. Calculate index based on the user's custom offset
        index = (start_offset + (day_index - 1)) % len(all_emojis)
        selected_char = all_emojis[index]
        
        name = meta_data.get(selected_char, {}).get('name', 'Unknown')
        return selected_char, name.title()

    except Exception as e:
        print(f"Error fetching emoji data: {e}")
        return "✨", "Sparkles" # Fallback emoji

def update_readme():
    now = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Bangkok"))
    day_of_year = int(now.strftime("%j"))
    total_days_this_year = int(datetime.date(now.year, 12, 31).strftime("%j"))
    date_str = now.strftime("%d %B %Y")

    char, name = get_emoji_data(day_of_year)
    
    # Generate the Markdown block to inject
    display_text = (
        f"<!-- EMOJI_CLOCK_START -->\n"
        f"### 🗓️ Today is {date_str}\n"
        f"# {char}\n"
        f"**Daily Emoji:** {name}  \n"
        f"**Day:** {day_of_year} / {total_days_this_year}  \n"
        f"<!-- EMOJI_CLOCK_END -->"
    )

    # Initialize README.md with placeholders if it doesn't exist
    if not os.path.exists("README.md"):
        print("README.md not found. Creating a new one.")
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("<!-- EMOJI_CLOCK_START -->\n<!-- EMOJI_CLOCK_END -->")

    # Read current content
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # If placeholders are completely missing from an existing README, append them to the top
    if "<!-- EMOJI_CLOCK_START -->" not in content:
        print("Placeholders missing. Appending block to the top of README.md.")
        content = "<!-- EMOJI_CLOCK_START -->\n<!-- EMOJI_CLOCK_END -->\n\n" + content

    # Swap out everything between the target tags with our updated Markdown text
    new_content = re.sub(r"<!-- EMOJI_CLOCK_START -->.*?<!-- EMOJI_CLOCK_END -->", 
                         display_text, content, count=1, flags=re.DOTALL)

    # Write the modified content back out to disk
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README.md successfully updated with the daily emoji!")

if __name__ == "__main__":
    update_readme()