"""
environment.py

Represents the environment surrounding
the shower system.
"""


class Environment:

    def __init__(self):

        self.hot_source = 60.0

        self.cold_source = 15.0

        self.room_temperature = 28.0

    # ---------------------------------------------------------
    # Mixed Water Temperature
    # ---------------------------------------------------------

    def mix_temperature(
        self,
        hot_percentage,
        cold_percentage
    ):
        """
        Compute mixed water temperature.
        """

        total = hot_percentage + cold_percentage

        if total == 0:

            return self.room_temperature

        hot_ratio = hot_percentage / total

        cold_ratio = cold_percentage / total

        mixed = (

            hot_ratio * self.hot_source +

            cold_ratio * self.cold_source

        )

        return round(
            mixed,
            2
        )

    # ---------------------------------------------------------
    # Ambient Cooling
    # ---------------------------------------------------------

    def apply_environment(
        self,
        water_temperature
    ):

        difference = (
            water_temperature -
            self.room_temperature
        )

        adjusted = (
            water_temperature -
            difference * 0.02
        )

        return round(
            adjusted,
            2
        )


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    env = Environment()

    temp = env.mix_temperature(
        80,
        20
    )

    print(temp)

    print(
        env.apply_environment(temp)
    )