#!/usr/bin/env python
"""
Main entry point for Morocco Delivery MAS
"""

import sys
from crew import MoroccoDeliveryMasCrew


def run():
    """
    Run the crew.
    """
    inputs = {
        'order': {
            'pickup_city': 'Casablanca',
            'delivery_city': 'Rabat',
            'items': [{'name': 'Package', 'weight_kg': 2.5}],
            'priority': 'express'
        }
    }
    
    MoroccoDeliveryMasCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
