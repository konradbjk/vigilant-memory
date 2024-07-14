from langflow.custom import Component
from langflow.helpers.data import data_to_text
from langflow.io import DataInput, MultilineInput, Output, StrInput
from langflow.schema.message import Message


class ParseDataComponent(Component):
    display_name = "Parse Data"
    description = "Convert Data into plain text following a specified template."
    icon = "braces"
    name = "ParseData"

    inputs = [
        DataInput(name="data", display_name="Data", info="The data to convert to text."),
        StrInput(name="sep", display_name="Separator", advanced=True, value="\n"),
    ]

    outputs = [
        Output(display_name="Text", name="text", method="parse_data"),
    ]

    def parse_data(self) -> Message:
        data = self.data if isinstance(self.data, list) else [self.data]
        
        result_string = ""
        for el in data:
            source = el.data.get('title', 'No Title Provided')  
            content = el.data.get('text', 'No Text Provided').replace('\n', ' ') 
            result_string += f"<quote title={source}>{content}</quote>\n"

        print(result_string)

        return result_string
