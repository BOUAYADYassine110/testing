"""
CTM Tools - Functions for inter-city transport via CTM or equivalent carriers.

These functions are intended to be exposed as tools to LLM-based agents in CrewAI.
Future: Integrate with real CTM API or carrier management system.
"""

from typing import List, Dict, Any
from crewai_tools import tool


# Placeholder CTM route database
_CTM_ROUTES = {
    ("Casablanca", "Rabat"): {"distance_km": 90, "duration_hours": 1.5, "cost_mad": 50, "frequency": "hourly"},
    ("Casablanca", "Marrakech"): {"distance_km": 240, "duration_hours": 3.0, "cost_mad": 80, "frequency": "every_2h"},
    ("Rabat", "Fes"): {"distance_km": 200, "duration_hours": 2.5, "cost_mad": 70, "frequency": "every_2h"},
    ("Marrakech", "Agadir"): {"distance_km": 250, "duration_hours": 3.5, "cost_mad": 90, "frequency": "daily"},
}


@tool("get_intercity_routes")
def get_intercity_routes(origin_city: str, destination_city: str) -> List[Dict[str, Any]]:
    """
    Get available CTM routes between two cities.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        origin_city: Origin city name
        destination_city: Destination city name
    
    Returns:
        List of available routes with details
    """
    route_key = (origin_city, destination_city)
    route_info = _CTM_ROUTES.get(route_key)
    
    if route_info:
        return [{
            "origin": origin_city,
            "destination": destination_city,
            "carrier": "CTM",
            **route_info
        }]
    
    # Check reverse route
    reverse_key = (destination_city, origin_city)
    if reverse_key in _CTM_ROUTES:
        route_info = _CTM_ROUTES[reverse_key]
        return [{
            "origin": origin_city,
            "destination": destination_city,
            "carrier": "CTM",
            **route_info
        }]
    
    return []


@tool("estimate_intercity_eta")
def estimate_intercity_eta(origin_city: str, destination_city: str, departure_time: str = None) -> Dict[str, Any]:
    """
    Estimate arrival time for inter-city transport.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        origin_city: Origin city name
        destination_city: Destination city name
        departure_time: Planned departure time (ISO format)
    
    Returns:
        ETA estimation dict
    """
    routes = get_intercity_routes(origin_city, destination_city)
    
    if not routes:
        return {"error": "No route found"}
    
    route = routes[0]
    duration_hours = route['duration_hours']
    
    return {
        "origin": origin_city,
        "destination": destination_city,
        "estimated_duration_hours": duration_hours,
        "estimated_arrival": "2024-01-15 14:30",  # Placeholder
        "confidence": "high"
    }


@tool("book_ctm_transport")
def book_ctm_transport(parcel_id: str, origin_city: str, destination_city: str, 
                       parcel_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Book CTM transport for a parcel.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        parcel_id: Parcel identifier
        origin_city: Origin city
        destination_city: Destination city
        parcel_details: Parcel size, weight, etc.
    
    Returns:
        Booking confirmation
    """
    print(f"[ctm_tools] Booking CTM transport for {parcel_id}: {origin_city} -> {destination_city}")
    
    routes = get_intercity_routes(origin_city, destination_city)
    if not routes:
        return {"status": "failed", "error": "No route available"}
    
    route = routes[0]
    
    return {
        "status": "confirmed",
        "booking_id": f"CTM_{parcel_id}",
        "parcel_id": parcel_id,
        "route": route,
        "pickup_location": f"CTM_Depot_{origin_city}",
        "delivery_location": f"CTM_Depot_{destination_city}",
        "cost_mad": route['cost_mad']
    }
