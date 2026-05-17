---
<!-- EMOJI_CLOCK_START -->
### 🗓️ Today is 18 May 2026
# 🪻
**Daily Emoji:** Hyacinth  
**Day of the Year:** 138 / 365  
<!-- EMOJI_CLOCK_END -->
---

---

## 🚀 Setup for Your Own Repo

If you want to fork this and use it yourself, follow these steps:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Install Dependencies (Local Testing):**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Add Your Markers:**
    Ensure your `README.md` has the following hidden comments:

    ```markdown
    <!-- EMOJI_CLOCK_START -->
### 🗓️ Today is 18 May 2026
# 🪻
**Daily Emoji:** Hyacinth  
**Day of the Year:** 138 / 365  
<!-- EMOJI_CLOCK_END -->

    ```

4.  **Push to GitHub:**
    Once pushed, navigate to the **Actions** tab in your GitHub repository and manually trigger the "Emoji Clock Workflow" to see it work for the first time!

---

## 🛠️ How This Emoji Clock Works

This repository uses **GitHub Actions** and **Python** to dynamically update the profile header based on the current calendar day.

### 🏗️ Architecture

The system is built with a modular structure to ensure clean code and easy maintenance:

1.  **Trigger:** A GitHub Action defined in `.github/workflows/date_to_emote.yml` runs on a `cron` schedule (every day at midnight Bangkok time).
2.  **Environment:** GitHub spins up a virtual Ubuntu environment and installs dependencies from `requirements.txt`.
3.  **Logic:** The script `scripts/update_emoji.py` calculates the **Day of the Year** (1-365) and uses it as an index to select a unique emoji from the `emoji` Python library.
4.  **Injection:** The script uses Regex to find the `<!-- EMOJI_CLOCK_START -->` tags and replaces the content with fresh data.
5.  **Deployment:** The Action commits the changes back to the repository automatically.

### 📁 File Structure

```text
├── .github/workflows/
│   └── date_to_emote.yml    # Workflow configuration
├── scripts/
│   └── update_emoji.py    # Python logic for emoji selection
├── README.md              # The file you are reading now!
├── requirements.txt       # Python dependencies (emoji)
└── .gitignore             # Prevents junk files from being uploaded
```

_Auto-updated via GitHub Actions._
