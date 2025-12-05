"""
Tasks module - High-level task flows that orchestrate agents.
These represent workflows that CrewAI can execute.
"""

from .plan_delivery_task import plan_delivery
from .optimize_routes_task import optimize_routes
from .intercity_transfer_task import intercity_transfer

__all__ = [
    'plan_delivery',
    'optimize_routes',
    'intercity_transfer'
]
