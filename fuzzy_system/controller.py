"""
controller.py

High-level fuzzy shower controller.

This module integrates:
1. Membership Functions
2. Rule Base
3. Inference Engine
4. Defuzzification

It provides a single interface for obtaining
hot and cold valve opening percentages.
"""

from fuzzy_system.inference import FuzzyInference
from fuzzy_system.defuzzification import Defuzzifier


class FuzzyController:
    """
    Main fuzzy controller for the shower system.
    """

    def __init__(self):

        self.inference = FuzzyInference()
        self.defuzzifier = Defuzzifier()

    # ---------------------------------------------------------
    # Compute Control Action
    # ---------------------------------------------------------

    def compute_control(self, current_temperature, target_temperature):
        """
        Compute valve control percentages.

        Parameters
        ----------
        current_temperature : float
            Current measured water temperature.

        target_temperature : float
            Desired water temperature.

        Returns
        -------
        dict
            Complete controller output.
        """

        # Step 1: Fuzzy Inference
        inference_result = self.inference.infer(
            current_temperature,
            target_temperature
        )

        # Step 2: Defuzzification
        valve_result = self.defuzzifier.compute(
            inference_result["hot_valve"],
            inference_result["cold_valve"]
        )

        # Step 3: Merge results
        output = {
            **inference_result,
            **valve_result
        }

        return output

    # ---------------------------------------------------------
    # Display Results
    # ---------------------------------------------------------

    @staticmethod
    def print_output(result):

        print("\n==============================")
        print(" FUZZY SHOWER CONTROLLER")
        print("==============================")

        print(f"Current Temperature : {result['current_temperature']} °C")
        print(f"Target Temperature  : {result['desired_temperature']} °C")
        print(f"Temperature Error   : {result['temperature_error']} °C")

        print("\nMembership Values")
        for key, value in result["memberships"].items():
            print(f"  {key:<10}: {value:.2f}")

        print("\nDominant Error :", result["dominant_error"])

        print("\nValve Actions")
        print(f"  Hot Valve Label  : {result['hot_valve']}")
        print(f"  Cold Valve Label : {result['cold_valve']}")

        print("\nValve Percentages")
        print(f"  Hot Valve  : {result['hot_valve_percent']:.2f}%")
        print(f"  Cold Valve : {result['cold_valve_percent']:.2f}%")

        print("==============================\n")


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    controller = FuzzyController()

    result = controller.compute_control(
        current_temperature=24,
        target_temperature=38
    )

    controller.print_output(result)