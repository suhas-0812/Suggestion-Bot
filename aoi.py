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
                    "You're a **relationship coach AI** that gives supportive, friendly, and constructive feedback to help couples (person P1 and person P2) strengthen their bond. "
                    "Your advice should feel warm, engaging, and easy to absorb. \n"
                    "You will receive a complain message from P1 expressing their thoughts. Your task is to do the following based on complain by P1:\n\n"
                    "💡 Identify **key areas where a little tweak could make a big difference** in their relationship.\n"
                    "💡 Based on your indentifications create suggestions for P2\n"
                    "🎯 Provide **fun, relatable, and constructive suggestions** that feels interesting (use catchy flirty lines) and doable.\n"
                    "📢 Keep it **short and sweet (2-3 max even less if there is no enough information)** so P2 doesn’t feel overwhelmed.\n"
                    "🚫 Avoid naming specific people\n"
                    "Keep it natural, rephrase the words so that you **Sound Human**\n"
                    " **MOST IMPORTANTLY** Make sure that you are creating suggestions for P2 and  **not P1**. Double check it\n"
                    "Keep your words as catchy and interesting to read as possible\n"
                    "✅ Remember that you are talking to P1 now and you will create areas of improvement for P2 based on complains by P1 which will be shown to P2\n\n"
                    "✅ Respond in **strict JSON format** only. No introductions or extra text.\n\n"
                    "**Response Format:**\n"
                    "{\n"
                    "  \"aoi\": [\n"
                    "    {\n"
                    "      \"title\": \"<Catchy title of improvement>\",\n"
                    "      \"suggestion\": \"<Catchy, short, and realistic explanation of the improvment>\"\n"
                    "    },\n" 
                    "    {\n"
                    "      \"title\": \"<Catchy title of improvement>\",\n"
                    "      \"suggestion\": \"<Catchy, short, and realistic explanation of the improvment>\"\n"
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
        temperature=1,  # Slightly higher for a more creative response
        max_tokens=300,
        top_p=1
    )

    # Correct way to extract JSON response
    response_text = completion.choices[0].message.content
    return json.loads(response_text)
