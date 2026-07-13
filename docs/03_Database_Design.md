Database Design
We'll log EVERYTHING.
Tables:
Users
id

email

password

role

created_at
________________________________________
Requests
request_id

user_id

prompt

intent

priority

status

confidence

created_at
________________________________________
Workflows
workflow_id

request_id

workflow_name

execution_time

retry_count

status

started_at

completed_at
________________________________________
Logs
log_id

workflow_id

service

level

message

timestamp
________________________________________
AI Decisions
This is the secret sauce.
decision_id

request_id

predicted_intent

confidence

tool_selected

reasoning_summary

timestamp

© 2026 Brian Sing'ombe Kibagendi

Project: KaziFlow Agent

Repository: github.com/G1thub001/kaziflow-agent