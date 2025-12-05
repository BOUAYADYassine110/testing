"""
Morocco Delivery Multi-Agent System - CrewAI Integration
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool

from .tools import routing_tools, courier_tools, ctm_tools, tracking_tools

@tool
def compute_city_routes_tool(couriers: str, tasks: str) -> str:
    """Compute optimal routes for couriers given tasks (VRP solver)"""
    import json
    try:
        couriers_list = json.loads(couriers) if isinstance(couriers, str) and couriers.strip().startswith('[') else []
        tasks_list = json.loads(tasks) if isinstance(tasks, str) and tasks.strip().startswith('[') else []
    except:
        # Fallback: create dummy data if parsing fails
        couriers_list = [{"id": "courier_001", "location": {"lat": 0, "lng": 0}}]
        tasks_list = [{"id": "task_001", "pickup_loc": {"lat": 0, "lng": 0}, "delivery_loc": {"lat": 0, "lng": 0}}]
    return json.dumps(routing_tools.compute_city_routes(couriers_list, tasks_list))

@tool
def get_available_couriers_tool(city: str) -> str:
    """Get list of available couriers in a city"""
    import json
    return json.dumps(courier_tools.get_available_couriers(city))

@tool
def get_intercity_routes_tool(origin_city: str, destination_city: str) -> str:
    """Get available CTM routes between two cities"""
    import json
    return json.dumps(ctm_tools.get_intercity_routes(origin_city, destination_city))

@tool
def assign_tasks_to_courier_tool(courier_id: str, task_ids: str) -> str:
    """Assign delivery tasks to a specific courier"""
    import json
    return json.dumps(courier_tools.assign_tasks_to_courier(courier_id, json.loads(task_ids)))

@tool
def update_parcel_status_tool(parcel_id: str, status: str, location: str) -> str:
    """Update the status of a parcel"""
    import json
    return json.dumps(tracking_tools.update_parcel_status(parcel_id, status, location))

@tool
def estimate_route_time_tool(route_points: str, vehicle_type: str = "moto") -> str:
    """Estimate time to complete a route"""
    import json
    try:
        points = json.loads(route_points) if isinstance(route_points, str) and route_points.strip().startswith('[') else []
    except:
        points = [{"lat": 0, "lng": 0}]
    return str(routing_tools.estimate_route_time(points, vehicle_type))

@tool
def estimate_intercity_eta_tool(origin_city: str, destination_city: str) -> str:
    """Estimate arrival time for inter-city transport"""
    import json
    return json.dumps(ctm_tools.estimate_intercity_eta(origin_city, destination_city))

@tool
def book_ctm_transport_tool(parcel_id: str, origin_city: str, destination_city: str, parcel_details: str) -> str:
    """Book CTM transport for a parcel"""
    import json
    return json.dumps(ctm_tools.book_ctm_transport(parcel_id, origin_city, destination_city, json.loads(parcel_details)))

@tool
def get_parcel_status_tool(parcel_id: str) -> str:
    """Get current status of a parcel"""
    import json
    return json.dumps(tracking_tools.get_parcel_status(parcel_id))

@tool
def get_parcel_history_tool(parcel_id: str) -> str:
    """Get full tracking history for a parcel"""
    import json
    return json.dumps(tracking_tools.get_parcel_history(parcel_id))


@CrewBase
class MoroccoDeliveryMasCrew:
    """Morocco Delivery Multi-Agent System crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def coordinator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coordinator_agent'],
            tools=[compute_city_routes_tool, get_available_couriers_tool, get_intercity_routes_tool],
            verbose=True
        )

    @agent
    def city_ops_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['city_ops_agent'],
            tools=[get_available_couriers_tool, assign_tasks_to_courier_tool, compute_city_routes_tool, update_parcel_status_tool],
            verbose=True
        )

    @agent
    def routing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['routing_agent'],
            tools=[compute_city_routes_tool, estimate_route_time_tool],
            verbose=True
        )

    @agent
    def intercity_carrier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intercity_carrier_agent'],
            tools=[get_intercity_routes_tool, estimate_intercity_eta_tool, book_ctm_transport_tool, update_parcel_status_tool],
            verbose=True
        )

    @agent
    def tracking_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tracking_support_agent'],
            tools=[get_parcel_status_tool, get_parcel_history_tool],
            verbose=True
        )

    @task
    def plan_delivery_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_delivery_task']
        )

    @task
    def optimize_routes_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_routes_task']
        )

    @task
    def intercity_transfer_task(self) -> Task:
        return Task(
            config=self.tasks_config['intercity_transfer_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Morocco Delivery MAS crew"""
        return Crew(
            agents=self.agents,
            tasks=[self.plan_delivery_task()],  # Only run first task to avoid rate limits
            process=Process.sequential,
            verbose=True
        )
