from groq import Groq
import json
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def get_areas_of_improvement(user_input_string):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You're a **relationship coach AI** that gives supportive, friendly, and constructive feedback to help couples strengthen their bond. "
                    "Your advice should feel warm, engaging, and easy to absorb. Your task is to:\n\n"
                    "💡 Identify **key areas where the partner (the one being talked about) can improve** to strengthen the relationship.\n"
                    "🎯 Provide **fun, relatable, and constructive suggestions** that feel natural and doable for them.\n"
                    "📢 Keep it **short and sweet (2-3 max)** so they don’t feel overwhelmed.\n"
                    "🚫 Avoid naming specific people or using phrases that sound like blame.\n"
                    "✅ Respond in **strict JSON format** only. No introductions or extra text.\n\n"
                    "**Important:**\n"
                    "- The suggestions should be **for the partner (the person being talked about), NOT for the person expressing concerns**.\n"
                    "- Keep suggestions **neutral, positive, and solution-oriented**.\n\n"
                    "**Response Format:**\n"
                    "{\n"
                    "  \"aoi\": [\n"
                    "    {\n"
                    "      \"title\": \"<Catchy title of improvement>\",\n"
                    "      \"suggestion\": \"<Friendly, encouraging, and realistic suggestion>\"\n"
                    "    },\n"
                    "    {\n"
                    "      \"title\": \"<Catchy title of improvement>\",\n"
                    "      \"suggestion\": \"<Friendly, encouraging, and realistic suggestion>\"\n"
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
        temperature=0.6,  # Slightly higher for a more creative response
        max_tokens=400,
        top_p=1
    )

    # Correct way to extract JSON response
    response_text = completion.choices[0].message.content
    return json.loads(response_text)
