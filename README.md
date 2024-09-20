# ResumeGenie




## Project Overview
The Resume Builder and Optimizer is a Streamlit application designed to assist users in creating professional resumes with the help of AI. Users can input their personal and professional details to generate a polished resume and receive constructive feedback for further enhancements.

## Features
- **AI-Generated Resumes**: Automatically generate a well-structured resume based on user inputs.
- **Feedback Mechanism**: Get actionable suggestions to improve the content, format, and presentation of the resume.
- **User-Friendly Interface**: Simple and intuitive UI powered by Streamlit for a seamless experience.

## Tech Stack
- **Python**: The main programming language used for development.
- **Streamlit**: Framework utilized for building the web application.
- **Google Generative AI (Gemini)**: Employed for generating resume content and providing feedback.

## Installation Instructions

### Prerequisites
- Python 3.7 or higher installed on your machine.
- Basic familiarity with command line interface.

### Steps to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/resume-builder.git
   cd resume-builder
   ```

2. **Install required packages**:
   Create a virtual environment (optional) and install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**:
   Before running the application, set your Google API key as an environment variable:
   - For Windows:
     ```bash
     set GOOGLE_API_KEY=your_actual_api_key_here
     ```
   - For macOS/Linux:
     ```bash
     export GOOGLE_API_KEY=your_actual_api_key_here
     ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

5. Open your web browser and navigate to `http://localhost:8501` to use the application.

## Usage Guide
1. **Input Fields**: Fill out the following sections:
   - **Full Name**: Enter your complete name.
   - **Contact Information**: Provide your email, phone number, and address.
   - **Education**: Include degrees, institutions, and years of graduation.
   - **Experience**: List job titles, companies, and durations of employment.
   - **Skills**: Mention relevant skills and certifications.
   - **Additional Information**: Add any other relevant details that may enhance your resume.

2. **Generate Resume**: Click the **Generate Resume** button to create your resume.

3. **View and Improve**: Review the generated resume and read through the feedback provided for potential improvements.

## File Structure
```
resume-builder/
│
├── main.py                   # Main application file for the Streamlit app
├── requirements.txt          # List of dependencies required to run the project
└── README.md                 # Documentation file describing the project
```

## Disclaimer
This project is intended for educational purposes only and is not designed from a user perspective. The application may not cover all aspects of resume building and optimization. Use the generated resumes at your own discretion.
