"""
Plan Delivery Task - Orchestrates the planning of a new delivery order.

This task coordinates GlobalCoordinatorAgent and other agents to create
a complete delivery plan.
"""

from typing import Dict, Any
from agents import GlobalCoordinatorAgent
from tools import db


def plan_delivery(order: Dict[str, Any]) -> Dict[str, Any]:
    """
    Plan a delivery from order intake to execution plan.
    
    This function represents a CrewAI task that:
    1. Validates the order
    2. Calls GlobalCoordinatorAgent to analyze and decompose
    3. Stores the plan in DB
    4. Returns execution plan
    
    Args:
        order: Order dict with {pickup_city, delivery_city, items, customer_info}
    
    Returns:
        Delivery plan dict
    """
    print("\n=== PLAN DELIVERY TASK ===")
    print(f"Order: {order}")
    
    # Step 1: Store order in DB
    order_id = db.add_order(order)
    order['order_id'] = order_id
    
    # Step 2: Call GlobalCoordinatorAgent
    coordinator = GlobalCoordinatorAgent()
    plan = coordinator.analyze_delivery_request(order)
    
    print(f"\nDelivery Plan Generated:")
    print(f"  Type: {plan['delivery_type']}")
    print(f"  Steps: {plan['plan']['steps']}")
    print(f"  Delegated Agents: {plan['plan']['delegated_agents']}")
    
    # Step 3: In CrewAI, this would trigger delegation to other agents
    # For now, just log what would happen
    for step, agent in zip(plan['plan']['steps'], plan['plan']['delegated_agents']):
        print(f"  -> Would delegate '{step}' to {agent}")
    
    return {
        "status": "planned",
        "order_id": order_id,
        "plan": plan
    }
