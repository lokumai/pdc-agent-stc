import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from src.ai.toolkits.toolkits import Toolkits
from src.ai.prompts.prompts import Prompts

load_dotenv()

class STCAgentConfig:
	@staticmethod
	def get_config():
		return {
			"prompt": Prompts.stc_prompt,
			"model": ChatOllama(
				model=os.getenv("MODEL_NAME", "qwen3:1.7b"),
				validate_model_on_init=True,
				temperature=1.0,
				seed=42,
				reasoning=False,
				num_ctx=32000,
				max_tokens=4096,
				base_url="http://localhost:11434",
			),
			"tools": Toolkits.dpc_toolkit,
		}
