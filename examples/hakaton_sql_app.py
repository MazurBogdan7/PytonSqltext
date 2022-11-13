import os
import sys

#from api.db.db_connect import send_query



sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.2, max_tokens=180)

# exemples fore learn 

gpt.add_example(Example("Покажи все записи", "select * from sport s"))
gpt.add_example(Example("Сколько записей в таблице", "select count(*) from sport s "))
gpt.add_example(Example("Сколько уникальных подсекций", "select count(distinct subsection) from sport s "))


gpt.add_example(Example("Сколько в среднем участников соревнований", "select avg(participants) from sport s"))
gpt.add_example(Example("Какое минимальное количество участников в соревнованиях", "select min(participants) from sport s"))
gpt.add_example(Example("Какое макисмальное количество участников соревнований", "select max(participants) from sport s"))

gpt.add_example(Example("Какие мероприятия были с минимальным количествои участников", "select * from sport s2 where participants = (select min(participants) from sport s)"))
gpt.add_example(Example("Какая минимальная дата начала соревнований", "select min([start]) from sport s"))
gpt.add_example(Example("Какая макисмальная дата начала соревнований", "select max([start]) from sport s"))
gpt.add_example(Example("Сколько соревнований проходит каждый год", "select count(*) from sport s group by datepart(year, [start])"))
gpt.add_example(Example("Самый популярный адрес для организации соревнований", "select top 1 [address], count(*) c from sport s group by [address] order by c desc"))
gpt.add_example(Example("Топ-10 популярных адресов для организации соревнований", "select top 10 address, count(*) c from sport s group by address order by c desc"))
gpt.add_example(Example("Какие адреса, где были соревнования лишь один раз", "select * from (select address, count(*) c from sport s group by address) s where c = 1"))
gpt.add_example(Example("Сколько дней идут самые длинные соревнования", "select max(datediff(day, [start], [stop])) from sport s "))
gpt.add_example(Example("Какие самые продолжительные соревнования", "select top 1 *, (datediff(day, [start], [stop])) as l from sport s order by l desc"))


gpt.add_example(Example("Сколько мероприятий проходит для каждого вида спорта", "select section, count(*) from sport s group by section"))
gpt.add_example(Example("Вид спорта с наибольшим количеством соревнований", "select top 1 section, count(*) c from sport s group by section order by c desc"))
gpt.add_example(Example("Вид спорта с самым большим количеством участников суммарно", "select top 1 section, sum(participants) c from sport s group by section order by c desc"))

gpt.add_example(Example("Самый популярный месяц в году для проведения соревнований", "select top 1 datepart(month, [start]) as m, count(*) as c from sport s group by datepart(month, [start]) order by c desc"))
gpt.add_example(Example("Сколько соревнований проходит каждый месяц", "select count(*) from sport s group by datepart(month, [start])"))
gpt.add_example(Example("Сколько кубков проходит каждый год", "select datepart(year, [start]) as m, count(*) as c from sport s2  where title like '%кубок%' group by datepart(year, [start])"))

gpt.add_example(Example("Самое редкое название мероприятия", "select top 1 title, count(*) as c from sport group by title order by c asc"))
gpt.add_example(Example("Самое популярное название мероприятия", "select top 1 title, count(*) as c from sport group by title order by c desc"))
gpt.add_example(Example("Какие мероприятия проводились не в России", "select * from sport s where address not like '%Россия%'"))
#gpt.add_example(Example("", ""))

# Define UI configuration
config = UIConfig(
    description="Learn Sql",
    button_text="Query",
    placeholder="Where are you?",
    show_example_form=False,
)

demo_web_app(gpt, config)


