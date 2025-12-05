"""
Optimize Routes Task - Orchestrates route optimization for a city.

This task coordinates CityOpsAgent and RoutingOptimizationAgent to
optimize courier routes.
"""

from typing import Dict, Any, List
from agents import CityOpsAgent, RoutingOptimizationAgent
from tools import get_available_couriers


def optimize_routes(city: str, pending_tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Optimize delivery routes for a city.
    
    This function represents a CrewAI task that:
    1. Gets available couriers via CityOpsAgent
    2. Calls RoutingOptimizationAgent to compute optimal routes
    3. Returns optimized assignments
    
    Args:
        city: City name
        pending_tasks: List of pending delivery tasks
    
    Returns:
        Optimized route assignments
    """
    print(f"\n=== OPTIMIZE ROUTES TASK ===")
    print(f"City: {city}")
    print(f"Pending Tasks: {len(pending_tasks)}")
    
    # Step 1: Get available couriers
    couriers = get_available_couriers(city)
    print(f"Available Couriers: {len(couriers)}")
    
    # Step 2: Call RoutingOptimizationAgent
    routing_agent = RoutingOptimizationAgent()
    optimized = routing_agent.optimize_routes(couriers, pending_tasks)
    
    print(f"\nOptimization Result:")
    print(f"  Total Distance: {optimized['total_distance_km']} km")
    print(f"  Total Time: {optimized['total_time_min']} min")
    print(f"  Routes: {len(optimized['routes'])} couriers assigned")
    
    # Step 3: In CrewAI, CityOpsAgent would execute assignments
    city_ops = CityOpsAgent(city=city)
    for courier_id, route_info in optimized['routes'].items():
        print(f"  -> Courier {courier_id}: {len(route_info['route'])} tasks")
    
    return {
        "status": "optimized",
        "city": city,
        "optimized_routes": optimized
    }
