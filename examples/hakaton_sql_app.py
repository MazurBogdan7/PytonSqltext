import os
import sys



sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.2, max_tokens=180)

# exemples fore learn 

gpt.add_example(Example("Сколько в серднем участников соревнований", "select avg(participants) from sport s"))
gpt.add_example(Example("Самый популярный адрес для организации соревнований", "select address, count(*) c from sport s group by address order by c desc limit 1"))
gpt.add_example(Example("Топ-10 популярных адресов для организации соревнований", "select address, count(*) c from sport s group by address order by c desc limit 10"))

# Define UI configuration
config = UIConfig(
    description="Learn Sql",
    button_text="Query",
    placeholder="Where are you?",
    show_example_form=True,
)

demo_web_app(gpt, config)
