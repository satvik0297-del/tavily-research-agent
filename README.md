[README.md](https://github.com/user-attachments/files/34860134/README.md)
# 🔎 Tavily Research Agent

**AI-powered web research and report generation using Tavily Search,
Google Gemini, and Streamlit.**

[![Open Live
App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://tavily-research-agent-bbvuzfysablls7fow3ye.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Powered by
Tavily](https://img.shields.io/badge/Search-Tavily-5A45FF)](https://tavily.com/)
[![Powered by
Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4)](https://ai.google.dev/)

## Overview

Researching a topic manually can involve searching many websites,
comparing information, identifying gaps, and preparing a structured
report. **Tavily Research Agent** streamlines this process in a web
application.

A user enters a topic and chooses a research depth. Google Gemini
creates focused research questions and analyses the collected evidence.
Tavily Search retrieves relevant web results. The application organises
unique sources, may request a limited follow-up search when evidence
appears incomplete, and asks Gemini to generate a structured report with
references. The report can be downloaded as a PDF.

**Live application:** [Open Tavily Research
Agent](https://tavily-research-agent-bbvuzfysablls7fow3ye.streamlit.app/)

## Key features

-   **Research planning:** Gemini breaks the topic into focused research
    questions.
-   **Web search:** Tavily performs advanced web searches for the
    generated questions.
-   **Evidence collection:** Search results are organised and duplicate
    URLs are removed.
-   **Evidence review:** Gemini assesses whether the collected evidence
    is sufficient and can suggest follow-up queries.
-   **Bounded research loop:** The workflow limits the number of
    research rounds and searches.
-   **Structured report generation:** Gemini creates an organised
    Markdown report using the collected evidence.
-   **Source references:** The report maps generated source IDs to URLs
    returned by Tavily and includes a references section.
-   **Research depth options:** Quick, Standard, and Detailed modes
    adjust question and result limits.
-   **PDF export:** Users can download the generated report.
-   **Error handling and retries:** The application checks for missing
    API credentials, handles research errors, and retries failed Gemini
    requests.

> **Transparency note:** Source IDs are mapped to URLs returned by
> Tavily. The current prototype does not independently verify every
> factual claim against the full source webpage. Report quality depends
> on the retrieved search evidence and the model's synthesis.

## How it works

1.  **User input:** The user enters a research topic and chooses Quick,
    Standard, or Detailed.
2.  **Planning:** Gemini creates focused research questions.
3.  **Search:** Tavily searches the web for each question.
4.  **Collection:** Results are stored by URL to avoid duplicate
    sources.
5.  **Evidence review:** Gemini assesses evidence coverage and
    identifies possible gaps.
6.  **Follow-up:** If evidence is insufficient, the workflow can perform
    a bounded follow-up search.
7.  **Synthesis:** Gemini generates a structured report grounded in the
    collected evidence.
8.  **Output:** The app displays the report, search statistics, source
    links, and a PDF download option.

## Architecture

``` text
                 User
                  |
                  v
       Streamlit topic + depth input
                  |
                  v
        Gemini Research Planner
       (focused research questions)
                  |
                  v
          Tavily Search API
       (search each question)
                  |
                  v
       Evidence Collector
     (store results, deduplicate URLs)
                  |
                  v
        Gemini Evidence Review
       (coverage, gaps, follow-ups)
                  |
          evidence sufficient?
             /          \
           yes           no
            |             |
            |       Bounded follow-up
            |         Tavily search
            |             |
            +-------------+
                  |
                  v
        Gemini Report Generator
                  |
                  v
      Markdown report + source links
                  |
          Streamlit results UI
                  |
                  v
             PDF download
```

## Research depth

The current settings in `app.py` are:

  Mode         Planned questions   Results per search   Follow-up allowance
  ---------- ------------------- -------------------- ---------------------
  Quick                        2                    2                     1
  Standard                     4                    3                     2
  Detailed                     4                    5                     2

The workflow also has a maximum of two evidence-review rounds. Actual
search counts can be lower when evidence is sufficient or when the
search limit is reached.

## Technology stack

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Main application language

  Streamlit                           Interactive web interface and
                                      deployment

  Tavily Search API                   Web search and retrieval

  `tavily-python`                     Python SDK for Tavily

  Google Gemini API                   Research planning, evidence review,
                                      and report synthesis

  `google-genai`                      Python SDK for Gemini

  ReportLab                           PDF report generation

  IPython                             Retained as a project dependency
                                      for notebook development

  Google Colab                        Original notebook development
                                      environment

  Streamlit Community Cloud           Hosting the web application
  -----------------------------------------------------------------------

## Repository structure

``` text
tavily-research-agent/
├── app.py
├── requirements.txt
├── README.md
└── Tavily_Research_Agent.ipynb
```

-   `app.py` --- Streamlit application, research workflow, and PDF
    export.
-   `requirements.txt` --- Python dependencies.
-   `README.md` --- Project documentation.
-   `Tavily_Research_Agent.ipynb` --- Original Google Colab notebook
    prototype.

## Run locally

### 1. Clone the repository

``` bash
git clone https://github.com/satvik0297-del/tavily-research-agent.git
cd tavily-research-agent
```

### 2. Install dependencies

Use Python 3.10 or later.

``` bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**

``` powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

``` bash
source .venv/bin/activate
```

Install the project packages:

``` bash
pip install -r requirements.txt
```

### 3. Configure API keys

The app needs: - `TAVILY_API_KEY` - `GEMINI_API_KEY`

For local development, create `.streamlit/secrets.toml` in the project
directory:

``` toml
TAVILY_API_KEY = "your_tavily_api_key"
GEMINI_API_KEY = "your_gemini_api_key"
```

Do not commit this file or publish API keys. Add
`.streamlit/secrets.toml` to `.gitignore`.

For the deployed app, configure the same two values in the app's
**Streamlit Community Cloud → App settings → Secrets** area.

### 4. Start the app

``` bash
streamlit run app.py
```

Open the local URL printed in the terminal (usually
`http://localhost:8501`).

## Using the live application

1.  Open the [live
    app](https://tavily-research-agent-bbvuzfysablls7fow3ye.streamlit.app/).
2.  Enter a clear research topic.
3.  Choose Quick, Standard, or Detailed.
4.  Click **Start Research**.
5.  Wait for the research process to complete.
6.  Review the report, statistics, and collected source links.
7.  Click the PDF download button to save the report.

**Example topic:**\
`How is artificial intelligence changing healthcare, education, and software development?`

## Configuration and security

-   Never hardcode API keys in source files.
-   Never commit `.streamlit/secrets.toml`, `.env`, or other credential
    files.
-   Keep Streamlit Cloud secrets private.
-   If a key was accidentally committed, revoke it at the provider and
    create a replacement; deleting it from the latest file alone is not
    sufficient.
-   Avoid sharing screenshots that show secret values.

## Current limitations and future improvements

This is a working hackathon prototype. Possible next improvements
include:

-   More robust Markdown-to-PDF formatting for tables, emphasis, and
    links.
-   Stronger source-quality assessment and independent claim-to-source
    verification.
-   Better handling of conflicting or outdated sources.
-   Research history and the ability to revisit previous reports.
-   Export to Markdown and DOCX.
-   Automated tests with mocked Tavily and Gemini responses.
-   More detailed progress indicators and clearer usage guidance.

## Project information

-   **Project:** Tavily Research Agent
-   **Category:** AI Agents / Intelligent Research
-   **Hackathon:** HackCulture Global AI Hackathon
-   **Core technologies:** Python, Tavily Search API, Google Gemini,
    Streamlit
-   **Live demo:** [Streamlit
    application](https://tavily-research-agent-bbvuzfysablls7fow3ye.streamlit.app/)
-   **Source code:** [GitHub
    repository](https://github.com/satvik0297-del/tavily-research-agent)

## Acknowledgements

-   [Tavily](https://tavily.com/) --- Web search infrastructure.
-   [Google AI / Gemini](https://ai.google.dev/) --- Generative AI
    models and API.
-   [Streamlit](https://streamlit.io/) --- Interactive Python web
    applications.
-   [ReportLab](https://www.reportlab.com/) --- PDF generation.
-   [Google Colab](https://colab.research.google.com/) --- Notebook
    development environment.

------------------------------------------------------------------------

*Built as a hackathon prototype to explore AI-assisted web research,
evidence review, and automated report generation.*
