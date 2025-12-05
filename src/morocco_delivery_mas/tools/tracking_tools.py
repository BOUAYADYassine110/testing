"""
Tracking Tools - Functions for parcel status tracking and updates.

These functions are intended to be exposed as tools to LLM-based agents in CrewAI.
"""

from typing import List, Dict, Any
from datetime import datetime


# In-memory tracking database (placeholder)
_TRACKING_DB = {}


def update_parcel_status(parcel_id: str, status: str, location: str, notes: str = "") -> Dict[str, Any]:
    """
    Update the status of a parcel.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        parcel_id: Parcel identifier
        status: New status (e.g., "picked_up", "in_transit", "delivered")
        location: Current location
        notes: Optional notes
    
    Returns:
        Update confirmation
    """
    timestamp = datetime.now().isoformat()
    
    if parcel_id not in _TRACKING_DB:
        _TRACKING_DB[parcel_id] = []
    
    event = {
        "timestamp": timestamp,
        "status": status,
        "location": location,
        "notes": notes
    }
    
    _TRACKING_DB[parcel_id].append(event)
    
    print(f"[tracking_tools] Updated {parcel_id}: {status} at {location}")
    
    return {
        "parcel_id": parcel_id,
        "status": "updated",
        "latest_event": event
    }


def get_parcel_status(parcel_id: str) -> Dict[str, Any]:
    """
    Get current status of a parcel.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        parcel_id: Parcel identifier
    
    Returns:
        Current parcel status
    """
    history = _TRACKING_DB.get(parcel_id, [])
    
    if not history:
        return {
            "parcel_id": parcel_id,
            "status": "not_found",
            "message": "No tracking information available"
        }
    
    latest = history[-1]
    
    return {
        "parcel_id": parcel_id,
        "current_status": latest['status'],
        "current_location": latest['location'],
        "last_updated": latest['timestamp'],
        "notes": latest.get('notes', '')
    }


def get_parcel_history(parcel_id: str) -> List[Dict[str, Any]]:
    """
    Get full tracking history for a parcel.
    
    This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
    
    Args:
        parcel_id: Parcel identifier
    
    Returns:
        List of all tracking events
    """
    history = _TRACKING_DB.get(parcel_id, [])
    
    print(f"[tracking_tools] Retrieved {len(history)} events for {parcel_id}")
    
    return history
