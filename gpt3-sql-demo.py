import os
import sys
from api import GPT, Example, UIConfig
from api import demo_web_app


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Construct GPT object and show some examples
gpt = GPT(engine="text-davinci-002", temperature=0.7, max_tokens=100)

gpt.add_example(Example(" select all instruments", " SELECT * FROM instrument"))
gpt.add_example(Example(" select all instruments of type Bond",
                        " SELECT * FROM instrument WHERE instrument_type_id = 'Bond'"))
gpt.add_example(Example(" select all instruments of type Bond and maturity date 2021-12-31",
                        " SELECT * FROM instrument WHERE instrument_type_id = 'Bond' AND maturity_date = "
                        "'2021-12-31'"))

# Define UI configuration
config = UIConfig(
    description="SQL from natural language",
    button_text="Generate SQL",
    placeholder="",
    show_example_form=False,
)

demo_web_app(gpt, config)
