import streamlit as st

def app():
    st.title("Contact Me")
    
    st.write("""
    Have questions or need assistance? I'm here to help!!!
    Feel free to reach out to me using the contact information below or by filling out the form.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Contact Information")
        st.write("Email: kgpian121@gmail.com")
        st.write("Phone: 1234567890")
        st.write("Address: Uttarakhand India")
        
        st.subheader("Hours of Operation")
        st.write("Monday - Friday: 9:00 AM - 5:00 PM")
        st.write("Saturday: 10:00 AM - 2:00 PM")
        st.write("Sunday: Closed")
    
    with col2:
        st.subheader("Send us a message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Your Message")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                # Here you would typically send this information to your backend
                # For now, we'll just display a success message
                st.success("Thank you for your message! We'll get back to you soon.")

if __name__ == "__main__":
    app()