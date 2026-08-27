"""
test_fuzzy.py

Unit tests for fuzzy logic modules.
"""

import sys
import os

import pytest


# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from fuzzy_system.membership import MembershipFunctions
from fuzzy_system.fuzzy_rules import FuzzyRules
from fuzzy_system.inference import FuzzyInference



# ---------------------------------------------------------
# Test Membership Functions
# ---------------------------------------------------------

def test_temperature_membership():

    membership = MembershipFunctions()

    result = membership.temperature_membership(
        25
    )


    assert "Cold" in result

    assert "Warm" in result

    assert "Hot" in result



def test_error_membership():

    membership = MembershipFunctions()

    result = membership.error_membership(
        10
    )


    assert result["Positive"] >= 0

    assert result["Zero"] >= 0

    assert result["Negative"] >= 0



# ---------------------------------------------------------
# Test Rules
# ---------------------------------------------------------

def test_fuzzy_rules():

    rules = FuzzyRules()


    action = rules.get_rule(
        "Positive"
    )


    assert action["hot"] == "High"

    assert action["cold"] == "Low"



# ---------------------------------------------------------
# Test Inference Engine
# ---------------------------------------------------------

def test_inference():

    inference = FuzzyInference()


    result = inference.infer(

        current_temp=25,

        desired_temp=38

    )


    assert result["temperature_error"] == 13


    assert "hot_valve" in result

    assert "cold_valve" in result