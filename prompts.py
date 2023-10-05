import openai
import json


# Prompt for the crash position, input statement and crash info in the {}
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Provide me the pre-condition that will not cause the crash for the given statement with current crash information, return directly as \"Pre-condition:...\" in programmatically way without explanation. If cannot generate a pre-condition, return FALSE: Statement: {}; Crash Info: {}"
)

# Prompt for the post-condition generation, input statement and crash info in the {}
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Provide me the pre-condition for the given statement with post-condition, return directly as \"Pre-condition:...\" in programmatically way without explanation. If cannot generate a pre-condition, return FALSE:	Statement: {};	Post-condition: {}"
)

# Prompt for the root cause judgement, input statement, actual variable values, pre-condition and post-condition in the {}
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Is the current statement the root cause for the conflict between pre/post-condition and the actual variable values, return directly as Y/N without explanation: Statement: {}; Actual Values: {}; Pre-condition: {}; Post-condition: {}"
)

# Prompt for the statement fix generation, input statement, actual variable values, pre-condition and post-condition in the {}
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Provide me the possibility percentage that current statement is the root cause for the conflict between pre/post-condition and the actual variable values with a possible fix on the given statement to make it can satisfy the pre/post-condition, return directly as \"Possibility:...; Fixing:...\" without explanation, possibility in number and fixing in the programmatically way: Statement: {}; Actual Values: {}; Pre-condition: {}; Post-condition: {}"
)

# Prompt for the statement fix generation update, input how many previous fixes you did in [] and input each fix with error message in {}
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="Your previous generated [] incorrect fixes that cannot pass the test case checking, including: Fixing: {}; Error Message: {};	... Fixing: {}; Error Message: {}"
)
