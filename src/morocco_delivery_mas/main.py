#!/usr/bin/env python
import sys
from morocco_delivery_mas.crew import MoroccoDeliveryMasCrew

def run():
    inputs = {
        'order': {
            'pickup_city': 'Casablanca',
            'delivery_city': 'Rabat',
            'items': [{'name': 'Package', 'weight_kg': 2.5}],
            'priority': 'express'
        }
    }
    MoroccoDeliveryMasCrew().crew().kickoff(inputs=inputs)

def train():
    inputs = {'order': {'pickup_city': 'Casablanca', 'delivery_city': 'Rabat'}}
    try:
        MoroccoDeliveryMasCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)
    except Exception as e:
        raise Exception(f"Training failed: {e}")

def replay():
    try:
        MoroccoDeliveryMasCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Replay failed: {e}")

def test():
    inputs = {'order': {'pickup_city': 'Casablanca', 'delivery_city': 'Rabat'}}
    try:
        MoroccoDeliveryMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Test failed: {e}")
