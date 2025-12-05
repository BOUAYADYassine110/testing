"""
Morocco Delivery Multi-Agent System - CrewAI Integration
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

from .tools.routing_tools import compute_city_routes, estimate_route_time
from .tools.courier_tools import get_available_couriers, assign_tasks_to_courier, get_courier_status
from .tools.ctm_tools import get_intercity_routes, estimate_intercity_eta, book_ctm_transport
from .tools.tracking_tools import update_parcel_status, get_parcel_status, get_parcel_history


@CrewBase
class MoroccoDeliveryMasCrew:
    """Morocco Delivery Multi-Agent System crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    @agent
    def coordinator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coordinator_agent'],
            tools=[compute_city_routes, get_available_couriers, get_intercity_routes],
            llm=self.llm,
            verbose=True
        )

    @agent
    def city_ops_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['city_ops_agent'],
            tools=[get_available_couriers, assign_tasks_to_courier, compute_city_routes, update_parcel_status],
            llm=self.llm,
            verbose=True
        )

    @agent
    def routing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['routing_agent'],
            tools=[compute_city_routes, estimate_route_time],
            llm=self.llm,
            verbose=True
        )

    @agent
    def intercity_carrier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intercity_carrier_agent'],
            tools=[get_intercity_routes, estimate_intercity_eta, book_ctm_transport, update_parcel_status],
            llm=self.llm,
            verbose=True
        )

    @agent
    def tracking_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tracking_support_agent'],
            tools=[get_parcel_status, get_parcel_history],
            llm=self.llm,
            verbose=True
        )

    @task
    def plan_delivery_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_delivery_task'],
            agent=self.coordinator_agent()
        )

    @task
    def optimize_routes_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_routes_task'],
            agent=self.routing_agent()
        )

    @task
    def intercity_transfer_task(self) -> Task:
        return Task(
            config=self.tasks_config['intercity_transfer_task'],
            agent=self.intercity_carrier_agent()
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Morocco Delivery MAS crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True
        )
