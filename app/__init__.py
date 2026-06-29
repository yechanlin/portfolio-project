import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

profile = {
    "name": "Ye Chan Lin",
    "tagline": "Software Engineer & CS Student at UCLA",
    "about": [
        "I'm a CS student at UCLA with hands-on experience building production "
        "systems — from geospatial ETL pipelines on AWS to full-stack web "
        "platforms serving thousands of users.",
        "I'm a 2× software engineer intern, hackathon winner, and robotics team "
        "lead who loves shipping clean, well-tested code — from React frontends "
        "to AWS-integrated backends.",
    ],
}

socials = [
    {"name": "GitHub", "url": "https://github.com/yechanlin"},
    {"name": "LinkedIn", "url": "https://linkedin.com/in/yechanlin"},
    {"name": "Email", "url": "mailto:yechanlin15703@gmail.com"},
]

experiences = [
    {
        "company": "Boundary RSS",
        "role": "Software Engineer Intern",
        "start": "Mar 2025",
        "end": "May 2025",
        "description": "Engineered a Python-based DEM extractor integrating the OpenTopography API and built a cloud ETL pipeline on AWS EC2, cutting data validation time by 40% with 100% unit test coverage.",
    },
    {
        "company": "CodeDay Labs",
        "role": "Open Source Contributor",
        "start": "Dec 2024",
        "end": "Feb 2025",
        "description": "Resolved a critical unit-conversion bug in the Open Energy Dashboard (PR #1426) impacting 200+ organizations, backed by a Mocha/Chai test suite covering 15+ edge cases at a 100% pass rate.",
    },
    {
        "company": "OC Robotics",
        "role": "Software Team Lead",
        "start": "Oct 2024",
        "end": "May 2025",
        "description": "Led an 8-person team building ROS2-based autonomous control for a Mars rover prototype that won 1st place at the OCC STEM Research Symposium, integrating LiDAR, computer vision, and motor control.",
    },
]

education = [
    {
        "school": "University of California, Los Angeles (UCLA)",
        "degree": "B.S. Computer Science",
        "start": "2023",
        "end": "Jun 2027",
        "description": "Relevant coursework: Data Structures & Algorithms, Computer Architecture, Discrete Math & Probability, OOP. Activities: 2× Hackathon Winner, ACM AI, BruinAI, OC Robotics.",
    },
]

projects = [
    {
        "name": "Talantis",
        "tech": "Next.js, FastAPI, PostgreSQL, Supabase, Claude Sonnet",
        "award": "LA Hacks — Best Figma Make Challenge Winner",
        "description": "A talent intelligence platform mapping internship pipelines across 63 companies and 64K+ placements, featuring Atlas — an agentic AI guide powered by Claude Sonnet with sub-second streamed responses.",
        "url": "",
    },
    {
        "name": "ClubApply.ai",
        "tech": "Python, FastAPI, React, AWS Bedrock, Multi-Agent",
        "award": "BruinAI Hackathon — Best Use of AWS Winner",
        "description": "An AI assistant analyzing club missions to generate personalized application tips for 1,200+ UCLA clubs, using multi-agent workflows on AWS Bedrock to cut tip generation time by 40%.",
        "url": "",
    },
    {
        "name": "Chad the Interviewer",
        "tech": "React, Node.js, Express, MongoDB, Deepgram, GPT-4",
        "award": "SB Hacks XII",
        "description": "A real-time AI interview platform with live voice interaction via Deepgram and GPT-4, streaming audio over WebSockets at sub-300ms latency with post-session AI feedback reports.",
        "url": "",
    },
]

skills = [
    {"category": "Languages", "items": "Python, JavaScript, TypeScript, C++, Java, SQL, HTML/CSS, Bash"},
    {"category": "Frameworks", "items": "React, Next.js, Node.js, Express, Django, FastAPI, ROS2, Pytest, Mocha/Chai"},
    {"category": "Cloud & DevOps", "items": "AWS (EC2, S3, Bedrock), Docker, Vercel, GitHub Actions, Linux, Git"},
    {"category": "Databases & Tools", "items": "PostgreSQL, Supabase, MongoDB, SQLite, Redis, Postman, Figma"},
]

# Add a matching image at app/static/img/<image> — falls back to the logo if missing.
hobbies = [
    {
        "name": "Watching Anime",
        "description": "Unwinding with a good anime series — from long-running shonen to tightly-written one-cours gems.",
        "image": "hobby_anime.jpg",
    },
    {
        "name": "Reality TV Shows",
        "description": "Getting hooked on reality TV — the drama, the competition, and the occasional guilty-pleasure binge.",
        "image": "hobby_reality_tv.jpg",
    },
    {
        "name": "Traveling",
        "description": "Exploring new places, cultures, and food whenever I get the chance to pack a bag and go.",
        "image": "hobby_travel.jpg",
    },
]

visited_locations = [
    {"name": "Japan", "lat": 36.2048, "lng": 138.2529},
    {"name": "China", "lat": 35.8617, "lng": 104.1954},
    {"name": "Myanmar", "lat": 21.9162, "lng": 95.9560},
    {"name": "Thailand", "lat": 15.8700, "lng": 100.9925},
    {"name": "Malaysia", "lat": 4.2105, "lng": 101.9758},
    {"name": "Italy", "lat": 41.8719, "lng": 12.5674},
    {"name": "France", "lat": 46.2276, "lng": 2.2137},
    {"name": "Switzerland", "lat": 46.8182, "lng": 8.2275},
]

# In-page section navigation. Anchors are absolute (/#id) so they also work
# from the standalone /hobbies page, jumping back to the relevant section.
pages = [
    {"name": "About", "url": "/#about"},
    {"name": "Experience", "url": "/#experience"},
    {"name": "Education", "url": "/#education"},
    {"name": "Projects", "url": "/#projects"},
    {"name": "Skills", "url": "/#skills"},
    {"name": "Hobbies", "url": "/#hobbies"},
    {"name": "Travel", "url": "/#travel"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Ye Chan Lin",
        url=os.getenv("URL"),
        profile=profile,
        socials=socials,
        experiences=experiences,
        education=education,
        projects=projects,
        skills=skills,
        hobbies=hobbies,
        visited_locations=visited_locations,
        pages=pages,
    )


@app.route("/hobbies")
def hobbies_page():
    return render_template(
        "hobbies.html",
        title="Hobbies",
        url=os.getenv("URL"),
        profile=profile,
        socials=socials,
        hobbies=hobbies,
        pages=pages,
    )
