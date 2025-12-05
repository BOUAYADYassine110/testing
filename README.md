# Morocco Delivery Multi-Agent System (MAS)

AI-powered multi-agent delivery system combining inter-city transport via CTM with intra-city last-mile delivery.

## Quick Start

```bash
# Install dependencies
crewai install

# Run the crew
crewai run
```

## Structure

```
src/morocco_delivery_mas/
├── config/
│   ├── agents.yaml    # Agent definitions
│   └── tasks.yaml     # Task definitions
├── tools/             # Python tool functions
├── crew.py            # Crew configuration
└── main.py            # Entry point
```

## Agents

- **Global Delivery Coordinator**: Orchestrates delivery operations
- **City Operations Manager**: Manages local courier operations
- **Route Optimization Specialist**: Optimizes delivery routes
- **Inter-City Transport Coordinator**: Manages CTM transport
- **Customer Support Agent**: Handles tracking queries

## Deployment

Push to GitHub and connect to CrewAI Platform for production deployment.
