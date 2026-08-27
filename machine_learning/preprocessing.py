"""
preprocessing.py

Loads, cleans, and preprocesses the dataset
for machine learning.
"""

import os

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import joblib


class DataPreprocessor:

    def __init__(
        self,
        dataset_path="dataset/shower_temperature_dataset.csv"
    ):

        self.dataset_path = dataset_path

        self.scaler = StandardScaler()

        self.data = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

    # ---------------------------------------------------------
    # Load Dataset
    # ---------------------------------------------------------

    def load_dataset(self):

        if not os.path.exists(self.dataset_path):

            raise FileNotFoundError(
                f"Dataset not found : {self.dataset_path}"
            )

        self.data = pd.read_csv(self.dataset_path)

        return self.data

    # ---------------------------------------------------------
    # Dataset Summary
    # ---------------------------------------------------------

    def summary(self):

        if self.data is None:
            self.load_dataset()

        print("\n========== DATA SUMMARY ==========\n")

        print(self.data.head())

        print("\nShape")

        print(self.data.shape)

        print("\nColumns")

        print(self.data.columns.tolist())

        print("\nMissing Values")

        print(self.data.isnull().sum())

        print("\n==================================")

    # ---------------------------------------------------------
    # Prepare Features
    # ---------------------------------------------------------

    def prepare_features(self):

        if self.data is None:
            self.load_dataset()

        X = self.data[
            [
                "InitialTemp",
                "DesiredTemp"
            ]
        ]

        y = self.data[
            [
                "HotValve",
                "ColdValve"
            ]
        ]

        return X, y

    # ---------------------------------------------------------
    # Train Test Split
    # ---------------------------------------------------------

    def split(self):

        X, y = self.prepare_features()

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test

        ) = train_test_split(

            X,
            y,

            test_size=0.20,

            random_state=42

        )

        return (

            self.X_train,
            self.X_test,

            self.y_train,
            self.y_test

        )

    # ---------------------------------------------------------
    # Feature Scaling
    # ---------------------------------------------------------

    def scale(self):

        if self.X_train is None:
            self.split()

        self.X_train = self.scaler.fit_transform(
            self.X_train
        )

        self.X_test = self.scaler.transform(
            self.X_test
        )

        return (
            self.X_train,
            self.X_test
        )

    # ---------------------------------------------------------
    # Save Scaler
    # ---------------------------------------------------------

    def save_scaler(
        self,
        path="models/scaler.pkl"
    ):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        joblib.dump(
            self.scaler,
            path
        )

        print(f"Scaler saved -> {path}")

    # ---------------------------------------------------------
    # Execute Complete Pipeline
    # ---------------------------------------------------------

    def process(self):

        self.load_dataset()

        self.summary()

        self.split()

        self.scale()

        self.save_scaler()

        return (

            self.X_train,

            self.X_test,

            self.y_train,

            self.y_test

        )


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    processor = DataPreprocessor()

    (
        X_train,
        X_test,
        y_train,
        y_test

    ) = processor.process()

    print("\nTraining Samples :", len(X_train))

    print("Testing Samples  :", len(X_test))