from categories import categories_dict, categories_list
from collections import namedtuple

import asyncio

ParserResponse = namedtuple("parser_response", ["text_result", "boolean_result"])

async def parse_categories(user_answer: str) -> ParserResponse:
    if user_answer == "exit":
        return ParserResponse("Работа программы завершена", True)

    try:
        categories_names = [categories_list[int(category_index) - 1] for category_index in user_answer.split(" ")]

        categories_tasks = list()
        
        for category_name in categories_names:
            category_task = asyncio.create_task(categories_dict[category_name]())
            categories_tasks.append(category_task)
        await asyncio.gather(*categories_tasks)

        return ParserResponse("Парсер выполнил работу", True)
    
    except IndexError as index_error:
        return ParserResponse("Вы ввели неверный идекс элемента из списка", False)
    
    except ValueError as value_error:
        return ParserResponse("На вход принимаются только целые цифры/числа" \
            "(или порядок цифр/чисел разделенных черещ пробел)", False)
    
    except Exception as error:
        return ParserResponse(error.__class__.__name__, False)


async def main():
    print("Категории доступные для парсинга:\n{}".format(
        '\n'.join(["\t{}. {}".format(index + 1, category) 
            for index, category in enumerate(categories_list)]) 
    ))
    
    print("Из предложенного списка введите индекс категории (категорий через пробел) для парсинга, для выхода введите `exit` ")
    while True:
        user_answer = input("Ваш запрос ")
        result = await parse_categories(user_answer=user_answer)
        print(result.text_result)
        if result.boolean_result:
            break
if __name__ == "__main__":
    asyncio.run(main())