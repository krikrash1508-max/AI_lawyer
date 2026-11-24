---
title: Название, визуальный стиль и макеты
version: 0.2.0
status: draft
owner: TBD
updated: 2026-11-24
---

# Название, визуальный стиль и макеты

Интерактивная версия (процесс, стиль, макеты экранов): [`docs/mockups/klauzula-design.html`](mockups/klauzula-design.html) — открыть в браузере.

## 1. Название
**Klauzula AI** (Klauzula — польск. «оговорка, пункт договора»): [ADR-0006](decisions/0006-product-name-klauzula-ai.md), proposed. Заменяет «Klauzula» из ADR-0005.
- Слоган: *Your playbook, every clause.* / *Twój playbook w każdej klauzuli.*
- Логотип: лист договора со знаком «§» и строкой с галочкой, подробнее в [разделе 4](#4-логотип).
- ~~Логотип: знак «§» в круге — как оттиск печати (pieczątka), без картинок и иконок.~~ **Устарело (0.2.0):** заменено сгенерированным логотипом (раздел 4). Лист со строкой и галочкой прямо показывает, что делает продукт: проверяет пункты договора.
- Тон: спокойный, точный, без обещаний «заменить юриста». Глаголы: check, flag, propose, decide.

## 2. Визуальный стиль
Идея: **стол юриста** — слева лист договора, справа замечания. Договор набран шрифтом с засечками (как документ), интерфейс — без засечек.

| Токен | Цвет | Роль |
|-------|------|------|
| `--ink` | `#16213A` | Текст, логотип |
| `--paper` | `#F2F4F8` | Фон страницы (холодный, не кремовый) |
| `--sheet` | `#FFFFFF` | Лист договора, карточки |
| `--stamp` | `#3A3D9E` | Акцент: фиолетово-синие чернила печати |
| `--risk` | `#B42318` | Red flag (семантика, не акцент) |
| `--review` | `#A15C07` | Review |
| `--ok` | `#1E7A4F` | OK |

| Роль | Шрифт | Где |
|------|-------|-----|
| Интерфейс | IBM Plex Sans | Кнопки, карточки, заголовки |
| Документ | IBM Plex Serif | Текст договора, цитаты, формулировки |
| Служебный | IBM Plex Mono | Номера пунктов «§ 4», ID правил, метки ПДн `[EMAIL_1]` |

Правила: цвет риска только для риска (полоса слева у карточки и пункта); акцент — только для действий и бренда; тёмная тема поддерживается.

## 3. Макеты экранов
| # | Экран | Что на нём | В v0.1 |
|---|-------|-----------|--------|
| 1 | Загрузка | Зона drag-and-drop, вставка текста, «Try the sample NDA» | ✅ |
| 2 | Проверка | Сводка (N Red flag / Review / OK, что замаскировано), лист договора с подсветкой, карточки находок с правкой и Accept / Reject | ✅ |
| 3 | Сравнение версий | Две версии, блок «Effect on the playbook» (New risk / Improved), пословный diff | ✅ |
| 4 | Плейбук | Таблица правил: стандарт, красный флаг, резервная формулировка | ✅ (только просмотр) |
| 5 | Надстройка Word (идея) | Боковая панель в Word с теми же карточками | ⬜ после пилота |

## 4. Логотип
Сгенерирован для курсового задания «промо-изображение решения». Файлы лежат в [`docs/brand/`](brand/).

| Файл | Вариант | Где использовать |
|------|---------|------------------|
| [`klauzula-logo-full.webp`](brand/klauzula-logo-full.webp) | Полный: символ и надпись «Klauzula AI» | Шапка сайта, слайды, постер |
| [`klauzula-symbol.png`](brand/klauzula-symbol.png) | Только символ (244×292 px) | Favicon, аватар, иконка приложения |

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
- Вариант для тёмной темы (фон `#11151F`).
- Выбор финальной версии голосованием группы.
