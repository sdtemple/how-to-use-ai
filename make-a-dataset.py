# Creating a synthetic dataset
# We will use Ctrl + I to help us write this code.

import numpy as np

if __name__ == "__main__":

    # Ctrl + I
    # I would like to generate a 1000 by 10 dataset 
    # that contains data for binary classification. 
    # The first column will be 1s and 0s. 
    # The other columns will be normally distributed. 
    # Insert some missing values for the 
    # 9 columns that have the predictor variables.

    rng = np.random.default_rng(42)
    n, p = 1000, 10

    y = rng.binomial(1, 0.5, size=(n, 1))
    X = rng.normal(loc=0.0, scale=1.0, size=(n, p - 1))

    missing_rate = 0.05
    mask = rng.random(size=X.shape) < missing_rate
    X[mask] = np.nan

    data = np.hstack((y, X))

    # Ctrl + I
    # The binary target variable will be has_healthy_diet 
    # and the predictor variables will be names of 
    # fruits, vegetables, and candy.

    col_names = [
        "has_healthy_diet",
        "apple",
        "banana",
        "carrot",
        "spinach",
        "broccoli",
        "orange",
        "strawberry",
        "grapes",
        "gummy_candy",
    ]
    assert len(col_names) == p

    _original_savetxt = np.savetxt
    def _savetxt_override(*args, **kwargs):
        kwargs["header"] = ",".join(col_names)
        return _original_savetxt(*args, **kwargs)

    np.savetxt = _savetxt_override

    np.savetxt("nonsensical-dataset.csv", data, delimiter=",", header="y," + ",".join(f"x{i}" for i in range(1, p)), comments="")

    # Ctrl + I
    # Now I want to create a new target variable based on 
    # a binary regression formula where the target variable
    #  is mostly driven by the values in the 
    # carrot, spinach, and broccoli columns.

    # Impute missing predictor values with column means
    col_means = np.nanmean(X, axis=0)
    X_imputed = np.where(np.isnan(X), col_means, X)

    # Coefficients: strong effects for carrot, spinach, broccoli (indices 2,3,4)
    coefs = np.array([0.05, 0.05, 1.5, 1.2, 1.3, 0.05, 0.05, 0.05, 0.05])
    intercept = -0.2

    # Add noise and compute probabilities via logistic link
    noise = rng.normal(0.0, 0.5, size=n)
    logits = intercept + X_imputed.dot(coefs) + noise
    probs = 1.0 / (1.0 + np.exp(-logits))

    # Sample new binary target and replace first column
    y_new = (rng.random(size=n) < probs).astype(int).reshape(n, 1)
    data[:, 0] = y_new.ravel()

    # Save the updated dataset
    np.savetxt("sensical-dataset.csv", data, delimiter=",", comments="")
