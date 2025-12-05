# CrewAI Integration Guide

## How This Template Connects to CrewAI

This project is structured to be automatically detected by the CrewAI platform once you connect your GitHub repository.

## 🔗 Connection Process

### Step 1: Push to GitHub

```bash
cd delivery_mas
git init
git add .
git commit -m "Initial commit: Morocco Delivery MAS"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/delivery_mas.git
git push -u origin main
```

### Step 2: Connect to CrewAI Platform

1. Log in to [CrewAI Platform](https://www.crewai.com)
2. Navigate to "New Crew" or "Import Crew"
3. Select "Connect GitHub Repository"
4. Authorize CrewAI to access your repository
5. Select the `delivery_mas` repository

### Step 3: CrewAI Auto-Detection

CrewAI will scan your repository and detect:

**From `config/crew_config.yaml`:**
- ✅ 6 Agents (coordinator, city_ops, routing, intercity_carrier, tracking_support, analytics)
- ✅ 12+ Tools (routing, courier, CTM, tracking, database functions)
- ✅ 3 Tasks (plan_delivery, optimize_routes, intercity_transfer)

**Agent Mapping:**
```yaml
coordinator → agents.coordinator_agent.GlobalCoordinatorAgent
city_ops → agents.city_ops_agent.CityOpsAgent
routing → agents.routing_agent.RoutingOptimizationAgent
intercity_carrier → agents.intercity_carrier_agent.IntercityCarrierAgent
tracking_support → agents.tracking_support_agent.TrackingSupportAgent
analytics → agents.analytics_agent.AnalyticsAgent
```

**Tool Mapping:**
```yaml
compute_city_routes → tools.routing_tools.compute_city_routes
get_available_couriers → tools.courier_tools.get_available_couriers
get_intercity_routes → tools.ctm_tools.get_intercity_routes
# ... and all other tools
```

### Step 4: Configure LLM

In the CrewAI platform:
1. Select your LLM provider (OpenAI, Anthropic, etc.)
2. Add your API key
3. Choose model (GPT-4, Claude-3, etc.)
4. Set default temperature (0.7 recommended)

### Step 5: Run Your Crew

Execute tasks through the CrewAI interface:

**Example: Plan a Delivery**
```python
# CrewAI will execute this via the platform
result = crew.kickoff(
    task="plan_delivery",
    inputs={
        "order": {
            "pickup_city": "Casablanca",
            "delivery_city": "Rabat",
            "items": [{"name": "Package", "weight_kg": 2.5}]
        }
    }
)
```

## 🎯 What Happens When CrewAI Runs Your Crew

### 1. Agent Initialization
CrewAI wraps your Python classes with LLM capabilities:
- Loads agent role, goal, backstory from YAML
- Gives agent access to specified tools
- Enables reasoning and decision-making via LLM

### 2. Task Execution
When you run a task (e.g., `plan_delivery`):

1. **GlobalCoordinatorAgent** receives the order
2. LLM analyzes: "Is this intra-city or inter-city?"
3. Agent calls tools: `get_intercity_routes("Casablanca", "Rabat")`
4. LLM reasons: "This requires CTM transport"
5. Agent delegates to **IntercityCarrierAgent**
6. Process continues until task completes

### 3. Tool Execution
When an agent needs to call a tool:
- CrewAI executes the Python function
- Returns result to the agent
- LLM interprets result and decides next action

## 📝 YAML Configuration Explained

### Agent Definition
```yaml
agents:
  - name: coordinator                    # Agent identifier
    role: Global Delivery Coordinator    # LLM role prompt
    goal: Analyze and orchestrate...     # LLM goal prompt
    backstory: You are the master...     # LLM context
    class: agents.coordinator_agent.GlobalCoordinatorAgent  # Python class
    tools:                               # Tools this agent can use
      - routing_tools.compute_city_routes
      - courier_tools.get_available_couriers
    max_iterations: 10                   # Max reasoning loops
    allow_delegation: true               # Can delegate to other agents
```

### Tool Definition
```yaml
tools:
  - name: compute_city_routes
    description: Compute optimal routes for couriers (VRP solver)
    function: tools.routing_tools.compute_city_routes
```

### Task Definition
```yaml
tasks:
  - name: plan_delivery
    description: Plan a new delivery order from intake to execution
    function: tasks.plan_delivery_task.plan_delivery
    agent: coordinator                   # Primary agent for this task
    expected_output: Delivery plan with steps and delegated agents
```

## 🔧 Customization for CrewAI

### Adding Environment Variables

Create `.env` file (not committed to Git):
```bash
OPENAI_API_KEY=your_key_here
CTM_API_KEY=your_ctm_key
DATABASE_URL=postgresql://...
```

Update `config/crew_config.yaml`:
```yaml
crew:
  env_file: .env
```

### Enabling Memory

Already configured in YAML:
```yaml
crew:
  memory: true  # Agents remember conversation context
```

### Changing Process Type

```yaml
crew:
  process: sequential    # Tasks run one after another
  # OR
  process: hierarchical  # Manager agent delegates to workers
```

## 🚀 Advanced: Custom CrewAI Features

### 1. Human-in-the-Loop

Add to agent config:
```yaml
agents:
  - name: coordinator
    human_input: true  # Ask human for confirmation before critical actions
```

### 2. Callbacks

Add to task config:
```yaml
tasks:
  - name: plan_delivery
    callback: tasks.callbacks.notify_customer  # Call after task completes
```

### 3. Conditional Flows

Use task dependencies:
```yaml
tasks:
  - name: plan_delivery
    next_tasks:
      - optimize_routes (if: delivery_type == "intra_city")
      - intercity_transfer (if: delivery_type == "inter_city")
```

## 📊 Monitoring in CrewAI

Once running, you'll see:
- **Agent Reasoning**: LLM thought process
- **Tool Calls**: Which tools were called and results
- **Task Progress**: Current step in workflow
- **Costs**: Token usage and API costs
- **Logs**: Full execution trace

## 🐛 Troubleshooting

### "Agent not found"
- Check `class:` path in YAML matches actual Python file
- Ensure `__init__.py` exports the class

### "Tool not found"
- Check `function:` path in YAML matches actual function
- Ensure function is in `tools/__init__.py` exports

### "Import errors"
- Run `pip install -r requirements.txt`
- Check Python version (3.9+ recommended)

### "LLM not responding"
- Verify API key is set
- Check LLM provider status
- Try reducing `max_iterations`

## 📚 Next Steps

1. **Test Locally**: Run `python main.py` to verify everything works
2. **Push to GitHub**: Commit and push your code
3. **Connect to CrewAI**: Link your repository
4. **Configure LLM**: Add API keys
5. **Run First Task**: Execute `plan_delivery` task
6. **Monitor & Iterate**: Watch agent reasoning, improve prompts

## 🔗 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [LangChain Tools](https://python.langchain.com/docs/modules/agents/tools/)

---

**Your multi-agent delivery system is now ready for CrewAI! 🚀**
