"""
valve.py

Represents a water valve in the shower system.
"""

from dataclasses import dataclass


@dataclass
class Valve:
    """
    Represents a hot or cold water valve.
    """

    name: str
    percentage: float = 50.0

    MIN_OPENING = 0.0
    MAX_OPENING = 100.0

    # ---------------------------------------------------------
    # Set Valve Opening
    # ---------------------------------------------------------

    def set_opening(self, percentage: float):
        """
        Set valve opening percentage.
        """

        percentage = max(
            self.MIN_OPENING,
            min(
                self.MAX_OPENING,
                percentage
            )
        )

        self.percentage = percentage

    # ---------------------------------------------------------
    # Increase Opening
    # ---------------------------------------------------------

    def increase(self, step=5.0):

        self.set_opening(
            self.percentage + step
        )

    # ---------------------------------------------------------
    # Decrease Opening
    # ---------------------------------------------------------

    def decrease(self, step=5.0):

        self.set_opening(
            self.percentage - step
        )

    # ---------------------------------------------------------
    # Current Flow
    # ---------------------------------------------------------

    def get_flow(self):
        """
        Return normalized flow (0–1).
        """

        return self.percentage / 100.0

    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(self):

        self.percentage = 50.0

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    def __str__(self):

        return (
            f"{self.name} Valve : "
            f"{self.percentage:.2f}%"
        )


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    hot = Valve("Hot")

    cold = Valve("Cold")

    hot.set_opening(85)

    cold.set_opening(15)

    print(hot)

    print(cold)

    hot.decrease(10)

    cold.increase(10)

    print(hot)

    print(cold)