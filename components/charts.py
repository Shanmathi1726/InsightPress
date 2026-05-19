import plotly.express as px


# -----------------------------------
# CATEGORY VIEWS CHART
# -----------------------------------
def create_category_views_chart(df):

    # Group data
    category_data = (
        df.groupby("category")["views"]
        .sum()
        .reset_index()
    )

    # Create chart
    fig = px.bar(
        category_data,
        x="category",
        y="views",
        color="category",
        title="Views by Category"
    )

    return fig

# -----------------------------------
# PUBLISHING TREND CHART
# -----------------------------------
def create_publishing_trend_chart(df):

    # Group by publish date
    trend_data = (
        df.groupby("publish_date")["views"]
        .sum()
        .reset_index()
    )

    # Create line chart
    fig = px.line(
        trend_data,
        x="publish_date",
        y="views",
        title="Publishing Trend Analysis",
        markers=True
    )

    return fig

# -----------------------------------
# AUTHOR PERFORMANCE CHART
# -----------------------------------
def create_author_performance_chart(df):

    # Group by author
    author_data = (
        df.groupby("author")["engagement_score"]
        .mean()
        .reset_index()
    )

    # Sort highest first
    author_data = author_data.sort_values(
        by="engagement_score",
        ascending=True
    )

    # Create horizontal bar chart
    fig = px.bar(
        author_data,
        x="engagement_score",
        y="author",
        orientation="h",
        color="author",
        title="Author Performance Analysis"
    )

    return fig