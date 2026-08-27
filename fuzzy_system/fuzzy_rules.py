"""
fuzzy_rules.py

Contains the fuzzy IF-THEN rules for the shower controller.
"""

from typing import Dict


class FuzzyRules:
    """
    Rule base for determining hot and cold valve actions
    based on temperature error.

    Temperature Error = Desired Temperature - Current Temperature
    """

    def __init__(self):
        self.rules = self._build_rules()

    # ---------------------------------------------------------
    # Define Rule Base
    # ---------------------------------------------------------

    def _build_rules(self) -> Dict[str, Dict[str, str]]:
        """
        Rule table.

        Returns:
            Dictionary containing valve actions.
        """

        return {

            "Positive": {
                "hot": "High",
                "cold": "Low"
            },

            "Zero": {
                "hot": "Medium",
                "cold": "Medium"
            },

            "Negative": {
                "hot": "Low",
                "cold": "High"
            }

        }

    # ---------------------------------------------------------
    # Retrieve Rule
    # ---------------------------------------------------------

    def get_rule(self, error_label: str):
        """
        Get valve settings for a given error label.

        Parameters
        ----------
        error_label : str

        Returns
        -------
        dict
        """

        return self.rules.get(
            error_label,
            {
                "hot": "Medium",
                "cold": "Medium"
            }
        )

    # ---------------------------------------------------------
    # Print Rule Base
    # ---------------------------------------------------------

    def print_rules(self):

        print("\n========== FUZZY RULE BASE ==========\n")

        print("Rule 1")
        print("IF Error is Positive")
        print("THEN Hot Valve = High")
        print("AND Cold Valve = Low\n")

        print("Rule 2")
        print("IF Error is Zero")
        print("THEN Hot Valve = Medium")
        print("AND Cold Valve = Medium\n")

        print("Rule 3")
        print("IF Error is Negative")
        print("THEN Hot Valve = Low")
        print("AND Cold Valve = High\n")

    # ---------------------------------------------------------
    # Evaluate Linguistic Error
    # ---------------------------------------------------------

    def evaluate(self, memberships):
        """
        Determine dominant linguistic label.

        Example input:
        {
            "Negative":0.1,
            "Zero":0.6,
            "Positive":0.3
        }

        Returns:
            ("Zero", {...})
        """

        label = max(
            memberships,
            key=memberships.get
        )

        return label, self.get_rule(label)


# ---------------------------------------------------------
# Standalone Test
# ---------------------------------------------------------

if __name__ == "__main__":

    rules = FuzzyRules()

    rules.print_rules()

    sample = {
        "Negative": 0.20,
        "Zero": 0.65,
        "Positive": 0.15
    }

    label, action = rules.evaluate(sample)

    print("\nDominant Error :", label)
    print("Valve Action   :", action)