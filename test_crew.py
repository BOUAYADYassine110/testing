"""
Test script to verify crew loads correctly
"""

try:
    from src.morocco_delivery_mas.crew import MoroccoDeliveryMasCrew
    
    print("✅ Crew class imported successfully")
    
    # Try to instantiate
    crew_instance = MoroccoDeliveryMasCrew()
    print("✅ Crew instance created")
    
    # Try to get the crew
    crew = crew_instance.crew()
    print("✅ Crew object created")
    
    # Check agents
    print(f"✅ Number of agents: {len(crew.agents)}")
    for agent in crew.agents:
        print(f"   - {agent.role}")
    
    # Check tasks
    print(f"✅ Number of tasks: {len(crew.tasks)}")
    for task in crew.tasks:
        print(f"   - {task.description[:50]}...")
    
    print("\n🎉 Crew is properly configured!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
