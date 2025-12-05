"""
Tools module - Python functions exposed as tools to LLM-based agents.
Each tool is designed to be callable by CrewAI agents.
"""

from .routing_tools import compute_city_routes, estimate_route_time
from .courier_tools import get_available_couriers, assign_tasks_to_courier, get_courier_status
from .ctm_tools import get_intercity_routes, estimate_intercity_eta, book_ctm_transport
from .tracking_tools import update_parcel_status, get_parcel_status, get_parcel_history
from .db_tools import DeliveryDB, db

__all__ = [
    'compute_city_routes',
    'estimate_route_time',
    'get_available_couriers',
    'assign_tasks_to_courier',
    'get_courier_status',
    'get_intercity_routes',
    'estimate_intercity_eta',
    'book_ctm_transport',
    'update_parcel_status',
    'get_parcel_status',
    'get_parcel_history',
    'DeliveryDB',
    'db'
]
