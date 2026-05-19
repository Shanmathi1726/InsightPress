import pandas as pd


# -----------------------------------
# REQUIRED COLUMNS
# -----------------------------------
REQUIRED_COLUMNS = [
    "article_id",
    "title",
    "author",
    "category",
    "publish_date",
    "views",
    "likes",
    "comments",
    "read_time",
    "bounce_rate",
    "shares"
]


# -----------------------------------
# LOAD DATA
# -----------------------------------
def load_data(file):

    df = pd.read_csv(file)

    return df


# -----------------------------------
# VALIDATE COLUMNS
# -----------------------------------
def validate_columns(df):

    missing_columns = []

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:
            missing_columns.append(column)

    return missing_columns


# -----------------------------------
# CLEAN DATA
# -----------------------------------
def clean_data(df):

    # Remove missing rows
    df = df.dropna()

    # Convert publish_date to datetime
    df["publish_date"] = pd.to_datetime(
        df["publish_date"]
    )

    # Convert numeric columns
    numeric_columns = [
        "views",
        "likes",
        "comments",
        "read_time",
        "bounce_rate",
        "shares"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df