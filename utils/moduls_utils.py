from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

def train_model(df, target):

    X = df.drop(columns=[target])

    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    if y.nunique() < 20:

        model = RandomForestClassifier()

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        score = accuracy_score(y_test, pred)

        task = "Classification"

    else:

        model = RandomForestRegressor()

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        score = r2_score(y_test, pred)

        task = "Regression"

    return model, score, task
