import plotly.express as px

from preswald import (
    chat,
    get_df,
    plotly,
    sidebar,
    table,
    text,
)

sidebar()

# Report Title
text(
    "# Netflix Titles Data Visualization Report \n This report provides a visual exploration of the Netflix titles dataset.It analyzes content characteristics such as type, release year, genres, and countries of production."
)

# Load the CSV
df = get_df("netflix_data")

# 1. Bar chart - Count of Shows by Type
text(
    "## Count of Shows by Type \n This bar chart shows the count of Netflix titles categorized as Movies or TV Shows."
)
fig1 = px.histogram(
    df,
    x="type",
    color="type",
    title="Distribution of Content Type",
    labels={"type": "Content Type"},
)
fig1.update_layout(template="plotly_white")
plotly(fig1)

# 2. Top 10 Countries Producing Netflix Content
text(
    "## Top Countries Producing Netflix Content \n This bar chart visualizes the top 10 countries producing the most content available on Netflix."
)
top_countries = (
    df["country"].value_counts().dropna().head(10).reset_index()
)
top_countries.columns = ["country", "count"]
fig2 = px.bar(
    top_countries,
    x="country",
    y="count",
    title="Top 10 Countries by Number of Titles",
)
fig2.update_layout(template="plotly_white")
plotly(fig2)

# 3. Content Released Over the Years
text(
    "## Netflix Content Released Over the Years \n This line chart shows how Netflix's content library has grown over time based on the release year."
)
year_counts = df["release_year"].value_counts().sort_index()
fig3 = px.line(
    x=year_counts.index,
    y=year_counts.values,
    labels={"x": "Release Year", "y": "Number of Titles"},
    title="Number of Netflix Titles Released per Year",
)
fig3.update_layout(template="plotly_white")
plotly(fig3)

# 4. Genre (listed_in) Word Cloud-like Bar Chart (Top 10 genres)
text(
    "## Top 10 Genres on Netflix \n This bar chart represents the most common genres among Netflix titles."
)
import pandas as pd

# Split and count genres
genre_series = df["listed_in"].dropna().str.split(", ").explode()
top_genres = genre_series.value_counts().head(10).reset_index()
top_genres.columns = ["genre", "count"]
fig4 = px.bar(
    top_genres,
    x="genre",
    y="count",
    title="Top 10 Genres on Netflix",
)
fig4.update_layout(template="plotly_white")
plotly(fig4)

# 5. Duration Distribution (Movies only)
text(
    "## Duration Distribution of Movies \n This histogram displays the distribution of movie durations on Netflix."
)
movies = df[df["type"] == "Movie"]
movies["duration_minutes"] = (
    movies["duration"].str.extract("(\d+)").astype(float)
)
fig5 = px.histogram(
    movies,
    x="duration_minutes",
    nbins=30,
    title="Distribution of Movie Durations",
    labels={"duration_minutes": "Duration (minutes)"},
)
fig5.update_layout(template="plotly_white")
plotly(fig5)

# Show a preview of the data
text(
    "## Sample of the Netflix Titles Dataset \n Below is a preview of the first 10 rows of the dataset."
)
table(df.head(10))

#Top 10 Directors on Netflix
text(
    "## Top 10 Directors on Netflix \n This bar chart shows the directors with the highest number of titles in the Netflix catalog."
)
top_directors = df["director"].dropna().value_counts().head(10).reset_index()
top_directors.columns = ["Director", "Number of Titles"]
fig6 = px.bar(
    top_directors,
    x="Director",
    y="Number of Titles",
    title="Top 10 Directors by Number of Netflix Titles",
)
fig6.update_layout(template="plotly_white", xaxis_tickangle=-45)
plotly(fig6)

#Top 10 Actors/Actresses on Netflix
text(
    "## Top 10 Cast Members on Netflix \n This chart displays the actors or actresses who appear most often in Netflix titles."
)
cast_series = df["cast"].dropna().str.split(", ").explode()
top_cast = cast_series.value_counts().head(10).reset_index()
top_cast.columns = ["Actor/Actress", "Count"]
fig7 = px.bar(
    top_cast,
    x="Actor/Actress",
    y="Count",
    title="Top 10 Actors/Actresses in Netflix Titles",
)
fig7.update_layout(template="plotly_white", xaxis_tickangle=-45)
plotly(fig7)

#TV Show Season Distribution
text(
    "## Season Distribution of TV Shows \n This bar chart displays the number of seasons for TV shows, helping us understand the typical length of TV content on Netflix."
)
tv_shows = df[df["type"] == "TV Show"].copy()
tv_shows["seasons"] = tv_shows["duration"].str.extract("(\d+)").astype(float)
fig8 = px.histogram(
    tv_shows,
    x="seasons",
    nbins=20,
    title="Distribution of TV Show Seasons",
    labels={"seasons": "Number of Seasons"},
)
fig8.update_layout(template="plotly_white")
plotly(fig8)

# Add an interactive chat interface
text(
    "## Interactive Chat Interface \n Use this chat to explore more about the Netflix dataset! Ask about specific countries, trends over time, or popular genres."
)
chat("netflix_titles")
