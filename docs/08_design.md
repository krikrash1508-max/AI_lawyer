---
title: Название, визуальный стиль и макеты
version: 0.3.0
status: draft
owner: TBD
updated: 2026-11-24
---

# Название, визуальный стиль и макеты

Интерактивная версия (процесс, стиль, макеты экранов, спецификация, наблюдения): [`docs/mockups/klauzula-design.html`](mockups/klauzula-design.html) — открыть в браузере.

> **0.3.0:** макеты перестроены по процессу TO-BE ([ADR-0007](decisions/0007-scope-v0-2-to-be-process.md)): экраны Upload → Report → Decision → Round 2 → Playbook; вкладка Compare и экран надстройки Word убраны из макетов; логотип перерисован в SVG и используется в прототипе; название «Klauzula AI» во всех макетах и в интерфейсе.

## 1. Название
**Klauzula AI** (Klauzula — польск. «оговорка, пункт договора»): [ADR-0006](decisions/0006-product-name-klauzula-ai.md), proposed. Заменяет «Klauzula» из ADR-0005.
- Слоган: *Your playbook, every clause.* / *Twój playbook w każdej klauzuli.*
- Логотип: лист договора со знаком «§» и строкой с галочкой, подробнее в [разделе 4](#4-логотип).
- ~~Логотип: знак «§» в круге — как оттиск печати (pieczątka), без картинок и иконок.~~ **Устарело (0.2.0):** заменено сгенерированным логотипом (раздел 4). Лист со строкой и галочкой прямо показывает, что делает продукт: проверяет пункты договора.
- Тон: спокойный, точный, без обещаний «заменить юриста». Глаголы: check, flag, propose, decide.

## 2. Визуальный стиль
Идея: **стол юриста** — слева лист договора, справа замечания, сверху — решение юриста «Any red flags?». Договор набран шрифтом с засечками (как документ), интерфейс — без засечек.

| Токен | Цвет | Роль |
|-------|------|------|
| `--ink` | `#16213A` | Текст, логотип |
| `--paper` | `#F2F4F8` | Фон страницы (холодный, не кремовый) |
| `--sheet` | `#FFFFFF` | Лист договора, карточки |
| `--stamp` | `#3A3D9E` | Акцент: фиолетово-синие чернила печати |
| `--risk` | `#B42318` | Red flag (семантика, не акцент) |
| `--review` | `#A15C07` | Review |
| `--ok` | `#1E7A4F` | OK |
| `--brand-ok` | `#6FD3A0` | Галочка в логотипе (только бренд, не статус) |

| Роль | Шрифт | Где |
|------|-------|-----|
| Интерфейс | IBM Plex Sans | Кнопки, карточки, заголовки |
| Документ | IBM Plex Serif | Текст договора, цитаты, формулировки |
| Служебный | IBM Plex Mono | Номера пунктов «§ 4», ID правил, метки `[NAME_1]`, `[EMAIL_1]` |

Правила: цвет риска только для риска (полоса слева у карточки и пункта); акцент — только для действий, бренда и блока решения юриста; ссылка на норму права — плашка в цвете `--stamp-soft` с пометкой «Polish law · to verify»; изменённые с прошлого раунда пункты — метка `modified / added / removed` и пословный diff прямо в тексте; тёмная тема поддерживается.

## 3. Макеты экранов
Экраны идут в порядке шагов TO-BE ([03_architecture.md](03_architecture.md), раздел 2). Всё — один экран «Review contract» и вкладка «Playbook».

| # | Экран | Шаг TO-BE | Что на нём | В v0.2 |
|---|-------|-----------|-----------|--------|
| 1 | Upload | Юрист загружает файл | «Task from sales / purchasing · round 1», drag-and-drop, вставка текста, «Try the sample NDA» | ✅ |
| 2 | Report | Маскирует → анализирует → генерирует отчёт | Сводка (N Red flag / Review / OK, что замаскировано, включая NAME), лист договора с подсветкой, карточки: цитата, объяснение, плейбук, **норма права**, правка с Accept / Reject | ✅ |
| 3 | Decision | Проверяет отчёт → «Есть красные флаги?» | Блок «Your decision»: число флагов и принятых правок; «No — ready for signing» / «Yes — send edits»; экспорт отчёта; список правок для бизнеса | ✅ |
| 4 | Round 2 | Новая версия — снова на проверку | «Upload new version» → блок «Since round 1» (New risk / Improved), изменённые пункты в тексте | ✅ (заменяет вкладку Compare) |
| 5 | Playbook | — | Таблица правил: стандарт, красный флаг, **норма права**, резервная формулировка | ✅ (только просмотр) |

~~Экран 5 «Надстройка Word»~~ **убран из макетов (0.3.0):** его нет на схеме TO-BE. Идея остаётся в наблюдениях как направление после пилота (track changes в .docx).

## 4. Логотип
Сгенерирован для курсового задания «промо-изображение решения». Файлы лежат в [`docs/brand/`](brand/).

| Файл | Вариант | Где использовать |
|------|---------|------------------|
| [`klauzula-logo-full.webp`](brand/klauzula-logo-full.webp) | Полный: символ и надпись «Klauzula AI» | Шапка сайта, слайды, постер |
| [`klauzula-symbol.png`](brand/klauzula-symbol.png) | Только символ (244×292 px) | Аватар |
| [`klauzula-mark.svg`](brand/klauzula-mark.svg) | Символ в векторе (перерисован вручную по PNG) | Favicon и шапка прототипа (`app/static/favicon.svg`, inline SVG), макеты; в тёмной теме цвета берутся из токенов |

### Сообщение изображения
Klauzula AI помогает in-house юристам польских компаний быстрее проверять NDA по плейбуку компании. Каждое замечание подкреплено цитатой из договора, решение остаётся за юристом.

### Состав знака
| Элемент | Значение |
|---------|----------|
| Лист с загнутым углом | Договор |
| «§» | Пункт договора, юридический контекст |
| Зелёная строка с галочкой | Пункт проверен по плейбуку |
| Цвета | Индиго `#3A3D9E` (`--stamp`) и зелёный `#6FD3A0` (`--ok` тёмной темы) на белом |

### Промт (полный логотип)
```text
Minimalist flat vector logo for "Klauzula", an AI tool that helps in-house lawyers review contracts (NDAs) faster against their company's rules.

Symbol: a simple geometric mark combining a document page with a folded corner and a section sign "§". One clause line on the page is highlighted with a small check mark, suggesting "clause reviewed". Clean, confident, trustworthy. No gavel, no scales of justice, no robot, no brain, no circuit lines.

Layout: symbol on the left, wordmark on the right, horizontally aligned, generous white space around. Centered on the canvas.

Text: exactly the word "Klauzula" — capital K, the rest lowercase, 8 letters: K-l-a-u-z-u-l-a. Modern geometric sans-serif, medium weight, slightly wide letter spacing. No other text, no slogan.

Colour scheme: deep indigo #3A3D9E as the main colour, a single accent of soft green #6FD3A0 for the check mark, on a plain white background. Maximum 2 colours plus white. No gradients, no shadows, no 3D, no texture.

Style: professional legal-tech / SaaS brand identity, Swiss design, flat vector, crisp edges, works in monochrome and at small sizes (favicon).

The logo must be completely original and must not resemble any existing company logo, trademark, app icon or artwork. Do not imitate any known brand or designer style. Avoid generic stock legal clichés.

Format: square 1:1, 1024x1024, high resolution.
```
Итерации в том же чате: генератор сначала выдал слитное «KlauzulaAI», затем «Klauzula AI» с пробелом. Это написание принято в ADR-0006.

### Промт (только символ)
```text
Now create a symbol-only version of this logo: just the document icon with "§" and the green check mark, no wordmark, no text. Centered in a square 1:1 canvas, filling about 70% of it, on white background. Keep the same colours and line style. It must stay clear and recognisable at 32x32 px.
```

### Проверка перед использованием (коммерческое использование)
| Проверка | Как | Статус |
|----------|-----|--------|
| Условия сервиса разрешают коммерческое использование | Актуальные Terms of Use сервиса и тарифа; сохранить скриншот и дату | ⬜ Не проверено (инструмент: TBD) |
| Нет сходства с чужими логотипами | Поиск по картинке: Google Lens, TinEye | ⬜ |
| Нет сходства с зарегистрированными знаками | EUIPO eSearch / TMview: по изображению и по слову «Klauzula AI» | ⬜ |
| Текст без искажений | Побуквенно: «Klauzula AI» | ✅ |
| Права на изображение | В ЕС изображение, созданное только ИИ, может не получить авторско-правовой защиты; для настоящего бренда логотип лучше доработать с дизайнером | ⚠️ Учтено |

Риск сходства: сочетание «§» и листа документа часто встречается у юридических брендов, поэтому поиск по картинке обязателен.

### Открыто
- Квадратный символ 1024×1024 для аватара (текущий файл маленький и не квадратный).
- ~~Вариант для тёмной темы (фон `#11151F`).~~ Решено в 0.3.0: SVG-символ берёт цвета из токенов темы.
- Сверить SVG-перерисовку с исходным PNG (пропорции, толщина линий) при выборе финальной версии.
- Выбор финальной версии голосованием группы.
