<!-- EMOJI_CLOCK_START -->
### 🗓️ Today is 13 June 2026
# 🥭
**Daily Emoji:** Mango  
**Day:** 164 / 365  
<!-- EMOJI_CLOCK_END -->

---

Automatically updates your README with a **daily emoji** based on a customizable starting index.

## 🚀 Setup for Your Own Repo

If you want to fork this and use it yourself, follow these steps:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Create a Workflow File:**
    In your repository, create a file at .github/workflows/date_to_emote.yml and add the following step to your workflow job:
    ```
    - name: Run Emoji Update
      uses: YourGitHubUsername/date-to-emote@v1.0.0
      with:
        start_offset: '120' # Optional: Adjusts the starting index for the emoji selection
    ```
3.  **Trigger the Action:**
    Commit the workflow file. Navigate to the **Actions** tab in your GitHub repository, select the workflow, and manually trigger it to see it update your file for the first time!

---

## 🛠️ How This Emoji Clock Works

This repository uses **GitHub Actions** and **Python** to dynamically update the profile header based on the current calendar day.

### 🏗️ Architecture

The system is built with a modular structure to ensure clean code and easy maintenance:

1. **Trigger:** A GitHub Action defined in `.github/workflows/date_to_emote.yml` runs on a `cron` schedule (every day at midnight Bangkok time).
2. **Environment:** GitHub spins up a virtual Ubuntu environment and installs dependencies from `requirements.txt`.
3. **Logic:** The script `scripts/update_emoji.py` calculates the **Day of the Year** (1-365) and uses it as an index to select a unique emoji.
4. **Injection:** The script uses Regex to find the `<!-- EMOJI_CLOCK_START -->` tags and replaces the content with fresh data.
5. **Deployment:** The Action commits the changes back to the repository automatically.

### 📁 File Structure

```text
date-to-emote/
├── .github/
│   ├── workflows/
│   │   └── date_to_emote.yml  # Workflow configuration to run the action
│   └── CODE_OF_CONDUCT.md        # Sets community boundaries & maintenance expectations
├── scripts/
│   └── update_emoji.py       # Python logic for emoji selection
├── LICENSE                   # MIT License
├── README.md                 # Updated with acknowledgements & documentation
├── action.yml                # Metadata file defining the GitHub Action inputs/outputs
└── requirements.txt          # Python dependencies (e.g., requests, emoji)
```

## Acknowledgements

This GitHub Action uses emoji data sourced from [unicode-emoji-json](https://github.com/muan/unicode-emoji-json), which is licensed under the MIT License, and contains data derived from the [Unicode Consortium](https://www.unicode.org/).

_Auto-updated via GitHub Actions._
