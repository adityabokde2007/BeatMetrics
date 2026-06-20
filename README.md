<div align="center">
  <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" width="100" alt="Python Logo">

  <h1> BeatMetrics</h1>
  <p><strong>Premium Spotify Music Intelligence Dashboard</strong></p>

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
    <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
    <a href="https://plotly.com/"><img src="https://img.shields.io/badge/Visualization-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" /></a>
    <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" /></a>
  </p>
</div>

---

## About BeatMetrics
**BeatMetrics** is a sophisticated, data-driven web application designed for deep exploratory analysis of Spotify music data. Developed as a comprehensive data science portfolio project, it transforms raw audio features and metadata into actionable insights through an elegant, high-performance interface.

Engineered with **Streamlit** and **Plotly**, BeatMetrics eschews standard templates for a custom, premium dark-mode aesthetic—reminiscent of professional enterprise tools like Bloomberg Terminals or Linear.app. It guarantees rapid data filtering and rendering while delivering an immaculate user experience.

---

## Key Features & Analytics

BeatMetrics offers a tailored, interactive experience for exploring music datasets:

### 1. Dynamic Filtering System
The heart of the dashboard, allowing granular data slicing.
- **Categorical Filters:** Instantly isolate tracks by specific Genres or Decades.
- **Popularity Range:** Fine-tune the dataset using an interactive popularity slider.
- **Real-Time Updates:** All visualizations and metrics instantaneously recalculate based on active filters.

### 2. Executive KPI Cards
High-level institutional monitoring at a glance.
- **Volume Metrics:** Track total song counts and unique artist footprints.
- **Audio Signatures:** Real-time averages for Popularity, Danceability, and Energy across the filtered subset.

### 3. Advanced Visualizations
7 deeply integrated, interactive Plotly charts designed for analytical rigor:
- **Genre & Artist Dominance:** Horizontal bar charts detailing the Top 10 Genres and Artists by volume.
- **Temporal Trends:** Area charts mapping the evolution of track popularity over the years.
- **Audio Feature Correlation:** Scatter plots dissecting the relationship between Energy and Danceability.
- **Decade Analysis:** Grouped bar charts comparing Valence, Energy, and Danceability across different eras.
- **Acoustic Profiling:** A custom Radar (Spider) chart mapping the 6 primary audio features of the dataset.
- **Distribution Histograms:** Detailed breakdowns of popularity score frequencies.

### 4. Raw Data Access
- **Top 20 Leaderboard:** An interactive data table displaying the most popular tracks that meet the current filter criteria, complete with full metadata.

---

## Technical Architecture & Stack

### Application Layer
- **Language:** Python 3.x
- **Framework:** Streamlit
- **UI/UX:** Custom CSS injections utilizing the `Inter` font, stripped-down borders, and a sophisticated muted gold (`#C0A060`) on deep black (`#0f0f0f`) color palette.
- **State Management:** Utilizes Streamlit's `@st.cache_data` for highly optimized, memory-efficient data loading and processing.

### Data & Visualization Engine
- **Data Processing:** Pandas (Handling large CSV datasets, null dropping, feature engineering like decade extraction and ms-to-min conversion).
- **Visualization:** Plotly Express & Plotly Graph Objects for fluid, interactive, and beautifully styled charts with custom gridlines and hover states.

---

## Aesthetics & UI/UX Posture
Visual presentation is paramount in BeatMetrics. 
- **Premium Palette:** Muted amber/gold accents against a dense `#0f0f0f` background.
- **Minimalist Design:** Zero gradients, zero neon colors, and zero extraneous borders.
- **Data-First Layout:** The UI gets out of the way so the data can speak, using subtle `#242424` borders and `#161616` card backgrounds.

---

## Installation & Setup Guide

### Prerequisites
- **Python:** Version 3.8 or higher.
- **Git:** For cloning the repository.

### Build Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/BeatMetrics.git
   cd BeatMetrics
   ```
2. **Setup Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install streamlit pandas plotly
   ```
4. **Data Configuration:**
   - Ensure the `spotify_data.csv` dataset is present in the root directory.
5. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

---

## Codebase Anatomy
```text
BeatMetrics/
├── app.py                 # Main Streamlit application and UI engine
├── spotify_data.csv       # Core dataset (Ignored in git via .gitignore)
├── analysis.ipynb         # Jupyter Notebook containing raw Exploratory Data Analysis (EDA)
├── .gitignore             # Configured for Python, Streamlit, and large datasets
└── README.md              # Project documentation
```

---

## Contributing
Contributions, issues, and feature requests are highly welcome! 
1. Fork the project.
2. Create your feature branch: `git checkout -b feature/NewAnalytics`
3. Commit your changes: `git commit -m 'Add new acousticness scatter plot'`
4. Push to the branch: `git push origin feature/NewAnalytics`
5. Open a Pull Request.

---

<p align="center">
  <i>Architected & Developed with ❤️ by Aditya Bokde for the Data Science Portfolio.</i>
</p>
