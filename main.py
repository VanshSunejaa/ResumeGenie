Here's the code for your `main.py`, with the API key hidden using environment variables:

```python
import streamlit as st
import google.generativeai as genai
import os

# Load API key from environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure Google API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Function to generate resume content
def generate_resume_content(name, contact_info, education, experience, skills, additional_info):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Create a professional resume for the following individual:

        Name: {name}
        Contact Information: {contact_info}
        Education: {education}
        Experience: {experience}
        Skills: {skills}
        Additional Information: {additional_info}

        Generate a polished resume with a professional format and structure.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the resume: {str(e)}"

# Function to provide feedback on the resume
def get_resume_feedback(resume):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Review the following resume and provide feedback on how to improve it based on industry standards:

        Resume:
        {resume}

        Provide suggestions for improving content, structure, and overall presentation.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the feedback: {str(e)}"

# Streamlit UI
st.title("Resume Builder and Optimizer")

# Input resume details
name = st.text_input("Full Name")
contact_info = st.text_area("Contact Information (email, phone, address)")
education = st.text_area("Education (include degrees, institutions, and years)")
experience = st.text_area("Experience (include job titles, companies, and durations)")
skills = st.text_area("Skills (include relevant skills and certifications)")
additional_info = st.text_area("Additional Information (include any other relevant details)")

if st.button("Generate Resume"):
    if name and contact_info and education and experience and skills:
        # Generate resume content
        resume = generate_resume_content(name, contact_info, education, experience, skills, additional_info)

        st.subheader("Generated Resume")
        st.write(resume)

        # Provide feedback
        feedback = get_resume_feedback(resume)
        st.subheader("Resume Feedback")
        st.write(feedback)
    else:
        st.error("Please fill in all required fields to generate the resume.")
```

### Instructions to Set Environment Variable
1. In your terminal or command prompt, set the environment variable:
   - For Windows:
     ```bash
     set GOOGLE_API_KEY=your_actual_api_key_here
     ```
   - For macOS/Linux:
     ```bash
     export GOOGLE_API_KEY=your_actual_api_key_here
     ```
2. Run your Streamlit app normally. The API key will be securely accessed from the environment variable.
