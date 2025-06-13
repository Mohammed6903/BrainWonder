from langchain_core.prompts import PromptTemplate

PREFERENCE_EXTRACTION_PROMPT = PromptTemplate.from_template(
    """Extract career preferences from this conversation. Return ONLY a JSON object with these fields:
    - interests: array of interests mentioned
    - skills: array of skills mentioned  
    - dislikes: array of dislikes mentioned
    - work_style: string describing work preference
    - confidence_score: number from 0.0 to 1.0

    Conversation: {conversation}

    JSON:"""
)

CAREER_MAPPING_PROMPT = PromptTemplate.from_template(
    """Based on these preferences, recommend 2-3 career paths from: Software Engineering, Data Science, Graphic Design, Marketing, Nursing, Engineering, Music Production, Sports Management.

    Preferences: {preferences}

    Return ONLY a JSON object:
    {{"career_paths": ["path1", "path2"], "match_reasons": ["reason1", "reason2"], "confidence_score": 0.8}}

    JSON:"""
)

EXPLANATION_PROMPT = PromptTemplate.from_template(
    """Explain why {career_path} is recommended for someone with these interests: {interests}

    Keep it under 100 words and focus on the match between their interests and this career.

    Explanation:"""
)

CLARIFYING_QUESTIONS = {
    "insufficient_info": "The user hasn't shared much about their interests. Ask 2 specific questions to learn about their hobbies, skills, or career goals.\n\nQuestions:",
    "general": "Ask 2 questions to better understand their career preferences based on: {context}\n\nQuestions:"
}
