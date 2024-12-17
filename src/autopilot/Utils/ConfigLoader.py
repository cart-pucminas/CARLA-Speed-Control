import json
from types import SimpleNamespace
import logging


class ConfigLoader:
    """
    A class to load and manage configuration for the simulation.
    """

    def __init__(self, filepath):
        """
        Initialize the ConfigLoader with a JSON configuration file path.

        :param filepath: Path to the JSON configuration file.
        """
        self.filepath = filepath
        self.config = {}

    def load(self):
        """
        Load the configuration from the JSON file.

        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(self.filepath, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Error: Configuration file '{self.filepath}' not found.")
            raise
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse configuration file. {e}")
            raise

    def get_args(self):
        """
        Convert the configuration dictionary into a SimpleNamespace for compatibility.

        :return: A SimpleNamespace object with configuration attributes.
        """
        return SimpleNamespace(**self.config)

    def get(self, key, default=None):
        """
        Retrieve a value from the configuration, with an optional default.

        :param key: The configuration key to retrieve.
        :param default: The default value to return if the key is not found.
        :return: The configuration value or the default.
        """
        return self.config.get(key, default)
