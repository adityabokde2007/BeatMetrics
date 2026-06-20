import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="BeatMetrics | Spotify Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background-color: #0f0f0f;
    color: #f0f0f0;
}

div[data-testid="stSidebarContent"] {
    background-color: #111111;
    border-right: 1px solid #242424;
}

div[data-testid="stMetric"] {
    background-color: #161616;
    border: 1px solid #242424;
    border-radius: 4px;
    padding: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #666666 !important;
    font-weight: 500;
    font-size: 13px;
}

div[data-testid="stMetricValue"] {
    color: #f0f0f0 !important;
    font-weight: 700;
    font-size: 24px;
}

.stSelectbox > div > div {
    background-color: #161616;
    border: 1px solid #242424;
    border-radius: 4px;
    color: #f0f0f0;
}

.stSlider > div > div > div > div {
    background-color: #C0A060;
}

h1, h2, h3 { color: #f0f0f0; font-weight: 700; }

.stDataFrame {
    border: 1px solid #242424;
    border-radius: 4px;
}

hr { border-color: #242424; }

.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    color: #C0A060;
    margin-bottom: 20px;
}

.section-header {
    font-size: 11px;
    font-weight: 600;
    color: #555555;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('spotify_data.csv')
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    df = df.dropna(subset=['artist_name', 'track_name'])
    df['duration_min'] = round(df['duration_ms'] / 60000, 2)
    df['decade'] = (df['year'] // 10) * 10
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file 'spotify_data.csv' not found.")
    st.stop()

st.sidebar.markdown('<div class="sidebar-title">BeatMetrics</div>', unsafe_allow_html=True)
st.sidebar.markdown('<p class="section-header">Filters</p>', unsafe_allow_html=True)

genres = ['All'] + sorted(df['genre'].astype(str).unique().tolist())
selected_genre = st.sidebar.selectbox("Genre", genres)

decades = ['All'] + sorted(df['decade'].dropna().astype(int).unique().tolist())
selected_decade = st.sidebar.selectbox("Decade", decades)

popularity_range = st.sidebar.slider("Popularity Range", 0, 100, (0, 100))

st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.markdown('<p class="section-header">Dataset Stats</p>', unsafe_allow_html=True)
st.sidebar.markdown(f"<span style='color:#666666; font-size:13px;'>Total Tracks:</span> <b style='color:#f0f0f0; font-size:13px;'>{len(df):,}</b>", unsafe_allow_html=True)
st.sidebar.markdown(f"<span style='color:#666666; font-size:13px;'>Unique Artists:</span> <b style='color:#f0f0f0; font-size:13px;'>{df['artist_name'].nunique():,}</b>", unsafe_allow_html=True)
st.sidebar.markdown(f"<span style='color:#666666; font-size:13px;'>Years:</span> <b style='color:#f0f0f0; font-size:13px;'>{int(df['year'].min())} - {int(df['year'].max())}</b>", unsafe_allow_html=True)

filtered_df = df.copy()
if selected_genre != 'All':
    filtered_df = filtered_df[filtered_df['genre'] == selected_genre]
if selected_decade != 'All':
    filtered_df = filtered_df[filtered_df['decade'] == selected_decade]

filtered_df = filtered_df[
    (filtered_df['popularity'] >= popularity_range[0]) &
    (filtered_df['popularity'] <= popularity_range[1])
]

st.markdown("""
    <h1 style='font-size:32px; font-weight:700; color:#f0f0f0; margin-bottom: 4px;'>BeatMetrics</h1>
    <p style='color:#666666; font-size:15px; font-weight:400; margin-bottom: 24px;'>Spotify Music Intelligence Dashboard</p>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Tracks", f"{len(filtered_df):,}")
col2.metric("Unique Artists", f"{filtered_df['artist_name'].nunique():,}")
col3.metric("Avg Popularity", f"{filtered_df['popularity'].mean():.1f}" if not filtered_df.empty else "0.0")
col4.metric("Avg Danceability", f"{filtered_df['danceability'].mean():.2f}" if not filtered_df.empty else "0.00")
col5.metric("Avg Energy", f"{filtered_df['energy'].mean():.2f}" if not filtered_df.empty else "0.00")

st.markdown("<br>", unsafe_allow_html=True)

PLOT_LAYOUT = dict(
    plot_bgcolor='#161616',
    paper_bgcolor='#161616',
    font=dict(color='#666666', family='Inter'),
    margin=dict(l=20, r=20, t=50, b=20),
    title=dict(font=dict(color='#999999', size=13, family='Inter', weight='normal')),
    xaxis=dict(gridcolor='#1e1e1e', linecolor='#242424', zerolinecolor='#242424', tickfont=dict(color='#555555'), title=dict(font=dict(color='#555555'))),
    yaxis=dict(gridcolor='#1e1e1e', linecolor='#242424', zerolinecolor='#242424', tickfont=dict(color='#555555'), title=dict(font=dict(color='#555555'))),
)

if not filtered_df.empty:
    r1c1, r1c2 = st.columns(2)

    with r1c1:
        genre_data = filtered_df['genre'].value_counts().head(10).reset_index()
        genre_data.columns = ['Genre', 'Count']
        genre_data['Count'] = pd.to_numeric(genre_data['Count'])
        genre_data = genre_data.sort_values('Count', ascending=True)
        fig1 = px.bar(
            genre_data, 
            x='Count', 
            y='Genre', 
            orientation='h',
            title='Top 10 Genres'
        )
        fig1.update_traces(marker_color='#C0A060', opacity=0.8)
        fig1.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig1, use_container_width=True)

    with r1c2:
        year_pop = filtered_df.groupby('year')['popularity'].mean().reset_index()
        fig2 = px.area(
            year_pop, 
            x='year', 
            y='popularity',
            title='Popularity Trend Over Years'
        )
        fig2.update_traces(line_color='#C0A060', line_width=2, fillcolor='rgba(192, 160, 96, 0.15)')
        fig2.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig2, use_container_width=True)

    r2c1, r2c2, r2c3 = st.columns(3)

    with r2c1:
        sample_df = filtered_df.sample(min(5000, len(filtered_df)), random_state=42)
        fig3 = px.scatter(
            sample_df, 
            x='danceability', 
            y='energy',
            title='Energy vs Danceability'
        )
        fig3.update_traces(marker=dict(color='#888888', size=3, opacity=0.3, line=dict(width=0)))
        fig3.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig3, use_container_width=True)

    with r2c2:
        decade_mood = filtered_df.groupby('decade')[['valence', 'energy', 'danceability']].mean().reset_index()
        fig4 = px.bar(
            decade_mood, 
            x='decade', 
            y=['valence', 'energy', 'danceability'],
            title='Mood & Energy by Decade',
            barmode='group',
            color_discrete_sequence=['#C0A060', '#8a7a5a', '#5a4a2a']
        )
        fig4.update_layout(**PLOT_LAYOUT)
        fig4.update_layout(legend=dict(title=dict(text='', font=dict(color='#555555')), font=dict(color='#555555')))
        st.plotly_chart(fig4, use_container_width=True)

    with r2c3:
        features = ['danceability', 'energy', 'speechiness', 'acousticness', 'liveness', 'valence']
        avg_vals = filtered_df[features].mean().values.tolist()
        fig5 = go.Figure(go.Scatterpolar(
            r=avg_vals + [avg_vals[0]],
            theta=[f.capitalize() for f in features] + [features[0].capitalize()],
            fill='toself',
            fillcolor='rgba(192, 160, 96, 0.15)',
            line=dict(color='#C0A060', width=1.5),
            marker=dict(color='#C0A060', size=4)
        ))
        
        polar_layout = PLOT_LAYOUT.copy()
        for k in ['xaxis', 'yaxis', 'title']:
            if k in polar_layout:
                del polar_layout[k]
        
        fig5.update_layout(
            title=dict(text='Audio Features Radar', font=dict(color='#999999', size=13, family='Inter', weight='normal')),
            polar=dict(
                bgcolor='#161616',
                radialaxis=dict(visible=True, range=[0, 1], gridcolor='#1e1e1e', linecolor='#242424', tickfont=dict(color='#555555')),
                angularaxis=dict(gridcolor='#1e1e1e', linecolor='#242424', tickfont=dict(color='#555555'))
            ),
            **polar_layout
        )
        st.plotly_chart(fig5, use_container_width=True)

    r3c1, r3c2 = st.columns(2)

    with r3c1:
        top_artists = filtered_df['artist_name'].value_counts().head(10).reset_index()
        top_artists.columns = ['Artist', 'Songs']
        top_artists['Songs'] = pd.to_numeric(top_artists['Songs'])
        top_artists = top_artists.sort_values('Songs', ascending=True)
        fig6 = px.bar(
            top_artists, 
            x='Songs', 
            y='Artist', 
            orientation='h',
            title='Top 10 Artists'
        )
        fig6.update_traces(marker_color='#C0A060', opacity=0.8)
        fig6.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig6, use_container_width=True)

    with r3c2:
        fig7 = px.histogram(
            filtered_df, 
            x='popularity', 
            nbins=40,
            title='Popularity Distribution'
        )
        fig7.update_traces(marker_color='#C0A060', opacity=0.8, marker_line_color='#161616', marker_line_width=1)
        fig7.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig7, use_container_width=True)

    st.markdown("<br><h3 style='color:#f0f0f0; font-size:14px; font-weight:600; border-bottom: 1px solid #242424; padding-bottom: 10px; margin-bottom: 20px;'>Top 20 Most Popular Tracks</h3>", unsafe_allow_html=True)
    top_tracks = filtered_df.nlargest(20, 'popularity')[
        ['track_name', 'artist_name', 'genre', 'year', 'popularity', 'danceability', 'energy', 'valence']
    ].reset_index(drop=True)
    top_tracks.index += 1
    
    st.dataframe(top_tracks, use_container_width=True)

else:
    st.warning("No data found for the selected filters.")

st.markdown("<hr style='margin-top: 50px;'>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; color:#555555; font-size:12px; margin-bottom: 20px;'>
    Built by Aditya Bokde | BeatMetrics 2024 | Data Science Portfolio
</div>
""", unsafe_allow_html=True)