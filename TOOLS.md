# Wellness Project MCP — Tool Catalog

The Wellness Project MCP server exposes **60 tools** to AI clients (Claude, ChatGPT). Read tools return your logged and synced health data; write tools log new entries. Every tool operates only on the authenticated user's own account.

_Generated from source. Do not edit by hand — run `node scripts/gen-mcp-catalog.mjs`._

## Workouts & exercises

| Tool | Type | Description |
|---|---|---|
| `list_exercises` | read | Returns all canonical exercise names from the exercise library, grouped by muscle group. Call this before log_workout or update_workout to match user-described exercise names to canonical ones. Canonical names ensure proper exercise tracking and NSI score calculation. |
| `log_workout` | write | Log a complete workout session including all exercises, sets, reps, weights, and session metadata. Use when the user describes finishing a workout, lists exercises performed, or asks to log training. |
| `list_workouts` | read | List workout sessions within a date range, returning each session's ID, date, focus type, location, and session-level NSI score with rating. Use this before get_workout to find a session ID. Also useful to answer questions like "how many times did I train this week?", "when was my last leg day?", "did I work out yesterday?", or "how is my NSI trending?". |
| `get_workout` | read | Retrieve the full detail of a specific workout session: all exercises, sets, reps, weights, superset groupings, heart points, session notes, plus NSI scoring at every grain. Use to answer detailed questions about a past workout, review training before making recommendations, confirm what was logged, or analyze how a session compared to population strength standards. |
| `update_workout` | write | Update a workout session — correct session metadata, fix set values, rename exercises, add new exercises, remove exercises, or move exercises between supersets. Use for any post-log correction or modification. |
| `delete_workout` | write | Permanently delete a workout session and all its exercises and sets. Use when the user wants to remove a logged workout entirely. |
| `get_exercise_history` | read | Look up everything the user has ever done for a single exercise: their all-time PR plus recent performance. Exercise-centric — one exercise across many sessions. |

## Nutrition

| Tool | Type | Description |
|---|---|---|
| `log_meal` | write | Log a meal to the user's food diary. Use when the user mentions eating something, describes a meal, or asks to log food. |
| `list_meals` | read | List all meals logged for a date or date range, including each meal's ID, date, type, food description, and macros. Use this before update_meal or delete_meal to find the correct meal ID. Also useful to answer "what did I eat today/this week/yesterday?" or to review what has been logged. |
| `update_meal` | write | Update one or more fields on an existing meal entry. Use when the user wants to correct or change something already logged. |
| `delete_meal` | write | Permanently delete a meal entry. Use when the user explicitly asks to remove or delete a logged meal. |

## Wearables & activity

| Tool | Type | Description |
|---|---|---|
| `list_wearable_data` | read | List daily wearable data (steps, RHR, HRV, Heart Points / AZM including the vigorous-intensity breakdown, VO2max, stress) within a date range. Use when the user asks about their step count, heart rate, HRV trends, vigorous minutes, or any wearable metrics over time. |
| `log_wearable` | write | Log daily wearable metrics (RHR, HRV, Heart Points / AZM, VO2max, stress, and supplemental steps). |

## Body metrics

| Tool | Type | Description |
|---|---|---|
| `log_body_metrics` | write | Log or update body composition metrics for a given date. Use when the user shares weight, body fat percentage, or any other body composition reading — whether typed manually, copy-pasted from a smart scale app, or described from a photo of a scale display. |
| `list_body_metrics` | read | List body composition entries within a date range. Use when the user asks about their weight history, body fat trend, or any body metrics over time. |

## Sleep

| Tool | Type | Description |
|---|---|---|
| `log_sleep` | write | Log a sleep entry. Use when the user shares sleep data — total duration, score, or stage breakdown — from Fitbit, Oura, Whoop, Apple Health, or manual recall. |
| `list_sleep` | read | List sleep log entries within a date range. Use when the user asks about their sleep history, trends, or quality over time. |

## Lab results

| Tool | Type | Description |
|---|---|---|
| `log_lab_results` | write | Log one or more blood test or biomarker results. Use when the user shares lab values — whether copy-pasted from a Quest/LabCorp PDF, typed from a paper report, or described from a photo of their results. |
| `list_lab_results` | read | List lab/biomarker results within a date range. Use when the user asks about their lab history, blood work trends, or specific marker values over time. Optionally filter by panel or marker name. |
| `list_lab_markers` | read | Returns all LOINC-coded markers in the reference library: canonical name, LOINC code, panel, typical unit, and common aliases. Call this BEFORE log_lab_results to match user-provided marker names to canonical entries — same pattern as list_exercises for workouts. Prevents name drift and ensures trending works across lab visits. |

## Injuries

| Tool | Type | Description |
|---|---|---|
| `log_injury` | write | Log a new injury or aggravation. Use when the user mentions getting hurt, feeling pain, straining something, or describes an injury. Injuries are date ranges — they start on a date and are ongoing until an end_date is set. |
| `list_injuries` | read | List injuries from the injury log. Use when the user asks about their injury history, current injuries, or rehab progress. Returns entry IDs needed for update_injury and delete_injury. Defaults to active and monitoring injuries. |
| `update_injury` | write | Update an existing injury entry. Use when the user reports an injury is improving, worsening, resolved, or wants to change details. When severity changes, the new value is automatically tracked in the severity history for trend analysis. |
| `delete_injury` | write | Permanently delete an injury entry by ID. Use list_injuries first to confirm the injury ID before deleting. Also removes all severity history for that injury. |

## Wellbeing

| Tool | Type | Description |
|---|---|---|
| `log_wellbeing` | write | Log subjective wellbeing ratings for a day, week, month, or custom date range. Use when the user describes how they feel — energy level, mood, stress, or muscle soreness. |
| `list_wellbeing` | read | List wellbeing log entries within a date range. Use when the user asks about their mood, energy, stress, or soreness trends over time. Returns entry IDs needed for update_wellbeing and delete_wellbeing. |
| `update_wellbeing` | write | Update an existing wellbeing entry by ID. Use list_wellbeing first to find the entry ID. Only updates fields that are provided — omitted fields remain unchanged. |
| `delete_wellbeing` | write | Permanently delete a wellbeing entry by ID. Use list_wellbeing first to confirm the entry ID before deleting. |

## Supplements

| Tool | Type | Description |
|---|---|---|
| `manage_supplement` | write | Add, update, end, or delete a medication or supplement. Use when the user describes their stack, adds a new medication or supplement, changes a dose or schedule, says they stopped taking something, or wants to remove an entry. |
| `log_supplement_taken` | write | Mark a medication or supplement as taken or not taken for a specific date. Only relevant when the user has daily tracking mode enabled. Use when the user says they took (or missed) a medication or supplement on a particular day. |
| `list_supplements` | read | List the user's medications and supplements. Use when the user asks what medications or supplements they're taking, asks to review their stack, or you need IDs before calling manage_supplement. |

## Recovery

| Tool | Type | Description |
|---|---|---|
| `manage_recovery_strategy` | write | Add, update, end, or delete a recovery/mindfulness strategy. Use when the user describes a new practice, changes a schedule, stops a practice, or removes one. Infer category from name, start_date defaults to today, infer schedule from context. ASK only if name is missing. For update/end/delete call list_recovery_strategies first. |
| `log_recovery_session` | write | Log a completed or skipped recovery/mindfulness session. Use when the user says they did (or skipped) a breathing exercise, meditation, cold plunge, sauna, stretching, or any recovery practice. Also use for one-off standalone sessions not linked to a recurring strategy. |
| `update_recovery_session` | write | Update one or more fields on an existing recovery session log entry. Use when the user wants to correct or change something already logged (e.g. wrong duration, quality rating, or notes). |
| `delete_recovery_session` | write | Permanently delete a recovery session log entry. This action is irreversible. |
| `list_recovery_strategies` | read | List the user's recovery and mindfulness strategies. Use when the user asks about their recovery practices, mindfulness routines, or you need strategy IDs before logging a session. |

## Runs

| Tool | Type | Description |
|---|---|---|
| `log_run` | write | Log a run to the user's running tracker. Use when the user mentions going for a run, jogging, or any running activity. |
| `list_runs` | read | List runs logged within a date range, returning each run's ID, date, distance, duration, pace, and type. Use to answer questions like "how far did I run this week?", "what was my last run?", or before delete_run to find a run ID. |
| `delete_run` | write | Delete a run by ID. Use when the user wants to remove a run entry. Call list_runs first to find the correct ID. |

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
| `list_cycle` | read | List the user's logged period records within a date range. Use to look up period history before updating or deleting a record, or when the user asks about their cycle history. |
| `update_cycle` | write | Update an existing period record by ID. Use to correct dates, add a missing end date, or clear an end date (resume). Use list_cycle first to find the record ID. |
| `delete_cycle` | write | Delete a period record by ID. Use list_cycle first to confirm the record before deleting. |

## Charts & visualizations

| Tool | Type | Description |
|---|---|---|
| `show_week_workouts` | read | Show the user their past 7 days of workouts (heart points per day, days trained) as an inline chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_week_fit_score` | read | Show the user their past 7 days of daily Fit Score (the app's 0-100 composite) as an inline chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_week_macros` | read | Show the user their past 7 days of calories and macros (protein, carbs, fat) vs targets as an inline chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_week_sleep` | read | Show the user their past 7 days of sleep (hours per night and sleep score) as an inline chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_week_steps` | read | Show the user their past 7 days of step counts vs their daily goal as an inline chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_body_weight` | read | Show the user their body weight (and body-fat %) trend over time as an interactive line chart with a 30/90-day/1-year range toggle. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_recovery` | read | Show the user their resting heart rate and HRV recovery trend over time as an interactive dual-line chart with a 30/90-day/1-year range toggle. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_runs` | read | Show the user their running mileage over the last 14 days as an inline bar chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_fit_score_breakdown` | read | Show how today's Fit Score breaks down across its six components (Train, Sleep, Fuel, Recovery, Steps, Wellbeing) as an inline donut/radial chart. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_exercise_progression` | read | Show the user's estimated 1-rep-max progression for a lift over time as an interactive line chart, with filters for date range (30/90-day/1-year) and muscle group, and an exercise picker. Use when the user asks about progress on a specific lift (e.g. "how's my bench progressing"). When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |
| `show_workout` | read | Show a single logged workout session's exercises and sets as an inline card. Defaults to the most recent workout; can target a specific date. When the user asks about this, prefer calling this tool and rendering the chart over describing the numbers in text. Interactive: 7d/30d/90d/1y range toggle and hover tooltips; returns a short text summary alongside the chart. |

## Notifications

| Tool | Type | Description |
|---|---|---|
| `create_notification` | write | Send a push notification to the user (the API-key holder), and drop the same row into their in-app alerts center. Use when a long-running background task you're driving needs to ping the user when it finishes — e.g. a scheduled audit completed and there's a result to review. |

## Reference

| Tool | Type | Description |
|---|---|---|
| `list_blog_posts` | read | Search the public Crew Blog at /blog for advisor-authored daily posts. Only call when the user explicitly asks about the blog or what an advisor has written; don't volunteer posts in normal conversation. |
| `get_app_guide_section` | read | Look up how this app works (features, settings, navigation, troubleshooting). Call when the user asks where something lives, how a feature works, what a metric is computed from, or how to do something inside the product. Do NOT call for advice about the user's body or data — those route to specialists. |
