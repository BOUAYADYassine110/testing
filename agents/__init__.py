"""
Agents module - LLM-based AI controllers for delivery orchestration.
Each agent is designed to be wrapped by CrewAI or similar orchestration platforms.
"""

from .coordinator_agent import GlobalCoordinatorAgent
from .city_ops_agent import CityOpsAgent
from .routing_agent import RoutingOptimizationAgent
from .intercity_carrier_agent import IntercityCarrierAgent
from .tracking_support_agent import TrackingSupportAgent
from .analytics_agent import AnalyticsAgent

__all__ = [
    'GlobalCoordinatorAgent',
    'CityOpsAgent',
    'RoutingOptimizationAgent',
    'IntercityCarrierAgent',
    'TrackingSupportAgent',
    'AnalyticsAgent'
]
