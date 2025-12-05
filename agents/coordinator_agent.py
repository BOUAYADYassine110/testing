"""
GlobalCoordinatorAgent - Master orchestrator for delivery requests.

This agent is the entry point for all delivery orders. It analyzes the request,
determines if it's intra-city or inter-city, and delegates to specialized agents.

CrewAI Integration: This class should be wrapped as a CrewAI Agent with role="coordinator"
and given access to all tools for delegation decisions.
"""

from typing import Dict, List, Any


class GlobalCoordinatorAgent:
    """
    LLM-based coordinator that decomposes delivery requests into actionable sub-tasks.
    
    Responsibilities:
    - Parse incoming delivery orders
    - Determine delivery type (intra-city vs inter-city)
    - Delegate to CityOpsAgent, IntercityCarrierAgent, etc.
    - Monitor overall delivery progress
    """
    
    def __init__(self, agent_config: Dict[str, Any] = None):
        """
        Initialize the coordinator agent.
        
        Args:
            agent_config: Configuration dict (e.g., LLM model, temperature, tools access)
        """
        self.config = agent_config or {}
        self.name = "GlobalCoordinator"
    
    def analyze_delivery_request(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze a delivery order and determine the delivery strategy.
        
        LLM Prompt Context:
        "Given this order, determine if it requires inter-city transport (CTM) or 
        is purely intra-city. Return a structured plan."
        
        Args:
            order: Dict with keys like {pickup_city, delivery_city, items, priority}
        
        Returns:
            Dict with {delivery_type, plan, delegated_agents}
        """
        pickup_city = order.get('pickup_city', '')
        delivery_city = order.get('delivery_city', '')
        
        # LLM would reason here; for now, simple logic
        if pickup_city.lower() != delivery_city.lower():
            delivery_type = "inter_city"
            plan = {
                "steps": [
                    "pickup_in_origin_city",
                    "ctm_intercity_transport",
                    "last_mile_in_destination_city"
                ],
                "delegated_agents": ["city_ops", "intercity_carrier", "city_ops"]
            }
        else:
            delivery_type = "intra_city"
            plan = {
                "steps": ["pickup_and_deliver_local"],
                "delegated_agents": ["city_ops"]
            }
        
        return {
            "order_id": order.get('order_id'),
            "delivery_type": delivery_type,
            "plan": plan
        }
    
    def delegate_task(self, task_type: str, task_data: Dict[str, Any]) -> str:
        """
        Delegate a sub-task to another agent.
        
        LLM would use this to call other agents via CrewAI's task delegation.
        
        Args:
            task_type: Type of task (e.g., "route_optimization", "intercity_transfer")
            task_data: Data needed by the target agent
        
        Returns:
            Task ID or confirmation message
        """
        print(f"[{self.name}] Delegating {task_type} with data: {task_data}")
        # In CrewAI, this would trigger another agent's task
        return f"task_{task_type}_delegated"
