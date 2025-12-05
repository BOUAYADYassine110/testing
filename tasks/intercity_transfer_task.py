"""
Intercity Transfer Task - Orchestrates CTM transport between cities.

This task coordinates IntercityCarrierAgent to handle inter-city transport.
"""

from typing import Dict, Any
from agents import IntercityCarrierAgent
from tools import update_parcel_status


def intercity_transfer(parcel_id: str, origin_city: str, destination_city: str, 
                       parcel_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute inter-city transfer via CTM.
    
    This function represents a CrewAI task that:
    1. Calls IntercityCarrierAgent to plan transport
    2. Books CTM transport
    3. Updates tracking status
    4. Returns transport details
    
    Args:
        parcel_id: Parcel identifier
        origin_city: Origin city
        destination_city: Destination city
        parcel_info: Parcel details
    
    Returns:
        Transfer confirmation and tracking info
    """
    print(f"\n=== INTERCITY TRANSFER TASK ===")
    print(f"Parcel: {parcel_id}")
    print(f"Route: {origin_city} -> {destination_city}")
    
    # Step 1: Call IntercityCarrierAgent to plan
    carrier_agent = IntercityCarrierAgent()
    transport_plan = carrier_agent.plan_intercity_transport(
        origin_city, destination_city, parcel_info
    )
    
    print(f"\nTransport Plan:")
    print(f"  Carrier: {transport_plan['carrier']}")
    print(f"  Route ID: {transport_plan['route_id']}")
    print(f"  ETA: {transport_plan['estimated_eta_hours']} hours")
    print(f"  Cost: {transport_plan['cost_mad']} MAD")
    
    # Step 2: Update tracking
    update_parcel_status(
        parcel_id, 
        "ctm_booked", 
        f"CTM_Depot_{origin_city}",
        f"Booked on route {transport_plan['route_id']}"
    )
    
    # Step 3: Simulate handoff confirmation
    handoff = carrier_agent.confirm_handoff(
        parcel_id, 
        "pickup", 
        f"CTM_Depot_{origin_city}"
    )
    
    print(f"\nHandoff Confirmed:")
    print(f"  Location: {handoff['location']}")
    print(f"  Timestamp: {handoff['timestamp']}")
    
    return {
        "status": "in_transit",
        "parcel_id": parcel_id,
        "transport_plan": transport_plan,
        "handoff": handoff
    }
