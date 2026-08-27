"""
defuzzification.py

Converts fuzzy valve outputs into crisp valve opening percentages
using the centroid (Center of Gravity) method.
"""

import numpy as np
import skfuzzy as fuzz

from fuzzy_system.membership import MembershipFunctions


class Defuzzifier:
    """
    Converts fuzzy linguistic values into
    crisp valve percentages.
    """

    def __init__(self):

        self.membership = MembershipFunctions()

        self.valve_range = self.membership.valve

    # ---------------------------------------------------------
    # Internal Helper
    # ---------------------------------------------------------

    def _membership_curve(self, label):
        """
        Return the membership curve for the valve label.
        """

        curves = {

            "Low": self.membership.valve_low,

            "Medium": self.membership.valve_medium,

            "High": self.membership.valve_high

        }

        return curves.get(label, self.membership.valve_medium)

    # ---------------------------------------------------------
    # Defuzzify a Single Valve
    # ---------------------------------------------------------

    def defuzzify(self, valve_label):
        """
        Convert a fuzzy valve label into a crisp percentage.

        Parameters
        ----------
        valve_label : str
            Low / Medium / High

        Returns
        -------
        float
        """

        curve = self._membership_curve(valve_label)

        crisp_value = fuzz.defuzz(
            self.valve_range,
            curve,
            "centroid"
        )

        return round(float(crisp_value), 2)

    # ---------------------------------------------------------
    # Defuzzify Both Valves
    # ---------------------------------------------------------

    def compute(self, hot_label, cold_label):
        """
        Convert hot and cold valve labels into percentages.

        Returns
        -------
        dict
        """

        hot_value = self.defuzzify(hot_label)

        cold_value = self.defuzzify(cold_label)

        return {

            "hot_valve_percent": hot_value,

            "cold_valve_percent": cold_value

        }

    # ---------------------------------------------------------
    # Pretty Printing
    # ---------------------------------------------------------

    @staticmethod
    def print_result(result):

        print("\n========== DEFUZZIFICATION ==========\n")

        print(
            f"Hot Valve  : {result['hot_valve_percent']:.2f}%"
        )

        print(
            f"Cold Valve : {result['cold_valve_percent']:.2f}%"
        )

        print("\n=====================================\n")


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    d = Defuzzifier()

    result = d.compute(
        hot_label="High",
        cold_label="Low"
    )

    d.print_result(result)