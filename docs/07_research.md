---
title: Research — проблема, пользователи, конкуренты (Project Step 2)
version: 0.3.0
status: draft
owner: TBD
updated: 2026-11-24
---

# Research: AI_lawyer — инструмент, ускоряющий работу юриста с договорами

**Трек:** Startup  **Целевая страна:** Польша (контекст — рынок ЕС)  **Дата исследования:** 23–24.11.2026
**Метод:** поиск через AI-инструмент, подключённый к поисковой системе; каждая цифра ниже помечена по степени надёжности источника (см. раздел 5).

> **Что изменилось в версии 0.2.0.** Команда приняла три вводные ([ADR-0002](decisions/0002-positioning-poland-in-house.md)):
> 1. продукт — **инструмент, ускоряющий работу юриста**, а не замена юриста для неюристов;
> 2. целевая страна — **Польша**;
> 3. целевой клиент — **компании, которым нужно оптимизировать работу юриста** (штатного или внешнего на постоянном обслуживании).
>
> Поэтому сегмент «МСБ без юриста», рекомендованный в версии 0.1.0, больше не целевой. Анализ проблемы, конкурентов, рисков и выводы пересмотрены под новые вводные; добавлены польские конкуренты для юристов (Wolters Kluwer, C.H.Beck).

---

## 1. Проблема

Юрист компании тратит значительную часть времени на однотипную проверку входящих договоров (NDA, поставки, услуги B2B). Бизнес ждёт согласования, юрист становится «узким горлом», а договоры с плохими условиями всё равно проходят.

- В среднем компании теряют **около 8,6–9% годовой выручки** из-за слабого управления договорами; лучшие — около 3%, худшие — 15% и больше (World Commerce & Contracting, 2025, по вторичным публикациям). ⚠️ Средняя надёжность: цифру публикуют вендоры CLM-систем.
- Юристы уже массово пробуют AI: **более 92%** опрошенных юристов используют хотя бы один AI-инструмент в ежедневной работе (опрос Wolters Kluwer: 810 юристов фирм и юротделов в США, Китае и 9 странах Европы). ⚠️ Опрос вендора, отдельных данных по Польше нет.
- Руководители юридических функций крупных компаний подчёркивают, что внедрять AI в юротделах нужно очень осторожно из-за чувствительности данных (EY Law General Counsel Study 2025, 1 000 руководителей юрфункций компаний с выручкой > $1 млрд). → Требование к продукту: конфиденциальность и контроль данных.
- **Размер пула юристов в Польше:** около **42,7 тыс. практикующих radców prawnych** (из 55,8 тыс. внесённых в списки) и **22,9 тыс. практикующих адвокатов** — по ответу на депутатский запрос, данные на июнь 2025. Radca prawny — основная профессия юристов, работающих в штате компаний (по трудовому договору). ⚠️ Сколько из них работает in-house, найти не удалось.

**Вывод:** боль «юрист не успевает, договоры проверяются медленно или поверхностно» реальна, и юристы готовы пользоваться AI. Но польских данных о времени юриста на один договор и о доле in-house юристов нет — этот пробел надо закрыть интервью.

## 2. Целевой клиент: сегменты

### 2.1 Кто покупает и кто пользуется

| Роль | Кто это | Что важно |
|---|---|---|
| **Пользователь** | In-house юрист (radca prawny / prawnik) | Быстрее проверить договор, не потерять качество, работать в Word |
| **Покупатель** | Head of Legal / General Counsel, в небольших компаниях — CFO или CEO | Снижение нагрузки на юриста без найма, измеримая экономия времени |
| **Выгодоприобретатель** | Продажи, закупки | Договор согласуется быстрее |
| **Контролёр** | IT / безопасность / DPO | Где хранятся данные, обучается ли модель на договорах |

### 2.2 Сравнение сегментов компаний

| Критерий | **Средние компании с 1–5 юристами** (основной) | Крупные компании с юротделом | Компании с внешним юристом на абонементе | МСБ без юриста (было в v0.1.0) |
|---|---|---|---|---|
| Боль | Юрист перегружен однотипными договорами, нанять ещё одного дорого | Большой поток договоров, нужны стандарты и контроль | Каждая проверка — оплачиваемые часы | Не понимают риски |
| Кто уже обслуживает | LEX / Libra, Beck-Noxtua, VAI Legal, ChatGPT/Claude | Luminance, LEGALFLY, Legartis, Legora, Libra | Сам внешний юрист со своими инструментами | ChatGPT/Claude, шаблоны |
| Готовность платить | Средняя: есть бюджет на правовые базы (LEX/Legalis) | Высокая, но долгие продажи и тендеры | Низкая: экономию получает юрфирма | Низкая |
| Риск «юридической консультации» | Низкий: решение принимает юрист | Низкий | Низкий | Высокий |
| Доступ для студенческой команды | Средний: сеть Kozminski, LinkedIn | Сложный | Средний | Лёгкий |
| Соответствие вводным | ✅ Полное | ✅, но рынок занят | Частичное | ❌ Не соответствует |

**Рекомендация:** основной сегмент — **польские средние компании с небольшой юридической функцией (1–5 юристов)**, у которых высокий поток **одного типа договоров** (например, NDA или договоры услуг/поставки B2B). Крупные юротделы — следующий этап, когда будет доказана экономия времени. Юрфирмы в текущие вводные не входят.

## 3. Конкуренты и отзывы клиентов

### 3.1 Польский рынок — прямые конкуренты

| Компания / продукт | Кто стоит | Для кого | Что делает | Надёжность данных |
|---|---|---|---|---|
| **LEX Expert AI + Libra** | Wolters Kluwer Polska | Юрфирмы и юротделы | AI-чат по польскому праву внутри базы LEX; Libra — рабочее пространство юриста (research, drafting, review), свои AI-ассистенты команды, надстройки для Word и Outlook. С мая 2026 — расширенный анализ договоров. Бесплатный пробный доступ. В августе 2026 Libra выбрала CRIDO | Низкая–средняя: пресс-релизы вендора |
| **Beck-Noxtua** | Noxtua + Wydawnictwo C.H.Beck (Legalis) | Юристы | AI-рабочее пространство с ответами со ссылками на контент Legalis; запуск в Польше заявлен на весну 2026 | Низкая: факт запуска не подтверждён |
| **VAI Legal** | Стартап | Юристы, компании | Анализ договоров по польскому праву, оценка рисков, правки в Word | Низкая: сайт компании |
| **Gaius-Lex** | Стартап | Юристы | «Суверенный» AI для польского и европейского права, данные в ЕЭЗ | Низкая: сайт компании |
| **LexTool** | Стартап | Юристы | Помощник по документам, от 249 zł нетто в месяц | Низкая: сайт компании |

**Ключевой вывод по Польше:** главные конкуренты — **издатели правовых баз (Wolters Kluwer, C.H.Beck)**. Юротделы уже платят им за LEX или Legalis, поэтому AI-функции продаются как дополнение к знакомому продукту, с готовыми продажами и доверием. Новому продукту придётся объяснять, почему его стоит купить в дополнение к ним.

### 3.2 Европейские игроки (для юротделов)

| Компания | Страна | Для кого | Что делает | Масштаб |
|---|---|---|---|---|
| **Legora** | Швеция | Юрфирмы, крупные юротделы | Универсальная AI-платформа для юристов | Series E €489 млн, оценка ~€7,8 млрд (окт. 2026) |
| **Luminance** | Великобритания | Крупные компании | Проверка и автоматические переговоры по договорам | Series C $75 млн, клиенты в 70+ странах |
| **LEGALFLY** | Бельгия | Юротделы компаний | Проверка договоров по правилам компании | ~€17 млн (seed + Series A €15 млн) |
| **Legartis** | Швейцария | Юротделы, закупки | Проверка входящих договоров по плейбуку компании, 150+ типов пунктов | Данные о финансировании не найдены |
| **Juro** | Великобритания | Растущие компании | Управление договорами (CLM) с AI | — |

**Универсальные AI-ассистенты.** В феврале 2026 Anthropic выпустила open-source плагин для проверки договоров в Claude, в мае 2026 — **Claude for Legal** с 12 плагинами. Плагин проверяет договор по плейбуку команды и даёт ссылку на пункт, риск и вариант правки. Для юриста это сильная альтернатива: он сам может проверить результат. Ограничения для компаний: политика безопасности данных и отсутствие польской правовой базы «из коробки».

### 3.3 Что говорят клиенты

| Продукт | Рейтинги | Что хвалят | На что жалуются |
|---|---|---|---|
| **Juro** | G2 4,5 (~180–240 отзывов); Capterra — 48 отзывов | Простота, поддержка, надстройка для Word | Слабые правки и переговоры, перенос форматирования из Word, отчёты; AI-функции «средние» (7,7–7,8 из 10 на G2) — подробнее ниже |
| **Luminance** | Gartner 4,6 (31 отзыв) | Автоматизация проверки, поддержка | Очень дорого, только для крупных компаний, долгое внедрение, нужно обучение |
| **Genie AI** | G2 4,4–4,6; Capterra 4,5 | Простота, скорость первого черновика | Хуже со сложными договорами; форматирование |
| **LEGALFLY** | Независимых отзывов нет | Отзыв клиента (ECS): проверка транспортных договоров по своим условиям | «−60% времени» — заявление компании |
| **Legartis** | Независимых отзывов нет | — | «До 85% быстрее» — маркетинг |
| **Libra, LEX Expert AI, Beck-Noxtua** | Независимых отзывов не найдено | — | — |

**Juro: каких функций не хватает (по отзывам)**

| Чего не хватает | Что пишут пользователи | Где |
|---|---|---|
| **Правки и переговоры (redlining)** | Правку контрагента можно только принять или отклонить целиком, нельзя внести правку поверх правки; в нескольких раундах переговоров неясно, кто что изменил. Самая частая жалоба в теме «Missing Features» (~8–10 отзывов) | [G2, стр. 2](https://g2.com/products/juro/reviews?page=2), [G2, стр. 3](https://g2.com/products/juro/reviews?page=3), [Oneflow (конкурент)](https://oneflow.com/uk/blog/juro-reviews/) |
| **Форматирование из Word** | Форматирование не всегда корректно переносится из Word; ограничена настройка таблиц, сложной вёрстки и условного форматирования | [G2](https://www.g2.com/products/juro/reviews), [Capterra](https://www.capterra.com/p/167130/Juro/) |
| **Отчёты и аналитика** | Отчёты ограничены; чтобы выгрузить детальные метрики (длительность согласования, риски по пунктам), нужна ручная работа или API | [Capterra](https://www.capterra.com/p/167130/Juro/), [GetApp](https://www.getapp.com/operations-management-software/a/juro/reviews/), [ContractSafe (конкурент)](https://www.contractsafe.com/contractsafe-vs-juro-comparison) |
| **Настройка** | Сложно менять договор после отправки контрагенту; неудобно переиспользовать шаблоны в разных рабочих пространствах; тема «Limited Customization» (~5 отзывов) | [G2](https://www.g2.com/products/juro/reviews), [Capterra](https://www.capterra.com/p/167130/Juro/) |
| **Интеграции** | Нет интеграции с Microsoft Teams; часть интеграций — только через Zapier | [G2](https://www.g2.com/products/juro/reviews), [PandaDoc (конкурент)](https://pandadoc.com/blog/juro-review) |

⚠️ Средняя надёжность: G2 закрыт для автоматической загрузки, поэтому данные взяты из фрагментов страниц отзывов в поиске; число отзывов по темам отличается между страницами. Обзоры Oneflow, ContractSafe и PandaDoc написаны конкурентами Juro.

**Что это значит для AI_lawyer:** юристам важны удобные правки в переговорах и работа прямо в Word без потери форматирования — это подтверждает выбор «работа в Word, правки в режиме исправлений». Отчёт о времени согласования — возможная функция для покупателя (руководителя юрфункции).

**Что видно по отзывам:** юротделы ценят простоту, скорость и настройку под свои правила; жалуются на цену и долгое внедрение enterprise-решений. Для средних компаний это окно: быстрое внедрение и понятная цена.

### 3.4 Польша: что говорят юристы

**Отзывы о польских продуктах.** Независимых отзывов клиентов о польских AI-инструментах для юристов найти не удалось:

| Продукт | Что нашлось | Источник |
|---|---|---|
| **LEX Expert AI** | Только материалы вендора: продукт тестировали юристы и radcowie prawni до запуска; интервью с проф. Марцином Дзюрдой (radca prawny), которого инструмент, по его словам, положительно удивил | [Wolters Kluwer](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/dlaczego-lex-expert-ai) |
| **Libra** | Крупнейший названный клиент — CRIDO (~200 юристов и консультантов, консалтинговая компания, не юротдел); отзывов юротделов нет | [Wolters Kluwer](https://www.wolterskluwer.com/pl-pl/news/crido-wybiera-libre-od-wolters-kluwer-jako-nowe-srodowisko-pracy-ai), [prawo.pl](https://www.prawo.pl/prawnicy-sady/libra-nowy-ai-ulatwiajacy-prace-prawnikow,1537789.html) |
| **Gaius-Lex** | Карточки на G2, Capterra, GetApp есть, отзывов нет (на GetApp — 0) | [GetApp](https://www.getapp.com/all-software/a/gaius-lex/), [G2](https://www.g2.com/products/gaius-lex/reviews) |
| **VAI Legal, LexTool, Beck-Noxtua** | Отзывов не найдено | — |

**Что польские юристы говорят в опросах**

| Исследование | Кто опрошен | Ключевые данные |
|---|---|---|
| **Raport Rynku Prawniczego 2025/2026** (Supesu Recruitment, янв.–март 2026) | 507 юристов юрфирм и **юротделов** | ~88% используют AI-инструменты; самые популярные — **общие**: ChatGPT (~63%), Copilot (56%), DeepL (51%); почти каждый второй говорит о выгорании |
| **Опрос Fundacji SET и Logit** | Адвокаты и radcowie prawni | 52,5% уже используют AI (22,5% — интенсивно), ещё 32,5% планируют. Опасения: **безопасность и конфиденциальность данных — 81%**, **ошибки AI — 75,9%**, профессиональная ответственность — 44,3%. **36,3% не знают ни одного** специализированного AI-инструмента для юристов на польском рынке («shadow AI») |
| **In-House Lawyer Innovation Forum 2025** (Варшава, 30.09.2025, организатор — Wolters Kluwer) | ~120–130 руководителей юротделов | Панель «AI в юротделе»: вопрос уже не «нужно ли», а «как». Главные темы: безопасность данных и где стоят серверы, бесконтрольное использование AI сотрудниками компании |

⚠️ Надёжность: Supesu и SET/Logit — средняя (независимые организации, но методику полностью не проверяли; данные по юротделам отдельно не выделены). Форум и материалы о продуктах — низкая–средняя: источник — Wolters Kluwer, продавец конкурирующих решений.

**Что это значит для AI_lawyer:**
1. **Юристы в Польше уже пользуются AI, но в основном общими инструментами** (ChatGPT, Copilot) — это и главный конкурент, и признак спроса.
2. **Главное возражение — данные, а не качество текста:** 81% опасаются за конфиденциальность. Хранение в ЕС, отказ от обучения на договорах и понятная политика данных — обязательное условие продажи.
3. **Рынок специализированных инструментов слабо известен** (36% не знают ни одного) — есть место для нового игрока, но придётся вкладываться в узнаваемость.
4. **Публичных отзывов польских юротделов нет** — их нужно получить самим через 5–10 интервью; данные опросов дают гипотезы для вопросов.


## 4. Самые сильные аргументы против идеи

1. **Функция становится стандартной.** Claude for Legal, ChatGPT, Libra уже проверяют договоры. Если продукт — «LLM + промт», его легко повторить.
2. **Сильные местные игроки с готовыми клиентами.** Wolters Kluwer и C.H.Beck продают AI тем же юротделам, которые уже платят им за правовые базы. Глобально рынок занят хорошо финансируемыми компаниями, и даже они проигрывают: британский **Robin AI** в 2025 не смог привлечь раунд, сократил персонал и был продан по частям.
3. **Юрист — требовательный пользователь.** Если инструмент ошибается или даёт «воду», юрист быстро перестаёт им пользоваться: проверить самому быстрее, чем перепроверять AI. Известно более 1 300 судебных дел с выдуманными AI ссылками (апрель 2026) — юристы знают этот риск и относятся к AI скептически.
4. **Конфиденциальность и долгие продажи в компании.** Договоры — чувствительные данные; нужны проверка IT/безопасности, DPO, договор поручения обработки данных (GDPR), иногда юридическая тайна. Это удлиняет продажу даже для средних компаний.
5. **Нужны знания польского права.** Качественная проверка требует польской правовой базы и практики; у издателей она есть, у стартапа — нет.
6. **Экономию времени надо доказать цифрами.** Покупатель (GC, CFO) платит за сэкономленные часы юриста; без измеримого результата продукт — «ещё одна подписка».

**Что ослабло по сравнению с v0.1.0:** риск запрещённой юридической консультации стал ниже — решение принимает юрист. В Польше закрепленными за адвокатами и radcami prawnymi являются в основном представительство в суде и органах; общая правовая помощь вне этих рамок прямо не запрещена другим лицам (по юридическим публикациям). ⚠️ Нужно проверить по тексту законов.

**Что можно противопоставить:**
- **Плейбук компании**, а не общий AI: проверка по правилам и позициям конкретного юротдела, одобренным его юристом.
- **Работа в Word** и экспорт правок в режиме исправлений — без новой системы.
- **Один тип договоров с высоким потоком** и измеримая метрика: минут на договор до и после.
- **Каждое замечание со ссылкой на текст договора** — юрист проверяет быстро.
- **Хранение данных в ЕС**, без обучения модели на договорах клиента.

## 5. Проверка источников

| Утверждение | Источник | Надёжность |
|---|---|---|
| Раунд Legora €489 млн | EU-Startups, Startup in Europe | Высокая (несколько СМИ) |
| Распад Robin AI | Legal Cheek, Sifted, Artificial Lawyer, Law360 | Высокая |
| Claude for Legal, май 2026 | ABA Journal, TechCrunch, LawNext | Высокая |
| Дела с «галлюцинациями» AI | База D. Charlotin, Stanford CIS, NPR | Высокая (по словам автора — занижено) |
| Число radców prawnych и адвокатов (июнь 2025) | Ответ на депутатский запрос (api.sejm.gov.pl) | Высокая (официальный документ), но доля in-house неизвестна |
| Осторожность GC при внедрении AI | EY Law General Counsel Study 2025 | Средняя: консалтинговая компания, крупные компании, не только Польша |
| 92% юристов используют AI | Wolters Kluwer через prawo.pl | Низкая–средняя: опрос вендора, Польша отдельно не выделена |
| Libra: анализ договоров, Word/Outlook, CRIDO | Пресс-релизы Wolters Kluwer, prawo.pl | Низкая–средняя: сведения вендора |
| Beck-Noxtua в Польше | Пресс-релиз Noxtua | Низкая: запуск не подтверждён |
| Правовая помощь вне представительства не закреплена за профессиями | Palestra (2022), e-prawnik.pl | Средняя/низкая: **проверить по законам** |
| Потери 8,6–9% выручки | WorldCC через вторичные публикации | Средняя: оригинал не открывался |
| Рейтинги G2/Capterra/Gartner | Страницы платформ | Средняя: числа отличаются между страницами |
| Опросы польских юристов (Supesu 2026, SET/Logit) | rp.pl, cyberdefence24.pl | Средняя: данные по юротделам отдельно не выделены |
| Отзывы о польских продуктах, форум in-house | Wolters Kluwer, prawo.pl, GetApp | Низкая–средняя: в основном материалы вендора; независимых отзывов нет |
| Недостающие функции Juro | Фрагменты отзывов G2, Capterra, GetApp; обзоры конкурентов | Средняя: G2 не открывается напрямую; часть обзоров — от конкурентов |
| Ускорение 60% (LEGALFLY), 85% (Legartis) | Сайты компаний | Низкая: маркетинг |
| Сведения о VAI Legal, Gaius-Lex, LexTool | Сайты компаний | Низкая: независимых обзоров нет |
| Статус EU AI Act для проверки договоров | Обзоры юрфирм | Не подтверждено: проверка договоров не упоминается в Annex III в найденных источниках |
| Данные о МСБ без юриста (YouGov/LawBite, Smallpdf) | — | Убраны из v0.2.0: сегмент больше не целевой |

## 6. Выводы

1. **Проблема перегрузки юриста подтверждается**, а юристы уже готовы пользоваться AI. Ценность AI_lawyer — не «AI читает договор», а **измеримая экономия времени юриста** на конкретном типе договоров.
2. **В Польше главные конкуренты — издатели правовых баз** (Wolters Kluwer с LEX и Libra, C.H.Beck с Beck-Noxtua): у них есть польское право, клиенты и продажи. Конкурировать в лоб с ними нельзя; нужна узкая специализация.
3. **Ниша:** средние польские компании с 1–5 юристами, один тип договоров с высоким потоком, проверка по плейбуку компании, работа в Word, данные в ЕС. Enterprise-решения для них дороги и долго внедряются.
4. **Доверие юриста — главное требование:** ссылка на текст договора в каждом замечании, мало ложных срабатываний, прозрачность, где хранятся данные.
5. **Перед разработкой проверить:** (а) сколько времени юрист реально тратит на выбранный тип договоров и сколько компания готова платить при наличии LEX/Legalis; (б) требования IT/DPO к хранению договоров — через **5–10 интервью с in-house юристами и руководителями юрфункций в Польше**.

## 7. Что обновить в Project Charter

- Решение: «AI-инструмент для in-house юристов польских компаний, который ускоряет проверку <тип договоров> по плейбуку компании и предлагает правки в Word».
- Целевой клиент: средние компании в Польше с небольшой юридической функцией; пользователь — юрист, покупатель — руководитель юрфункции / CFO.
- Как поймём, что работает: время проверки одного договора снизилось на X% на тестовом наборе; доля замечаний AI, принятых юристом; готовность опрошенных компаний платить.
- Открытые вопросы: тип договоров; кто из юристов поможет составить первый плейбук; ценовая гипотеза относительно LEX/Legalis.

---

## Источники

**Польский рынок**
- [Число адвокатов и radców prawnych, июнь 2025 (ответ на депутатский запрос)](https://api.sejm.gov.pl/sejm/term10/interpellations/attachment/ATTDMXK2C/i12392-o1.pdf)
- [LEX Expert AI — запуск (PAP MediaRoom)](https://www.pap.pl/mediaroom/zaufany-czat-ai-dla-prawnikow-wolters-kluwer-polska-wprowadza-lex-expert-ai) · [LEX Expert AI для юротдела](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/zastosowania-ai-w-dziale-prawnym)
- [Libra на польском рынке (февраль 2026)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-wprowadza-na-polski-rynek-platforme-libra-w-ramach-europejskiej-ekspansji) · [Libra — анализ договоров (май 2026)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-rozwija-platforme-libra) · [CRIDO выбирает Libra](https://www.wolterskluwer.com/en/news/crido-chooses-libra-by-wolters-kluwer) · [Libra (prawo.pl)](https://www.prawo.pl/prawnicy-sady/libra-nowy-ai-ulatwiajacy-prace-prawnikow,1537789.html)
- [Beck-Noxtua for Poland (Noxtua)](https://www.noxtua.com/news/press-releases/beck-noxtua-poland)
- [VAI Legal](https://vai.legal/) · [Gaius-Lex](https://gaius-lex.pl/) · [LexTool](https://www.lextool.pl/) · [Обзор AI для юристов в Польше (Lexedit)](https://lexedit.ai/pl/blog/ai-dla-prawnikow-narzedzia-zastosowania)

**Юристы и AI**
- [Raport Rynku Prawniczego 2025/2026 — Supesu (Rzeczpospolita)](https://www.rp.pl/zawody-prawnicze/art44314141-raport-prawnicy-miedzy-algorytmami-a-wypaleniem)
- [AI в юридическом секторе — опрос Fundacji SET и Logit (CyberDefence24)](https://cyberdefence24.pl/polityka-i-prawo/sztuczna-inteligencja-w-sektorze-prawniczym-miedzy-innowacja-a-ryzykiem-systemowym)
- [In-House Lawyer Innovation Forum 2025 (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/news/in-house-lawyer-innovation-forum-2025) · [prawo.pl](https://www.prawo.pl/biznes/in-house-lawyer-innovation-forum-2025,535159.html)
- [LEX Expert AI — почему (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/dlaczego-lex-expert-ai) · [CRIDO выбирает Libra (PL)](https://www.wolterskluwer.com/pl-pl/news/crido-wybiera-libre-od-wolters-kluwer-jako-nowe-srodowisko-pracy-ai) · [Gaius-Lex — GetApp](https://www.getapp.com/all-software/a/gaius-lex/) · [Gaius-Lex — G2](https://www.g2.com/products/gaius-lex/reviews)
- [EY Law General Counsel Study 2025 (PL)](https://www.ey.com/pl_pl/newsroom/2025/04/ey-law-general-counsel-study-pl)
- [Юристы ежедневно пользуются AI (prawo.pl)](https://www.prawo.pl/biznes/prawnicy-na-co-dzien-korzystaja-z-ai-a-ai-zmienia-model-ich-zawodu,1540345.html)
- [Future Ready Lawyer 2026 (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-publikuje-raport-z-badania-future-ready-lawyer-2026)

**Конкуренты в Европе**
- [Legora — €489 млн (EU-Startups)](https://www.eu-startups.com/2026/10/theres-no-stopping-legora-e489-million-for-stockholms-legaltech-unicorn/) · [Startup in Europe](https://startup-in-europe.com/legora-raises-approximately-e505-million-to-accelerate-its-expansion/)
- [Legal AI startups by fundraising (New Market Pitch)](https://newmarketpitch.com/blogs/news/legal-ai-top-startups-fundraising)
- [LEGALFLY Series A (Law.com)](https://law.com/legaltechnews/2024/07/16/belgian-ai-startup-legalfly-secures-16-3-million-in-series-a-keeps-the-legal-tech-funding-streak-hot) · [seed (Tech.eu)](https://tech.eu/2023/11/28/ai-co-pilot-legalfly-secures-over-2m-in-seed-funding/) · [ITdaily](https://itdaily.com/blogs/software/legalfly-legal-ai-organisation/) · [Legal 500](https://www.legal500.com/suppliers/legalfly/)
- [Legartis — AI contract review](https://legartis.ai/ai-contract-review) · [CB Insights](https://www.cbinsights.com/company/legartis/customers)
- [Robin AI — Legal Technology](https://legaltechnology.com/robin-ai-listed-for-distressed-sale-nine-months-after-making-the-sunday-times-100-tech-list/) · [Sifted](https://sifted.eu/articles/robin-ai-cuts-a-third-of-staff) · [Artificial Lawyer](https://www.artificiallawyer.com/2025/10/27/robin-ai-lays-off-staff-as-growth-disappoints/)
- [Claude for Legal (ABA Journal)](https://www.abajournal.com/news/article/anthropic-launches-claude-for-legal-giving-lawyers-20-new-program-integrations-and-12-practice-area-plugins/) · [Artificial Lawyer](https://artificiallawyer.com/2026/02/02/anthropic-moves-into-legal-tech) · [TechCrunch](https://techcrunch.com/2026/05/12/the-ai-legal-services-industry-is-heating-up-anthropic-is-getting-in-on-the-action)

**Отзывы клиентов**
- [Genie AI — G2](https://www.g2.com/products/genieai/reviews) · [Capterra](https://www.capterra.com/p/10003121/Genie-AI/reviews/)
- [Juro — G2](https://www.g2.com/products/juro/reviews) · [Capterra](https://www.capterra.com/p/167130/Juro/) · [GetApp](https://www.getapp.com/operations-management-software/a/juro/reviews/) · [Oneflow о Juro (конкурент)](https://oneflow.com/uk/blog/juro-reviews/) · [ContractSafe vs Juro (конкурент)](https://www.contractsafe.com/contractsafe-vs-juro-comparison) · [PandaDoc о Juro (конкурент)](https://pandadoc.com/blog/juro-review)
- [Luminance — Gartner](https://www.gartner.com/reviews/vendor/luminance) · [ToolRadar](https://toolradar.com/tools/luminance) · [Spellbook о ценах Luminance (конкурент)](https://spellbook.com/learn/luminance-pricing)

**Проблема**
- [WorldCC — Contract Management 2025](https://info.worldcc.com/contract-management-aug-2025)
- [Legal Dive — contract value erosion](https://legaldive.com/news/contract-value-erosion-CLM-software-contracts-contracting/688790)

**Риски и регулирование**
- [AI-галлюцинации в судах (UNC Law Library)](https://library.law.unc.edu/2026/06/handling-hallucinations-a-reflection/) · [Stanford CIS](https://cyberlaw.stanford.edu/blog/2025/10/whos-submitting-ai-tainted-filings-in-court/)
- [Правовая помощь вне закреплённых профессий (Palestra)](https://ojs.academicon.pl/palestra/article/download/8212/8452/22856) · [Uprawnienia do świadczenia pomocy prawnej (e-prawnik.pl)](https://e-prawnik.pl/porady-prawne/uprawnienia-do-swiadczenia-pomocy-prawnej.html)
- [BGH Smartlaw (LTO)](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech) — контекст ЕС
- [EU AI Act Omnibus (Hogan Lovells)](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules) · [Orrick](https://www.orrick.com/ja-JP/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)
