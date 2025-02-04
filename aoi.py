from groq import Groq
import json

client = Groq(GROQ_API_KEY)

def get_areas_of_improvement(user_input_string):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant designed to help couples strengthen their relationship through supportive and constructive feedback. "
                    "You will receive a message from one partner expressing their thoughts. Your task is to:\n\n"
                    "- Identify key areas for relationship improvement while keeping feedback neutral and non-confrontational.\n"
                    "- Provide polite, constructive, and actionable suggestions in strict JSON format.\n"
                    "- Keep the response minimal (2-3 key points, or even less if the message contains limited information) to avoid overwhelming the user.\n"
                    "- Hide any direct references to specific people or behaviors to prevent defensiveness.\n"
                    "- No introductions or extra text—only return JSON output.\n\n"
                    "Response Format:\n"
                    "{\n"
                    "  \"aoi\": [\n"
                    "    {\n"
                    "      \"title\": \"<Concise title of improvement>\",\n"
                    "      \"suggestion\": \"<Polite, constructive, and general relationship-focused suggestion>\"\n"
                    "    },\n"
                    "    {\n"
                    "      \"title\": \"<Concise title of improvement>\",\n"
                    "      \"suggestion\": \"<Polite, constructive, and general relationship-focused suggestion>\"\n"
                    "    }\n"
                    "  ]\n"
                    "}"
                )
            },
            {
                "role": "user",
                "content": user_input_string
            }
        ],
        temperature=0.5,
        max_tokens=400,
        top_p=1
    )

    # Correct way to extract JSON response
    response_text = completion.choices[0].message.content
    return json.loads(response_text)