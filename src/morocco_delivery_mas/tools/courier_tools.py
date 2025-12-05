"""
Courier Tools - Functions for managing couriers and task assignments.

These functions are intended to be exposed as tools to LLM-based agents in CrewAI.
"""

from typing import List, Dict, Any


# In-memory courier database (placeholder)
_COURIERS_DB = {
    "Casablanca": [
        {"id": "courier_cas_001", "name": "Ahmed", "vehicle": "moto", "status": "available", "location": {"lat": 33.5731, "lng": -7.5898}},
        {"id": "courier_cas_002", "name": "Fatima", "vehicle": "car", "status": "available", "location": {"lat": 33.5892, "lng": -7.6031}},
    ],
    "Rabat": [
        {"id": "courier_rab_001", "name": "Youssef", "vehicle": "moto", "status": "available", "location": {"lat": 34.0209, "lng": -6.8416}},
    ],
    "Marrakech": [
        {"id": "courier_mar_001", "name": "Laila", "vehicle": "van", "status": "busy", "location": {"lat": 31.6295, "lng": -7.9811}},
    ]
}


def get_available_couriers(city: str) -> List[Dict[str, Any]]:
    """
    Get list of available couriers in a specific city.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        city: City name (e.g., "Casablanca", "Rabat")
    
    Returns:
        List of available courier dicts
    """
    couriers = _COURIERS_DB.get(city, [])
    available = [c for c in couriers if c['status'] == 'available']
    
    print(f"[courier_tools] Found {len(available)} available couriers in {city}")
    return available


def assign_tasks_to_courier(courier_id: str, task_ids: List[str]) -> Dict[str, Any]:
    """
    Assign delivery tasks to a specific courier.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        courier_id: Courier identifier
        task_ids: List of task IDs to assign
    
    Returns:
        Assignment confirmation
    """
    print(f"[courier_tools] Assigning tasks {task_ids} to courier {courier_id}")
    
    # Placeholder: In real system, persist to DB and notify courier
    
    return {
        "status": "assigned",
        "courier_id": courier_id,
        "task_ids": task_ids,
        "assigned_at": "2024-01-15 10:00"
    }


def get_courier_status(courier_id: str) -> Dict[str, Any]:
    """
    Get current status and location of a courier.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        courier_id: Courier identifier
    
    Returns:
        Courier status dict
    """
    # Placeholder: Search all cities
    for city, couriers in _COURIERS_DB.items():
        for courier in couriers:
            if courier['id'] == courier_id:
                return {
                    "courier_id": courier_id,
                    "status": courier['status'],
                    "location": courier['location'],
                    "city": city
                }
    
    return {"error": "Courier not found"}
