import streamlit as st
import ollama

# ---------------- Page Config ----------------
st.set_page_config(page_title="MindEase | Mental Health Support", layout="wide")

# ---------------- Custom CSS ----------------
background_url = "https://images.unsplash.com/photo-1501785888041-af3ef285b470"

st.markdown(f"""
<style>
/* Background */
.stApp {{
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{background_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    scroll-behavior: smooth;
}}

/* Navbar */
.navbar {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(0,0,0,0.8);
    padding: 15px 30px;
    display: flex;
    justify-content: center;
    gap: 50px;
    z-index: 999;
    border-radius: 0 0 20px 20px;
}}
.navbar a {{
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.1em;
}}
.navbar a:hover {{
    color: #90EE90;
}}

/* Hero Section */
.hero {{
    background: rgba(0,0,0,0.7);
    padding: 80px;
    border-radius: 25px;
    text-align: center;
    margin: 120px auto 50px auto;
    width: 80%;
    animation: fadeIn 2s ease-in-out;
}}
.hero h1 {{
    font-size: 3.5em;
    font-weight: 900;
    background: linear-gradient(90deg, #ffdde1, #ee9ca7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}}
.hero p {{
    font-size: 1.3em;
    color: #f1f1f1;
}}
.hero img {{
    margin-top: 20px;
    border-radius: 15px;
}}

/* Chat Bubbles */
.chat-bubble {{
    padding: 14px 22px;
    border-radius: 25px;
    margin: 10px;
    max-width: 70%;
    font-size: 1.1em;
    animation: fadeInUp 0.5s;
}}
.user-bubble {{
    background: linear-gradient(135deg, #90EE90, #32CD32);
    color: black;
    margin-left: auto;
    text-align: right;
}}
.ai-bubble {{
    background: rgba(255,255,255,0.15);
    color: white;
    margin-right: auto;
}}

/* Buttons */
.stButton>button {{
    background: linear-gradient(135deg, #6EE7B7, #3B82F6);
    color: white;
    border-radius: 30px;
    font-size: 16px;
    padding: 12px 30px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: transform 0.3s ease, background 0.3s ease;
}}
.stButton>button:hover {{
    background: linear-gradient(135deg, #34D399, #2563EB);
    transform: scale(1.05);
}}

/* Resource Cards */
.resource-card {{
    background: rgba(255,255,255,0.12);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    transition: 0.3s;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}}
.resource-card img {{
    width: 100px;
    margin-bottom: 10px;
    border-radius: 15px;
}}
.resource-card a {{
    font-weight: bold;
    text-decoration: none;
    color: #fff;
}}

/* Contact Form */
.contact-wrapper {{
    display: flex;
    justify-content: space-around;
    align-items: center;
    gap: 40px;
}}
.contact-img {{
    flex: 1;
}}
.contact-img img {{
    width: 100%;
    border-radius: 20px;
}}
.contact-form {{
    flex: 1;
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
}}

/* Animations */
@keyframes fadeIn {{
    from {{ opacity: 0; }}
    to {{ opacity: 1; }}
}}
@keyframes fadeInUp {{
    from {{ transform: translateY(20px); opacity: 0; }}
    to {{ transform: translateY(0); opacity: 1; }}
}}
</style>
""", unsafe_allow_html=True)

# ---------------- Navbar ----------------
st.markdown("""
<div class="navbar">
    <a href="#home">Home</a>
    <a href="#chat">Chatbot</a>
    <a href="#resources">Resources</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---------------- State ----------------
st.session_state.setdefault('conversation_history', [])

# ---------------- Helper Functions ----------------
def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    response = ollama.chat(model="llama3.1:8b", messages=st.session_state['conversation_history'])
    ai_response = response['message']['content']
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed"
    response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# ---------------- Home Section ----------------
st.markdown("""
<section id="home">
<div class="hero">
    <h1>🌸 Welcome to MindEase 🌸</h1>
    <p>Your safe space for mental wellness, positivity, and guided support.</p>
    <p>Explore chatbot, resources, or contact us for help.</p>
    <img src="https://media.giphy.com/media/3o6ZsYm5XlPOq7rZ3m/giphy.gif">
</div>
</section>
""", unsafe_allow_html=True)

# ---------------- Chatbot Section ----------------
st.markdown("<section id='chat'><h1 style='text-align:center;'>🤖 Mental Health Chatbot</h1>", unsafe_allow_html=True)
for msg in st.session_state['conversation_history']:
    if msg['role'] == "user":
        st.markdown(f"<div class='chat-bubble user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble ai-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.text_input("💬 Type your message here:")
if user_input:
    with st.spinner("Thinking..."):
        response = generate_response(user_input)
        st.markdown(f"<div class='chat-bubble ai-bubble'>{response}</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🌸 Positive Affirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"<div class='chat-bubble ai-bubble'><b>Affirmation:</b> {affirmation}</div>", unsafe_allow_html=True)
with col2:
    if st.button("🧘 Guided Meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"<div class='chat-bubble ai-bubble'><b>Meditation:</b> {meditation_guide}</div>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;'>Relaxing Videos & Music</h3>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=inpok4MKVLM")
st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")
st.markdown("</section>", unsafe_allow_html=True)

# ---------------- Resources Section ----------------
st.markdown("<section id='resources'><h1 style='text-align:center;'>📚 Helpful Resources</h1>", unsafe_allow_html=True)
cols = st.columns(3)
resources = [
    ("WHO Mental Health", "https://upload.wikimedia.org/wikipedia/commons/9/9e/WHO_logo.svg", "https://www.who.int/mental_health/en/"),
    ("NAMI (US)", "https://www.nami.org/NAMI/media/NAMI-Media/Logos/NAMI_FullColor.png", "https://www.nami.org/Home"),
    ("Mind UK", "https://www.mind.org.uk/media/7482/mind-logo.png", "https://www.mind.org.uk/"),
    ("Headspace App", "https://seeklogo.com/images/H/headspace-logo-8B00B24FE6-seeklogo.com.png", "https://www.headspace.com/"),
    ("Calm App", "https://seeklogo.com/images/C/calm-logo-76A6116605-seeklogo.com.png", "https://www.calm.com/"),
    ("BetterHelp", "https://seeklogo.com/images/B/betterhelp-logo-9BB22B6AF1-seeklogo.com.png", "https://www.betterhelp.com/")
]
for i, (name, img, link) in enumerate(resources):
    with cols[i % 3]:
        st.markdown(f"<div class='resource-card'><img src='{img}'><br><a href='{link}' target='_blank'>{name}</a></div>", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;'>🎥 Videos & GIFs for Mindfulness</h3>
<center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/oz1R7h2YwLQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    <br><br>
    <img src="https://media.giphy.com/media/l4FGpP4lxGGgK5CBW/giphy.gif" width="300">
</center>
""", unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)

# ---------------- Contact Section ----------------
st.markdown("<section id='contact'><h1 style='text-align:center;'>📩 Contact Us</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="contact-wrapper">
    <div class="contact-img">
        <img src="https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif">
        <p style='text-align:center;'>We’d love to hear from you 💌</p>
    </div>
    <div class="contact-form">
""", unsafe_allow_html=True)
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success(f"✅ Thank you {name}! Your message has been received. We’ll reach out to {email} soon.")
st.markdown("</div></div></section>", unsafe_allow_html=True)
