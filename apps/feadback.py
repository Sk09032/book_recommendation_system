import streamlit as st

def app():
    st.title("Feedback and Bug Report")
    
    st.write("""
    We value your feedback! Please use this form to report any bugs you've encountered 
    or to provide suggestions for improving our Book Recommendation System.
    """)
    
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        
        feedback_type = st.selectbox(
            "Type of Feedback",
            ("Bug Report", "Feature Request", "General Feedback")
        )
        
        description = st.text_area("Please describe your feedback or the bug you encountered")
        
        severity = st.slider("If reporting a bug, how severe is it?", 1, 5, 3)
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            # Here you would typically save this information to a database
            # For now, we'll just display a success message
            st.success("Thank you for your feedback! We've received your submission.")
            st.write(f"Feedback Type: {feedback_type}")
            st.write(f"Description: {description}")
            if feedback_type == "Bug Report":
                st.write(f"Severity: {severity}")

if __name__ == "__main__":
    app()