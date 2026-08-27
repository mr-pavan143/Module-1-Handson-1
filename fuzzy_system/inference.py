"""
inference.py

Fuzzy inference engine for the shower controller.

This module:
1. Calculates temperature error
2. Fuzzifies the error
3. Applies fuzzy rules
4. Produces fuzzy outputs
"""

from fuzzy_system.membership import MembershipFunctions
from fuzzy_system.fuzzy_rules import FuzzyRules


class FuzzyInference:
    """
    Performs fuzzy inference based on
    current and desired temperatures.
    """

    def __init__(self):

        self.membership = MembershipFunctions()
        self.rules = FuzzyRules()

    # ---------------------------------------------------------
    # Calculate Error
    # ---------------------------------------------------------

    @staticmethod
    def calculate_error(current_temp, desired_temp):
        """
        Error = Desired - Current
        """

        return desired_temp - current_temp

    # ---------------------------------------------------------
    # Fuzzification
    # ---------------------------------------------------------

    def fuzzify(self, error):

        return self.membership.error_membership(error)

    # ---------------------------------------------------------
    # Rule Evaluation
    # ---------------------------------------------------------

    def evaluate_rules(self, memberships):

        label, valve_action = self.rules.evaluate(memberships)

        return label, valve_action

    # ---------------------------------------------------------
    # Complete Inference
    # ---------------------------------------------------------

    def infer(self, current_temp, desired_temp):
        """
        Execute the complete inference process.

        Returns
        -------
        dict
        """

        error = self.calculate_error(
            current_temp,
            desired_temp
        )

        memberships = self.fuzzify(error)

        label, action = self.evaluate_rules(
            memberships
        )

        return {

            "current_temperature": current_temp,

            "desired_temperature": desired_temp,

            "temperature_error": error,

            "memberships": memberships,

            "dominant_error": label,

            "hot_valve": action["hot"],

            "cold_valve": action["cold"]

        }

    # ---------------------------------------------------------
    # Pretty Printing
    # ---------------------------------------------------------

    @staticmethod
    def print_result(result):

        print("\n========== FUZZY INFERENCE ==========\n")

        print(f"Current Temperature : {result['current_temperature']} °C")
        print(f"Desired Temperature : {result['desired_temperature']} °C")
        print(f"Temperature Error   : {result['temperature_error']} °C")

        print("\nMembership Values")

        for key, value in result["memberships"].items():
            print(f"{key:<10}: {value:.2f}")

        print("\nDominant Error :", result["dominant_error"])

        print("Hot Valve      :", result["hot_valve"])

        print("Cold Valve     :", result["cold_valve"])

        print("\n=====================================")


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    inference = FuzzyInference()

    result = inference.infer(
        current_temp=25,
        desired_temp=38
    )

    inference.print_result(result)