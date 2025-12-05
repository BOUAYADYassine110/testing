# Deployment Troubleshooting

## "Crew not found or unavailable"

This error means CrewAI platform can't detect your crew. Here's how to fix:

### Solution 1: Verify File Structure

Ensure you have:
```
testing/
├── src/
│   └── morocco_delivery_mas/
│       ├── __init__.py
│       ├── crew.py          ← Must exist
│       ├── main.py
│       ├── config/
│       │   ├── agents.yaml  ← Must exist
│       │   └── tasks.yaml   ← Must exist
│       └── tools/
├── pyproject.toml           ← Must exist
└── uv.lock                  ← Must exist
```

### Solution 2: Check pyproject.toml

Verify `pyproject.toml` has correct package name:
```toml
[project]
name = "morocco-delivery-mas"

[tool.hatch.build.targets.wheel]
packages = ["src/morocco_delivery_mas"]
```

### Solution 3: Verify crew.py Export

At the end of `crew.py`, ensure:
```python
# Instantiate crew for CrewAI platform
morocco_delivery_crew = MoroccoDeliveryMasCrew().crew()
```

### Solution 4: Push All Files

```bash
git add -A
git commit -m "Fix crew detection"
git push
```

### Solution 5: Alternative - Use crewai.yaml

If platform still can't detect, create `crewai.yaml` in root:

```yaml
project:
  name: morocco-delivery-mas
  version: 0.1.0
  
crew:
  module: morocco_delivery_mas.crew
  class: MoroccoDeliveryMasCrew
  
agents:
  - coordinator_agent
  - city_ops_agent
  - routing_agent
  - intercity_carrier_agent
  - tracking_support_agent

tasks:
  - plan_delivery_task
  - optimize_routes_task
  - intercity_transfer_task
```

### Solution 6: Check Platform Logs

In CrewAI platform:
1. Go to your deployment
2. Click "Logs" or "Build Logs"
3. Look for specific error messages
4. Share error here for help

### Solution 7: Manual Deployment

If auto-detection fails, try manual setup:

1. In CrewAI platform, click "Manual Setup"
2. Specify:
   - **Crew File**: `src/morocco_delivery_mas/crew.py`
   - **Crew Class**: `MoroccoDeliveryMasCrew`
   - **Config Path**: `src/morocco_delivery_mas/config`

### Common Issues

**Issue**: "Module not found"
**Fix**: Ensure `src/morocco_delivery_mas/__init__.py` exists

**Issue**: "Invalid YAML"
**Fix**: Check `agents.yaml` and `tasks.yaml` syntax

**Issue**: "Dependencies failed"
**Fix**: Run `crewai install` locally first to verify

### Test Locally First

Before deploying, test locally:
```bash
cd testing
crewai install
crewai run
```

If it works locally, it should work on platform.

### Still Not Working?

Try deploying with CrewAI CLI:
```bash
crewai login
crewai deploy
```

This gives more detailed error messages.
