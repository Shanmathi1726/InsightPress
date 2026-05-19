# -----------------------------------
# GENERATE SMART INSIGHTS
# -----------------------------------
def generate_insights(df):

    insights = []

    # Top category
    top_category = (
        df.groupby("category")["views"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Top performing category is {top_category}"
    )

    # Best author
    best_author = (
        df.groupby("author")["engagement_score"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"Highest engagement author is {best_author}"
    )

    # Bounce rate warning
    avg_bounce = df["bounce_rate"].mean()

    if avg_bounce > 45:

        insights.append(
            "High bounce rate detected. Improve reader retention."
        )

    # Read time insight
    avg_read_time = df["read_time"].mean()

    if avg_read_time > 5:

        insights.append(
            "Readers are spending strong time on articles."
        )

    return insights