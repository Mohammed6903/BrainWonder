import json
from typing import List, Dict
from langchain_core.output_parsers import JsonOutputParser
from models.schemas import PreferenceExtraction, CareerRecommendation
from models.career import CAREER_PATHS
from prompts.templates import PREFERENCE_EXTRACTION_PROMPT, CAREER_MAPPING_PROMPT, EXPLANATION_PROMPT, CLARIFYING_QUESTIONS

class CareerRecommendationSystem:
    def __init__(self, llm):
        self.llm = llm
        self.preference_parser = JsonOutputParser(pydantic_object=PreferenceExtraction)
        self.recommendation_parser = JsonOutputParser(pydantic_object=CareerRecommendation)
        
        # Initialize prompt templates
        self._setup_prompts()
    
    def _setup_prompts(self):
        self.preference_extraction_prompt = PREFERENCE_EXTRACTION_PROMPT
        
        self.career_mapping_prompt = CAREER_MAPPING_PROMPT
        
        self.explanation_prompt = EXPLANATION_PROMPT
        
        self.clarifying_questions = CLARIFYING_QUESTIONS
    
    def extract_preferences(self, conversation: str) -> Dict:
        """Extract preferences from conversation text"""
        prompt = self.preference_extraction_prompt.format(conversation=conversation)
        
        response = self.llm.invoke(prompt)
        try:
            # Try to extract JSON from response
            response_text = response.strip()
            if response_text.startswith('```json'):
                response_text = response_text.replace('```json', '').replace('```', '').strip()
            
            return json.loads(response_text)
        except:
            # Fallback parsing
            return self._fallback_preference_extraction(conversation)
    
    def recommend_careers(self, preferences: Dict) -> Dict:
        """Map preferences to career recommendations"""
        prompt = self.career_mapping_prompt.format(preferences=json.dumps(preferences))
        
        response = self.llm.invoke(prompt)
        try:
            response_text = response.strip()
            if response_text.startswith('```json'):
                response_text = response_text.replace('```json', '').replace('```', '').strip()
            
            return json.loads(response_text)
        except:
            return self._fallback_career_recommendation(preferences)
    
    def generate_explanations(self, career_path: str, interests: List[str]) -> str:
        """Generate detailed explanation for a career recommendation"""
        prompt = self.explanation_prompt.format(
            career_path=career_path,
            interests=', '.join(interests)
        )
        
        return self.llm.invoke(prompt)
    
    def ask_clarifying_questions(self, conversation: str = "", question_type: str = "insufficient_info") -> str:
        """Generate clarifying questions based on the situation"""
        if question_type == "insufficient_info":
            prompt = self.clarifying_questions["insufficient_info"].format()
        else:
            prompt = self.clarifying_questions["general"].format(context=conversation[:200])
        
        return self.llm.invoke(prompt)
    
    def _format_career_database(self) -> str:
        """Format career database for prompt"""
        formatted = ""
        for category, paths in CAREER_PATHS.items():
            formatted += f"\n{category}:\n"
            for path in paths:
                formatted += f"  - {path.name}: {path.description}\n"
                formatted += f"    Skills: {', '.join(path.required_skills)}\n"
                formatted += f"    Roles: {', '.join(path.typical_roles)}\n"
        return formatted
    
    def _fallback_preference_extraction(self, conversation: str) -> Dict:
        """Fallback method if JSON parsing fails"""
        return {
            "interests": [],
            "skills": [],
            "dislikes": [],
            "work_style": "unknown",
            "confidence_score": 0.3
        }
    
    def _fallback_career_recommendation(self, preferences: Dict) -> Dict:
        """Fallback method if recommendation parsing fails"""
        return {
            "career_paths": ["General Business", "Liberal Arts"],
            "match_reasons": ["Broad applicability", "Flexible options"],
            "confidence_score": 0.4
        }
    
    def full_recommendation_pipeline(self, conversation: str) -> Dict:
        """Complete pipeline from conversation to recommendations"""
        # Step 1: Extract preferences
        preferences = self.extract_preferences(conversation)
        
        # Step 2: Check if we need clarifying questions
        if preferences["confidence_score"] < 0.6:
            questions = self.ask_clarifying_questions(conversation)
            print("Need more information. Questions to ask:")
            print(questions)
            return {
                "status": "needs_clarification",
                "questions": questions,
                "extracted_preferences": preferences
            }
        
        # Step 3: Get recommendations
        recommendations = self.recommend_careers(preferences)
        
        # Step 4: Generate explanations
        explanations = []
        for i, career_path in enumerate(recommendations["career_paths"]):
            match_reason = recommendations["match_reasons"][i] if i < len(recommendations["match_reasons"]) else "Good general fit"
            explanation = self.generate_explanations(career_path, preferences.get("interests", []))
            explanations.append({
                "career_path": career_path,
                "explanation": explanation,
                "match_reason": match_reason
            })
        
        return {
            "status": "complete",
            "preferences": preferences,
            "recommendations": recommendations,
            "explanations": explanations
        }
