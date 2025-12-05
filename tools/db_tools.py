"""
Database Tools - Simple in-memory database for delivery data.

This is a placeholder that can be swapped with PostgreSQL, MongoDB, etc.
Functions are intended to be exposed as tools to LLM-based agents in CrewAI.
"""

from typing import List, Dict, Any
from datetime import datetime


class DeliveryDB:
    """
    Simple in-memory database for delivery system.
    
    Future: Replace with SQLAlchemy + PostgreSQL or MongoDB.
    """
    
    def __init__(self):
        self.orders = []
        self.deliveries = []
        self.couriers = []
        self.routes = []
    
    def add_order(self, order: Dict[str, Any]) -> str:
        """
        Add a new delivery order.
        
        Args:
            order: Order details dict
        
        Returns:
            Order ID
        """
        order_id = f"ORD_{len(self.orders) + 1:06d}"
        order['order_id'] = order_id
        order['created_at'] = datetime.now().isoformat()
        self.orders.append(order)
        
        print(f"[db_tools] Added order {order_id}")
        return order_id
    
    def get_order(self, order_id: str) -> Dict[str, Any]:
        """
        Retrieve an order by ID.
        
        Args:
            order_id: Order identifier
        
        Returns:
            Order dict or None
        """
        for order in self.orders:
            if order['order_id'] == order_id:
                return order
        return None
    
    def query_deliveries(self, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Query deliveries with optional filters.
        
        This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
        
        Args:
            filters: Dict with filter criteria (e.g., {city: "Casablanca", status: "delivered"})
        
        Returns:
            List of matching deliveries
        """
        if not filters:
            return self.deliveries
        
        results = self.deliveries
        for key, value in filters.items():
            results = [d for d in results if d.get(key) == value]
        
        return results
    
    def add_delivery_record(self, delivery: Dict[str, Any]) -> None:
        """
        Add a delivery record for analytics.
        
        Args:
            delivery: Delivery details
        """
        delivery['recorded_at'] = datetime.now().isoformat()
        self.deliveries.append(delivery)
    
    def get_performance_metrics(self, time_period: str = "last_7_days") -> Dict[str, Any]:
        """
        Calculate performance metrics.
        
        This function is intended to be exposed as a tool to LLM-based agents in CrewAI.
        
        Args:
            time_period: Time period for analysis
        
        Returns:
            Performance metrics dict
        """
        # Placeholder calculation
        total = len(self.deliveries)
        on_time = sum(1 for d in self.deliveries if d.get('on_time', True))
        
        return {
            "time_period": time_period,
            "total_deliveries": total,
            "on_time_deliveries": on_time,
            "on_time_rate": on_time / total if total > 0 else 0,
            "avg_delivery_time_hours": 4.2  # Placeholder
        }


# Global instance (for simple usage)
db = DeliveryDB()
