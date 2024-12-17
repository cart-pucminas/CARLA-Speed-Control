#!/usr/bin/env python
"""Our Plate Segmentation Project"""

from __future__ import print_function

import logging
from types import SimpleNamespace
from Controls.Simulation import Simulation
from Utils.ConfigLoader import ConfigLoader


def main():
    """Main method"""

    # Directly define the simulation configuration
    config = ConfigLoader("./config.json")
    config.load()

    # Set up logging based on debug mode
    log_level = logging.DEBUG if config.get("debug") else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('Listening to server %s:%s', config.get("host"), config.get("port"))

    print(__doc__)

    try:
        # Pass the configuration to the Simulation class
    
        simulation = Simulation(config.get_args())
        simulation.initialize()
        simulation.run()
    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')



if __name__ == '__main__':
    main()
