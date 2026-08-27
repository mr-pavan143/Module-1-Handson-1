"""
evaluate_model.py

Evaluate the trained Machine Learning model.
"""

import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from machine_learning.preprocessing import DataPreprocessor


class ModelEvaluator:

    def __init__(self):

        self.model_path = "models/trained_model.pkl"

        self.preprocessor = DataPreprocessor()

        self.model = None

    # -------------------------------------------------
    # Load Trained Model
    # -------------------------------------------------

    def load_model(self):

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                "Trained model not found."
            )

        self.model = joblib.load(self.model_path)

    # -------------------------------------------------
    # Evaluate
    # -------------------------------------------------

    def evaluate(self):

        (
            X_train,
            X_test,
            y_train,
            y_test

        ) = self.preprocessor.process()

        self.load_model()

        predictions = self.model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        mse = mean_squared_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(mse)

        r2 = r2_score(
            y_test,
            predictions
        )

        metrics = {

            "MAE": mae,

            "MSE": mse,

            "RMSE": rmse,

            "R2": r2

        }

        return (
            metrics,
            y_test,
            predictions
        )

    # -------------------------------------------------
    # Prediction Graph
    # -------------------------------------------------

    def prediction_graph(
        self,
        actual,
        predicted
    ):

        os.makedirs(
            "results",
            exist_ok=True
        )

        plt.figure(figsize=(8, 5))

        plt.plot(
            actual.iloc[:, 0].values,
            label="Actual Hot Valve"
        )

        plt.plot(
            predicted[:, 0],
            label="Predicted Hot Valve"
        )

        plt.title(
            "Actual vs Predicted"
        )

        plt.xlabel("Samples")

        plt.ylabel("Valve Percentage")

        plt.legend()

        plt.grid(True)

        plt.savefig(
            "results/temperature_graph.png"
        )

        plt.close()

    # -------------------------------------------------
    # Residual Plot
    # -------------------------------------------------

    def residual_plot(
        self,
        actual,
        predicted
    ):

        residual = (
            actual.iloc[:, 0].values
            - predicted[:, 0]
        )

        plt.figure(figsize=(8, 5))

        plt.scatter(
            predicted[:, 0],
            residual
        )

        plt.axhline(
            y=0,
            linestyle="--"
        )

        plt.title(
            "Residual Error"
        )

        plt.xlabel(
            "Predicted"
        )

        plt.ylabel(
            "Residual"
        )

        plt.grid(True)

        plt.savefig(
            "results/accuracy_report.png"
        )

        plt.close()

    # -------------------------------------------------
    # Save Metrics
    # -------------------------------------------------

    def save_metrics(
        self,
        metrics
    ):

        with open(
            "results/evaluation.txt",
            "w"
        ) as file:

            file.write(
                "MODEL EVALUATION\n\n"
            )

            for key, value in metrics.items():

                file.write(
                    f"{key}: {value:.4f}\n"
                )

    # -------------------------------------------------
    # Complete Evaluation
    # -------------------------------------------------

    def execute(self):

        print("\nEvaluating Model...\n")

        (
            metrics,
            actual,
            prediction

        ) = self.evaluate()

        self.prediction_graph(
            actual,
            prediction
        )

        self.residual_plot(
            actual,
            prediction
        )

        self.save_metrics(
            metrics
        )

        print("Evaluation Completed\n")

        for key, value in metrics.items():

            print(
                f"{key:<8}: {value:.4f}"
            )


if __name__ == "__main__":

    evaluator = ModelEvaluator()

    evaluator.execute()