import plotly.express as px

def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        color_discrete_sequence=["#636EFA"]
    )

    return fig


def boxplot(df, column):

    fig = px.box(df, y=column)

    return fig


def correlation_heatmap(df):

    fig = px.imshow(
        df.corr(numeric_only=True),
        text_auto=True,
        color_continuous_scale="RdBu"
    )

    return fig
