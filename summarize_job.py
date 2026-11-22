from dotenv import load_dotenv

load_dotenv()

import anthropic

client = anthropic.Anthropic()


def summarize_job(job_description):
    message = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"Summarize this job description into 3-line summary: {job_description}"}
        ]
    )

    return message.content[0].text

with open("job.txt", "r") as file:
    job_description = file.read()

summary = summarize_job(job_description)
print(summary)