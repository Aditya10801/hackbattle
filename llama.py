system_prompt = """
You are a Calendar assistant.

You will be given a list of the TO-DO tasks that a user needs to accomplish in the day, and their calendar schedule for the day. Your job is to create a new calendar schedule using time blocking such that they most efficiently accomplish all of their TODOs during the day, i.e., optimize their day for maximum productivity.

IMPORTANT NOTE: YOU MUST NOT MAKE ANY CHANGES TO THE USER'S EXISTING SCHEDULE, OR ALTER THE TIMINGS OF ANY CRUCIAL EVENTS LIKE CLASSES (IF THEY ARE A STUDENT), OR PROFESSIONAL MEETINGS.

For each event that you propose for the user, return a response with the following JSON format:
{
"Event": name of the event,
"Start time": The time at which the event should start,
"End Time": The time at which the event would be completed by,
"Duration": duration of the event,
"Importance": ["High", "Medium", "Low", "Daily habits"]
}
under the common heading "Events".

In your JSON response, one of the the heading should be "scheduling_conflicts" wherein you list out the new events you're proposing should be there, but they clash with the user's current schedule, in the same format as the one you're using to list out your events. 

Some other headings in your JSON response should be the date of which you're proposing the new calendar, and a 4-5 word short description of what the day looks like. For example, if the user has their CS exam on the day, then the description of the day should look something like "CS Exam and Studying".

NOTE: ALL YOUR TIMES IN THE JSON RESPONSE MUST BE IN 24-HOUR FORMAT.

NOTE: Please return your "Events" JSON in the correct order of the events being displayed as the day progresses."""

test_user_prompt = """
Date: 25 September 2024
Preferred Breakfast timing: 8:00
Preferred Lunch timing: 12:00
Preferred Dinner timing: 19:00
Work Style: Frequent Breaks

| Time | Activity |
|------|----------|
| 07:00 - 08:15 | Wake up, get ready, and commute to classes |
| 08:30 - 09:20 | Theory Class: Mathematics |
| 09:30 - 10:20 | Theory Class: Computer Science |
| 10:30 - 11:20 | Free Period / Study Time |
| 11:30 - 12:20 | Theory Class: Physics |
| 12:30 - 14:00 | Lunch break and relaxation |
| 14:10 - 15:50 | Lab Class: Computer Programming |
| 16:00 - 18:00 | Free time / Extracurricular activities |
| 18:00 - 19:00 | Dinner |
| 19:00 - 21:30 | Study / Homework time |
| 21:30 - 23:00 | Free time / Social activities |
| 23:00 | Lights out |

## TO-DO List

1. [ ] Complete Mathematics assignment (due Friday)
2. [ ] Prepare for Computer Science quiz
3. [ ] Submit Physics lab report
4. [ ] Make 1 hr worth of progress on ML project
5. [ ] Clean hostel room
6. [ ] Do laundry
7. [ ] Pay hostel mess fees
8. [ ] Call parents on Sunday
"""

user_second_prompt = """
I gave you some instructions earlier on creating the most optimal calendar schedule for me without disturbing my current schedule, and you returned a response. How do you think you can improve the response to better optimize my day for productivity, without actually making any changes to my day in my original schedule? 

DO NOT CHANGE THE FORMAT OF YOUR JSON OUTPUT, JUST MAKE THE CHANGES PROPOSED IN THE INSTRUCTIONS.

The JSON output must contain the following headers: "Date", "Description", "scheduling_conflicts", "Events" with the events header containing "activity" "Start time", "End Time", "Duration", and "Importance". 
"""

messages=[
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": "Date: 25 September 2024\nPreferred Breakfast timing: 8:00\nPreferred Lunch timing: 12:00\nPreferred Dinner timing: 19:00\nWork Style: Frequent Breaks\n\n| Time | Activity |\n|------|----------|\n| 07:00 - 08:15 | Wake up, get ready, and commute to classes |\n| 08:30 - 09:20 | Theory Class: Mathematics |\n| 09:30 - 10:20 | Theory Class: Computer Science |\n| 10:30 - 11:20 | Free Period / Study Time |\n| 11:30 - 12:20 | Theory Class: Physics |\n| 12:30 - 14:00 | Lunch break and relaxation |\n| 14:10 - 15:50 | Lab Class: Computer Programming |\n| 16:00 - 18:00 | Free time / Extracurricular activities |\n| 18:00 - 19:00 | Dinner |\n| 19:00 - 21:30 | Study / Homework time |\n| 21:30 - 23:00 | Free time / Social activities |\n| 23:00 | Lights out |\n\n## TO-DO List\n\n1. [ ] Complete Mathematics assignment (due Friday)\n2. [ ] Prepare for Computer Science quiz\n3. [ ] Submit Physics lab report\n4. [ ] Make 1 hr worth of progress on ML project\n5. [ ] Clean hostel room\n6. [ ] Do laundry\n7. [ ] Pay hostel mess fees\n8. [ ] Call parents on Sunday"
    }
]

from groq import Groq
import json 

client = Groq(api_key="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")
def get_response(messages):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages = messages,
        stream=False,
        response_format={ "type": "json_object" },
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )
    
    return completion.choices[0].message.content

first_completion = get_response(messages)
print("Got first completion")

messages.append({"role": "assistant", "content": first_completion})
messages.append({"role": "user", "content": user_second_prompt})

second_completion = get_response(messages)

print(second_completion)
