# Wellness Project MCP — Tool Catalog

The Wellness Project MCP server exposes **73 tools** to AI clients (Claude, ChatGPT). Read tools return your logged and synced health data; write tools log new entries. Every tool operates only on the authenticated user's own account.

_Generated from source. Do not edit by hand — run `node scripts/gen-mcp-catalog.mjs`._

## Workouts & exercises

| Tool | Type | Description |
|---|---|---|
| `list_exercises` | read | Returns all canonical exercise names from the exercise library, grouped by muscle group. Call this before log_workout or update_workout to match user-described exercise names to canonical ones. Canonical names ensure proper exercise tracking and NSI score calculation. |
| `log_workout` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `list_workouts` | read | List workout sessions in a date range: ID, date, focus type, location, and session-level NSI with rating. Use before get_workout to find a session ID, or to answer "how many times did I train this week?", "when was my last leg day?", "did I work out yesterday?", "how is my NSI trending?". |
| `get_workout` | read | Retrieve full detail of a workout session: exercises, sets, reps, weights, superset groupings, heart points, notes, and NSI scoring at every grain. Use for detailed questions about a past workout, reviewing training before recommendations, confirming what was logged, or comparing a session to population strength standards. |
| `update_workout` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `delete_workout` | write | Permanently delete a workout session and all its exercises and sets. Use when the user wants to remove a logged workout entirely. |
| `get_exercise_history` | read | Look up everything the user has done for ONE exercise: all-time PR plus recent performance, across many sessions. |

## Nutrition

| Tool | Type | Description |
|---|---|---|
| `log_meal` | write | Log a meal to the user's food diary. Use when the user mentions eating, describes a meal, or asks to log food. |
| `list_meals` | read | List all meals logged for a date or date range, including each meal's ID, date, type, food description, and macros. update_meal and delete_meal can resolve a meal on their own from date (+ optional name substring), so this is no longer required before either — use it to answer "what did I eat today/this week/yesterday?", review what has been logged, or get an id after an ambiguous update_meal/delete_meal match. |
| `update_meal` | write | Update an existing meal. Use only when the current message explicitly changes, corrects, or adds to a meal already logged. Never infer an update from earlier chat history. A plain food statement ("coffee with milk") is a new entry: use log_meal, even if that meal type already exists today. |
| `delete_meal` | write | Permanently delete a meal entry. Use when the user explicitly asks to remove or delete a logged meal. |

## Wearables & activity

| Tool | Type | Description |
|---|---|---|
| `list_wearable_data` | read | List daily wearable data (steps, RHR, HRV, Zone Minutes / AZM including the vigorous-intensity breakdown, VO2max, calories eaten / dietary energy, calories burned / active energy / total energy expenditure, maintenance calories / TDEE, stress, and physiological vital signs reported by connected sources or manual overrides) within a date range. Use when the user asks about their step count, heart rate, HRV trends, vigorous minutes, calories eaten / dietary energy, calories burned, active or total energy expenditure, maintenance calories, TDEE, cardio fitness, blood glucose, vital signs, or any wearable metrics over time. |
| `log_wearable` | write | Log daily wearable/manual health metrics (RHR, HRV, Zone Minutes / AZM, VO2max, calories eaten / dietary energy, stress, supplemental steps, and physiological vitals including SpO₂, respiratory rate, skin temperature, blood pressure, blood glucose, and core temperature). |

## Body metrics

| Tool | Type | Description |
|---|---|---|
| `log_body_metrics` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `list_body_metrics` | read | List body composition entries within a date range. Use when the user asks about their weight history, body fat trend, or any body metrics over time. |

## Sleep

| Tool | Type | Description |
|---|---|---|
| `log_sleep` | write | Log a sleep entry. Use when the user shares sleep data — total duration, score, stage breakdown, bedtime, or wake time — from Fitbit, Oura, Whoop, Apple Health, or manual recall. |
| `list_sleep` | read | List sleep log entries within a date range. Each entry includes total duration, sleep score, stage breakdown, and the canonical bedtime and wake_time (full ISO 8601 timestamps with preserved timezone offset) for the user's primary overnight sleep session (excluding daytime naps). |

## Lab results

| Tool | Type | Description |
|---|---|---|
| `log_lab_results` | write | Log one or more blood test or biomarker results. Use when the user shares lab values — copy-pasted from a Quest/LabCorp PDF, typed from a paper report, or described from a photo of their results. |
| `list_lab_results` | read | List lab/biomarker results within a date range, including each result's ID. update_lab_result and delete_lab_result can resolve a result on their own from date (+ optional marker or panel_name), so this is no longer required before either — use it to review lab history, answer questions about blood work trends or specific marker values over time, or get an id after an ambiguous update_lab_result/delete_lab_result match. Optionally filter by panel or marker name. |
| `list_lab_markers` | read | Returns all LOINC-coded markers in the reference library: canonical name, LOINC code, panel, typical unit, and common aliases. Call this BEFORE log_lab_results to match user-provided marker names to canonical entries — same pattern as list_exercises for workouts. Prevents name drift and ensures trending works across lab visits. |

## Injuries

| Tool | Type | Description |
|---|---|---|
| `log_injury` | write | Log a new injury or aggravation. Use when the user mentions getting hurt, feeling pain, straining something, or describes an injury. Injuries are date ranges — they start on a date and are ongoing until an end_date is set. |
| `list_injuries` | read | List injuries from the injury log. update_injury and delete_injury can resolve an injury on their own from injury (+ optional date), so this is no longer required before either — use it to review the injury log, answer questions about injury history or rehab progress, or get an id after an ambiguous update_injury/delete_injury match. Defaults to active and monitoring injuries. |
| `update_injury` | write | Update an existing injury entry. Use when the user reports an injury is improving, worsening, resolved, or wants to change details. When severity changes, the new value is automatically tracked in the severity history for trend analysis. Only send fields that need to change. |
| `delete_injury` | write | Permanently delete an injury entry. Also removes all severity history for that injury. |

## Wellbeing

| Tool | Type | Description |
|---|---|---|
| `log_wellbeing` | write | Log subjective wellbeing ratings for a day, week, month, or custom date range. Use when the user describes how they feel — energy level, mood, stress, or muscle soreness. |
| `list_wellbeing` | read | List wellbeing log entries within a date range. update_wellbeing and delete_wellbeing can resolve an entry on their own from date, so this is no longer required before either — use it to answer questions about mood, energy, stress, or soreness trends over time, or get an id after an ambiguous update_wellbeing/delete_wellbeing match. |
| `update_wellbeing` | write | Update an existing wellbeing entry. Only updates fields that are provided — omitted fields remain unchanged. |
| `delete_wellbeing` | write | Permanently delete a wellbeing entry. |

## Supplements

| Tool | Type | Description |
|---|---|---|
| `manage_supplement` | write | Add, update, end, or delete a medication or supplement. Use when the user describes their stack, adds a new item, changes a dose or schedule, says they stopped taking something, or wants to remove an entry. |
| `log_supplement_taken` | write | Mark a medication or supplement as taken or not taken for a specific date. Only relevant when the user has daily tracking mode enabled. Use when the user says they took (or missed) a medication or supplement on a particular day. |
| `list_supplements` | read | List the user's medications and supplements. manage_supplement can resolve an item on its own from supplement_name, so this is no longer required before it — use it when the user asks what medications or supplements they're taking, asks to review their stack, or to get an id after an ambiguous manage_supplement match. |

## Recovery

| Tool | Type | Description |
|---|---|---|
| `manage_recovery_strategy` | write | Add, update, end, or delete a recovery/mindfulness strategy. Use when the user describes a new practice, changes a schedule, stops a practice, or removes one. Infer category from name, start_date defaults to today, infer schedule from context. ASK only if name is missing. |
| `log_recovery_session` | write | Log a completed or skipped recovery/mindfulness session. Use when the user says they did (or skipped) a breathing exercise, meditation, cold plunge, sauna, stretching, or any recovery practice. Also use for one-off standalone sessions not linked to a recurring strategy. |
| `update_recovery_session` | write | Update one or more fields on an existing recovery session log entry. Use when the user wants to correct or change something already logged (e.g. wrong duration, quality rating, category, or notes). Only send the fields that need to change; omit all others. |
| `delete_recovery_session` | write | Permanently delete a recovery session log entry. This action is irreversible. If the user's intent is ambiguous, ask which session to remove. |
| `list_recovery_strategies` | read | List the user's recovery and mindfulness strategies. Use when the user asks about their recovery practices, mindfulness routines, or you need strategy IDs before logging a session. |

## Runs

| Tool | Type | Description |
|---|---|---|
| `log_run` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `list_runs` | read | List runs within a date range. Returns a compact Runner State summary first, then individual runs. This is the preferred single read for Elias: current-week volume, four-week baseline, longest run, confirmed easy/quality mix, unclassified mileage, pace trend, heart points and available HR are computed together rather than pieced together from several calls. |
| `delete_run` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |

## Rest days

| Tool | Type | Description |
|---|---|---|
| `log_rest_day` | write | Mark a date as an intentional rest day. Use when the user says they took a rest day, are taking one today, or wants to mark a past day as rest after the fact (e.g. "this past Monday was a rest day", "today is a rest day", "I rested yesterday"). Suppresses the workout-prompt nudges for that date and lets the engine treat the day as planned, not skipped. |
| `list_rest_days` | read | List the dates a user has marked as rest days within a range. Use when the user asks about their rest pattern ("how many rest days have I taken this month?", "did I rest last week?"). |
| `cancel_rest_day` | write | Remove a previously declared rest day. Use when the user changes their mind ("scratch that, I'm going to lift today after all") or wants to undo a mistaken declaration. |

## Menstrual cycle

| Tool | Type | Description |
|---|---|---|
| `log_cycle` | write | Log a period to the user's cycle log. Handles all cases: |
| `list_cycle` | read | List the user's logged period records within a date range. update_cycle and delete_cycle can resolve a record on their own from date, so this is no longer required before either — use it when the user asks about their cycle history, or get an id after an ambiguous update_cycle/delete_cycle match. |
| `update_cycle` | write | Update an existing period record. Use to correct dates, add a missing end date, or clear an end date (resume). |
| `delete_cycle` | write | Delete a period record. Only delete if the user explicitly asks to remove a specific record. Do not delete to "fix" a record — use update_cycle instead. |

## Charts & visualizations

| Tool | Type | Description |
|---|---|---|
| `show_week_workouts` | read | Show the user their past 7 days of workouts (heart points per day, days trained) as an inline chart. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_week_fit_score` | read | Show the user their current Fit Score (the app's 0-100 composite), how it breaks down across its six components (Train, Fuel, Sleep, Recovery, Steps, Wellbeing), and the past 7 days of daily scores, as one inline card. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_week_macros` | read | Show the user their past 7 days of calories and macros (protein, carbs, fat) vs targets as an inline chart. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_week_sleep` | read | Show the user their past 7 days of sleep (hours per night and sleep score) as an inline chart. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_week_steps` | read | Show the user their past 7 days of step counts vs their daily goal as an inline chart. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_body_weight` | read | Show the user their body weight (and body-fat %) trend over time as an interactive line chart with a 30/90-day/1-year range toggle. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_recovery` | read | Show the user their resting heart rate and HRV recovery trend over time as an interactive dual-line chart with a 30/90-day/1-year range toggle. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_runs` | read | Show the user their running mileage over the last 14 days as an inline bar chart. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_exercise_progression` | read | Show the user's estimated 1-rep-max progression for a lift over time as an interactive line chart, with filters for date range and muscle group, and an exercise picker. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_workout` | read | Show a single logged workout session's exercises and sets as an inline card. Defaults to the most recent workout; can target a specific date. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |

## Reference

| Tool | Type | Description |
|---|---|---|
| `list_blog_posts` | read | Search the public Crew Blog at /blog for advisor-authored daily posts. Only call when the user explicitly asks about the blog or what an advisor has written; don't volunteer posts in normal conversation. |
| `get_app_guide_section` | read | Look up general customer help for the Wellness Project app. Use this only for broad questions about where a feature lives, how to use it, what a visible feature does, common troubleshooting steps, or pricing. |

## Other

| Tool | Type | Description |
|---|---|---|
| `mark_empty_day` | write | Set, change, or undo the answer to "why is this day empty?" for a date with no real meals logged. Use when the user wants to flip a fast day to forgotten (or back), or undo either one, in chat instead of the in-app prompt. |
| `list_hydration` | read | Review hydration events and stored effective hydration totals. Use when the user explicitly asks about hydration history or fluid intake. Hydration tracking must already be enabled in Settings. Maximum range 31 days. Defaults to the last 7 days. |
| `update_lab_result` | write | Update one or more fields on an existing lab result. Use when the user wants to correct a result already logged, most often its collection date. Only send the fields that need to change; omit all others. |
| `delete_lab_result` | write | Permanently delete one or more lab results. Use when the user explicitly asks to remove or delete a logged lab result. Never guess a selector. |
| `list_recovery_sessions` | read | List logged recovery sessions (completions and skips) within a date range, each with its ID. list_recovery_strategies only returns the recurring strategies (the schedule), never the individual logged entries against them — this is the only way to see those. |
| `list_goals` | read | Analyze or show the user's current and past goals. Returns active/paused formal goals, completed/historical formal goals, and current standard targets. |
| `create_goal` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `update_goal` | write | UNIT INPUTS: never convert units yourself. Pass the user's number for a _lb / _mi / _in field exactly as stated, and when they gave kg / km / cm set input_weight_unit / input_distance_unit / input_length_unit in that same object. Omit the companion when the number is already lb / mi / in. The tool converts once before storage, so this overrides any wording that asks you to do the arithmetic. |
| `show_health_overview` | read | Show a rich overview of wearable health signals including steps, Zone Minutes, resting heart rate, HRV, VO2max, and stress. Prefer this for broad wearable or overall health-trend questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_sleep_detail` | read | Show one night of sleep in detail with duration, score, stages, bedtime, wake time, awakenings, and recent-night context. Prefer this for last-night or specific-night sleep questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_body_composition` | read | Show body composition over time with an interactive metric picker for weight, body fat, lean and muscle mass, hydration, visceral fat, BMI, waist, and related scale metrics. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_meal_diary` | read | Show the meals logged on a day as a rich diary with daily calories and macros versus targets. Prefer this for what-did-I-eat and daily food-log review questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_wellbeing` | read | Show energy, mood, stress, and soreness together with recent context and an overall wellbeing trend. Prefer this for how-I-have-been-feeling and subjective recovery questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `list_personal_context` | read | List the user's active Personal Context memories: durable circumstances and preferences remembered across conversations (e.g. travels most weeks, gym has no squat rack, trains early mornings, wants blunt feedback). Use when the user asks what has been remembered about them, or before proposing a new memory to check whether an existing one already covers the subject. Read-only. |
| `add_or_update_personal_context` | write | Add a new Personal Context memory, or update an existing one by id. A memory is a durable circumstance or preference that should carry across future unrelated conversations (e.g. "travels most weeks", "gym has no squat rack", "prefers short home workouts", "wants blunt feedback"). Use list_personal_context first to check whether an existing memory already covers the subject, and pass its id with operation update rather than creating a duplicate. |
