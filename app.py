import streamlit as st
import pandas as pd


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="InsightPress",
    page_icon="📊",
    layout="wide"
)


# -----------------------------------
# TOP NAVIGATION
# -----------------------------------
page = st.radio(
    "",
    [
        "Home",
        "About",
        "Media Source",
        "Analytics",
        "Insights"
    ],
    horizontal=True
)

# ===================================
# HOME PAGE
# ===================================
if page == "Home":

    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center; font-size:130px; font-weight:800;'>"
        "<span style='color:#FF3B3B;'>Insight</span>"
        "<span style='color:white;'>Press</span>"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; color:#9FA6B2; font-size:34px; margin-top:-30px;'>"
        "Measure Engagement. Understand Readers."
        "</p>",
        unsafe_allow_html=True
    )

# ===================================
# ABOUT PAGE
# ===================================
elif page == "About":

    st.markdown("<br>", unsafe_allow_html=True)

    # TITLE
    st.markdown(
        """
        <h1 style='
            text-align:center;
            font-size:72px;
            font-weight:800;
            margin-bottom:40px;
            letter-spacing:1px;
        '>
            <span style='color:#FF3B3B;'>About</span>
            <span style='color:white;'> InsightPress</span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    # HERO IMAGE
    st.image(
        "assets/about_dashboard image.png",
        use_container_width=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # DESCRIPTION
    st.markdown(
        """
        <div style='
            color:#D6D9E0;
            font-size:26px;
            line-height:2;
            text-align:justify;
            padding-left:50px;
            padding-right:50px;
        '>

        <span style='color:#FF3B3B; font-weight:700;'>
        InsightPress
        </span>

        is a modern reader engagement intelligence platform built for
        digital publishing and media analytics.

        It enables publishers and editorial teams to better understand
        how audiences interact with content through data-driven insights
        and interactive analytics.

        The platform allows users to upload structured article analytics
        datasets through the

        <span style='color:#FF3B3B; font-weight:700;'>
        Media Source Portal
        </span>.

        <span style='color:#FF3B3B; font-weight:700;'>
        InsightPress
        </span>

        then processes this data to generate interactive dashboards,
        engagement intelligence, content performance rankings,
        publishing trends, and reader behavior insights.

        By transforming raw analytics into actionable intelligence,
        <span style='color:#FF3B3B; font-weight:700;'>
        InsightPress
        </span>

        helps editorial teams:

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # BULLET POINTS
    st.markdown(
        """
        <div style='
            color:white;
            font-size:24px;
            line-height:2.4;
            padding-left:90px;
        '>

        • Identify high-performing articles and content categories<br>

        • Understand audience interests and reading patterns<br>

        • Analyze engagement metrics and publishing trends<br>

        • Improve content strategy and reader retention<br>

        • Make smarter, data-driven publishing decisions<br>

        </div>
        """,
        unsafe_allow_html=True
    )

# ===================================
# MEDIA SOURCE PAGE
# ===================================
elif page == "Media Source":

    st.markdown("<br>", unsafe_allow_html=True)

    # TITLE
    st.markdown(
        """
        <h1 style='
            text-align:center;
            font-size:60px;
            font-weight:800;
            margin-bottom:20px;
        '>
            <span style='color:#FF3B3B;'>Media</span>
            <span style='color:white;'> Source</span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    # DESCRIPTION
    st.markdown(
        """
        <div style='
            color:#B8BCC8;
            font-size:22px;
            line-height:2;
            text-align:center;
            padding-left:120px;
            padding-right:120px;
            margin-bottom:40px;
        '>

        Upload a structured CSV dataset containing
        article analytics and reader engagement metrics.

        Required fields include article titles,
        categories, authors, publishing dates,
        views, likes, comments, shares,
        read time, and bounce rate.

        </div>
        """,
        unsafe_allow_html=True
    )

    # IMPORT
    from services.data_loader import (
        load_data
    )

    # FILE UPLOAD
    uploaded_file = st.file_uploader(
        "Upload Analytics Dataset",
        type=["csv"]
    )

    # PROCESS FILE
    if uploaded_file is not None:

        # LOAD DATAFRAME
        df = load_data(uploaded_file)

        # SAVE GLOBALLY
        st.session_state["df"] = df

        # SUCCESS MESSAGE
        st.success(
            "Dataset uploaded and connected successfully."
        )

        # DATA PREVIEW
        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

    # NOTE
    st.markdown(
        """
        <div style='
            color:#FF3B3B;
            font-size:20px;
            font-weight:600;
            margin-top:30px;
            text-align:center;
            letter-spacing:1px;
            line-height:2;
        '>

        Note: After uploading the dataset,
        navigate to the Analytics and Insights
        sections to explore dashboards,
        engagement intelligence, and
        reader behavior insights.

        </div>
        """,
        unsafe_allow_html=True
    )

# ===================================
# ANALYTICS PAGE
# ===================================
elif page == "Analytics":

    st.title("Analytics Dashboard")

    # CHECK IF DATA EXISTS
    if "df" not in st.session_state:

        st.markdown(
            """
            <div style='
                color:#FF3B3B;
                font-size:24px;
                font-weight:600;
                text-align:center;
                margin-top:120px;
                line-height:2;
            '>

            No analytics dataset detected.<br><br>

            Please upload a CSV dataset in the
            Media Source section before accessing Analytics.

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        # GET DATAFRAME
        df = st.session_state["df"]

        from services.data_loader import (
            validate_columns,
            clean_data
        )

        from services.scoring import (
            calculate_engagement_score
        )

        from services.analytics import (
            calculate_total_views,
            calculate_total_articles,
            calculate_avg_read_time,
            calculate_avg_bounce_rate,
            calculate_total_likes
        )

        from components.charts import (
            create_category_views_chart,
            create_publishing_trend_chart,
            create_author_performance_chart
        )

        # VALIDATE
        missing_columns = validate_columns(df)

        if len(missing_columns) > 0:

            st.error(
                f"Missing columns: {missing_columns}"
            )

        else:

            # CLEAN DATA
            df = clean_data(df)

            # ENGAGEMENT SCORE
            df["engagement_score"] = (
                calculate_engagement_score(df)
            )

            # ===================================
            # FILTERS
            # ===================================
            st.subheader("Filters")

            col1, col2, col3 = st.columns(3)

            with col1:
                selected_category = st.selectbox(
                    "Category",
                    ["All"] + list(df["category"].unique())
                )

            with col2:
                selected_author = st.selectbox(
                    "Author",
                    ["All"] + list(df["author"].unique())
                )

            with col3:
                search_query = st.text_input(
                    "Search Article"
                )

            filtered_df = df.copy()

            if selected_category != "All":
                filtered_df = filtered_df[
                    filtered_df["category"] == selected_category
                ]

            if selected_author != "All":
                filtered_df = filtered_df[
                    filtered_df["author"] == selected_author
                ]

            if search_query:
                filtered_df = filtered_df[
                    filtered_df["title"]
                    .str.contains(search_query, case=False)
                ]

            # ===================================
            # KPI SECTION
            # ===================================
            total_views = calculate_total_views(filtered_df)

            total_articles = calculate_total_articles(
                filtered_df
            )

            avg_read_time = calculate_avg_read_time(
                filtered_df
            )

            avg_bounce_rate = calculate_avg_bounce_rate(
                filtered_df
            )

            total_likes = calculate_total_likes(
                filtered_df
            )

            st.subheader("Platform KPIs")

            kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

            kpi1.metric(
                "Total Views",
                f"{total_views:,}"
            )

            kpi2.metric(
                "Articles",
                total_articles
            )

            kpi3.metric(
                "Avg Read Time",
                f"{avg_read_time} min"
            )

            kpi4.metric(
                "Bounce Rate",
                f"{avg_bounce_rate}%"
            )

            kpi5.metric(
                "Total Likes",
                f"{total_likes:,}"
            )

            # ===================================
            # CATEGORY CHART
            # ===================================
            st.subheader("Category Performance")

            category_chart = (
                create_category_views_chart(filtered_df)
            )

            st.plotly_chart(
                category_chart,
                use_container_width=True
            )

            # ===================================
            # PUBLISHING TRENDS
            # ===================================
            st.subheader("Publishing Trends")

            trend_chart = (
                create_publishing_trend_chart(filtered_df)
            )

            st.plotly_chart(
                trend_chart,
                use_container_width=True
            )

            # ===================================
            # AUTHOR PERFORMANCE
            # ===================================
            st.subheader("Author Performance")

            author_chart = (
                create_author_performance_chart(
                    filtered_df
                )
            )

            st.plotly_chart(
                author_chart,
                use_container_width=True
            )

            # ===================================
            # TOP ARTICLES
            # ===================================
            st.subheader("Top Performing Articles")

            top_articles = (
                filtered_df.sort_values(
                    by="engagement_score",
                    ascending=False
                )[
                    [
                        "title",
                        "category",
                        "views",
                        "likes",
                        "engagement_score"
                    ]
                ]
                .head(5)
            )

            st.dataframe(
                top_articles,
                use_container_width=True
            )
# ===================================
# INSIGHTS PAGE
# ===================================
elif page == "Insights":

    st.markdown(
        """
        <h1 style='
            text-align:center;
            font-size:70px;
            font-weight:800;
            margin-bottom:40px;
        '>
            <span style='color:#FF3B3B;'>Insight</span>
            <span style='color:white;'> Intelligence</span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    # CHECK DATA
    if "df" not in st.session_state:

        st.markdown(
            """
            <div style='
                color:#FF3B3B;
                font-size:24px;
                font-weight:600;
                text-align:center;
                margin-top:120px;
                line-height:2;
            '>

            No analytics dataset detected.<br><br>

            Please upload a CSV dataset in the
            Media Source section before accessing Insights.

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        # LOAD DATA
        df = st.session_state["df"]

        from services.data_loader import (
            clean_data
        )

        from services.scoring import (
            calculate_engagement_score
        )

        # CLEAN
        df = clean_data(df)

        # ENGAGEMENT SCORE
        df["engagement_score"] = (
            calculate_engagement_score(df)
        )

        # ===================================
        # CALCULATIONS
        # ===================================

        # TOP CATEGORY
        top_category = (
            df.groupby("category")["views"]
            .sum()
            .idxmax()
        )

        # WORST CATEGORY
        weak_category = (
            df.groupby("category")["views"]
            .sum()
            .idxmin()
        )

        # TOP AUTHOR
        top_author = (
            df.groupby("author")["engagement_score"]
            .mean()
            .idxmax()
        )

        # TOP ARTICLE
        top_article = (
            df.loc[df["views"].idxmax(), "title"]
        )

        # BEST DAY
        df["publish_date"] = pd.to_datetime(
            df["publish_date"]
        )

        df["day_name"] = (
            df["publish_date"]
            .dt.day_name()
        )

        best_day = (
            df.groupby("day_name")["views"]
            .mean()
            .idxmax()
        )

        # RETENTION
        avg_read_time = df["read_time"].mean()

        # BOUNCE
        avg_bounce = df["bounce_rate"].mean()

        # VIRAL
        viral_article = (
            df.sort_values(
                by="engagement_score",
                ascending=False
            )
            .iloc[0]["title"]
        )

        # TREND
        trend_category = (
            df.groupby("category")["shares"]
            .sum()
            .idxmax()
        )

        # ===================================
        # TITLE
        # ===================================
        st.markdown(
            """
            <h2 style='
                color:white;
                margin-bottom:30px;
            '>
            Executive Insights
            </h2>
            """,
            unsafe_allow_html=True
        )

        # ===================================
        # INSIGHT CARDS
        # ===================================

        insights = [

            f"Top Performing Category: {top_category} content currently drives the highest audience reach and engagement.",

            f"Most Engaging Author: {top_author} consistently generates stronger reader interaction.",

            f"Highest Viewed Article: '{top_article}' attracted the largest audience volume.",

            f"Best Publishing Day: Articles published on {best_day} show stronger overall performance.",

            f"Audience Retention Insight: Average read time currently stands at {avg_read_time:.1f} minutes.",

            f"Bounce Rate Warning: Average bounce rate is {avg_bounce:.1f}%. Reducing early exits could improve retention.",

            f"Recommended Focus Category: {top_category} shows the strongest engagement potential for future publishing.",

            f"Viral Article Detection: '{viral_article}' demonstrates unusually high audience engagement patterns.",

            f"Engagement Trend Summary: {trend_category} content currently generates the strongest social sharing activity.",

            f"Content Recommendation: Increase publishing frequency for high-performing audience-interest categories.",

            f"Weakest Performing Category: {weak_category} currently underperforms compared to other publishing segments.",

            f"Reader Attention Drop Alert: Shorter read times may indicate audience attention loss in lower-performing articles.",

            f"High Potential Content Area: {trend_category} demonstrates strong audience interest and future growth potential.",

            f"Publishing Consistency Insight: Consistent publishing schedules can significantly improve engagement stability.",

            f"Audience Interest Shift: Reader engagement patterns indicate growing interest in {trend_category} content."

        ]

        # ===================================
        # DISPLAY CARDS
        # ===================================

        for insight in insights:

            st.markdown(
                f"""
                <div style='
                    background-color:#111827;
                    border-left:6px solid #FF3B3B;
                    padding:25px;
                    margin-bottom:20px;
                    border-radius:12px;
                    color:white;
                    font-size:20px;
                    line-height:1.8;
                    box-shadow:0px 0px 15px rgba(255,59,59,0.08);
                '>

                {insight}

                </div>
                """,
                unsafe_allow_html=True
            )


