# Wellness Project MCP — Tool Catalog

The Wellness Project MCP server exposes **85 tools** to AI clients (Claude, ChatGPT). Read tools return your logged and synced health data; write tools log new entries. Every tool operates only on the authenticated user's own account.

_Generated from source. Do not edit by hand — run `node scripts/gen-mcp-catalog.mjs`._

## Workouts & exercises

| Tool | Type | Description |
|---|---|---|
| `list_exercises` | read | Every canonical library exercise as "Name [id]", grouped by primary muscle. use: before logging, adding or renaming exercises when canonical names are not already known. skip: metadata or set-value edits. why: canonical names and ids drive exercise tracking and NSI scoring. |
| `log_workout` | write | UNIT INPUTS: |
| `list_workouts` | read | List workout sessions in a date range, plus user-marked Rest Day, Sick Day or Travel Day context (returned even on a date with no workout). Context labels explain a day, they are not workouts; Travel Day can coexist with training. |
| `get_workout` | read | Full detail of one workout session: exercises, sets, reps, weights, superset groupings, heart points, notes, NSI scoring at every grain. |
| `update_workout` | write | UNIT INPUTS: |
| `delete_workout` | write |  |
| `get_exercise_history` | read | Everything the user has done for ONE exercise across sessions: all-time PR plus recent performance. |

## Nutrition

| Tool | Type | Description |
|---|---|---|
| `log_meal` | write | RECIPE SAVE: |
| `list_meals` | read | List meals logged for a date or date range: ID, date, recorded local time (when known), type, food description, macros. |
| `update_meal` | write | Update an existing meal. Use only when the current message explicitly changes, corrects, or adds to a meal already logged. Never infer an update from earlier chat history. A plain food statement ("coffee with milk") is a new entry: use log_meal, even if that meal type already exists today. |
| `delete_meal` | write | Permanently delete a meal entry. use: the user explicitly asks to remove or delete a logged meal. |

## Wearables & activity

| Tool | Type | Description |
|---|---|---|
| `list_wearable_data` | read | List daily wearable data in a date range: steps, daytime resting HR, sleeping resting HR (estimated), overnight minimum HR, provider RHR, HRV, Zone Minutes / AZM with the vigorous-intensity breakdown, VO2max, calories eaten / dietary energy, calories burned / active energy / total energy expenditure, maintenance calories / TDEE, stress, and physiological vital signs from connected sources or manual overrides. use: step count, heart rate, HRV trends, vigorous minutes, calories eaten or burned, active or total energy expenditure, maintenance calories, TDEE, cardio fitness, blood glucose, vital signs, or any wearable metric over time. |
| `list_blood_pressure_readings` | read | Read individual timestamped systolic/diastolic blood pressure pairs imported from connected health sources, including Apple Health and Health Connect. use: actual BP readings, their times, sources, or changes within a day. Daily summaries: list_wearable_data. Dates are in the user's local timezone; default last seven calendar days, max 31 days. At most 400 observations; narrow the date range if exceeded. Only recorded pairs are shown, no interpolation. Missing measurements do not imply normal blood pressure. |
| `log_wearable` | write | Log daily wearable/manual health metrics: RHR, HRV, Zone Minutes / AZM, VO2max, calories eaten / dietary energy, stress, supplemental steps, and physiological vitals (SpO₂, respiratory rate, skin temperature, blood pressure, blood glucose, core temperature). |

## Body metrics

| Tool | Type | Description |
|---|---|---|
| `log_body_metrics` | write | UNIT INPUTS: |
| `list_body_metrics` | read | List body composition entries in a date range. use: weight history, body fat trend, or any body metric over time. |

## Sleep

| Tool | Type | Description |
|---|---|---|
| `log_sleep` | write | Log an overnight sleep entry or a separate nap. use: a concrete sleep event from a tracker or recall. Question/habit/hypothetical alone: no write. |
| `list_sleep` | read | List primary overnight sleep and daytime naps in a date range. Overnight: duration, Wellness Project sleep score, the source's own sleep score when recorded, stages, and timezone-aware bedtime/wake times. Naps: listed separately with duration and start/end times; they never increase the overnight total or score. |

## Lab results

| Tool | Type | Description |
|---|---|---|
| `log_lab_results` | write | Log one or more blood test or biomarker results. use: requested logging/import of lab values or a concrete result to record. Review/interpretation alone: no write. |
| `list_lab_results` | read | List lab/biomarker results in a date range, each with its ID; optional panel or marker name filter. use: reviewing lab history, blood work trends or specific marker values over time, or getting an id after an ambiguous update_lab_result/delete_lab_result match. Not required before update_lab_result or delete_lab_result: they resolve a result themselves from date (+ optional marker or panel_name). |
| `list_lab_markers` | read | LOINC-coded markers in the reference library: canonical name, LOINC code, panel, typical unit, common aliases. Call BEFORE log_lab_results to match user-provided marker names to canonical entries; this prevents name drift and keeps trending working across lab visits. |

## Injuries

| Tool | Type | Description |
|---|---|---|
| `log_injury` | write | Log a new injury or aggravation. use: the user mentions getting hurt, feeling pain, straining something, or describes an injury. Injuries are date ranges: they start on a date and are ongoing until an end_date is set. |
| `list_injuries` | read | List injuries from the injury log; defaults to Active and Monitoring. use: reviewing the log, injury history or rehab progress, or getting an id after an ambiguous update_injury/delete_injury match. Not required before update_injury or delete_injury: they resolve an injury themselves from injury (+ optional date). |
| `update_injury` | write | Update an existing injury entry. use: the user reports an injury improving, worsening or resolved, or wants details changed. Send only fields that change. |
| `delete_injury` | write | Permanently delete an injury entry and all its severity history. |

## Wellbeing

| Tool | Type | Description |
|---|---|---|
| `log_wellbeing` | write | Log subjective wellbeing ratings for a day, week, month, or custom date range. use: logging request or concrete wellbeing report to record. Question, general pattern or venting alone: no write. |
| `list_wellbeing` | read | List wellbeing entries in a date range. use: mood, energy, stress, soreness or (when enabled) chronic pain trends over time, or getting an id after an ambiguous update_wellbeing/delete_wellbeing match. Not required before update_wellbeing or delete_wellbeing: they resolve an entry themselves from date. |
| `update_wellbeing` | write | Update an existing wellbeing entry; omitted fields stay unchanged. |
| `delete_wellbeing` | write | Permanently delete a wellbeing entry. |

## Supplements

| Tool | Type | Description |
|---|---|---|
| `manage_supplement` | write | Add, update, end, or delete a medication or supplement. use: the user describes their stack, adds an item, changes a dose or schedule, says they stopped taking something, or wants an entry removed. |
| `log_supplement_taken` | write | Mark a medication or supplement as taken or not taken on a date. Only relevant when the user has daily tracking mode enabled. use: the user says they took (or missed) one on a particular day. |
| `list_supplements` | read | List the user's medication/supplement stack and schedules: each item's id, name, dose, schedule and start/end dates. include_adherence=true reads recorded daily check-ins: use it for questions comparing supplements with sleep, HRV or other metrics, or asking which days items were taken or missed. |

## Recovery

| Tool | Type | Description |
|---|---|---|
| `manage_recovery_strategy` | write | Add, update, end, or delete a recovery/mindfulness strategy. use: the user describes a new practice, changes a schedule, stops a practice, or removes one. Infer category from the name and schedule from context; start_date defaults to today. ASK only if name is missing. |
| `log_recovery_session` | write | Log a completed or skipped recovery/mindfulness session. use: the user did (or skipped) a breathing exercise, meditation, cold plunge, sauna, stretching, or any recovery practice; also one-off standalone sessions not linked to a recurring strategy. |
| `update_recovery_session` | write | Update fields on an existing recovery session log entry. use: correcting or changing something already logged (e.g. wrong duration, quality rating, category, or notes). Send only the fields that change. |
| `delete_recovery_session` | write | Permanently delete a recovery session log entry. Irreversible. Ambiguous intent -> ask which session to remove. |
| `list_recovery_strategies` | read | List the user's recovery and mindfulness strategies: id, name, category, schedule, start_date, end_date. use: questions about recovery practices or mindfulness routines, or getting strategy IDs before logging a session. |

## Runs

| Tool | Type | Description |
|---|---|---|
| `log_run` | write | UNIT INPUTS: |
| `list_runs` | read | List runs in a date range, or the full saved detail of one run when run_id is given. |
| `delete_run` | write | UNIT INPUTS: |

## Rest days

| Tool | Type | Description |
|---|---|---|
| `log_rest_day` | write | Mark a date with user-selected day context: Rest Day, Sick Day, or Travel Day. rest = the user intentionally takes the day off training; sick = they say they are sick/recovering; travel = they say they are traveling. The context is visible to the AI team and workout-history reads. |
| `list_rest_days` | read | List user-selected Rest Day, Sick Day, and Travel Day context in a range. use: understanding why a date has no workout, or why recovery, sleep or nutrition data looks unusual. Travel Day is context-only and can coexist with training. |
| `cancel_rest_day` | write | Remove a previously declared Rest Day, Sick Day, or Travel Day status. |

## Menstrual cycle

| Tool | Type | Description |
|---|---|---|
| `log_cycle` | write | Log a new period or resume one ended today. Edits: update_cycle(date) when offered; it finds the record itself, no list_cycle needed. Voice without update_cycle: log_cycle can save a known start/end or resume an ended-today period using started_on=today with no ended_on. "Ended today" alone does not supply a start date. |
| `list_cycle` | read | List the user's logged period records in a date range. use: cycle history, or getting an id after an ambiguous update_cycle/delete_cycle match. Not required before update_cycle or delete_cycle: they resolve a record themselves from date. |
| `update_cycle` | write | Update an existing period record: correct dates, add a missing end date, or clear an end date (resume). |
| `delete_cycle` | write | Delete a period record, only when the user explicitly asks to remove a specific record. Never delete to "fix" a record: use update_cycle. |

## Analysis

| Tool | Type | Description |
|---|---|---|
| `deep_analysis` | read | Deep Analysis: read-only SQLite SQL over a private copy of the user's full health history. |

## Charts & visualizations

| Tool | Type | Description |
|---|---|---|
| `show_week_workouts` | read | Visual training trend for 7d, 30d, 90d, or 1y. Includes user-marked Rest Day, Sick Day, and Travel Day context even when no workout exists. Returns an interactive chart plus short summary. |
| `show_week_fit_score` | read | Visual Fit Score trend and component breakdown for 7d, 30d, 90d, or 1y. Returns an interactive card plus short summary. |
| `show_week_macros` | read | Visual calories and macros versus targets for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_week_sleep` | read | Visual sleep duration and score trend for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_week_steps` | read | Visual step-count trend versus goal for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_body_weight` | read | Visual weight and body-fat trend for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_recovery` | read | Visual resting-heart-rate and HRV trend for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_runs` | read | Visual running-mileage trend for 7d, 30d, 90d, or 1y. Returns an interactive chart plus short summary. |
| `show_exercise_progression` | read | Show the user's estimated 1-rep-max progression for a lift over time as an interactive line chart, with filters for date range and muscle group, and an exercise picker. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `show_workout` | read | Show a single logged workout session's exercises and sets as an inline card. Defaults to the most recent workout; can target a specific date. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |

## Reference

| Tool | Type | Description |
|---|---|---|
| `list_blog_posts` | read | Search the public Crew Blog at /blog for advisor-authored daily posts. Call only when the user explicitly asks about the blog or what an advisor has written; never volunteer posts in normal conversation. |
| `get_app_guide_section` | read | Look up customer-facing Wellness Project product knowledge. Use it for app navigation, visible features, integrations, metric meanings, logging methods, permissions/sync questions, or troubleshooting. |

## Other

| Tool | Type | Description |
|---|---|---|
| `mark_empty_day` | write | Set, change, or undo the answer to "why is this day empty?" for a date with no real meals logged. use: the user wants to flip a fast day to forgotten (or back), or undo either one, in chat instead of the in-app prompt. |
| `get_saved_recipe` | read | Read saved recipe nutrition without logging or changing a meal. Use before answering questions about a saved recipe, checking previous meal macros, or follow-ups that challenge a recipe-based estimate. |
| `list_caffeine` | read | List caffeine doses by local date with daily totals. use: caffeine history or today's total. |
| `list_hydration` | read | Review hydration events and stored effective hydration totals. use: the user explicitly asks about hydration history or fluid intake. Hydration tracking must already be enabled in Settings. Max range 31 days; default last 7 days. |
| `list_glucose_readings` | read | Read actually measured, timestamped blood glucose readings imported from Health Connect or Ultrahuman, in the user's glucose unit setting. |
| `update_lab_result` | write | Update fields on an existing lab result. use: correcting a result already logged, most often its collection date. Send only the fields that change. |
| `delete_lab_result` | write | Permanently delete one or more lab results. use: the user explicitly asks to remove or delete a logged lab result. Never guess a selector. |
| `set_supplement_nutrients` | write | Set the nutrient content of ONE configured dose of a medication or supplement, as printed on its label. use: the user shares a Supplement Facts / Nutrition Facts panel, states specific nutrient amounts from a label, or corrects a previously stored value. |
| `list_recovery_sessions` | read | List logged recovery sessions (completions and skips) in a date range, each with its ID. This is the only way to see individual logged entries: list_recovery_strategies returns only the recurring strategies (the schedule). |
| `list_goals` | read | Show or analyze the user's goals: active/paused formal goals, completed/historical formal goals, current standard targets. |
| `create_goal` | write | UNIT INPUTS: |
| `update_goal` | write | UNIT INPUTS: |
| `show_health_overview` | read | Show a rich overview of wearable health signals including steps, Zone Minutes, resting heart rate, HRV, VO2max, and stress, with a 7-day/30-day/90-day/1-year range toggle. Prefer this for broad wearable or overall health-trend questions. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `show_sleep_detail` | read | Show one night of sleep in detail with duration, score, stages, bedtime, wake time, awakenings, and recent-night context. Prefer this for last-night or specific-night sleep questions. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `show_body_composition` | read | Show body composition over time with an interactive metric picker for weight, body fat, lean and muscle mass, hydration, visceral fat, BMI, waist, and related scale metrics, with a 7-day/30-day/90-day/1-year range toggle. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `show_meal_diary` | read | Show the meals logged on a day as a rich diary with daily calories and macros versus targets. Prefer this for what-did-I-eat and daily food-log review questions. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `show_wellbeing` | read | Show energy, mood, stress, soreness, and optional chronic pain together with recent context and an overall wellbeing trend, with a 7-day/30-day/90-day/1-year range toggle. Prefer this for how-I-have-been-feeling and subjective recovery questions. Prefer this interactive view over describing the underlying rows in text. Returns a short text summary alongside it. |
| `list_personal_context` | read | List the user's active Personal Context memories: durable circumstances and preferences remembered across conversations (e.g. travels most weeks, gym has no squat rack, trains early mornings, wants blunt feedback). Use when the user asks what has been remembered about them, or before proposing a new memory to check whether an existing one already covers the subject. Read-only. |
| `add_or_update_personal_context` | write | Add a new Personal Context memory, or update an existing one by id. |
| `list_locations` | read | List the user's saved training locations (home gym, hotel, gym) with the equipment at each, heaviest dumbbell and barbell load included. Use when the user asks where or with what they can train, before editing a location, or when planning needs to know what equipment is available. Planning rule: listed equipment is known available, not proof that unlisted incidental supports are absent; respect known load ceilings and explicit user limits, and let the user's stated location/equipment override assumptions. Returns each location id for manage_location. Read-only. |
| `manage_location` | write | UNIT INPUTS: |
| `get_nutrient_summary` | read | Summarize logged micronutrient (and macro) intake for one day or a short range, with each nutrient's target and coverage. use: "how's my vitamin D / sodium / iron this week", or a general "how are my micronutrients looking" (default: every tracked nutrient except amino acids, for today). |
| `get_nutrient_history` | read | Day-by-day history for ONE nutrient over a range, with its target, how many days met it, and how many days went over the upper limit. use: "show my vitamin D over the last month", "am I usually over on sodium". Only dates with logged data are returned. |
| `get_nutrient_contributors` | read | Top logged foods and supplements contributing to ONE nutrient over a day or short range, highest amount first. use: "what gave me most of my sodium today", "what's driving my potassium this week". |
| `set_nutrient_target` | write | Set or remove the user's OWN daily target for one vitamin, mineral or other tracked nutrient. |
