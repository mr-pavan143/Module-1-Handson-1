"""
test_ml.py

Unit tests for machine learning modules.
"""


import sys
import os

import pytest


sys.path.append(

    os.path.dirname(
        os.path.dirname(__file__)
    )

)


from machine_learning.preprocessing import DataPreprocessor



# ---------------------------------------------------------
# Test Dataset Loading
# ---------------------------------------------------------

def test_dataset_loading():

    processor = DataPreprocessor()


    data = processor.load_dataset()


    assert data is not None


    assert len(data) > 0



# ---------------------------------------------------------
# Test Feature Preparation
# ---------------------------------------------------------

def test_feature_generation():

    processor = DataPreprocessor()


    X, y = processor.prepare_features()


    assert X.shape[1] == 2


    assert y.shape[1] == 2



# ---------------------------------------------------------
# Test Split
# ---------------------------------------------------------

def test_train_test_split():

    processor = DataPreprocessor()


    (
        X_train,
        X_test,
        y_train,
        y_test

    ) = processor.split()


    assert len(X_train) > 0

    assert len(X_test) > 0