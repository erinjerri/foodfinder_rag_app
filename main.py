import autogen
from autogen import AssistantAgent, UserProxyAgent
from yelp_api import yelp_search
from doordash_api import doordash_create_delivery
from env import OPEN_AI_KEY

# Define OpenAI Configuration
openai_config= {
    "api_key": os.getenv("OPEN_API_KEY"),
    "model": "gpt-4-turbo"   
}

# Initialize the assistant agent
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant capable of retrieving business information and creating delivery requests.",
    llm_config=llm_config,
)

# Register the Yelp search tool
assistant.register_tool(yelp_search)

# Register the DoorDash delivery creation tool
assistant.register_tool(doordash_create_delivery)

# Initialize the user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",  # Adjust based on your application's requirements
    max_consecutive_auto_reply=3,
)

# Define the user's query
user_query = "Find Italian restaurants in San Francisco and create a delivery request."

# Initiate the chat
user_proxy.initiate_chat(
    assistant,
    message=user_query,
    location="San Francisco, CA",
    category="italian",
    term=None,
    limit=5,
    delivery_details={
        "external_delivery_id": "D-12345",
        "pickup_address": "123 Main St, Anytown, USA",
        "pickup_business_name": "Sender's Business",
        "pickup_phone_number": "+1234567890",
        "dropoff_address": "456 Elm St, Othertown, USA",
        "dropoff_business_name": "Recipient's Business",
        "dropoff_phone_number": "+0987654321",
        "order_value": 1999,  # Value in cents
        "currency": "USD",
        "contactless_dropoff": True,
        "tip": 500,  # Tip in cents
    }
)