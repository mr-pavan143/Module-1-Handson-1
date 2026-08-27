"""
membership.py

Defines all fuzzy membership functions used in the
Fuzzy Shower Temperature Controller.
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class MembershipFunctions:
    """
    Creates and manages fuzzy membership functions.
    """

    def __init__(self):

        # Universe of discourse
        self.temperature = np.arange(0, 61, 1)
        self.error = np.arange(-30, 31, 1)
        self.valve = np.arange(0, 101, 1)

        self._create_temperature_sets()
        self._create_error_sets()
        self._create_valve_sets()

    # ---------------------------------------------------------
    # Temperature Membership Functions
    # ---------------------------------------------------------

    def _create_temperature_sets(self):

        self.temp_cold = fuzz.trimf(
            self.temperature,
            [0, 0, 20]
        )

        self.temp_warm = fuzz.trimf(
            self.temperature,
            [15, 30, 45]
        )

        self.temp_hot = fuzz.trimf(
            self.temperature,
            [40, 60, 60]
        )

    # ---------------------------------------------------------
    # Error Membership Functions
    # ---------------------------------------------------------

    def _create_error_sets(self):

        self.error_negative = fuzz.trimf(
            self.error,
            [-30, -30, 0]
        )

        self.error_zero = fuzz.trimf(
            self.error,
            [-5, 0, 5]
        )

        self.error_positive = fuzz.trimf(
            self.error,
            [0, 30, 30]
        )

    # ---------------------------------------------------------
    # Valve Membership Functions
    # ---------------------------------------------------------

    def _create_valve_sets(self):

        self.valve_low = fuzz.trimf(
            self.valve,
            [0, 0, 40]
        )

        self.valve_medium = fuzz.trimf(
            self.valve,
            [25, 50, 75]
        )

        self.valve_high = fuzz.trimf(
            self.valve,
            [60, 100, 100]
        )

    # ---------------------------------------------------------
    # Membership Evaluation
    # ---------------------------------------------------------

    def temperature_membership(self, value):

        return {
            "Cold": fuzz.interp_membership(
                self.temperature,
                self.temp_cold,
                value
            ),

            "Warm": fuzz.interp_membership(
                self.temperature,
                self.temp_warm,
                value
            ),

            "Hot": fuzz.interp_membership(
                self.temperature,
                self.temp_hot,
                value
            )
        }

    def error_membership(self, value):

        return {

            "Negative": fuzz.interp_membership(
                self.error,
                self.error_negative,
                value
            ),

            "Zero": fuzz.interp_membership(
                self.error,
                self.error_zero,
                value
            ),

            "Positive": fuzz.interp_membership(
                self.error,
                self.error_positive,
                value
            )

        }

    def valve_membership(self, value):

        return {

            "Low": fuzz.interp_membership(
                self.valve,
                self.valve_low,
                value
            ),

            "Medium": fuzz.interp_membership(
                self.valve,
                self.valve_medium,
                value
            ),

            "High": fuzz.interp_membership(
                self.valve,
                self.valve_high,
                value
            )

        }

    # ---------------------------------------------------------
    # Plot Temperature Membership
    # ---------------------------------------------------------

    def plot_temperature(self):

        plt.figure(figsize=(8, 5))

        plt.plot(
            self.temperature,
            self.temp_cold,
            label="Cold"
        )

        plt.plot(
            self.temperature,
            self.temp_warm,
            label="Warm"
        )

        plt.plot(
            self.temperature,
            self.temp_hot,
            label="Hot"
        )

        plt.title("Temperature Membership Functions")

        plt.xlabel("Temperature (°C)")
        plt.ylabel("Membership")

        plt.legend()
        plt.grid(True)

        plt.show()

    # ---------------------------------------------------------
    # Plot Error Membership
    # ---------------------------------------------------------

    def plot_error(self):

        plt.figure(figsize=(8, 5))

        plt.plot(
            self.error,
            self.error_negative,
            label="Negative"
        )

        plt.plot(
            self.error,
            self.error_zero,
            label="Zero"
        )

        plt.plot(
            self.error,
            self.error_positive,
            label="Positive"
        )

        plt.title("Temperature Error Membership")

        plt.xlabel("Error")

        plt.ylabel("Membership")

        plt.legend()

        plt.grid(True)

        plt.show()

    # ---------------------------------------------------------
    # Plot Valve Membership
    # ---------------------------------------------------------

    def plot_valve(self):

        plt.figure(figsize=(8, 5))

        plt.plot(
            self.valve,
            self.valve_low,
            label="Low"
        )

        plt.plot(
            self.valve,
            self.valve_medium,
            label="Medium"
        )

        plt.plot(
            self.valve,
            self.valve_high,
            label="High"
        )

        plt.title("Valve Membership Functions")

        plt.xlabel("Valve Opening (%)")

        plt.ylabel("Membership")

        plt.legend()

        plt.grid(True)

        plt.show()

    # ---------------------------------------------------------
    # Plot Everything
    # ---------------------------------------------------------

    def visualize(self):

        self.plot_temperature()
        self.plot_error()
        self.plot_valve()


# -------------------------------------------------------------
# Standalone Testing
# -------------------------------------------------------------

if __name__ == "__main__":

    mf = MembershipFunctions()

    print(mf.temperature_membership(22))

    print(mf.error_membership(-7))

    print(mf.valve_membership(65))

    mf.visualize()