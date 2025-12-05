"""
CrewAI Integration - Instantiate and run the Morocco Delivery Multi-Agent System.

This file bridges your Python agent classes with CrewAI's framework.
Run this file to execute tasks using LLM-powered agents.
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Import tools
from tools import (
    compute_city_routes, estimate_route_time,
    get_available_couriers, assign_tasks_to_courier, get_courier_status,
    get_intercity_routes, estimate_intercity_eta, book_ctm_transport,
    update_parcel_status, get_parcel_status, get_parcel_history
)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# ============================================================================
# DEFINE AGENTS
# ============================================================================

coordinator_agent = Agent(
    role="Global Delivery Coordinator",
    goal="Analyze delivery orders and orchestrate the entire delivery process",
    backstory="""You are the master coordinator for a Morocco-wide delivery network.
    You decide whether deliveries are intra-city or require CTM inter-city transport,
    and you delegate tasks to specialized agents.""",
    tools=[compute_city_routes, get_available_couriers, get_intercity_routes],
    llm=llm,
    verbose=True,
    allow_delegation=True,
    max_iter=10
)

city_ops_agent = Agent(
    role="City Operations Manager",
    goal="Manage local pickups, deliveries, and courier assignments within a city",
    backstory="""You are responsible for all delivery operations within a specific city.
    You coordinate couriers, handle CTM handoffs, and ensure smooth last-mile delivery.""",
    tools=[get_available_couriers, assign_tasks_to_courier, compute_city_routes, update_parcel_status],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=8
)

routing_agent = Agent(
    role="Route Optimization Specialist",
    goal="Optimize delivery routes to minimize time and distance",
    backstory="""You are an expert in vehicle routing problems (VRP) and logistics optimization.
    You use advanced algorithms to create the most efficient routes for couriers.""",
    tools=[compute_city_routes, estimate_route_time],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=5
)

intercity_carrier_agent = Agent(
    role="Inter-City Transport Coordinator",
    goal="Manage CTM transport between cities",
    backstory="""You coordinate with CTM and other carriers to move parcels between cities.
    You select optimal routes, estimate ETAs, and track parcels during transit.""",
    tools=[get_intercity_routes, estimate_intercity_eta, book_ctm_transport, update_parcel_status],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=6
)

tracking_support_agent = Agent(
    role="Customer Support & Tracking Agent",
    goal="Answer customer queries and provide parcel tracking information",
    backstory="""You are a friendly customer support agent who helps customers track their parcels
    and answers questions about delivery status. You escalate issues when needed.""",
    tools=[get_parcel_status, get_parcel_history],
    llm=llm,
    verbose=True,
    allow_delegation=True,
    max_iter=5
)

# ============================================================================
# DEFINE TASKS
# ============================================================================

def create_plan_delivery_task(order_details):
    """Create a task to plan a delivery order."""
    return Task(
        description=f"""Plan the delivery for this order:
        - Pickup City: {order_details.get('pickup_city')}
        - Delivery City: {order_details.get('delivery_city')}
        - Items: {order_details.get('items')}
        - Priority: {order_details.get('priority', 'standard')}
        
        Determine if this is intra-city or inter-city delivery.
        If inter-city, coordinate CTM transport.
        Assign couriers for pickup and last-mile delivery.""",
        agent=coordinator_agent,
        expected_output="Delivery plan with assigned couriers, routes, and estimated timeline"
    )

def create_optimize_routes_task(city, tasks):
    """Create a task to optimize courier routes."""
    return Task(
        description=f"""Optimize delivery routes for {city}:
        - Number of tasks: {len(tasks)}
        - Tasks: {tasks}
        
        Find available couriers and compute optimal routes to minimize time and distance.""",
        agent=routing_agent,
        expected_output="Optimized route assignments for each courier with estimated times"
    )

def create_intercity_transfer_task(parcel_id, origin, destination):
    """Create a task for inter-city transfer."""
    return Task(
        description=f"""Coordinate CTM transport:
        - Parcel ID: {parcel_id}
        - Origin: {origin}
        - Destination: {destination}
        
        Find best CTM route, book transport, and provide tracking updates.""",
        agent=intercity_carrier_agent,
        expected_output="Transport booking confirmation with tracking information"
    )

def create_tracking_query_task(parcel_id, customer_query):
    """Create a task to handle customer tracking query."""
    return Task(
        description=f"""Answer customer query about parcel {parcel_id}:
        Query: "{customer_query}"
        
        Provide current status, location, and estimated delivery time.""",
        agent=tracking_support_agent,
        expected_output="Customer-friendly response with tracking information"
    )

# ============================================================================
# CREATE CREW
# ============================================================================

delivery_crew = Crew(
    agents=[
        coordinator_agent,
        city_ops_agent,
        routing_agent,
        intercity_carrier_agent,
        tracking_support_agent
    ],
    tasks=[],  # Tasks will be added dynamically
    process=Process.sequential,
    verbose=True,
    memory=True
)

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def run_delivery_planning_example():
    """Example: Plan an inter-city delivery."""
    print("\n" + "="*60)
    print("CREWAI EXAMPLE: Inter-City Delivery Planning")
    print("="*60 + "\n")
    
    order = {
        "pickup_city": "Casablanca",
        "delivery_city": "Rabat",
        "pickup_address": "123 Rue Mohammed V",
        "delivery_address": "456 Avenue Hassan II",
        "items": [{"name": "Package", "weight_kg": 2.5}],
        "priority": "express"
    }
    
    task = create_plan_delivery_task(order)
    
    crew = Crew(
        agents=[coordinator_agent, city_ops_agent, intercity_carrier_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    
    return result

def run_tracking_query_example():
    """Example: Handle customer tracking query."""
    print("\n" + "="*60)
    print("CREWAI EXAMPLE: Customer Tracking Query")
    print("="*60 + "\n")
    
    # First, create some tracking data
    update_parcel_status("PKG_123", "in_transit", "Casablanca CTM Depot")
    
    task = create_tracking_query_task("PKG_123", "Where is my package?")
    
    crew = Crew(
        agents=[tracking_support_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    
    return result

if __name__ == "__main__":
    print("\n" + "="*60)
    print("MOROCCO DELIVERY MAS - CREWAI INTEGRATION")
    print("="*60)
    print("\nMake sure you have set OPENAI_API_KEY in your .env file!\n")
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        print("See .env.example for reference.")
        exit(1)
    
    # Run examples
    try:
        run_delivery_planning_example()
        # run_tracking_query_example()  # Uncomment to run
    except Exception as e:
        print(f"\nError running crew: {e}")
        print("\nMake sure you have:")
        print("1. Installed all dependencies: pip install -r requirements.txt")
        print("2. Set OPENAI_API_KEY in .env file")
        print("3. Have sufficient OpenAI API credits")
