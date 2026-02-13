from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.models.lite_llm import LiteLlm
from catalog_agent.agent import catalog_agent


def save_user_info(
    tool_context: ToolContext,
    name: str,
    email: str,
    mobile: str
):
    tool_context.state["name"] = name
    tool_context.state["email"] = email
    tool_context.state["mobile"] = mobile
    tool_context.state["user_info_saved"] = True


local_model = LiteLlm(
    model="ollama_chat/qwen2.5:7b-instruct"
)


root_agent = LlmAgent(
    name="ecommerce_agent",
    description="Root purchasing agent",
    model=local_model,
    instruction="""
SYSTEM ROLE:
You are an ECOMMERCE PURCHASING AGENT.

FIRST RESPONSE (MANDATORY):
- Introduce yourself as a purchasing assistant.
- Say user details are required to proceed.
- Ask ONLY for the user's NAME.

USER INFO COLLECTION (STRICT ORDER):
1. name
2. email
3. mobile

RULES:
- Ask ONLY one field at a time.
- Do NOT talk about products before info collection.
- Once all three are collected, call save_user_info EXACTLY ONCE.

AFTER SAVING USER INFO:
Ask:
"Would you like to browse products or track an existing order?"

INTENT ROUTING:
- Browse / buy → catalog_agent

TOOLS ALLOWED:
- save_user_info
- transfer_to_agent

FORBIDDEN:
- No generic greetings
- No answering product questions
""",
    tools=[save_user_info],
    sub_agents=[catalog_agent]
)
