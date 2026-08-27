"""
temperature_sensor.py

Simulates a water temperature sensor.
"""

import random


class TemperatureSensor:

    def __init__(
        self,
        initial_temperature=25.0
    ):

        self.temperature = initial_temperature

    # ---------------------------------------------------------
    # Read Temperature
    # ---------------------------------------------------------

    def read(self):
        """
        Return the measured temperature
        with a small amount of sensor noise.
        """

        noise = random.uniform(
            -0.3,
            0.3
        )

        return round(
            self.temperature + noise,
            2
        )

    # ---------------------------------------------------------
    # Update Temperature
    # ---------------------------------------------------------

    def update(
        self,
        new_temperature
    ):

        self.temperature = new_temperature

    # ---------------------------------------------------------
    # Reset
    # ---------------------------------------------------------

    def reset(
        self,
        value=25.0
    ):

        self.temperature = value


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    sensor = TemperatureSensor()

    print(sensor.read())

    sensor.update(37.5)

    print(sensor.read())