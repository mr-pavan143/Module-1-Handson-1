"""
shower.py

Represents the complete shower system.
"""

from simulation.valve import Valve
from simulation.environment import Environment
from simulation.temperature_sensor import TemperatureSensor


class Shower:

    def __init__(self):

        self.environment = Environment()

        self.hot_valve = Valve("Hot")

        self.cold_valve = Valve("Cold")

        self.sensor = TemperatureSensor()

    # -------------------------------------------------------
    # Apply Controller Output
    # -------------------------------------------------------

    def apply_valves(
        self,
        hot_percentage,
        cold_percentage
    ):

        self.hot_valve.set_opening(hot_percentage)

        self.cold_valve.set_opening(cold_percentage)

    # -------------------------------------------------------
    # Calculate Water Temperature
    # -------------------------------------------------------

    def update_temperature(self):

        mixed = self.environment.mix_temperature(

            self.hot_valve.percentage,

            self.cold_valve.percentage

        )

        adjusted = self.environment.apply_environment(
            mixed
        )

        self.sensor.update(adjusted)

        return adjusted

    # -------------------------------------------------------
    # Read Current Temperature
    # -------------------------------------------------------

    def get_temperature(self):

        return self.sensor.read()

    # -------------------------------------------------------
    # Reset
    # -------------------------------------------------------

    def reset(self):

        self.hot_valve.reset()

        self.cold_valve.reset()

        self.sensor.reset()

    # -------------------------------------------------------
    # Status
    # -------------------------------------------------------

    def status(self):

        return {

            "temperature": self.sensor.read(),

            "hot_valve": self.hot_valve.percentage,

            "cold_valve": self.cold_valve.percentage

        }


if __name__ == "__main__":

    shower = Shower()

    shower.apply_valves(80,20)

    shower.update_temperature()

    print(shower.status())