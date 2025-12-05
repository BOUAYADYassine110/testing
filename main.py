"""
Main entry point for Morocco Delivery Multi-Agent System.

This demonstrates how agents and tools work together.
Run this locally to test the system before connecting to CrewAI.
"""

from tasks import plan_delivery, optimize_routes, intercity_transfer
from agents import TrackingSupportAgent, AnalyticsAgent
from tools import update_parcel_status, get_parcel_status


def demo_intra_city_delivery():
    """Demo: Simple intra-city delivery in Casablanca."""
    print("\n" + "="*60)
    print("DEMO 1: Intra-City Delivery (Casablanca)")
    print("="*60)
    
    order = {
        "pickup_city": "Casablanca",
        "delivery_city": "Casablanca",
        "pickup_address": "123 Rue Mohammed V",
        "delivery_address": "456 Boulevard Zerktouni",
        "items": [{"name": "Package", "weight_kg": 2.5}],
        "customer_name": "Ahmed El Fassi",
        "priority": "standard"
    }
    
    result = plan_delivery(order)
    print(f"\nResult: {result['status']}")


def demo_inter_city_delivery():
    """Demo: Inter-city delivery from Casablanca to Rabat."""
    print("\n" + "="*60)
    print("DEMO 2: Inter-City Delivery (Casablanca -> Rabat)")
    print("="*60)
    
    order = {
        "pickup_city": "Casablanca",
        "delivery_city": "Rabat",
        "pickup_address": "789 Avenue Hassan II",
        "delivery_address": "321 Rue Souissi",
        "items": [{"name": "Documents", "weight_kg": 0.5}],
        "customer_name": "Fatima Benali",
        "priority": "express"
    }
    
    result = plan_delivery(order)
    print(f"\nResult: {result['status']}")


def demo_route_optimization():
    """Demo: Route optimization for multiple deliveries."""
    print("\n" + "="*60)
    print("DEMO 3: Route Optimization")
    print("="*60)
    
    pending_tasks = [
        {"id": "task_1", "pickup_loc": {"lat": 33.5731, "lng": -7.5898}, "delivery_loc": {"lat": 33.5892, "lng": -7.6031}},
        {"id": "task_2", "pickup_loc": {"lat": 33.5800, "lng": -7.5950}, "delivery_loc": {"lat": 33.5950, "lng": -7.6100}},
        {"id": "task_3", "pickup_loc": {"lat": 33.5750, "lng": -7.5920}, "delivery_loc": {"lat": 33.5880, "lng": -7.6050}},
    ]
    
    result = optimize_routes("Casablanca", pending_tasks)
    print(f"\nResult: {result['status']}")


def demo_intercity_transfer():
    """Demo: CTM inter-city transfer."""
    print("\n" + "="*60)
    print("DEMO 4: CTM Inter-City Transfer")
    print("="*60)
    
    parcel_info = {
        "parcel_id": "PKG_001",
        "weight_kg": 3.0,
        "size": "medium"
    }
    
    result = intercity_transfer(
        "PKG_001",
        "Casablanca",
        "Marrakech",
        parcel_info
    )
    print(f"\nResult: {result['status']}")


def demo_tracking_support():
    """Demo: Customer support tracking query."""
    print("\n" + "="*60)
    print("DEMO 5: Customer Support - Tracking Query")
    print("="*60)
    
    # First, create some tracking data
    update_parcel_status("PKG_123", "picked_up", "Casablanca Depot")
    update_parcel_status("PKG_123", "in_transit", "En route to Rabat")
    
    # Now query as customer support agent
    support_agent = TrackingSupportAgent()
    response = support_agent.handle_customer_query(
        "Where is my package?",
        "PKG_123"
    )
    
    print(f"\nAgent Response: {response}")
    
    # Get full history
    history = support_agent.get_parcel_history("PKG_123")
    print(f"\nTracking History ({len(history)} events):")
    for event in history:
        print(f"  - {event['timestamp']}: {event['status']} at {event['location']}")


def demo_analytics():
    """Demo: Analytics and insights."""
    print("\n" + "="*60)
    print("DEMO 6: Analytics & Insights")
    print("="*60)
    
    analytics_agent = AnalyticsAgent()
    
    # Analyze performance
    performance = analytics_agent.analyze_delivery_performance("last_7_days")
    print(f"\nPerformance Metrics:")
    print(f"  Total Deliveries: {performance['total_deliveries']}")
    print(f"  On-Time Rate: {performance['on_time_rate']*100:.1f}%")
    print(f"  Avg Delivery Time: {performance['avg_delivery_time_hours']} hours")
    
    # Identify bottlenecks
    bottlenecks = analytics_agent.identify_bottlenecks()
    print(f"\nBottlenecks Identified: {len(bottlenecks)}")
    for bottleneck in bottlenecks:
        print(f"  - {bottleneck['type']}: {bottleneck['issue']}")
        print(f"    Recommendation: {bottleneck['recommendation']}")


def main():
    """Run all demos."""
    print("\n" + "="*60)
    print("MOROCCO DELIVERY MULTI-AGENT SYSTEM - DEMO")
    print("="*60)
    print("\nThis demo shows how agents and tools work together.")
    print("In production, CrewAI will orchestrate these agents with LLMs.\n")
    
    demo_intra_city_delivery()
    demo_inter_city_delivery()
    demo_route_optimization()
    demo_intercity_transfer()
    demo_tracking_support()
    demo_analytics()
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)
    print("\nNext Steps:")
    print("1. Push this code to GitHub")
    print("2. Connect your GitHub repo to CrewAI platform")
    print("3. CrewAI will detect agents, tools, and tasks from config/crew_config.yaml")
    print("4. Run your crew on the CrewAI platform with real LLMs!")
    print()


if __name__ == "__main__":
    main()
