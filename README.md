<div align="center">

# 🧠 Pre-Meeting Briefing Agent

### Walk into every meeting already knowing what happened this month.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Tavily](https://img.shields.io/badge/Research-Tavily-6C5CE7)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?logo=google&logoColor=white)
![Hackathon](https://img.shields.io/badge/Geek%20Room%20x%20HackCulture-AI%20Hackathon%202026-ec4899)

**🚀 [Try the live app](https://tavily-meeting-briefing-hpm3jbkwap5apyoz7jzmwa.streamlit.app/~/+/#tavily-research-agent)**

</div>

---

## 😩 The problem

Before an important meeting you end up with 15 browser tabs, half-remembered headlines, and AI summaries that sound confident but may be **made up**.

## ✨ Our solution

Type a **company or person** and a **meeting date**. In about a minute you get a **one-page, source-backed briefing** covering the **previous 30 days**: news, launches, hires, business moves, plus **discussion points** and **open questions** you can actually use in the room.

Every finding has a **dated source link**. Anything we couldn't verify goes into an **Evidence Gaps** section instead of being invented.

---

## 🔄 How it works

```
 📝 You enter              🔎 Tavily                 🧹 Filter & clean          🤖 Gemini               📄 You get
 company / person   ->   6 focused web      ->    keep only sources    ->   writes the        ->   briefing in app
 date, time, zone        searches                 from the 30-day           briefing from           + one-page PDF
 purpose, context                                 window, remove dupes      the evidence only
```

| Step | What happens |
|------|--------------|
| 1. Input | Name, context, meeting purpose, date, time, timezone |
| 2. Research | 6 focused Tavily searches: news, launches, leadership and hires, business developments, announcements, other updates |
| 3. Filter | Reads publication dates, keeps `meeting date - 30 days` to `meeting date - 1 day`, removes duplicates |
| 4. Analyse | Gemini writes the briefing using only the collected evidence |
| 5. Export | Read it in the app or download the PDF |

---

## 📋 What's inside every briefing

| Section | Why it helps |
|---------|--------------|
| 🎯 Executive Snapshot | Understand the whole situation in 20 seconds |
| 📰 Important Recent Developments | What actually happened, with dates and links |
| 🤝 What This Means for the Meeting | Connects the news to *your* meeting purpose |
| 💬 Suggested Discussion Points | Ready-made talking points |
| ❓ Open Questions | Smart questions to ask |
| ⚠️ Evidence Gaps | What we could not confirm, shown honestly |
| 🔗 Research Sources | Every link so you can verify |

---

## 🛡️ Built to avoid made-up facts

- ✅ Every claim comes from a **dated, linked source**
- ✅ Sources **outside the 30-day window are excluded**
- ✅ Duplicate sources are removed
- ✅ Unknown or missing info is flagged under **Evidence Gaps**
- ✅ Retries plus a **fallback Gemini model** so the demo stays reliable

---

## 🧰 Tech stack

| Part | Tool |
|------|------|
| Interface | Streamlit |
| Web research | Tavily Search API |
| AI analysis | Google Gemini API (`google-genai`) |
| PDF export | ReportLab |
| Language | Python |

---

## ▶️ Run it yourself

```bash
# 1. Install requirements
pip install -r requirements.txt

# 2. Add your keys in .streamlit/secrets.toml
#    TAVILY_API_KEY = "your-tavily-key"
#    GEMINI_API_KEY = "your-gemini-key"

# 3. Start the app
streamlit run app.py
```

🔒 `secrets.toml` is git-ignored. Never commit your keys.

---

## 🧪 Tested with

- 🏢 Google
- 🏢 Microsoft
- 👤 Sundar Pichai

---

## 🔌 A note on Bifrost

The challenge suggests Bifrost for model requests. We installed it locally, configured Gemini as a provider, and successfully sent a Gemini request through its OpenAI-compatible endpoint. We could not get the Google GenAI SDK route working inside our app in time, so the final version calls Gemini directly. Bifrost is not part of the final app.

---

## ⚠️ Limitations

- Quality depends on what Tavily can find and date. Lesser-known companies or people may get thinner briefings.
- Treat the briefing as preparation. Verify critical facts in the linked sources.

---

## 👥 Team

| Member | Contribution |
|--------|--------------|
| **Satvik** | ADD-ROLE (for example: app design, Python code, Tavily and Gemini integration, PDF export, deployment) |
| **TEAMMATE-NAME** | ADD-ROLE (only what they really did, such as testing, research, docs, slides) |

---

## 🤖 AI assistance disclosure

AI assistants were used for guidance and code help during development. Edit this line to match what you actually did and what the hackathon rules require.

---

<div align="center">

Built for the **Geek Room x HackCulture Global AI Hackathon 2026** · Problem Statement 05

</div>
