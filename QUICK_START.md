# Quick Start Guide

## 🚀 Get Running in 3 Minutes

### Step 1: Test Locally (1 minute)
```bash
cd delivery_mas
python main.py
```

You should see 6 demos run successfully showing all agents and tools in action.

### Step 2: Push to GitHub (1 minute)
```bash
git init
git add .
git commit -m "Initial commit: Morocco Delivery MAS"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/delivery_mas.git
git push -u origin main
```

### Step 3: Connect to CrewAI (1 minute)
1. Go to CrewAI platform
2. Click "New Crew" → "Connect GitHub"
3. Select `delivery_mas` repository
4. CrewAI auto-detects everything from `config/crew_config.yaml`
5. Add your OpenAI/Anthropic API key
6. Click "Run Crew"

## ✅ What You Get

- **6 AI Agents**: Coordinator, CityOps, Routing, CTM, Support, Analytics
- **12+ Tools**: Routing, courier management, CTM, tracking, database
- **3 Tasks**: Plan delivery, optimize routes, intercity transfer
- **Full Demo**: Working examples of all functionality

## 📁 Key Files

| File | Purpose |
|------|---------|
| `main.py` | Run demos locally |
| `config/crew_config.yaml` | CrewAI configuration |
| `agents/*.py` | AI agent classes |
| `tools/*.py` | Tool functions |
| `tasks/*.py` | Workflow orchestration |

## 🎯 Example Usage

### Local Testing
```python
from tasks import plan_delivery

order = {
    "pickup_city": "Casablanca",
    "delivery_city": "Rabat",
    "items": [{"name": "Package", "weight_kg": 2.5}]
}

result = plan_delivery(order)
print(result)
```

### On CrewAI Platform
The platform will execute the same tasks but with LLM reasoning:
- Agents analyze situations
- Make intelligent decisions
- Call tools dynamically
- Adapt to changes

## 🔧 Customization

### Add a New City
Edit `tools/courier_tools.py`:
```python
_COURIERS_DB = {
    "YourCity": [
        {"id": "courier_001", "vehicle": "moto", "status": "available"}
    ]
}
```

### Add a New Tool
1. Create function in `tools/your_tool.py`
2. Add to `tools/__init__.py`
3. Add to `config/crew_config.yaml` under `tools:`
4. Assign to agents that need it

### Add a New Agent
1. Create class in `agents/your_agent.py`
2. Add to `agents/__init__.py`
3. Add to `config/crew_config.yaml` under `agents:`

## 📚 Documentation

- **Full docs**: See `README.md`
- **CrewAI setup**: See `CREWAI_INTEGRATION.md`
- **Project overview**: See `PROJECT_SUMMARY.md`

## 🐛 Troubleshooting

**Demo doesn't run?**
```bash
pip install -r requirements.txt
python main.py
```

**Import errors?**
Make sure you're in the `delivery_mas` directory.

**CrewAI can't find agents?**
Check that `config/crew_config.yaml` paths match your Python files.

## 🎉 Success!

If `python main.py` runs and shows all 6 demos, you're ready to:
1. Push to GitHub
2. Connect to CrewAI
3. Run your AI-powered delivery system!

---

**Need help?** Check the full documentation in `README.md` and `CREWAI_INTEGRATION.md`
