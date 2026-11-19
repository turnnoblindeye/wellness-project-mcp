# Wellness Project MCP — Tool Catalog

The Wellness Project MCP server exposes **85 tools** to AI clients (Claude, ChatGPT). Read tools return your logged and synced health data; write tools log new entries. Every tool operates only on the authenticated user's own account.

_Generated from source. Do not edit by hand — run `node scripts/gen-mcp-catalog.mjs`._

## Workouts & exercises

| Tool | Type | Description |
|---|---|---|
| `list_exercises` | read | Returns every canonical exercise in the library as "Name [id]", grouped by primary muscle. lookup: before logging, adding or renaming exercises when canonical names are not already known. Metadata/set-value edits: no catalog lookup. Canonical names and ids ensure proper exercise tracking and NSI score calculation. |
| `log_workout` | write | UNIT INPUTS: |
| `list_workouts` | read | List workout sessions in a date range plus user-marked Rest Day, Sick Day, or Travel Day context. Day context is returned even when that date has no workout. Treat context labels as explanatory context, not workouts; Travel Day can coexist with training. |
| `get_workout` | read | Retrieve full detail of a workout session: exercises, sets, reps, weights, superset groupings, heart points, notes, and NSI scoring at every grain. Use for detailed questions about a past workout, reviewing training before recommendations, confirming what was logged, or comparing a session to population strength standards. |
| `update_workout` | write | UNIT INPUTS: |
| `delete_workout` | write |  |
| `get_exercise_history` | read | Look up everything the user has done for ONE exercise: all-time PR plus recent performance, across many sessions. |

## Nutrition

| Tool | Type | Description |
|---|---|---|
| `log_meal` | write | RECIPE SAVE: |
| `list_meals` | read | List all meals logged for a date or date range, including each meal's ID, date, recorded local time (when known), type, food description, and macros. Use the IDs with list_glucose_readings.meal_id for observed before/after-meal glucose; do not assume a time for untimed rows. update_meal and delete_meal can resolve a meal on their own from date (+ optional name substring), so this is no longer required before either — use it to answer "what did I eat today/this week/yesterday?", review what has been logged, or get an id after an ambiguous update_meal/delete_meal match. |
| `update_meal` | write | Update an existing meal. Use only when the current message explicitly changes, corrects, or adds to a meal already logged. Never infer an update from earlier chat history. A plain food statement ("coffee with milk") is a new entry: use log_meal, even if that meal type already exists today. |
| `delete_meal` | write | Permanently delete a meal entry. Use when the user explicitly asks to remove or delete a logged meal. |

## Wearables & activity

| Tool | Type | Description |
|---|---|---|
| `list_wearable_data` | read | List daily wearable data (steps, daytime resting HR, sleeping resting HR (estimated), overnight minimum HR, provider RHR, HRV, Zone Minutes / AZM including the vigorous-intensity breakdown, VO2max, calories eaten / dietary energy, calories burned / active energy / total energy expenditure, maintenance calories / TDEE, stress, and physiological vital signs reported by connected sources or manual overrides) within a date range. Use when the user asks about their step count, heart rate, HRV trends, vigorous minutes, calories eaten / dietary energy, calories burned, active or total energy expenditure, maintenance calories, TDEE, cardio fitness, blood glucose, vital signs, or any wearable metrics over time. |
| `list_blood_pressure_readings` | read | Read individual timestamped systolic/diastolic blood pressure pairs imported from connected health sources, including Apple Health and Health Connect. Use when the user asks for actual BP readings, their times, sources, or changes within a day. Use list_wearable_data for daily summaries. Dates use the user's local timezone; defaults to the last seven calendar days, maximum 31 days. Returns at most 400 observations; narrow the date range if exceeded. Only recorded pairs are shown, with no interpolation. Missing measurements do not imply normal blood pressure. |
| `log_wearable` | write | Log daily wearable/manual health metrics (RHR, HRV, Zone Minutes / AZM, VO2max, calories eaten / dietary energy, stress, supplemental steps, and physiological vitals including SpO₂, respiratory rate, skin temperature, blood pressure, blood glucose, and core temperature). |

## Body metrics

| Tool | Type | Description |
|---|---|---|
| `log_body_metrics` | write | UNIT INPUTS: |
| `list_body_metrics` | read | List body composition entries within a date range. Use when the user asks about their weight history, body fat trend, or any body metrics over time. |

## Sleep

| Tool | Type | Description |
|---|---|---|
| `log_sleep` | write | Log an overnight sleep entry or a separate nap. Use for a concrete sleep event from a tracker or recall. Question/habit/hypothetical alone: no write. |
| `list_sleep` | read | List primary overnight sleep and daytime naps within a date range. Overnight entries include duration, Wellness Project sleep score, the source's own sleep score when recorded, stages, and timezone-aware bedtime/wake times. Naps are listed separately with duration and start/end times; they never increase the overnight total or score. |

## Lab results

| Tool | Type | Description |
|---|---|---|
| `log_lab_results` | write | Log one or more blood test or biomarker results. use: requested logging/import of lab values or a concrete result to record. Review/interpretation alone: no write. |
| `list_lab_results` | read | List lab/biomarker results within a date range, including each result's ID. update_lab_result and delete_lab_result can resolve a result on their own from date (+ optional marker or panel_name), so this is no longer required before either — use it to review lab history, answer questions about blood work trends or specific marker values over time, or get an id after an ambiguous update_lab_result/delete_lab_result match. Optionally filter by panel or marker name. |
| `list_lab_markers` | read | Returns LOINC-coded markers in the reference library: canonical name, LOINC code, panel, typical unit, and common aliases. Call this BEFORE log_lab_results to match user-provided marker names to canonical entries — same pattern as list_exercises for workouts. Prevents name drift and ensures trending works across lab visits. |

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
| `log_wellbeing` | write | Log subjective wellbeing ratings for a day, week, month, or custom date range. use: logging request or concrete wellbeing report to record. Question, general pattern or venting alone: no write. |
| `list_wellbeing` | read | List wellbeing log entries within a date range. update_wellbeing and delete_wellbeing can resolve an entry on their own from date, so this is no longer required before either — use it to answer questions about mood, energy, stress, soreness, or (when enabled) chronic pain trends over time, or get an id after an ambiguous update_wellbeing/delete_wellbeing match. |
| `update_wellbeing` | write | Update an existing wellbeing entry. Only updates fields that are provided — omitted fields remain unchanged. |
| `delete_wellbeing` | write | Permanently delete a wellbeing entry. |

## Supplements

| Tool | Type | Description |
|---|---|---|
| `manage_supplement` | write | Add, update, end, or delete a medication or supplement. Use when the user describes their stack, adds a new item, changes a dose or schedule, says they stopped taking something, or wants to remove an entry. |
| `log_supplement_taken` | write | Mark a medication or supplement as taken or not taken for a specific date. Only relevant when the user has daily tracking mode enabled. Use when the user says they took (or missed) a medication or supplement on a particular day. |
| `list_supplements` | read | List the user's medication/supplement stack and schedules. For questions comparing supplements with sleep, HRV or other metrics, or asking which days items were taken or missed, set include_adherence=true to read recorded daily check-ins. |

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
| `log_run` | write | UNIT INPUTS: |
| `list_runs` | read | List runs within a date range, or return full saved detail for one run when run_id is provided. Range reads stay compact and return a Runner State summary first. A run_id read returns that run's stored splits and structured segments plus the detailed metrics Elias needs for interval analysis. Individual run reads expose structured min_hr, hr_series (minute averages, at most 600 points), hr_zones and reported_avg_pace_sec_per_mi, plus recorded_detail with heart rate, laps and device metrics the run page shows. |
| `delete_run` | write | UNIT INPUTS: |

## Rest days

| Tool | Type | Description |
|---|---|---|
| `log_rest_day` | write | Mark a date with user-selected day context: Rest Day, Sick Day, or Travel Day. Use Rest Day when the user intentionally takes the day off training, Sick Day when they say they are sick/recovering, and Travel Day when they say they are traveling. This context is visible to the AI team and workout-history reads. |
| `list_rest_days` | read | List user-selected Rest Day, Sick Day, and Travel Day context within a range. Use this to understand why a date may have no workout or why recovery, sleep, or nutrition data may look unusual. Travel Day is context-only and can coexist with training. |
| `cancel_rest_day` | write | Remove a previously declared Rest Day, Sick Day, or Travel Day status. |

## Menstrual cycle

| Tool | Type | Description |
|---|---|---|
| `log_cycle` | write | Log a new period or resume one ended today. Edits: update_cycle(date) when offered; it finds the record itself, no list_cycle needed. Voice without update_cycle: log_cycle can save a known start/end or resume an ended-today period using started_on=today with no ended_on. "Ended today" alone does not supply a start date. |
| `list_cycle` | read | List the user's logged period records within a date range. update_cycle and delete_cycle can resolve a record on their own from date, so this is no longer required before either — use it when the user asks about their cycle history, or get an id after an ambiguous update_cycle/delete_cycle match. |
| `update_cycle` | write | Update an existing period record. Use to correct dates, add a missing end date, or clear an end date (resume). |
| `delete_cycle` | write | Delete a period record. Only delete if the user explicitly asks to remove a specific record. Do not delete to "fix" a record — use update_cycle instead. |

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
| `show_exercise_progression` | read | Show the user's estimated 1-rep-max progression for a lift over time as an interactive line chart, with filters for date range and muscle group, and an exercise picker. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_workout` | read | Show a single logged workout session's exercises and sets as an inline card. Defaults to the most recent workout; can target a specific date. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |

## Reference

| Tool | Type | Description |
|---|---|---|
| `list_blog_posts` | read | Search the public Crew Blog at /blog for advisor-authored daily posts. Only call when the user explicitly asks about the blog or what an advisor has written; don't volunteer posts in normal conversation. |
| `get_app_guide_section` | read | Look up customer-facing Wellness Project product knowledge. Use it for app navigation, visible features, integrations, metric meanings, logging methods, permissions/sync questions, or troubleshooting. |

## Other

| Tool | Type | Description |
|---|---|---|
| `mark_empty_day` | write | Set, change, or undo the answer to "why is this day empty?" for a date with no real meals logged. Use when the user wants to flip a fast day to forgotten (or back), or undo either one, in chat instead of the in-app prompt. |
| `get_saved_recipe` | read | Read saved recipe nutrition without logging or changing a meal. Use before answering questions about a saved recipe, checking previous meal macros, or follow-ups that challenge a recipe-based estimate. The profile only contains recipe TITLES; never conclude stored macros are unavailable from that. Supply recipe_id for an exact ID, or name for a case-insensitive partial title search. With neither, list up to 50 recent recipe names and IDs, then look up the chosen one. Multiple partial matches return candidates, not guessed nutrition. All values are the user's stored per-serving facts; absent values are unknown, not zero. |
| `list_caffeine` | read | List caffeine doses by local date with daily totals. Use for caffeine history or today's total. Supports up to 366 days per call; daily totals cover every dose in the range, while the dose list shows the 200 most recent and says how many it omitted. |
| `list_hydration` | read | Review hydration events and stored effective hydration totals. Use when the user explicitly asks about hydration history or fluid intake. Hydration tracking must already be enabled in Settings. Maximum range 31 days. Defaults to the last 7 days. |
| `list_glucose_readings` | read | Read actually measured, timestamped blood glucose readings imported from Health Connect or Ultrahuman, using the user's glucose unit setting. Use meal_id to compare a recorded meal time with observed readings in the 30 minutes before and two hours after eating (or choose context minutes); an untimed meal cannot be compared. Use workout_id for before/during/after-workout readings with its EXACT stored started_at and duration_sec. Otherwise use a bounded UTC-offset timestamp range (default last six hours, maximum 48 hours). meal_id, workout_id and a direct range are mutually exclusive. Returns at most 400 measured points: narrow the range if the limit is exceeded. Missing readings remain unknown, never zero or interpolated. Time alignment is correlation only, not evidence food or exercise caused a glucose change. Lab tests belong in separate lab records. |
| `update_lab_result` | write | Update one or more fields on an existing lab result. Use when the user wants to correct a result already logged, most often its collection date. Only send the fields that need to change; omit all others. |
| `delete_lab_result` | write | Permanently delete one or more lab results. Use when the user explicitly asks to remove or delete a logged lab result. Never guess a selector. |
| `set_supplement_nutrients` | write | Set the nutrient content of ONE configured dose of a medication or supplement, as printed on its label. Use when the user shares a Supplement Facts / Nutrition Facts panel, states specific nutrient amounts from a label, or corrects a previously stored value. |
| `list_recovery_sessions` | read | List logged recovery sessions (completions and skips) within a date range, each with its ID. list_recovery_strategies only returns the recurring strategies (the schedule), never the individual logged entries against them — this is the only way to see those. |
| `list_goals` | read | Analyze or show the user's current and past goals. Returns active/paused formal goals, completed/historical formal goals, and current standard targets. |
| `create_goal` | write | UNIT INPUTS: |
| `update_goal` | write | UNIT INPUTS: |
| `show_health_overview` | read | Show a rich overview of wearable health signals including steps, Zone Minutes, resting heart rate, HRV, VO2max, and stress, with a 7-day/30-day/90-day/1-year range toggle. Prefer this for broad wearable or overall health-trend questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_sleep_detail` | read | Show one night of sleep in detail with duration, score, stages, bedtime, wake time, awakenings, and recent-night context. Prefer this for last-night or specific-night sleep questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_body_composition` | read | Show body composition over time with an interactive metric picker for weight, body fat, lean and muscle mass, hydration, visceral fat, BMI, waist, and related scale metrics, with a 7-day/30-day/90-day/1-year range toggle. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_meal_diary` | read | Show the meals logged on a day as a rich diary with daily calories and macros versus targets. Prefer this for what-did-I-eat and daily food-log review questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `show_wellbeing` | read | Show energy, mood, stress, soreness, and optional chronic pain together with recent context and an overall wellbeing trend, with a 7-day/30-day/90-day/1-year range toggle. Prefer this for how-I-have-been-feeling and subjective recovery questions. When the user asks about this, prefer calling this tool and rendering the interactive MCP app over describing the underlying rows in text. Returns a short text summary alongside the visual view. |
| `list_personal_context` | read | List the user's active Personal Context memories: durable circumstances and preferences remembered across conversations (e.g. travels most weeks, gym has no squat rack, trains early mornings, wants blunt feedback). Use when the user asks what has been remembered about them, or before proposing a new memory to check whether an existing one already covers the subject. Read-only. |
| `add_or_update_personal_context` | write | Add a new Personal Context memory, or update an existing one by id. A memory is a durable circumstance or preference that should carry across future unrelated conversations (e.g. "travels most weeks", "gym has no squat rack", "prefers short home workouts", "wants blunt feedback"). Use list_personal_context first to check whether an existing memory already covers the subject, and pass its id with operation update rather than creating a duplicate. |
| `list_locations` | read | List the user's saved training locations (home gym, hotel, gym) with the equipment at each, heaviest dumbbell and barbell load included. Use when the user asks where or with what they can train, before editing a location, or when planning needs to know what equipment is available. Planning rule: listed equipment is known available, not proof that unlisted incidental supports are absent; respect known load ceilings and explicit user limits, and let the user's stated location/equipment override assumptions. Returns each location id for manage_location. Read-only. |
| `manage_location` | write | UNIT INPUTS: |
| `get_nutrient_summary` | read | Summarize logged micronutrient (and macro) intake for one day or a short range, with each nutrient's target and coverage. Use for "how's my vitamin D / sodium / iron this week", or a general "how are my micronutrients looking" (default: every tracked nutrient except amino acids, for today). |
| `get_nutrient_history` | read | Day-by-day history for ONE nutrient over a range, with its target, how many days met it, and how many days went over the upper limit. Use for "show my vitamin D over the last month" or "am I usually over on sodium". Only dates with logged data are returned. |
| `get_nutrient_contributors` | read | Top logged foods and supplements contributing to ONE nutrient over a day or short range, highest amount first. Use for "what gave me most of my sodium today" or "what's driving my potassium this week". |
| `set_nutrient_target` | write | Set or remove the user's OWN daily target for one vitamin, mineral or other tracked nutrient. Use ONLY when the user explicitly asks to set, change or remove their own target ("set my vitamin D target to 50 mcg"). Never call it on your own initiative, to apply a recommendation, or to act on a lab result. A user target is the user's personal preference, never a clinical prescription; do not present it as one. It replaces the reference intake for that nutrient in every nutrient view. Calories and macros are goals, not nutrient targets. |
