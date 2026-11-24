# AI Lawyer

Веб-сервис, который помогает проверять и сравнивать договоры между контрагентами.

> Название продукта: **Klauzula AI** (ADR-0006, proposed) — проверка NDA по плейбуку компании и нормам права Польши для in-house юристов.
> Статус: прототип v0.2 (Project Step 3, по процессу TO-BE).

## Где что лежит
| Путь | Содержание |
|------|------------|
| `docs/00_overview.md` | Суть продукта и целевой пользователь |
| `docs/01_requirements.md` | Требования |
| `docs/02_user_stories.md` | Пользовательские сценарии |
| `docs/03_architecture.md` | Архитектура |
| `docs/04_ai_prompts.md` | Промты для LLM и их версии |
| `docs/05_legal_compliance.md` | GDPR, конфиденциальность, дисклеймеры |
| `docs/06_playbook/` | Чек-листы проверки договоров |
| `docs/07_research.md` | Исследование: проблема, пользователи, конкуренты в Польше и ЕС (Project Step 2) |
| `docs/08_design.md` | Название, визуальный стиль, макеты (Step 3) |
| `docs/mockups/` | Дизайн-пак: процесс, стиль, макеты экранов (HTML) |
| `docs/diagrams/` | Схемы процессов (SVG) |
| `skills/nda-review/SKILL.md` | Инструкции для AI (prompt-v1) |
| `app/` | Прототип v0.2: сервер, движок проверки, интерфейс, тесты |
| `docs/decisions/` | Архитектурные решения (ADR) |
| `docs/meetings/` | Заметки встреч и интервью |
| `CHANGELOG.md` | История изменений |
| `CLAUDE.md` | Инструкции для Claude по ведению проекта |

## Запуск прототипа
Нужен только Python 3.9+ (уже есть на macOS), без установки пакетов.

```bash
python3 app/server.py
```

Откройте http://localhost:8000 и нажмите **Try the sample NDA**. Дальше: примите правки → «Yes — send edits to the counterparty» → «Try sample version 2» (раунд 2). Остановить сервер: `Ctrl+C`.

Тесты:

```bash
python3 -m unittest discover -s app/tests
```

### Claude-режим (по желанию)
По умолчанию работает rule-based проверка (демо, офлайн). Чтобы проверять через Claude, нужен Python ≥ 3.10:

```bash
pip3 install anthropic
export ANTHROPIC_API_KEY=...   # ключ не коммитить
python3 app/server.py
```

В правом верхнем углу появится «Claude mode». Перед отправкой текст маскируется (ФИО после слов-маркеров, e-mail, телефоны, PESEL, NIP, KRS, IBAN).

> Не загружайте реальные конфиденциальные договоры — только обезличенные примеры.
