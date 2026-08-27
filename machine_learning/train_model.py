"""
train_model.py

Trains the machine learning model for predicting
hot and cold valve opening percentages.
"""

import os
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from machine_learning.preprocessing import DataPreprocessor


class ModelTrainer:
    """
    Train and save the ML model.
    """

    def __init__(self):

        self.preprocessor = DataPreprocessor()

        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            max_depth=10
        )

    # ---------------------------------------------------------
    # Train Model
    # ---------------------------------------------------------

    def train(self):

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = self.preprocessor.process()

        self.model.fit(
            X_train,
            y_train
        )

        predictions = self.model.predict(
            X_test
        )

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        mse = mean_squared_error(
            y_test,
            predictions
        )

        rmse = mse ** 0.5

        r2 = r2_score(
            y_test,
            predictions
        )

        metrics = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2 Score": r2
        }

        return metrics

    # ---------------------------------------------------------
    # Save Model
    # ---------------------------------------------------------

    def save_model(
        self,
        model_path="models/trained_model.pkl"
    ):

        os.makedirs(
            os.path.dirname(model_path),
            exist_ok=True
        )

        joblib.dump(
            self.model,
            model_path
        )

        print(f"Model saved -> {model_path}")

    # ---------------------------------------------------------
    # Save Metrics
    # ---------------------------------------------------------

    def save_metrics(
        self,
        metrics,
        file_path="models/model_accuracy.txt"
    ):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("MODEL PERFORMANCE\n")
            file.write("=========================\n\n")

            for key, value in metrics.items():
                file.write(f"{key}: {value:.4f}\n")

        print(f"Metrics saved -> {file_path}")

    # ---------------------------------------------------------
    # Complete Pipeline
    # ---------------------------------------------------------

    def execute(self):

        print("\nTraining Model...\n")

        metrics = self.train()

        self.save_model()

        self.save_metrics(metrics)

        print("\nTraining Complete\n")

        print("Performance Metrics\n")

        for key, value in metrics.items():

            print(f"{key:<12}: {value:.4f}")

        return metrics


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    trainer = ModelTrainer()

    trainer.execute()