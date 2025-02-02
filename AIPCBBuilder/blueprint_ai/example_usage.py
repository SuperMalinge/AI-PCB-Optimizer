from blueprint_ai.main import BlueprintAI

# Initialize the AI
ai = BlueprintAI()

# Load your blueprint data
blueprint_data = load_blueprint_data()  # Your data loading function

# Train the AI
ai.train(blueprint_data)

# Improve a specific blueprint
improved_blueprint = ai.improve_blueprint(your_blueprint)