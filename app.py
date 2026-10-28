import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Len.icon",
    page_icon="🟡",
    layout="wide",
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Hertz Miscreola"

pages = ["Hertz Miscreola", "Len.icon", "Projects", "Skills", "Contact"]

# ==========================================
# THEMES
# ==========================================
THEMES = {
    "Hertz Miscreola": {
        "bg": "#F8FAFC",
        "card_bg": "#FFFFFF",
        "text": "#1E293B",
        "primary": "#3276EB",
        "border": "#CBD5E1",
        "shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05)"
    },
    "Len.icon": {
        "bg": "#100B27",
        "card_bg": "#100B27",
        "text": "#E2E8F0",
        "primary": "#F5D151",
        "border": "#2a2444",
        "shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.2), 0 8px 10px -6px rgba(0, 0, 0, 0.2)"
    },
    "Projects": {
        "bg": "#0E1117",
        "card_bg": "#1E1E2E",
        "text": "#E7E6E9",
        "primary": "#F5D151",
        "border": "#2B2B3D",
        "shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3)"
    },
    "Skills": {
        "bg": "#130E1F",
        "card_bg": "#1F1733",
        "text": "#F3E8FF",
        "primary": "#C084FC",
        "border": "#3B2863",
        "shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3)"
    },
    "Contact": {
        "bg": "#100B27",
        "card_bg": "#100B27",
        "text": "#E2E8F0",
        "primary": "#F5D151",
        "border": "#2a2444",
        "shadow": "0 10px 25px -5px rgba(0, 0, 0, 0.2), 0 8px 10px -6px rgba(0, 0, 0, 0.2)"
    },
}

# Load active theme based strictly on current page state
theme = THEMES[st.session_state.page]
BG_COLOR = theme["bg"]
CARD_BG = theme["card_bg"]
TEXT_COLOR = theme["text"]
PRIMARY_COLOR = theme["primary"]
CARD_BORDER = theme["border"]
CARD_SHADOW = theme["shadow"]

# ==========================================
# NAVIGATION
# ==========================================
selected_page = st.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page),
    horizontal=True,
    label_visibility="hidden",
    key="nav_radio"
)


if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

# ==========================================
# CSS DESIGN
# ==========================================
st.markdown(
    f"""
    <style>
        /* Main application background */
        .stApp {{
            background-color: {BG_COLOR} !important;
            color: {TEXT_COLOR} !important;
            transition: background-color 0.3s ease, color 0.3s ease;
        }}
        
        /* Hide top header and reduce top padding */
        header[data-testid="stHeader"] {{
            display: none !important;
        }}
        .block-container {{
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 1200px !important;
        }}

        /* --- MODERNIZED NAVIGATION TABS --- */
        div[role="radiogroup"] {{
            display: flex !important;
            flex-direction: row !important;
            gap: 1rem !important;
            justify-content: center !important;
            background-color: {CARD_BG} !important;
            padding: 0.5rem 1rem !important;
            border-radius: 50px !important;
            border: 1px solid {CARD_BORDER} !important;
            box-shadow: {CARD_SHADOW} !important;
            margin-bottom: 0rem !important;
        }}

        div[role="radiogroup"] input[type="radio"] {{
            display: none !important;
        }}
        
        div[role="radiogroup"] label[data-baseweb="radio"] div:has(> input[type="radio"]) {{
            display: none !important;
        }}
        
        div[role="radiogroup"] div[data-testid="stMarkdownContainer"] {{
            display: contents !important;
        }}

        div[role="radiogroup"] label[data-baseweb="radio"] {{
            background-color: transparent !important;
            border: none !important;
            padding: 8px 18px !important;
            margin: 0 !important;
            border-radius: 30px !important;
            cursor: pointer !important;
            transition: all 0.25s ease !important;
        }}

        div[role="radiogroup"] label[data-baseweb="radio"] p {{
            color: {TEXT_COLOR} !important;
            font-size: 1rem !important;
            font-weight: 500 !important;
            opacity: 0.8;
            margin: 0 !important;
        }}

        div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) {{
            background-color: {PRIMARY_COLOR} !important;
        }}

        div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) p {{
            color: {"#0E1117" if PRIMARY_COLOR in ["#F5D151", "#2563EB"] else "#FFFFFF"} !important;
            font-weight: 700 !important;
            opacity: 1 !important;
        }}

        div[role="radiogroup"] label[data-baseweb="radio"]:hover {{
            background-color: {CARD_BORDER} !important;
        }}
        
        div[role="radiogroup"] label[data-baseweb="radio"]:hover p {{
            opacity: 1 !important;
        }}

        /* --- CARD CONTAINER STYLING --- */
        .content-card {{
            background-color: {CARD_BG};
            border: 1px solid {CARD_BORDER};
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: {CARD_SHADOW};
            transition: all 0.3s ease;
        }}

        /* Typography & Custom Elements */
        h1, h2, h3, h4, h5, h6, p, span, label {{
            color: {TEXT_COLOR} !important;
        }}
        
        .accent-text {{
            color: {PRIMARY_COLOR} !important;
            font-weight: 600;
        }}

        .badge {{
            display: inline-block;
            padding: 0.35rem 0.85rem;
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: 50px;
            background-color: {CARD_BORDER};
            color: {TEXT_COLOR};
            margin: 0.2rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# PAGE CONTENT
# ==========================================
if st.session_state.page == "Hertz Miscreola":
    with st.container():
        col_text, col_img = st.columns([2, 1], gap="large")

        with col_text:
            st.title("Hertz Lenin C. Miscreola")
            st.markdown(f"<h3 style='color: {PRIMARY_COLOR}; margin-top: 0;'>Software Developer & Game Designer</h3>", unsafe_allow_html=True)
            st.markdown(
                f"""
                <p style="font-size: 1.1rem; line-height: 1.7; text-align: justify; opacity: 0.9;">
                The first turning point of my life was when I found my sister's book on web development for her computer subject in junior high school. 
                The book was simple, merely touching upon creating HTML websites with Notepad, but that was enough to light a flame. 
                Ever since then, I have been exploring the world of creation—developing games, crafting websites, drawing, and writing.
                This was the official start of my journey.
                </p>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown(f"<hr style='border-color: {CARD_BORDER}; margin: 1.5rem 0;'></hr>", unsafe_allow_html=True)
            
            # Profile Details Table
            st.markdown(
                f"""
                <table style="border: none; background: transparent; width: 100%; font-size: 1.1rem;">
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold; width: 35%;">School:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Cebu Institute of Technology – University</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Program & Year:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">BS Computer Science – 3rd Year – F1</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Birthdate:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">August 8, 2006</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Nationality:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Filipino</td>
                    </tr>
                </table>
                """,
                unsafe_allow_html=True
            )

        with col_img:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            try:
                st.image("images/Hertz.jpg", width="content")
            except Exception:
                st.info("💡 Place your photo in `images/Hertz.jpg`")
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Len.icon":
    with st.container():
        col_text, col_img = st.columns([2, 1], gap="large")

        with col_text:
            st.title("🟡 Len.icon")
            st.markdown(f"<h3 style='color: {PRIMARY_COLOR}; margin-top: 0;'>You can call me <em>Len</em>, but I'd rather be <em>Yours</em> 💞</h3>", unsafe_allow_html=True)
            st.markdown(
                f"""
                <p style="font-size: 1.1rem; line-height: 1.7; text-align: justify; opacity: 0.9;">
                The second turning point of my life was trying to find my name. I thought of "Len.icon" when I was thinking of a Subeta username at midnight. It started from "Lincoln" to "Lencon" to "Len.ico" to now.
                </p>
                <p style="font-size: 1.1rem; line-height: 1.7; text-align: justify; opacity: 0.9;">
                My academics were fairly average. I was stupid, yes, but just the right amount of it, mixed with genius and creativity. I could keep up with classes and I'm pretty decent at adapting to the skill level of my classmates. Often behind, yes, but still over the line. I mean, come on now, I'm competing against Einstein and Tesla over here.  
                </p>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"<hr style='border-color: {CARD_BORDER}; margin: 1.5rem 0;'></hr>", unsafe_allow_html=True)
            
            st.markdown(
                f"""
                <table style="border: none; background: transparent; width: 100%; font-size: 1.1rem;">
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold; width: 25%;">Height:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Enough to see your pretty face</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Weight:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Enough to fit in your heart</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Hobbies:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Brawlhalla, Imagining, Programming</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Yummers:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Corned Beef, Monggo Soup, Rice</td>
                    </tr>
                    <tr style="border: none; background: transparent;">
                        <td style="border: none; padding: 8px 16px 8px 0; font-weight: bold;">Yuckers:</td>
                        <td style="border: none; color: {PRIMARY_COLOR}; font-weight: 600;">Eggplant, Togue, Slime</td>
                    </tr>
                </table>
                """,
                unsafe_allow_html=True
            )

        with col_img:
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            try:
                st.image("images/Len.png", width="content")
            except Exception:
                st.info("💡 Place your photo in `images/Len.png`")
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Projects":
    with st.container():
        st.title("Projects")
        
        # Category Tabs / Subsections
        proj_tab1, proj_tab2, proj_tab3 = st.tabs(["Game Development", "Applications and Websites", "Tools and Utilities"])
        
        with proj_tab2:
            st.markdown("### Applications and Websites")
            projects_web = [
                ("Assesser", "A site where you can make tests with anti-cheat. Requested by father for midterms. Made with NextJS, Firebase Hosting, and Supabase.", "https://assesser.web.app"),
                ("Len.icon", "Portfolio website showcasing 3D modeling and development. Made with NextJS, Firebase Hosting, and ThreeJS.", "https://lenicondev.web.app"),
                ("DaisieDex", "An app where you can scan plants and give them nicknames and a story. Made with Flutter.", "https://github.com/Lenicon/daisiedex"),
                ("Town of Bogmoore", "Frog people and weird stuff website created for birthday. Made with React, Typescript, and Firebase Hosting.", "https://town-of-bogmoore.web.app/"),
                ("Friend.ly", "A messaging site where you anonymously make friends in school (USC). Research thesis project. Made with React, Typescript, and Firebase Hosting.", "https://friendly-23d49.web.app/")
            ]
            for name, desc, link in projects_web:
                with st.container(border=True):
                    st.markdown(f"#### [{name}]({link})")
                    st.write(desc)
                    
        with proj_tab3:
            st.markdown("### Tools and Utilities")
            projects_tools = [
                ("Godot DAT Editor", "Tool where you can easily modify and view save (.DAT) files for testing in Godot. Made for SWYN 1.0.", "https://lenicon.itch.io/gdat-edit"),
                ("Trash Toolbox", "A collection of weekly tools created during a content creator challenge.", "https://trash-toolbox.web.app/")
            ]
            for name, desc, link in projects_tools:
                with st.container(border=True):
                    st.markdown(f"#### [{name}]({link})")
                    st.write(desc)
                    
        with proj_tab1:
            st.markdown("### Game Development")
            projects_games = [
                ("Mean Unicorns Sing In Chiptune", "A 13kb rhythm-dodging game with 4 songs made with HTML, CSS, JS for js13kGames 2026.", "https://js13kgames.com/2026/games/mean-unicorns-sing-in-chiptune"),
                ("Dating.data", "A blind date between two faulty robots with dialogue interpreter in Godot 4 for Wavedash Game Jam.", "https://wavedash.com/games/dating-data"),
                ("DROPSWEEPER", "A roguelite x minesweeper game with cute characters made with Godot 4 for Comfy Jam: Spring.", "https://lenicon.itch.io/dropsweeper"),
                ("SWYN 1.0", "A pig game about ideas that ranked #1 in Audio. Made with Godot 4 for the Oink Jam.", "https://lenicon.itch.io/swyn"),
                ("SPEEDBUN", "Burgers in 20 seconds experiment with vector art. Made with Godot 4 for 20 Second Game Jam 2025.", "https://lenicon.itch.io/speedbun"),
                ("KAMPILAN", "Boss rush with Filipino mythical creatures. Team jam winner made with Godot 4 for Sugbuanon Saga 2025.", "https://lenicon.itch.io/kampilan"),
                ("Light Blue", "Short date with Bluey featuring custom visual novel system made with Godot 3 for NaNoRenO 2023.", "https://lenicon.itch.io/light-blue"),
                ("Kairos", "Dungeon game where you can pause time, featuring first boss fight and state machines in Godot 3.", "https://lenicon.itch.io/kairos"),
                ("Overchrome", "Game where you switch bodies with a robot by shooting your heart. Made with GDevelop.", "https://lenicon.itch.io/overchrome"),
                ("Bogware", "Warioware-type game with a hacker made with GDevelop Weekend Jam #1.", "https://lenicon.itch.io/bogware"),
                ("Switch, Shoot, & Jump", "Switch between dark and light backgrounds to solve puzzles made with CT.js.", "https://lenicon.itch.io/switch-shoot-jump"),
                ("My Best Friend's Birthday", "Make a cupcake and buy flowers for your best friend's birthday. Made with Ren'Py.", "https://lenicon.itch.io/mbfbday"),
                ("SP LIT", "First ever game uploaded online and first game jam made with Gamemaker.", "https://lenicon.itch.io/sp-lit")
            ]
            for name, desc, link in projects_games:
                with st.container(border=True):
                    st.markdown(f"#### [{name}]({link})")
                    st.write(desc)
                    
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Skills":
    with st.container():
        st.title("Skills and Experience")
        st.markdown(f"<h3 style='color: {PRIMARY_COLOR}; margin-top: 0;'>Monthly meters of experience in different tools and engines</h3>", unsafe_allow_html=True)
        st.markdown(f"<hr style='border-color: {CARD_BORDER}; margin: 1.5rem 0;'></hr>", unsafe_allow_html=True)
        
        
        # Skill experience dataset (months and target max of 72 months)
        max_mo = 100
        skills_data = [
            {"skill": "Godot & GDScript", "months": 80, "max": max_mo},
            {"skill": "HTML / CSS / JS", "months": 50, "max": max_mo},
            {"skill": "React & Next.js", "months": 50, "max": max_mo},
            {"skill": "TypeScript", "months": 50, "max": max_mo},
            {"skill": "Python", "months": 12, "max": max_mo},
            {"skill": "Flutter & Dart", "months": 12, "max": max_mo},
        ]

        # Helper function to render a SVG circular progress ring
        def render_circular_bar(title, months, max_months=72):
            percent = min(months / max_months, 1.0)
            radius = 36
            circumference = 2 * 3.14159 * radius
            dashoffset = circumference * (1 - percent)
            
            return f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem; background-color: {BG_COLOR}; border: 1px solid {CARD_BORDER}; border-radius: 16px;">
                <div style="position: relative; width: 100px; height: 100px;">
                    <svg width="100" height="100" viewBox="0 0 100 100" style="transform: rotate(-90deg);">
                        <!-- Background Circle Track -->
                        <circle cx="50" cy="50" r="{radius}" stroke="{CARD_BORDER}" stroke-width="8" fill="none" />
                        <!-- Progress Circle Ring -->
                        <circle cx="50" cy="50" r="{radius}" stroke="{PRIMARY_COLOR}" stroke-width="8" stroke-dasharray="{circumference}" stroke-dashoffset="{dashoffset}" stroke-linecap="round" fill="none" style="transition: stroke-dashoffset 0.5s ease;" />
                    </svg>
                    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <span style="font-weight: 700; font-size: 1.1rem; color: {TEXT_COLOR};">{months}mo</span>
                    </div>
                </div>
                <span style="margin-top: 0.75rem; font-weight: 600; font-size: 0.95rem; color: {TEXT_COLOR}; text-align: center;">{title}</span>
            </div>
            """

        # Display skills in a clean 3-column grid layout
        cols = st.columns(3)
        for idx, item in enumerate(skills_data):
            with cols[idx % 3]:
                st.markdown(render_circular_bar(item["skill"], item["months"], item["max"]), unsafe_allow_html=True)
                st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    with st.container():
        st.title("Contact")
        st.markdown(f"<h3 style='color: {PRIMARY_COLOR}; margin-top: 0;'>Get in touch or leave feedback!</h3>", unsafe_allow_html=True)
        st.markdown(f"<hr style='border-color: {CARD_BORDER}; margin: 1.5rem 0;'></hr>", unsafe_allow_html=True)
        
        # Interactive contact form with session state response handling
        if "form_submitted" not in st.session_state:
            st.session_state.form_submitted = False

        if not st.session_state.form_submitted:
            with st.form("contact_form"):
                sender_name = st.text_input("Your Name")
                sender_email = st.text_input("Your Email")
                message_type = st.selectbox("Inquiry Type", ["General Inquiry", "Collaboration / Project", "Feedback", "Just Saying Hi!"])
                message_body = st.text_area("Your Message")
                
                submitted = st.form_submit_button("Send Message &nbsp; ➤")
                if submitted:
                    if sender_name and sender_email and message_body:
                        st.session_state.form_submitted = True
                        st.session_state.sender_name = sender_name
                        st.rerun()
                    else:
                        st.error("Please fill out all required fields before submitting.")
        else:
            st.success(f"Thank you, {st.session_state.get('sender_name', 'friend')}! Your message has been sent successfully. I'll get back to you soon!")
            if st.button("Send Another Message"):
                st.session_state.form_submitted = False
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)