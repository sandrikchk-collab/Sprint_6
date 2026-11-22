# Sprint_6 — автотесты для «Яндекс.Самоката»

UI-автотесты на Selenium + pytest с Page Object Model и отчётом Allure для учебного сервиса [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/).

## Что проверяется
| Файл | Проверки |
|---|---|
| `tests/test_faq.py` | «Вопросы о важном»: по клику на каждый из 8 вопросов открывается нужный ответ (параметризация) |
| `tests/test_order.py` | позитивный сценарий заказа: две точки входа (кнопка «Заказать» вверху и внизу) × два набора данных |
| `tests/test_logo.py` | логотип «Самоката» ведёт на главную, логотип Яндекса открывает Дзен в новом окне |

## Структура
- `pages/` — Page Object: `BasePage`, `MainPage`, `OrderPage`
- `locators/` — локаторы для каждой страницы
- `data.py` — URL, тексты ответов FAQ, наборы данных для заказа
- `tests/` — тесты и фикстуры (`conftest.py`)
- `allure_results/` — результаты прогона для отчёта Allure

## Запуск
```bash
pip install -r requirements.txt
pytest -v                    # в Firefox, результаты пишутся в allure_results
allure serve allure_results  # открыть отчёт
```
Тесты запускаются в Mozilla Firefox. Для отладки можно запустить в Chrome: `pytest --browser chrome`.
