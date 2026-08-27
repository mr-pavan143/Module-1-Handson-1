"""
predict.py

Load the trained machine learning model and scaler
to predict hot and cold valve opening percentages.
"""

import os
import sys
import joblib
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

sys.modules.pop("config", None)

from project_config import MODEL_PATH, SCALER_PATH


class Predictor:
    """
    Predict hot and cold valve percentages using
    the trained machine learning model.
    """

    def __init__(self):

        self.model = None
        self.scaler = None

        self.load_model()
        self.load_scaler()

    # ---------------------------------------------------------
    # Load Model
    # ---------------------------------------------------------

    def load_model(self):

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}"
            )

        self.model = joblib.load(MODEL_PATH)

    # ---------------------------------------------------------
    # Load Scaler
    # ---------------------------------------------------------

    def load_scaler(self):

        if not os.path.exists(SCALER_PATH):
            raise FileNotFoundError(
                f"Scaler not found: {SCALER_PATH}"
            )

        self.scaler = joblib.load(SCALER_PATH)

    # ---------------------------------------------------------
    # Prepare Input
    # ---------------------------------------------------------

    @staticmethod
    def prepare_input(initial_temp, desired_temp):

        return np.array([[initial_temp, desired_temp]])

    # ---------------------------------------------------------
    # Predict
    # ---------------------------------------------------------

    def predict(self, initial_temp, desired_temp):

        sample = self.prepare_input(
            initial_temp,
            desired_temp
        )

        sample = self.scaler.transform(sample)

        prediction = self.model.predict(sample)[0]

        return {

            "HotValve": round(float(prediction[0]), 2),

            "ColdValve": round(float(prediction[1]), 2)

        }

    # ---------------------------------------------------------
    # Display Prediction
    # ---------------------------------------------------------

    @staticmethod
    def print_prediction(result):

        print("\n========== ML PREDICTION ==========\n")

        print(
            f"Hot Valve  : {result['HotValve']:.2f}%"
        )

        print(
            f"Cold Valve : {result['ColdValve']:.2f}%"
        )

        print("\n===================================\n")


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    predictor = Predictor()

    result = predictor.predict(
        initial_temp=25,
        desired_temp=38
    )

    predictor.print_prediction(result)