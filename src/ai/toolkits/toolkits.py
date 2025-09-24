from src.ai.toolkits.dpc_toolkit import DPCToolkit
from src.ai.toolkits.example_toolkit import ExampleToolkit

class Toolkits:
    dpc_toolkit = DPCToolkit.get_tools()
    example_toolkit = ExampleToolkit.get_tools()