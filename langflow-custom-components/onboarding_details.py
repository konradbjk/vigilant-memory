from langflow.base.io.text import TextComponent
from langflow.io import MultilineInput, Output
from langflow.schema.message import Message


class TextInputComponent(TextComponent):
    display_name = "Onboarding Details"
    description = "Get text inputs from the Playground."
    icon = "type"
    name = "TextInput"

    inputs = [
        MultilineInput(
            name="goal",
            display_name="Goal",
            info="Text to be passed as input.",
        ),
        MultilineInput(
            name="industry",
            display_name="Industry",
            info="Text to be passed as input.",
        ),
        MultilineInput(
            name="audience",
            display_name="Audience",
            info="Text to be passed as input.",
        ),
        MultilineInput(
            name="perception",
            display_name="Perception",
            info="Text to be passed as input.",
        ),
        MultilineInput(
            name="uvp",
            display_name="Unique Value Points",
            info="Text to be passed as input.",
        ),
        MultilineInput(
            name="tov",
            display_name="Tone of Voice",
            info="Text to be passed as input.",
        ),
    ]
    outputs = [
        Output(display_name="Goal", name="goal_text", method="text_response"),
        Output(display_name="Industry", name="industry_text", method="get_industry"),
        Output(display_name="Audience", name="audience_text", method="get_audience"),        
        Output(display_name="Perception", name="perception_text", method="get_perception"),
        Output(display_name="UVP", name="uvp_text", method="get_uvp"),
        Output(display_name="Tone of Voice", name="tov_text", method="get_tov"),

    ]

    def text_response(self) -> Message:
        message = Message(
            text=self.goal,
        )
        return message


    def get_industry(self) -> Message:
        message = Message(
            text=self.industry,
        )
        return message
        
    def get_audience(self) -> Message:
        message = Message(
            text=self.audience,
        )
        return message
        
    def get_uvp(self) -> Message:
        message = Message(
            text=self.uvp,
        )
        return message
        
    def get_perception(self) -> Message:
        message = Message(
            text=self.perception,
        )
        return message
        
    def get_tov(self) -> Message:
        message = Message(
            text=self.tov,
        )
        return message