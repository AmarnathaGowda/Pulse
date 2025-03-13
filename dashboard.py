import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and layout
st.title("Employee Sentiment Visualization Dashboard")
st.write("Explore employee sentiment trends over time.")

# Load the aggregated data
@st.cache_data  # Cache the data to improve performance
def load_data():
    df = pd.read_csv('data/aggregated_sentiment.csv')
    df['date'] = pd.to_datetime(df['date'])  # Ensure date is in datetime format
    return df

df = load_data()

# --- Visualization 1: Line Chart for Sentiment Trends ---
st.subheader("Average Sentiment Over Time")
fig_line = px.line(df, x='date', y='compound', title='Average Sentiment Over Time')
fig_line.update_layout(xaxis_title='Date', yaxis_title='Average Sentiment Score')
st.plotly_chart(fig_line)

# --- Visualization 2: Bar Chart for Sentiment Counts ---
st.subheader("Sentiment Counts Over Time")
df_melted = df.melt(id_vars='date', value_vars=['positive_count', 'negative_count', 'neutral_count'],
                    var_name='sentiment_type', value_name='count')
fig_bar = px.bar(df_melted, x='date', y='count', color='sentiment_type', title='Sentiment Counts Over Time')
fig_bar.update_layout(xaxis_title='Date', yaxis_title='Count', barmode='group')
st.plotly_chart(fig_bar)

# --- Visualization 3: Pie Chart for Overall Sentiment Distribution ---
st.subheader("Overall Sentiment Distribution")
overall_sentiment = df[['positive_count', 'negative_count', 'neutral_count']].sum()
fig_pie = px.pie(values=overall_sentiment, names=overall_sentiment.index, title='Overall Sentiment Distribution')
st.plotly_chart(fig_pie)

# Optional: Add a sidebar with additional info or filters
st.sidebar.header("About")
st.sidebar.write("This dashboard visualizes employee sentiment data over time, showing trends and distributions.")