# CrewAI Setup Guide

## Quick Start - Local Development

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-...
```

### 3. Run CrewAI Locally

```bash
# Run with CrewAI framework
python crew.py

# Or run standalone demo (no LLM required)
python main.py
```

## Connecting to CrewAI Platform

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Morocco Delivery MAS with CrewAI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/delivery_mas.git
git push -u origin main
```

### Step 2: Connect Repository to CrewAI

1. Go to [CrewAI Platform](https://www.crewai.com)
2. Click "New Crew" or "Import from GitHub"
3. Authorize GitHub access
4. Select your `delivery_mas` repository
5. CrewAI will auto-detect:
   - 6 agents from `config/crew_config.yaml`
   - 12+ tools from `tools/` directory
   - 3 tasks from `tasks/` directory

### Step 3: Configure on Platform

1. **Set API Keys**: Add your OpenAI API key in platform settings
2. **Select LLM**: Choose GPT-4, GPT-3.5-turbo, or Claude
3. **Review Agents**: Check that all 6 agents are detected
4. **Review Tools**: Verify all tools are mapped correctly

### Step 4: Run Your First Task

Execute a delivery planning task through the CrewAI interface:

```python
# This runs on the CrewAI platform
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

## File Structure for CrewAI

```
delivery_mas/
├── agents/              # Agent classes (detected by CrewAI)
├── tools/               # Tools with @tool decorators (auto-detected)
├── tasks/               # Task orchestration functions
├── config/
│   └── crew_config.yaml # Main config (read by CrewAI platform)
├── crew.py              # Local CrewAI instantiation
├── main.py              # Standalone demo (no LLM)
├── .env                 # API keys (DO NOT COMMIT)
├── .env.example         # Template for .env
└── requirements.txt     # Dependencies
```

## What CrewAI Detects

### From `config/crew_config.yaml`:

✅ **Agents**:
- coordinator (Global Delivery Coordinator)
- city_ops (City Operations Manager)
- routing (Route Optimization Specialist)
- intercity_carrier (Inter-City Transport Coordinator)
- tracking_support (Customer Support & Tracking)
- analytics (Analytics & Insights Specialist)

✅ **Tools** (with @tool decorators):
- compute_city_routes
- estimate_route_time
- get_available_couriers
- assign_tasks_to_courier
- get_courier_status
- get_intercity_routes
- estimate_intercity_eta
- book_ctm_transport
- update_parcel_status
- get_parcel_status
- get_parcel_history

✅ **Tasks**:
- plan_delivery
- optimize_routes
- intercity_transfer

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"
```bash
# Make sure .env file exists with:
OPENAI_API_KEY=sk-your-key-here
```

### "Tool not detected by CrewAI"
- Check that `@tool` decorator is present
- Verify function is exported in `tools/__init__.py`
- Ensure function is listed in `config/crew_config.yaml`

### "Agent not working as expected"
- Review agent backstory and goal in YAML
- Check that tools are assigned to correct agents
- Increase `max_iterations` if agent times out

## Next Steps

1. ✅ Test locally with `python crew.py`
2. ✅ Push to GitHub
3. ✅ Connect to CrewAI platform
4. ✅ Run first task on platform
5. 🔄 Monitor agent reasoning and tool calls
6. 🔄 Iterate on agent prompts and tools
7. 🚀 Deploy to production

## Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [LangChain Tools](https://python.langchain.com/docs/modules/agents/tools/)
