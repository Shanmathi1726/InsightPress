# -----------------------------------
# ENGAGEMENT SCORE
# -----------------------------------
def calculate_engagement_score(df):

    score = (
        (df["views"] * 0.40) +
        (df["likes"] * 0.25) +
        (df["comments"] * 0.15) +
        (df["shares"] * 0.10) +
        (df["read_time"] * 0.10)
    )

    return score.round(2)