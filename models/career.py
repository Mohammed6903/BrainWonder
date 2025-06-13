from dataclasses import dataclass
from typing import List

@dataclass
class CareerPath:
    name: str
    category: str
    description: str
    required_skills: List[str]
    typical_roles: List[str]

CAREER_PATHS = {
    "STEM": [
        CareerPath("Software Engineering", "STEM", "Design and develop software applications and systems", 
                  ["Programming", "Problem-solving", "Logic"], ["Developer", "Engineer", "Architect"]),
        CareerPath("Data Science", "STEM", "Analyze data to extract insights and build predictive models",
                  ["Statistics", "Programming", "Analytics"], ["Data Scientist", "Analyst", "ML Engineer"]),
        CareerPath("Biomedical Research", "STEM", "Conduct research to advance medical knowledge and treatments",
                  ["Research", "Biology", "Critical thinking"], ["Researcher", "Lab Technician", "Scientist"]),
        CareerPath("Engineering", "STEM", "Design and build solutions to technical problems",
                  ["Math", "Physics", "Design"], ["Civil Engineer", "Mechanical Engineer", "Electrical Engineer"])
    ],
    "Arts": [
        CareerPath("Graphic Design", "Arts", "Create visual content for digital and print media",
                  ["Creativity", "Design software", "Visual communication"], ["Designer", "Art Director", "Creative Lead"]),
        CareerPath("Music Production", "Arts", "Create, record, and produce musical content",
                  ["Music theory", "Audio editing", "Creativity"], ["Producer", "Sound Engineer", "Composer"]),
        CareerPath("Writing & Journalism", "Arts", "Create written content for various media and audiences",
                  ["Writing", "Research", "Communication"], ["Writer", "Journalist", "Editor", "Content Creator"]),
        CareerPath("Film & Video", "Arts", "Create visual storytelling content for entertainment and media",
                  ["Storytelling", "Video editing", "Creativity"], ["Director", "Editor", "Cinematographer"])
    ],
    "Sports": [
        CareerPath("Athletic Training", "Sports", "Help athletes prevent and recover from injuries",
                  ["Anatomy", "Physical therapy", "Sports knowledge"], ["Trainer", "Therapist", "Coach"]),
        CareerPath("Sports Management", "Sports", "Manage sports teams, facilities, and events",
                  ["Management", "Business", "Sports knowledge"], ["Manager", "Agent", "Event Coordinator"]),
        CareerPath("Fitness Coaching", "Sports", "Help individuals achieve their fitness and health goals",
                  ["Exercise science", "Motivation", "Communication"], ["Personal Trainer", "Coach", "Instructor"])
    ],
    "Business": [
        CareerPath("Marketing", "Business", "Promote products and services to target audiences",
                  ["Communication", "Analytics", "Creativity"], ["Marketer", "Brand Manager", "Social Media Manager"]),
        CareerPath("Finance", "Business", "Manage money, investments, and financial planning",
                  ["Math", "Analytics", "Risk assessment"], ["Analyst", "Advisor", "Investment Banker"]),
        CareerPath("Entrepreneurship", "Business", "Start and run your own business ventures",
                  ["Leadership", "Risk-taking", "Innovation"], ["Founder", "CEO", "Business Owner"])
    ],
    "Healthcare": [
        CareerPath("Nursing", "Healthcare", "Provide direct patient care and medical support",
                  ["Empathy", "Medical knowledge", "Communication"], ["Nurse", "Nurse Practitioner", "Care Manager"]),
        CareerPath("Psychology", "Healthcare", "Help people with mental health and behavioral issues",
                  ["Empathy", "Communication", "Analysis"], ["Therapist", "Counselor", "Psychologist"])
    ]
}

