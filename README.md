# Morocco Delivery Multi-Agent System (MAS)

AI-powered multi-agent delivery system combining inter-city transport via CTM (or equivalent carrier) with intra-city last-mile delivery. Designed to be controlled by LLM-based agents using tools and orchestrated by platforms like CrewAI.

## 🎯 Overview

This system uses multiple specialized AI agents to coordinate complex delivery operations across Morocco:

- **Inter-city transport**: CTM bus/cargo network between major cities
- **Last-mile delivery**: Local couriers (motos, cars, vans) for pickup and final delivery
- **AI orchestration**: LLM-based agents that reason, plan, and execute using Python tools

## 🏗️ Architecture

```
delivery_mas/
├── agents/           # LLM-based AI controller agents
│   ├── coordinator_agent.py       # Master orchestrator
│   ├── city_ops_agent.py          # City-level operations
│   ├── routing_agent.py           # Route optimization (VRP)
│   ├── intercity_carrier_agent.py # CTM transport coordination
│   ├── tracking_support_agent.py  # Customer support & tracking
│   └── analytics_agent.py         # Performance analysis
├── tools/            # Python functions exposed to agents
│   ├── routing_tools.py           # VRP/route computation
│   ├── courier_tools.py           # Courier management
│   ├── ctm_tools.py               # Inter-city transport
│   ├── tracking_tools.py          # Parcel tracking
│   └── db_tools.py                # Database operations
├── tasks/            # High-level workflow orchestration
│   ├── plan_delivery_task.py      # Order planning
│   ├── optimize_routes_task.py    # Route optimization
│   └── intercity_transfer_task.py # CTM transfers
├── config/
│   └── crew_config.yaml           # CrewAI configuration
├── main.py           # Demo entry point
├── requirements.txt
└── README.md
```

## 🤖 Agents

### 1. GlobalCoordinatorAgent
- Analyzes delivery orders
- Determines if intra-city or inter-city
- Decomposes into sub-tasks and delegates

### 2. CityOpsAgent
- Manages local operations within a city
- Assigns couriers to tasks
- Handles CTM handoffs for last-mile

### 3. RoutingOptimizationAgent
- Solves Vehicle Routing Problems (VRP)
- Optimizes courier routes for efficiency
- Re-optimizes on delays or changes

### 4. IntercityCarrierAgent
- Coordinates CTM transport between cities
- Selects routes and estimates ETAs
- Tracks parcels during inter-city transit

### 5. TrackingSupportAgent
- Answers customer queries ("Where is my parcel?")
- Provides tracking information
- Escalates issues to other agents

### 6. AnalyticsAgent
- Analyzes historical delivery data
- Identifies bottlenecks and inefficiencies
- Generates performance reports

## 🛠️ Tools

Each tool is a Python function that agents can call:

- **Routing**: `compute_city_routes`, `estimate_route_time`
- **Couriers**: `get_available_couriers`, `assign_tasks_to_courier`
- **CTM**: `get_intercity_routes`, `estimate_intercity_eta`, `book_ctm_transport`
- **Tracking**: `update_parcel_status`, `get_parcel_status`, `get_parcel_history`
- **Database**: `DeliveryDB` class with query and analytics methods

## 🚀 Quick Start

### 1. Setup Local Environment

```bash
# Clone or navigate to project directory
cd delivery_mas

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Local Demo

```bash
python main.py
```

This runs 6 demos showing:
1. Intra-city delivery (Casablanca)
2. Inter-city delivery (Casablanca → Rabat)
3. Route optimization
4. CTM inter-city transfer
5. Customer support tracking
6. Analytics and insights

### 3. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Morocco Delivery MAS"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/delivery_mas.git
git push -u origin main
```

### 4. Connect to CrewAI Platform

1. Go to [CrewAI Platform](https://www.crewai.com) (or your CrewAI instance)
2. Connect your GitHub repository
3. CrewAI will automatically detect:
   - Agents defined in `config/crew_config.yaml`
   - Tools mapped to Python functions
   - Tasks and workflows
4. Configure your LLM (GPT-4, Claude, etc.)
5. Run your crew!

## 📋 CrewAI Integration

The `config/crew_config.yaml` file defines:

- **Agents**: Role, goal, backstory, tools, and Python class mapping
- **Tools**: Function paths that agents can call
- **Tasks**: High-level workflows with expected outputs
- **Crew**: Overall configuration (process type, LLM settings)

CrewAI will:
1. Parse this YAML configuration
2. Instantiate agents with LLM capabilities
3. Give agents access to specified tools
4. Execute tasks according to the defined process (sequential/hierarchical)

## 🔧 Development

### Adding a New Agent

1. Create agent class in `agents/new_agent.py`
2. Add to `agents/__init__.py`
3. Define in `config/crew_config.yaml` with role, goal, tools
4. Test locally in `main.py`

### Adding a New Tool

1. Create function in appropriate `tools/*.py` file
2. Add docstring: "This function is intended to be exposed as a tool to LLM-based agents in CrewAI."
3. Add to `tools/__init__.py`
4. Reference in `config/crew_config.yaml` under `tools:`
5. Assign to relevant agents

### Adding a New Task

1. Create task function in `tasks/new_task.py`
2. Orchestrate agent calls and tool usage
3. Add to `tasks/__init__.py`
4. Define in `config/crew_config.yaml` under `tasks:`

## 🗺️ Roadmap

### Phase 1: Core System (Current)
- ✅ Agent architecture
- ✅ Tool layer with stubs
- ✅ Task orchestration
- ✅ CrewAI configuration

### Phase 2: Real Integrations
- [ ] Integrate Google OR-Tools for VRP
- [ ] Connect to real CTM API (or build adapter)
- [ ] Add PostgreSQL/MongoDB database
- [ ] Implement real-time courier tracking (GPS)

### Phase 3: Production Features
- [ ] REST API with FastAPI
- [ ] Web dashboard for monitoring
- [ ] Mobile app for couriers
- [ ] Customer notification system (SMS/email)

### Phase 4: Advanced AI
- [ ] Predictive ETAs using ML
- [ ] Dynamic pricing optimization
- [ ] Demand forecasting
- [ ] Autonomous re-routing on delays

## 📊 Example Workflow

**Scenario**: Customer orders delivery from Casablanca to Rabat

1. **GlobalCoordinatorAgent** receives order
   - Determines: Inter-city delivery required
   - Delegates: Pickup → CTM → Last-mile

2. **CityOpsAgent (Casablanca)** handles pickup
   - Calls: `get_available_couriers("Casablanca")`
   - Assigns courier to pick up parcel
   - Delivers to CTM depot

3. **IntercityCarrierAgent** manages CTM transport
   - Calls: `get_intercity_routes("Casablanca", "Rabat")`
   - Books: CTM transport
   - Updates: Tracking status

4. **CityOpsAgent (Rabat)** handles last-mile
   - Receives parcel at CTM depot
   - Assigns local courier
   - Delivers to customer

5. **TrackingSupportAgent** answers customer queries
   - Calls: `get_parcel_status(parcel_id)`
   - Responds: "Your parcel is out for delivery in Rabat"

6. **AnalyticsAgent** learns from delivery
   - Records metrics
   - Identifies if route was optimal
   - Suggests improvements

## 🤝 Contributing

This is a starter template. Contributions welcome:

- Add real API integrations
- Improve routing algorithms
- Add more agents (e.g., InventoryAgent, PricingAgent)
- Build web dashboard
- Add tests

## 📄 License

MIT License - feel free to use and modify for your projects.

## 🙋 Support

For questions about:
- **This codebase**: Open a GitHub issue
- **CrewAI platform**: Check [CrewAI docs](https://docs.crewai.com)
- **Morocco logistics**: Adapt to your specific carrier/courier network

---

**Built with ❤️ for Morocco's delivery ecosystem**
