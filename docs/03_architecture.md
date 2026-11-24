---
title: Архитектура и процесс
version: 0.2.0
status: draft
owner: TBD
updated: 2026-11-24
---

# Архитектура и процесс

## 1. Бизнес-процесс: как сейчас (AS-IS)

```mermaid
flowchart LR
    A[Отдел продаж / закупок<br>получает NDA от контрагента] --> B[Письмо юристу<br>«посмотри, срочно»]
    B --> C[Очередь юриста<br>ожидание 1–5 дней]
    C --> D[Юрист читает весь текст<br>сверяет с практикой по памяти]
    D --> E[Правки вручную в Word<br>комментарий в письме]
    E --> F{Контрагент<br>согласен?}
    F -- нет, новая версия --> G[Юрист ищет, что поменяли<br>сравнение вручную]
    G --> D
    F -- да --> H[Подписание]
```

Узкие места: очередь к юристу, ручная сверка с правилами, ручное сравнение версий.

## 2. Бизнес-процесс: с Klauzula (TO-BE)

```mermaid
flowchart LR
    A[NDA от контрагента] --> B[Юрист загружает DOCX<br>в Klauzula]
    B --> C[Маскирование ПДн]
    C --> D[Проверка по плейбуку<br>OK / Review / Red flag]
    D --> E{Есть красные<br>флаги?}
    E -- нет --> H[Юрист подтверждает<br>→ подписание]
    E -- да --> F[Юрист правит предложенные<br>формулировки, Accept / Reject]
    F --> G[Отчёт в Word<br>→ ответ контрагенту]
    G --> I{Новая версия?}
    I -- да --> J[Сравнение версий:<br>что поменяли + новые риски]
    J --> F
    I -- нет --> H
```

Решение на каждом шаге принимает юрист (human-in-the-loop). Klauzula убирает ручную сверку и ручное сравнение.

## 3. Компоненты v0.1

| Компонент | Файл | Технология | Что делает |
|-----------|------|------------|-----------|
| Frontend | `app/static/` | HTML + CSS + JS без фреймворков | 3 экрана: Review, Compare, Playbook |
| Backend | `app/server.py` | Python 3.9+ стандартная библиотека (`http.server`) | REST API, без внешних пакетов |
| Парсер | `app/engine/parser.py` | `zipfile` + XML | DOCX/TXT → пункты |
| Маскирование | `app/engine/masking.py` | регулярные выражения | e-mail, телефон, PESEL, NIP, KRS, IBAN → метки |
| Проверка (demo) | `app/engine/rules.py` | правила на регулярных выражениях | 10 правил NDA, детерминированно |
| Проверка (AI) | `app/engine/llm.py` | Claude API (`anthropic` SDK), structured output | Тот же плейбук, инструкции из `skills/nda-review/SKILL.md` |
| Сравнение | `app/engine/compare.py` | `difflib` | Diff по пунктам + изменения рисков |
| Отчёт | `app/engine/report.py` | HTML для Word, Markdown | Экспорт с решениями юриста |
| Плейбук | `app/playbooks/nda_pl.json` | JSON | Правила компании |
| Хранилище | — | — | v0.1 ничего не хранит |

Решение о стеке: [ADR-0004](decisions/0004-prototype-stack.md).

## 4. Поток данных

```mermaid
sequenceDiagram
    participant U as Юрист (браузер)
    participant S as server.py
    participant M as masking
    participant R as rules / llm
    participant C as Claude API (опц.)
    U->>S: POST /api/review (DOCX base64 или текст)
    S->>S: parser: DOCX → текст
    S->>M: маскирование ПДн
    M-->>S: текст с метками [EMAIL_1]…
    S->>S: parser: текст → пункты
    alt Claude-режим (есть ключ)
        S->>C: пункты + плейбук + SKILL.md
        C-->>S: JSON-находки
    else Demo-режим
        S->>R: rules.check(пункты, плейбук)
    end
    S-->>U: находки + пункты (ничего не сохраняется)
    U->>S: POST /api/export (находки + решения)
    S-->>U: nda-review.doc / .md
```

## 5. API

| Метод | Путь | Вход | Выход |
|-------|------|------|-------|
| GET | `/api/status` | — | доступен ли Claude-режим, модель |
| GET | `/api/playbook` | — | плейбук JSON |
| GET | `/api/samples` | — | обезличенные образцы NDA |
| POST | `/api/review` | `text` или `file_b64` + `filename` | пункты, находки, счётчики, что замаскировано |
| POST | `/api/compare` | `old_text`, `new_text` | изменения по пунктам, изменения рисков |
| POST | `/api/export` | `review`, `decisions`, `format` (doc/md) | файл отчёта |

## Связанные решения
- [ADR-0003](decisions/0003-mvp-contract-type-nda.md) — тип договора NDA
- [ADR-0004](decisions/0004-prototype-stack.md) — стек прототипа
