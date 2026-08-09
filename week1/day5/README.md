As part of my AI learning journey, I built an automated AI resume parsing and candidate ranking tool using Python and LLMs.

The goal was to create a system that evaluates multiple resumes against a specific job description and outputs structured evaluation metrics rather than unstructured text.

How it works:

Data Extraction: The script reads candidates' resumes from PDF and DOCX files using pypdf and python-docx to extract raw text cleanly.

Structured LLM Evaluation: Instead of getting free-form responses, I used Pydantic with Gemini (via LiteLLM / OpenAI API interface) to enforce a strict JSON schema output for every candidate.

Candidate Scoring and Breakdown: For each applicant, the system extracts:

Candidate name and contact information

Matching skills and key missing skills

Verification of education and experience requirements

An overall match percentage score

A short final summary evaluation

Ranking: The script processes all candidates and prints out the top-ranked profiles along with candidates who fell short of the requirements.

Working with structured output schemas makes integrating LLM evaluations into downstream application logic much cleaner and more predictable.

