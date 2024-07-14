from typing import Optional
from langchain_openai import ChatOpenAI
from pydantic.v1 import SecretStr

from langflow.base.constants import STREAM_INFO_TEXT
from langflow.base.models.model import LCModelComponent
from langflow.field_typing import LanguageModel
from langflow.inputs import (
    BoolInput,
    DictInput,
    DropdownInput,
    FloatInput,
    IntInput,
    MessageInput,
    SecretStrInput,
    StrInput,
)

class OpenAIModelComponent(LCModelComponent):
    display_name = "AIML API"
    description = "Generates text using AI/ML API"
    icon = "ChatInput"

    inputs = [
        MessageInput(name="input_value", display_name="Input"),
        IntInput(
            name="max_tokens",
            display_name="Max Tokens",
            advanced=True,
            info="The maximum number of tokens to generate. Set to 0 for unlimited tokens.",
        ),
        DropdownInput(
            name="model_name", 
            display_name="Model Name", 
            advanced=False, 
            options=["claude-3-5-sonnet-20240620", "claude-3-opus-20240229", "gpt-4o", "meta-llama/Llama-3-70b-chat-hf",
               "mistralai/Mistral-7B-Instruct-v0.2"], 
            value="claude-3-5-sonnet-20240620"
        ),
        StrInput(
            name="openai_api_base",
            display_name="OpenAI API Base",
            advanced=True,
            info="The base URL of the OpenAI API. Defaults to https://api.openai.com/v1. You can change this to use other APIs like JinaChat, LocalAI and Prem.",
        ),
        SecretStrInput(
            name="openai_api_key",
            display_name="OpenAI API Key",
            info="The OpenAI API Key to use for the OpenAI model.",
            advanced=False,
            value="OPENAI_API_KEY",
        ),
        FloatInput(
            name="temperature",
            display_name="Temperature",
            value=0.1
        ),
        BoolInput(name="stream", display_name="Stream", info=STREAM_INFO_TEXT, advanced=True),
        StrInput(
            name="system_message",
            display_name="System Message",
            info="System message to pass to the model.",
            advanced=True,
        ),
    ]

    def build_model(
        self
    ) -> LanguageModel:
        
        openai_api_key = self.openai_api_key
        temperature = self.temperature
        model_name: str = self.model_name
        max_tokens = self.max_tokens or 2048
        openai_api_base = self.openai_api_base or "https://api.openai.com/v1"
            
        if not openai_api_base:
            openai_api_base = "https://api.aimlapi.com/v1"
        if openai_api_key:
            api_key = SecretStr(openai_api_key)
        else:
            api_key = None

        output = ChatOpenAI(
            max_tokens=max_tokens or None,
            model=model_name,
            base_url=openai_api_base,
            api_key=api_key,
            temperature=temperature,
        )

        return output