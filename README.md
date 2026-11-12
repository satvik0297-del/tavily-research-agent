# 🔍 Tavily Research Agent
### AI-Powered Web Research and Report Generation

An AI-powered research application that combines "Tavily Search API" and "Google Gemini" to collect web information, analyse retrieved content, and generate structured research reports with source references.

🚀 Overview

Researching a topic often requires visiting multiple websites, collecting information, comparing findings, and organising everything into a readable report.

The Tavily Research Agent simplifies this process by automating web search and AI-powered research synthesis.

Users enter a research topic, Tavily retrieves relevant web sources, and Gemini analyses the collected information to generate a structured Markdown report.

🎯 Problem Statement

Manual web research can be time-consuming because users need to:

- Search across multiple websites.
- Read and organise information from different sources.
- Identify important findings and trends.
- Prepare structured research summaries.
- Keep track of the original sources.

The project aims to reduce this effort through an integrated web-search and AI-report-generation workflow.

💡 Our Solution

The Tavily Research Agent combines web search and generative AI in a simple Python application.

**The workflow:**

1. The user enters a research topic.
2. Tavily searches the web for relevant information.
3. The application collects up to five search results.
4. Gemini analyses the retrieved content.
5. The application generates a structured Markdown research report.
6. The report includes inline source links and a references section.

✨ Current Features

- Automated Web Search: Uses Tavily to retrieve relevant web information.
- Advanced Search: Uses Tavily's advanced search depth.
- AI-Powered Analysis: Uses Google Gemini to synthesise collected research.
- Structured Reports: Generates executive summaries, key insights, analysis, recommendations and references.
- Source References: Includes links to the original URLs returned by Tavily.
- Error Handling: Handles missing credentials, empty results and API errors.
- Secure API Configuration: Retrieves API keys from Google Colab Secrets instead of hardcoding credentials.

🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tavily Search API | Web search and information retrieval |
| Tavily Python SDK | Python integration with Tavily |
| Google Gemini API | Research synthesis and report generation |
| `google-genai` | Python integration with Gemini |
| IPython Markdown | Displays formatted research reports |
| Google Colab | Development and execution environment |

⚙️ Project Architecture

```text
             USER
               |
               v
       Research Topic Input
               |
               v
        Tavily Search API
               |
               v
       Retrieve Web Sources
               |
               v
       Organise Search Data
               |
               v
        Google Gemini API
               |
               v
       Research Synthesis
               |
               v
       Markdown Report
               |
               v
      Sources and References
```
📋 Requirements

- Python 3.10 or later (recommended).
- Google account with access to Google Colab.
- Tavily API key.
- Google Gemini API key.
- Internet connection.

🚀 Getting Started

1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/tavily-research-agent.git
```

Replace `YOUR-USERNAME` with your GitHub username.

2. Open Google Colab

Open the project notebook:

`Tavily_Research_Agent.ipynb`

Upload it to Google Colab or open it from your GitHub repository.

3. Configure API keys securely

In Google Colab:

1. Open the Secrets panel using the key icon on the left sidebar.
2. Add a secret named `TAVILY_API_KEY`.
3. Add another secret named `GEMINI_API_KEY`.
4. Paste the respective API keys into their secret values.
5. Enable notebook access for both secrets.

The notebook retrieves credentials using:

```python
from google.colab import userdata

TAVILY_API_KEY = userdata.get("TAVILY_API_KEY")
GEMINI_API_KEY = userdata.get("GEMINI_API_KEY")
```

**Never upload actual API keys to GitHub.**

4. Install dependencies

The notebook installs the required libraries:

```bash
pip install -q --upgrade tavily-python google-genai
```

5. Run the notebook

Run the notebook cells in order.

Enter a research topic when prompted.

Example:

```text
Artificial Intelligence: Latest Developments
```

The application will search the web and generate a structured research report.

📄 Report Structure

The generated report contains:

1. Executive Summary – Overview of the research topic and major findings.
2. Key Insights & Analysis – Important findings, trends, opportunities and challenges.
3. Actionable Takeaways / Future Outlook – Recommendations and possible future developments.
4. Sources & References– Titles and original URLs of retrieved sources.

⚠️ Current Limitations

The current implementation is a single-pass research pipeline.

- It retrieves up to five web search results per topic.
- It does not yet automatically create research sub-questions.
- It does not perform iterative research or autonomous re-search.
- Citations link to retrieved sources but are not independently validated against every factual claim.
- Report quality depends on the relevance and quality of retrieved webpage content.
- It currently runs through Google Colab rather than a standalone web interface.

These limitations are acknowledged as areas for future development.

🔮 Future Improvements

Planned enhancements include:

- Research planning and automatic question decomposition.
- Multiple focused web searches.
- Evidence organisation and source-quality analysis.
- Evidence-based citation validation.
- Bounded iterative research when important information is missing.
- Follow-up questions about generated reports.
- PDF report export.
- Interactive web interface using Streamlit.

👨‍💻 Project Information

Project: Tavily Research Agent  
Category: AI Agents & Intelligent Systems  
Hackathon: HackCulture Global AI Hackathon  
Core Technologies: Python, Tavily Search API and Google Gemini  
Platform: Google Colab

🙌 Acknowledgements

- [Tavily](https://tavily.com/) – Web search infrastructure for AI applications.
- [Google Gemini](https://ai.google.dev/) – Generative AI capabilities.
- [Google Colab](https://colab.research.google.com/) – Cloud-based Python development environment.

---

*Built as a hackathon prototype exploring AI-powered web research and automated report generation.*
