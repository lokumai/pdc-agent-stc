"""Workflow for running a LangGraph ReAct agent with a weather tool and a chat model."""

import json
from langgraph.prebuilt import create_react_agent
import logging
from src.ai.configs.configs import AgentConfigs

logging.basicConfig(level=logging.INFO)


# ===================== CREATE AGENT USING CONFIG ===========================
stc_agent = create_react_agent(**AgentConfigs.stc_config)


# ====================== RUN
# response = stc_agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
# logging.info(json.dumps(response, indent=2, default=str))
# logging.info(response["messages"][-1].content)
