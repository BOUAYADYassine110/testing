"""
TrackingSupportAgent - Customer support agent for parcel tracking queries.

Handles customer inquiries like "Where is my parcel?" using tracking tools.

CrewAI Integration: Wrap as Agent with role="customer_support" and tracking_tools access.
"""

from typing import Dict, List, Any


class TrackingSupportAgent:
    """
    LLM-based conversational agent for customer support and tracking.
    
    Responsibilities:
    - Answer customer queries about parcel status
    - Provide delivery ETAs
    - Escalate issues to other agents if needed
    """
    
    def __init__(self, agent_config: Dict[str, Any] = None):
        """
        Initialize tracking support agent.
        
        Args:
            agent_config: Configuration dict
        """
        self.config = agent_config or {}
        self.name = "TrackingSupport"
    
    def handle_customer_query(self, query: str, parcel_id: str = None) -> str:
        """
        Handle a customer query about their parcel.
        
        LLM Prompt Context:
        "Customer asks: '{query}'. Use tracking_tools.get_parcel_status to find info
        and respond in a friendly, helpful manner."
        
        Args:
            query: Customer's question
            parcel_id: Parcel ID if provided
        
        Returns:
            Natural language response
        """
        print(f"[{self.name}] Handling query: {query}")
        
        if not parcel_id:
            return "I'd be happy to help! Could you please provide your parcel tracking number?"
        
        # LLM would call: tracking_tools.get_parcel_status(parcel_id)
        # Then generate natural response
        
        return f"Your parcel {parcel_id} is currently in transit and expected to arrive by 2PM today."
    
    def get_parcel_history(self, parcel_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve full tracking history for a parcel.
        
        Args:
            parcel_id: Parcel identifier
        
        Returns:
            List of tracking events
        """
        print(f"[{self.name}] Retrieving history for {parcel_id}")
        
        # LLM would call: tracking_tools.get_parcel_history(parcel_id)
        from tools import get_parcel_history
        return get_parcel_history(parcel_id)
    
    def escalate_issue(self, parcel_id: str, issue_description: str) -> Dict[str, Any]:
        """
        Escalate a customer issue to appropriate agent (CityOps, Coordinator, etc.).
        
        Args:
            parcel_id: Parcel identifier
            issue_description: Description of the issue
        
        Returns:
            Escalation confirmation
        """
        print(f"[{self.name}] Escalating issue for {parcel_id}: {issue_description}")
        
        return {
            "parcel_id": parcel_id,
            "issue": issue_description,
            "escalated_to": "city_ops_agent",
            "ticket_id": "TICKET_001"
        }
