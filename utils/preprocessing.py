from sklearn.preprocessing import LabelEncoder

def preprocess(df):

    df = df.copy()

    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].fillna("Unknown")

            le = LabelEncoder()

            df[col] = le.fit_transform(df[col])

    df.fillna(df.median(numeric_only=True), inplace=True)

    return df
