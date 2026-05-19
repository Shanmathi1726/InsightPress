# -----------------------------------
# TOTAL VIEWS
# -----------------------------------
def calculate_total_views(df):

    return df["views"].sum()


# -----------------------------------
# TOTAL ARTICLES
# -----------------------------------
def calculate_total_articles(df):

    return len(df)


# -----------------------------------
# AVERAGE READ TIME
# -----------------------------------
def calculate_avg_read_time(df):

    return round(
        df["read_time"].mean(),
        2
    )


# -----------------------------------
# AVERAGE BOUNCE RATE
# -----------------------------------
def calculate_avg_bounce_rate(df):

    return round(
        df["bounce_rate"].mean(),
        2
    )


# -----------------------------------
# TOTAL LIKES
# -----------------------------------
def calculate_total_likes(df):

    return df["likes"].sum()