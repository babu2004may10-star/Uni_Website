import html
import re

import streamlit as st

st.set_page_config(
    page_title="Northbridge University",
    page_icon="assets/favicon.svg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PAGES = ["Discover", "Study", "Admissions", "Campus life", "Research & news", "Visit"]

PROGRAMMES = [
    {
        "title": "Artificial Intelligence & Society",
        "level": "Undergraduate",
        "school": "Science & Engineering",
        "award": "BSc · 3 years",
        "summary": "Build intelligent systems — and understand their impact on people.",
        "description": "Examine how intelligent systems shape the way we live, work, and make decisions. Build technical confidence while exploring the ethical, social, and human questions at the heart of AI.",
        "careers": "AI researcher, product analyst, responsible technology consultant",
        "requirements": "A-levels: ABB or equivalent, including Mathematics or Computer Science.",
        "number": "01",
    },
    {
        "title": "Visual Communication",
        "level": "Undergraduate",
        "school": "Arts & Humanities",
        "award": "BA · 3 years",
        "summary": "Make ideas visible through design, image, and story.",
        "description": "Develop a distinct creative voice through typography, image-making, digital media, and storytelling. Work on live briefs with cultural organisations and design studios.",
        "careers": "Graphic designer, brand strategist, editorial designer, creative director",
        "requirements": "A-levels: BBC or equivalent. A portfolio of creative work is required.",
        "number": "02",
    },
    {
        "title": "Environmental Science",
        "level": "Undergraduate",
        "school": "Science & Engineering",
        "award": "BSc · 3 years",
        "summary": "Read the planet. Design a more resilient future.",
        "description": "Investigate the systems that sustain our planet through fieldwork, laboratory research, and data analysis. Learn to turn environmental evidence into action.",
        "careers": "Environmental scientist, conservation officer, climate analyst",
        "requirements": "A-levels: ABB or equivalent, including one science subject.",
        "number": "03",
    },
    {
        "title": "International Relations",
        "level": "Undergraduate",
        "school": "Arts & Humanities",
        "award": "BA · 3 years",
        "summary": "Understand power, place, and the possibilities for change.",
        "description": "Follow the forces shaping our world — from diplomacy and trade to migration and global justice. Spend a semester studying with one of our international partners.",
        "careers": "Policy analyst, diplomat, campaign strategist, journalist",
        "requirements": "A-levels: BBB or equivalent, including an essay-based subject.",
        "number": "04",
    },
    {
        "title": "Sustainable Engineering",
        "level": "Undergraduate",
        "school": "Science & Engineering",
        "award": "BEng · 4 years",
        "summary": "Build the systems a changing world depends on.",
        "description": "Design infrastructure, materials, and energy systems for a low-carbon world. Combine engineering fundamentals with hands-on projects and a year in industry.",
        "careers": "Renewable energy engineer, design engineer, sustainability consultant",
        "requirements": "A-levels: ABB or equivalent, including Mathematics and a science subject.",
        "number": "05",
    },
    {
        "title": "Psychology",
        "level": "Undergraduate",
        "school": "Business & Society",
        "award": "BSc · 3 years",
        "summary": "Study the mind — and what makes us human.",
        "description": "Explore the science of mind and behaviour through research methods, cognitive psychology, and real-world application. Our labs give you direct experience of psychological research.",
        "careers": "Clinical trainee, researcher, behavioural analyst, human resources",
        "requirements": "A-levels: ABB or equivalent, including one science or social science subject.",
        "number": "06",
    },
    {
        "title": "Climate Data Science",
        "level": "Postgraduate",
        "school": "Science & Engineering",
        "award": "MSc · 1 year",
        "summary": "Use data to help the world adapt and thrive.",
        "description": "Turn complex climate data into decisions that matter. Blend data science, climate modelling, and policy analysis in a programme built around real public-sector projects.",
        "careers": "Climate data scientist, environmental modeller, policy researcher",
        "requirements": "A 2:1 honours degree in a numerate subject or equivalent professional experience.",
        "number": "07",
    },
    {
        "title": "Design for Social Impact",
        "level": "Postgraduate",
        "school": "Arts & Humanities",
        "award": "MA · 1 year",
        "summary": "Create with purpose, alongside communities.",
        "description": "Use design to challenge inequality and create meaningful change. Work alongside community partners on projects that address real social needs.",
        "careers": "Service designer, design researcher, social innovation lead",
        "requirements": "A 2:1 honours degree or equivalent experience. A portfolio and project proposal are required.",
        "number": "08",
    },
    {
        "title": "Responsible Business",
        "level": "Postgraduate",
        "school": "Business & Society",
        "award": "MBA · 2 years part-time",
        "summary": "Lead organisations that work for people and planet.",
        "description": "Lead with clarity in a complex world. Our part-time MBA connects strategy, ethics, and systems thinking so you can create value that lasts.",
        "careers": "Operations leader, sustainability director, strategy consultant",
        "requirements": "An honours degree and three years of relevant professional experience.",
        "number": "09",
    },
]

STORIES = [
    {
        "key": "climate-centre",
        "type": "Campus · 12 November 2026",
        "date": "12 November 2026",
        "category": "Campus",
        "title": "Our new Centre for Climate Innovation opens its doors",
        "summary": "A collaborative space bringing researchers, students, and local partners together to prototype a more resilient future.",
        "image": "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=900&q=85",
        "body": [
            "The Centre for Climate Innovation has opened on the eastern edge of campus, creating a shared home for climate research, teaching, and public engagement.",
            "Its first programme brings together environmental scientists, engineers, designers, and community organisations to test practical responses to rising temperatures and changing weather patterns.",
            "Students will have access to live projects, specialist laboratories, and a public events space designed to make research visible and useful beyond the university.",
        ],
    },
    {
        "key": "inclusive-campus",
        "type": "Student life · 5 November 2026",
        "date": "5 November 2026",
        "category": "Student life",
        "title": "Meet the students building a more inclusive campus",
        "summary": "How a student-led accessibility project is changing the way we design spaces, services, and everyday experiences.",
        "image": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=900&q=85",
        "body": [
            "A group of students has spent the past year auditing the places where campus life happens — from lecture halls and libraries to social spaces and digital services.",
            "Their report combines lived experience with practical recommendations, including clearer wayfinding, quieter study areas, and more flexible ways to take part in events.",
            "The university is now working with the team to put the first recommendations into practice, with student involvement continuing throughout the process.",
        ],
    },
    {
        "key": "northbridge-medal",
        "type": "Community · 28 October 2026",
        "date": "28 October 2026",
        "category": "Community",
        "title": "Northbridge graduates recognised for community impact",
        "summary": "Three alumni receive this year’s Northbridge Medal for work in public health, education, and environmental justice.",
        "image": "https://images.unsplash.com/photo-1523580846011-d3a5bc25702b?auto=format&fit=crop&w=900&q=85",
        "body": [
            "The annual Northbridge Medal recognises graduates whose work has made a lasting difference to communities beyond the university.",
            "This year’s recipients have helped expand access to public health support, built new learning opportunities for young people, and campaigned for cleaner, safer neighbourhoods.",
            "They were honoured at a ceremony on campus, where students also presented projects developed through the university’s community partnership programme.",
        ],
    },
]


def go_to(page):
    st.session_state.nav = page


def brand_mark():
    return """
    <svg viewBox="0 0 46 46" aria-hidden="true">
      <path d="M3 38V20L23 4l20 16v18H3Z" fill="none" stroke="currentColor" stroke-width="2.4"/>
      <path d="M15 38V24.5L23 18l8 6.5V38M20 38V30h6v8M12 11V4h6v3.2" fill="none" stroke="currentColor" stroke-width="2.4"/>
    </svg>
    """


def render_header():
    st.markdown(
        f"""
        <div class="announcement">
          <span><i></i> Applications for Autumn 2027 are now open</span>
          <span>Open day · Saturday 23 January 2027 <b>→</b></span>
        </div>
        <div class="brandbar">
          <div class="brand">
            <span class="brand-mark">{brand_mark()}</span>
            <span class="brand-name">Northbridge<small>University</small></span>
          </div>
          <div class="brand-utility">Where curiosity finds direction</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_nav():
    st.radio(
        "Primary navigation",
        PAGES,
        horizontal=True,
        key="nav",
        label_visibility="collapsed",
    )


def section_eyebrow(text):
    return f'<p class="eyebrow"><span></span>{html.escape(text)}</p>'


def render_home():
    st.markdown(
        f"""
        <section class="hero">
          <div class="hero-copy">
            {section_eyebrow("A different kind of university")}
            <h1>Where curiosity<br>finds <em>direction.</em></h1>
            <p class="lede">At Northbridge, you will learn with people who ask better questions, test bold ideas, and turn knowledge into lasting change.</p>
            <div class="hero-proof">
              <strong>Join a community of 8,400</strong>
              <span>thinkers, makers, and doers.</span>
            </div>
          </div>
          <div class="hero-visual">
            <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1400&q=85" alt="Historic university building framed by trees and a lawn">
            <span class="hero-stamp">Est.<br>1964</span>
            <div class="open-day">
              <p>Meet us on campus</p>
              <div class="open-day-row">
                <div class="open-day-date">Sat<br><strong>23</strong><br>Jan</div>
                <div>
                  <strong>Undergraduate Open Day</strong>
                  <small>10:00–15:00 · Northbridge Campus</small>
                </div>
              </div>
            </div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    hero_buttons = st.columns([1, 1, 2.3])
    with hero_buttons[0]:
        st.button("Explore programmes →", type="primary", use_container_width=True, on_click=go_to, args=("Study",))
    with hero_buttons[1]:
        st.button("Book a campus visit", use_container_width=True, on_click=go_to, args=("Visit",))

    st.markdown(
        """
        <div class="quick-grid">
          <div class="quick"><span>01</span><strong>Programmes</strong><small>Find your course</small></div>
          <div class="quick"><span>02</span><strong>Fees &amp; funding</strong><small>Invest in your future</small></div>
          <div class="quick"><span>03</span><strong>Accommodation</strong><small>Make yourself at home</small></div>
          <div class="quick"><span>04</span><strong>What’s on</strong><small>Events and open days</small></div>
        </div>

        <section class="section about-section">
          <div class="split-heading">
            <div>
              <p class="eyebrow"><span></span>Why Northbridge</p>
              <h2>Big ideas need<br><em>room to grow.</em></h2>
            </div>
            <div class="body-copy">
              <p>We bring together different disciplines, perspectives, and lived experiences. Here, you will be challenged to think independently — and supported to go further than you thought possible.</p>
              <p>Our teaching is personal, our research is purposeful, and our community is built on the belief that the best answers come from asking together.</p>
            </div>
          </div>
          <div class="about-grid">
            <figure class="about-photo">
              <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=85" alt="Students talking together outside a campus building">
              <figcaption>Learn in a community that knows your name.</figcaption>
            </figure>
            <div class="about-side">
              <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=900&q=85" alt="Students collaborating around a table in a bright studio">
              <div class="stat-card">
                <p>A place to belong</p>
                <strong>80+</strong>
                <span>student-led clubs and societies</span>
              </div>
            </div>
          </div>
          <div class="stats">
            <div><strong>12<em>:1</em></strong><span>Student-to-staff ratio</span></div>
            <div><strong>38</strong><span>Degree programmes</span></div>
            <div><strong>64</strong><span>Countries represented</span></div>
            <div><strong>92<em>%</em></strong><span>Graduates in work or study</span></div>
          </div>
        </section>

        <section class="dark-band">
          <p class="eyebrow light"><span></span>Study at Northbridge</p>
          <div class="dark-heading">
            <h2>Find the subject<br>that moves <em>you.</em></h2>
            <p>From climate science to creative technology, our programmes are designed for a world that needs new ways of thinking.</p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    home_programmes = st.columns([1, 1, 2.4])
    with home_programmes[0]:
        st.button("Browse all programmes →", type="primary", use_container_width=True, on_click=go_to, args=("Study",))

    st.markdown(
        """
        <section class="coral-band">
          <div>
            <p class="eyebrow light"><span></span>Come and see</p>
            <h2>Your future<br>feels <em>different</em><br>up close.</h2>
          </div>
          <div class="coral-band-copy">
            <p>Join us on campus for an open day, a campus tour, or a one-to-one conversation with our admissions team.</p>
            <p class="address">8 Wrenfield Avenue<br>Northbridge NB2 6QS<br><a href="mailto:hello@northbridge.example">hello@northbridge.example</a></p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    visit_button = st.columns([1, 3])
    with visit_button[0]:
        st.button("Plan your visit →", type="primary", use_container_width=True, on_click=go_to, args=("Visit",))


def programme_card(programme, index):
    safe_title = html.escape(programme["title"])
    safe_school = html.escape(programme["school"])
    safe_summary = html.escape(programme["summary"])
    safe_award = html.escape(programme["award"])
    with st.container(border=True):
        st.markdown(
            f"""
            <article class="programme-card">
              <div class="programme-top"><span>{safe_award}</span><i>{programme["number"]}</i></div>
              <p class="programme-school">{safe_school}</p>
              <h3>{safe_title}</h3>
              <p>{safe_summary}</p>
            </article>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore programme →", key=f"programme-{index}", use_container_width=True):
            show_programme_dialog(programme)


@st.dialog("Programme details", width="large")
def show_programme_dialog(programme):
    st.caption(f"{programme['school']} · {programme['award']}")
    st.markdown(f"## {programme['title']}")
    st.write(programme["description"])
    st.markdown("**Entry requirements**")
    st.write(programme["requirements"])
    st.markdown("**Career pathways**")
    st.write(programme["careers"])
    st.caption("Demonstration programme information for this website concept.")


def clear_study_filters():
    st.session_state.study_search = ""
    st.session_state.study_level = "All levels"
    st.session_state.study_school = "All schools"


def render_study():
    st.markdown(
        f"""
        <section class="page-header dark">
          {section_eyebrow("Study at Northbridge")}
          <h1>Find the subject<br>that moves <em>you.</em></h1>
          <p>From climate science to creative technology, our programmes are designed for a world that needs new ways of thinking.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    filters = st.columns([1.5, 1.1, 1], gap="medium")
    with filters[0]:
        search = st.text_input(
            "Search by subject or keyword",
            key="study_search",
            placeholder="Try “climate”, “design”, or “psychology”",
        )
    with filters[1]:
        level = st.segmented_control(
            "Study level",
            ["All levels", "Undergraduate", "Postgraduate"],
            default="All levels",
            key="study_level",
        )
    with filters[2]:
        school = st.selectbox(
            "School",
            ["All schools", "Arts & Humanities", "Business & Society", "Science & Engineering"],
            key="study_school",
        )

    query = (search or "").strip().lower()
    results = []
    for programme in PROGRAMMES:
        searchable = f"{programme['title']} {programme['school']} {programme['summary']}".lower()
        matches_search = not query or query in searchable
        matches_level = not level or level == "All levels" or programme["level"] == level
        matches_school = school == "All schools" or programme["school"] == school
        if matches_search and matches_level and matches_school:
            results.append(programme)

    meta = st.columns([4, 1])
    with meta[0]:
        noun = "programme" if len(results) == 1 else "programmes"
        st.caption(f"Showing {len(results)} of {len(PROGRAMMES)} {noun}")
    with meta[1]:
        if st.button("Clear filters", use_container_width=True, on_click=clear_study_filters):
            pass

    if not results:
        st.info("No programmes match your search. Try a broader term or clear the filters.")
        return

    for start in range(0, len(results), 3):
        row = results[start:start + 3]
        columns = st.columns(3, gap="medium")
        for column, programme in zip(columns, row):
            with column:
                programme_card(programme, PROGRAMMES.index(programme))

    st.markdown(
        """
        <div class="note-panel">
          <div><strong>Not sure which programme is right for you?</strong><span>Our admissions team can help you compare your options.</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cta = st.columns([1, 3])
    with cta[0]:
        st.button("Talk to admissions →", type="primary", use_container_width=True, on_click=go_to, args=("Visit",))


def render_admissions():
    st.markdown(
        f"""
        <section class="page-header cream">
          {section_eyebrow("Admissions")}
          <h1>Your next chapter<br>starts with a <em>first step.</em></h1>
          <p class="wide-copy">We look for curiosity, resilience, and the potential to make a difference — not just a set of grades. Find everything you need to apply with confidence.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([0.9, 1.1], gap="large")
    with left:
        st.markdown(
            """
            <div class="admissions-visual">
              <img src="https://images.unsplash.com/photo-1571260899304-425eee4c7efc?auto=format&fit=crop&w=1000&q=85" alt="Student reviewing notes with a laptop at a library table">
              <div class="deadline">
                <p>Next application deadline</p>
                <strong>5 February <em>2027</em></strong>
                <span>Applications for Autumn 2027 close at 23:59.</span>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.button("Start your application →", type="primary", use_container_width=True, on_click=go_to, args=("Visit",))
    with right:
        with st.expander("01  Explore your options", expanded=True):
            st.write("Compare programmes, meet our academics, and get a feel for life at Northbridge. Our admissions team can help you weigh up your choices.")
            st.markdown("- Book an open day or campus tour\n- Review entry requirements for your programme\n- Check fees, funding, and scholarship options")
        with st.expander("02  Prepare your application"):
            st.write("You will need your academic transcripts, a personal statement, and one academic reference. Some programmes also ask for a portfolio or interview.")
            st.markdown("- Personal details and education history\n- A 500-word statement about your interests\n- Supporting documents and references")
        with st.expander("03  Submit and connect"):
            st.write("Submit your application online. You can track its progress, upload documents, and message our team through your applicant portal.")
            st.markdown("- Application fee: £55\n- Decisions within four to six weeks\n- Scholarship consideration is automatic")
        with st.expander("Fees, scholarships, and financial support"):
            st.write("Northbridge offers scholarships, bursaries, and flexible payment plans. The figures below are demonstration content.")
            st.markdown("- **Undergraduate tuition:** £9,250 per year for UK students\n- **Postgraduate tuition:** From £21,500 for a full master’s programme\n- **Northbridge Opportunity Award:** Means-tested awards of up to £8,000 per year")

    st.markdown(
        """
        <div class="note-panel step-note">
          <div><strong>Cost should not decide your future.</strong><span>Explore scholarships, bursaries, and flexible payment plans with our team.</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_campus():
    st.markdown(
        f"""
        <section class="page-header">
          {section_eyebrow("Life at Northbridge")}
          <h1>More than a place<br>to <em>study.</em></h1>
          <p class="wide-copy">Our campus is a neighbourhood of ideas, friendships, and late-night conversations. Come as you are — and find your people.</p>
        </section>
        <div class="campus-grid">
          <figure class="campus-main">
            <img src="https://images.unsplash.com/photo-1519452635265-7b1fbfd1e4e0?auto=format&fit=crop&w=1200&q=85" alt="Students walking past historic university buildings">
            <figcaption><span>01</span> A campus with room to breathe</figcaption>
          </figure>
          <figure>
            <img src="https://images.unsplash.com/photo-1523580494863-6f3031224c94?auto=format&fit=crop&w=900&q=85" alt="Graduates celebrating together outdoors">
            <figcaption><span>02</span> Traditions worth making</figcaption>
          </figure>
          <figure>
            <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?auto=format&fit=crop&w=900&q=85" alt="Students in conversation during a seminar">
            <figcaption><span>03</span> Ideas shared face to face</figcaption>
          </figure>
          <div class="campus-quote">
            <blockquote>“I came for the course. I stayed for the people who made me feel like I belonged.”</blockquote>
            <p><strong>Maya Chen</strong><br>BA International Relations, 2026</p>
          </div>
        </div>
        <div class="campus-features">
          <div><span>01</span><h3>Find your community</h3><p>From filmmaking to birdwatching, our 80+ societies are a place to try something new and meet people who share your curiosity.</p></div>
          <div><span>02</span><h3>A home on campus</h3><p>Guaranteed accommodation for first-year students, with lived-in common spaces, cooking facilities, and support close by.</p></div>
          <div><span>03</span><h3>Support that stays</h3><p>Dedicated wellbeing, accessibility, and financial advisers are here from your first day to graduation and beyond.</p></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    campus_cta = st.columns([1, 3])
    with campus_cta[0]:
        st.button("Visit our campus →", type="primary", use_container_width=True, on_click=go_to, args=("Visit",))


@st.dialog("Northbridge story", width="large")
def show_story_dialog(story):
    st.caption(story["type"])
    st.markdown(f"## {story['title']}")
    st.write(story["summary"])
    for paragraph in story["body"]:
        st.write(paragraph)
    st.caption("Demonstration story for this website concept.")


def render_research():
    st.markdown(
        f"""
        <section class="research-hero">
          <div>
            {section_eyebrow("Research with purpose")}
            <h1>Questions today.<br>Impact <em>tomorrow.</em></h1>
            <p>Our research crosses disciplines and borders to address the challenges that matter most. From climate resilience to responsible technology, we work with communities to turn knowledge into real-world change.</p>
            <div class="research-stats"><p><strong>12</strong><span>research centres</span></p><p><strong>340</strong><span>active projects</span></p></div>
          </div>
          <figure class="research-feature">
            <img src="https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=1100&q=85" alt="Sunlit library reading room with tall bookshelves">
            <figcaption>
              <span>Featured project · Climate &amp; Society</span>
              <h3>Designing cities for a warmer future</h3>
              <p>A five-year study working with local councils to make urban neighbourhoods cooler, greener, and more liveable.</p>
            </figcaption>
          </figure>
        </section>
        <section class="news-section">
          {section_eyebrow("News & ideas")}
          <div class="split-heading news-heading"><h2>What’s happening<br>at <em>Northbridge.</em></h2><p>Stories from our community of researchers, students, and partners.</p></div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    for start in range(0, len(STORIES), 3):
        row = STORIES[start:start + 3]
        columns = st.columns(3, gap="medium")
        for column, story in zip(columns, row):
            with column:
                with st.container(border=True):
                    st.markdown(
                        f"""
                        <article class="news-card">
                          <div class="news-image"><img src="{story["image"]}" alt=""><span>{html.escape(story["category"])}</span></div>
                          <p class="news-meta">{story["date"]} · 3 min read</p>
                          <h3>{html.escape(story["title"])}</h3>
                          <p>{html.escape(story["summary"])}</p>
                        </article>
                        """,
                        unsafe_allow_html=True,
                    )
                    if st.button("Read story →", key=f"story-{story['key']}", use_container_width=True):
                        show_story_dialog(story)

    st.markdown(
        """
        <section class="events-section">
          <div class="events-heading">
            <p class="eyebrow"><span></span>Upcoming events</p>
            <h2>On campus</h2>
          </div>
          <div class="event-list">
            <div class="event"><div class="event-date"><span>Nov</span><strong>21</strong></div><div><p>Open day · Undergraduate</p><h3>Discover Northbridge</h3><span>10:00–14:00 · Northbridge Campus</span></div></div>
            <div class="event"><div class="event-date"><span>Dec</span><strong>03</strong></div><div><p>Public lecture · Climate</p><h3>Living with a changing planet</h3><span>18:30–20:00 · Wren Hall</span></div></div>
            <div class="event"><div class="event-date"><span>Dec</span><strong>11</strong></div><div><p>Portfolio evening · Arts</p><h3>Make. Show. Tell.</h3><span>17:00–20:00 · Studio North</span></div></div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    event_cta = st.columns([1, 3])
    with event_cta[0]:
        st.button("Book an open day →", type="primary", use_container_width=True, on_click=go_to, args=("Visit",))


def render_visit():
    st.markdown(
        f"""
        <section class="page-header cream">
          {section_eyebrow("Come and see")}
          <h1>Your future feels<br><em>different</em> up close.</h1>
          <p class="wide-copy">Join us on campus for an open day, a campus tour, or a one-to-one conversation with our admissions team.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    contact_col, form_col = st.columns([0.8, 1.15], gap="large")
    with contact_col:
        st.markdown(
            """
            <div class="contact-details">
              <div><h3>Visit us</h3><p>Northbridge University<br>8 Wrenfield Avenue<br>Northbridge NB2 6QS</p></div>
              <div><h3>Talk to us</h3><p><a href="mailto:hello@northbridge.example">hello@northbridge.example</a><br><a href="tel:+442079460164">+44 (0)20 7946 0164</a></p></div>
              <div><h3>Open day</h3><p>Saturday 23 January 2027<br>10:00–15:00</p></div>
            </div>
            <div class="map-card">
              <span>Northbridge campus</span>
              <strong>8 Wrenfield Avenue</strong>
              <p>Ten minutes from Northbridge station, with direct trains from the city centre.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with form_col:
        st.markdown(
            """
            <div class="form-heading">
              <h2>Book a visit</h2>
              <p>Tell us a little about yourself and we’ll be in touch.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("visit_form", clear_on_submit=True):
            name = st.text_input("Full name")
            email = st.text_input("Email address")
            interest = st.selectbox(
                "What would you like to explore?",
                ["Select an option", "Undergraduate study", "Postgraduate study", "Research and partnerships", "Campus visit or open day"],
            )
            message = st.text_area("Anything you’d like us to know? (optional)", height=100)
            consent = st.checkbox("I agree to the privacy notice for this demonstration form.")
            submitted = st.form_submit_button("Request a visit →", type="primary", use_container_width=True)

        if submitted:
            errors = []
            if len(name.strip()) < 2:
                errors.append("Please enter your name.")
            if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$", email.strip()):
                errors.append("Enter a valid email address.")
            if interest == "Select an option":
                errors.append("Please select what you would like to explore.")
            if not consent:
                errors.append("Please agree to the privacy notice.")
            if errors:
                st.error("Please check the following:\n\n" + "\n".join(f"- {error}" for error in errors))
            else:
                st.success("Thank you — your request is ready. This demonstration form has not sent or stored any data.")
                st.info(f"A real visit request for {name.strip()} would now be sent to the admissions team.")


def render_footer():
    st.markdown(
        """
        <footer class="site-footer">
          <div>
            <div class="footer-brand">
              <span class="brand-mark">
                <svg viewBox="0 0 46 46" aria-hidden="true">
                  <path d="M3 38V20L23 4l20 16v18H3Z" fill="none" stroke="currentColor" stroke-width="2.4"/>
                  <path d="M15 38V24.5L23 18l8 6.5V38M20 38V30h6v8M12 11V4h6v3.2" fill="none" stroke="currentColor" stroke-width="2.4"/>
                </svg>
              </span>
              <span class="brand-name">Northbridge<small>University</small></span>
            </div>
            <p class="footer-tagline">Where curiosity finds direction.</p>
            <p class="footer-address">8 Wrenfield Avenue<br>Northbridge NB2 6QS<br><a href="mailto:hello@northbridge.example">hello@northbridge.example</a></p>
          </div>
          <div><h3>Study</h3><p>Undergraduate<br>Postgraduate<br>Admissions<br>Fees &amp; funding</p></div>
          <div><h3>University</h3><p>About us<br>Research<br>Campus life<br>News &amp; events</p></div>
          <div><h3>Visit</h3><p>Open days<br>Campus tours<br>Contact us<br>Accessibility</p></div>
        </footer>
        <div class="footer-bottom">
          <span>© 2026 Northbridge University. A fictional university created for this website concept.</span>
          <span>Built with Streamlit · Demonstration content only</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Manrope:wght@400;500;600;700&display=swap');

      :root {
        --ink: #17332f;
        --ink-deep: #102825;
        --ink-soft: #3d594f;
        --muted: #55675f;
        --cream: #f3efe5;
        --paper: #fbf9f3;
        --white: #fffdf8;
        --coral: #dd6546;
        --coral-deep: #b8432a;
        --lime: #dceaab;
        --line: rgba(23, 51, 47, 0.17);
        --serif: "Fraunces", Georgia, "Times New Roman", serif;
        --sans: "Manrope", "Helvetica Neue", Arial, sans-serif;
      }

      html, body, [class*="css"], .stApp, button, input, select, textarea {
        font-family: var(--sans) !important;
      }

      .stApp { background: var(--paper); color: var(--ink); }
      [data-testid="stHeader"] { display: none; }
      [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }
      [data-testid="stAppViewContainer"] > .main { background: var(--paper); }
      [data-testid="stMainBlockContainer"] {
        width: min(100% - 3rem, 1240px) !important;
        max-width: 1240px !important;
        padding: 0 0 2rem !important;
        margin-inline: auto;
      }
      [data-testid="stVerticalBlock"] { gap: 0.8rem; }
      footer:not(.site-footer), #MainMenu { visibility: hidden; height: 0; }
      [data-testid="stDecoration"] { display: none; }
      [data-testid="stToolbar"] { display: none; }

      h1, h2, h3 { font-family: var(--serif) !important; color: var(--ink); font-weight: 500 !important; letter-spacing: -0.035em; }
      p, li, label, small, span { color: inherit; }
      a { color: inherit; }
      .stMarkdown p:empty { display: none; }

      .announcement {
        display: flex; justify-content: space-between; align-items: center; gap: 1rem;
        min-height: 2.5rem; margin-top: 0.2rem; padding: 0.45rem 1rem;
        color: var(--cream); background: var(--ink); font-size: 0.67rem; font-weight: 600;
      }
      .announcement span { display: flex; align-items: center; gap: 0.55rem; }
      .announcement i { width: 0.4rem; height: 0.4rem; border-radius: 50%; background: var(--lime); box-shadow: 0 0 0 4px rgba(220,234,171,.12); }
      .announcement b { color: var(--lime); font-size: 0.9rem; }

      .brandbar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 1rem 0 0.85rem;
      }
      .brand, .footer-brand { display: flex; align-items: center; gap: 0.65rem; }
      .brand-mark { display: block; width: 2.15rem; height: 2.15rem; color: var(--ink); }
      .brand-mark svg { width: 100%; height: 100%; }
      .brand-name { display: flex; flex-direction: column; font-size: 0.98rem; font-weight: 700; line-height: 1.08; letter-spacing: -0.02em; color: var(--ink); }
      .brand-name small { color: var(--muted); font-size: 0.58rem; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase; }
      .brand-utility { color: var(--muted); font-size: 0.67rem; font-style: italic; }

      div[data-testid="stRadio"] { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 0.2rem 0; margin-bottom: 1.4rem; }
      div[data-testid="stRadio"] > label { display: none; }
      div[data-testid="stRadio"] div[role="radiogroup"] { display: flex; flex-wrap: wrap; gap: 1.55rem; }
      div[data-testid="stRadio"] label[data-baseweb="radio"] { margin: 0 !important; padding: 0.62rem 0; }
      div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child { display: none; }
      div[data-testid="stRadio"] label[data-baseweb="radio"] div[data-testid="stMarkdownContainer"] p { font-size: 0.77rem; font-weight: 600; color: var(--ink-soft); }
      div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) { border-bottom: 2px solid var(--coral-deep); }
      div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p { color: var(--ink); }

      .stButton > button, div[data-testid="stFormSubmitButton"] > button {
        border-radius: 3px !important; border: 1px solid var(--ink) !important;
        min-height: 2.9rem; font-size: 0.76rem !important; font-weight: 700 !important;
        transition: all 180ms ease;
      }
      .stButton > button[kind="secondary"], div[data-testid="stFormSubmitButton"] > button[kind="secondary"] {
        background: transparent; color: var(--ink);
      }
      .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        border-color: var(--coral-deep) !important; background: var(--coral-deep) !important; color: var(--white) !important;
      }
      .stButton > button[kind="primary"], div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
        border-color: var(--ink) !important; background: var(--ink) !important; color: var(--white) !important;
      }
      .stButton > button[kind="primary"]:hover, div[data-testid="stFormSubmitButton"] > button[kind="primary"]:hover {
        background: var(--coral-deep) !important; border-color: var(--coral-deep) !important;
      }
      .stButton > button:focus-visible { outline: 3px solid var(--coral); outline-offset: 3px; }

      .hero { display: grid; grid-template-columns: 1.02fr 0.98fr; gap: clamp(2.5rem, 5vw, 5rem); align-items: center; padding: 2.7rem 0 3.6rem; }
      .eyebrow { display: flex; align-items: center; gap: 0.7rem; margin: 0 0 1.2rem; color: var(--ink-soft); font-size: 0.66rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
      .eyebrow > span { display: block; width: 1.7rem; height: 2px; background: var(--coral-deep); }
      .eyebrow.light { color: rgba(255,253,248,.8); }
      .hero h1, .page-header h1, .research-hero h1 {
        margin: 0 0 1.4rem; font-size: clamp(3.5rem, 6.5vw, 6.7rem); line-height: 0.93; font-weight: 500 !important;
      }
      h1 em, h2 em { color: var(--coral-deep); font-weight: 400; }
      .hero .lede { max-width: 32rem; margin: 0 0 1.7rem; color: var(--ink-soft); font-size: clamp(.95rem, 1.2vw, 1.08rem); line-height: 1.7; }
      .hero-proof { display: flex; flex-direction: column; gap: 0.1rem; padding-top: 1.2rem; border-top: 1px solid var(--line); max-width: 29rem; color: var(--muted); font-size: 0.72rem; }
      .hero-proof strong { color: var(--ink); font-size: 0.78rem; }
      .hero-visual { position: relative; }
      .hero-visual > img { width: 100%; height: clamp(28rem, 42vw, 39rem); object-fit: cover; border-radius: 13rem 13rem 0.5rem 0.5rem; }
      .hero-stamp { position: absolute; top: 2.5rem; right: 1rem; display: flex; align-items: center; justify-content: center; width: 4.7rem; height: 4.7rem; border: 1px solid rgba(255,253,248,.65); border-radius: 50%; color: var(--white); background: rgba(23,51,47,.28); backdrop-filter: blur(8px); font-family: var(--serif); font-size: .75rem; font-style: italic; text-align: center; line-height: 1.15; transform: rotate(8deg); }
      .open-day { position: absolute; bottom: -1rem; left: -2rem; right: 1rem; padding: 1.1rem 1.2rem; background: var(--white); box-shadow: 0 24px 70px rgba(23,51,47,.14); border: 1px solid rgba(23,51,47,.08); }
      .open-day > p { margin: 0 0 .7rem; color: var(--coral-deep); font-size: .59rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
      .open-day-row { display: flex; align-items: center; gap: 1rem; }
      .open-day-date { min-width: 3.4rem; padding-right: 1rem; border-right: 1px solid var(--line); color: var(--muted); font-size: .58rem; line-height: 1.1; text-align: center; text-transform: uppercase; }
      .open-day-date strong { display: block; color: var(--ink); font-family: var(--serif); font-size: 2rem; font-weight: 400; line-height: 1; }
      .open-day-row > div:last-child strong { display: block; font-size: .82rem; }
      .open-day-row > div:last-child small { color: var(--muted); font-size: .61rem; }

      .quick-grid { display: grid; grid-template-columns: repeat(4,1fr); border: 1px solid var(--line); background: var(--white); margin: 1.2rem 0 0; }
      .quick { display: flex; flex-direction: column; gap: .2rem; padding: 1.3rem 1.4rem; border-right: 1px solid var(--line); }
      .quick:last-child { border-right: 0; }
      .quick > span { color: var(--coral-deep); font-family: var(--serif); font-size: .65rem; font-style: italic; }
      .quick strong { font-size: .77rem; }
      .quick small { color: var(--muted); font-size: .61rem; }

      .section { margin-top: clamp(4rem, 7vw, 6rem); }
      .split-heading { display: grid; grid-template-columns: 1.1fr .8fr; gap: clamp(2rem, 7vw, 7rem); align-items: end; margin-bottom: 2.8rem; }
      .split-heading h2, .dark-heading h2, .news-heading h2, .coral-band h2 { font-size: clamp(2.6rem, 4.6vw, 4.5rem); line-height: 1; }
      .body-copy p, .wide-copy { color: var(--ink-soft); font-size: .86rem; line-height: 1.7; }
      .body-copy p + p { margin-top: .8rem; }
      .about-section { padding-top: .5rem; }
      .about-grid { display: grid; grid-template-columns: 1.35fr .72fr; gap: 1rem; margin-bottom: 2rem; }
      .about-photo { position: relative; height: 28rem; margin: 0; }
      .about-photo img { width: 100%; height: 100%; object-fit: cover; }
      .about-photo figcaption { position: absolute; bottom: .8rem; left: .8rem; padding: .65rem .8rem; color: var(--white); background: rgba(23,51,47,.86); font-size: .61rem; }
      .about-side { display: grid; grid-template-rows: .9fr 1.1fr; gap: 1rem; }
      .about-side > img { width: 100%; height: 100%; object-fit: cover; min-height: 11rem; }
      .stat-card { padding: 1.4rem; background: var(--ink); color: var(--cream); display: flex; flex-direction: column; justify-content: space-between; }
      .stat-card p { margin: 0; color: rgba(243,239,229,.7); font-size: .58rem; letter-spacing: .1em; text-transform: uppercase; }
      .stat-card strong { font-family: var(--serif); color: var(--lime); font-size: 3.4rem; font-weight: 400; line-height: .9; }
      .stat-card span { color: var(--cream); font-family: var(--serif); font-size: 1.05rem; line-height: 1.2; }
      .stats { display: grid; grid-template-columns: repeat(4,1fr); border-top: 1px solid var(--line); }
      .stats > div { display: flex; flex-direction: column-reverse; gap: .2rem; padding: 1.35rem 1rem 0; border-right: 1px solid var(--line); }
      .stats > div:last-child { border-right: 0; }
      .stats strong { font-family: var(--serif); font-size: clamp(2rem, 3vw, 3rem); font-weight: 400; line-height: 1; }
      .stats em { color: var(--coral-deep); font-size: .6em; font-style: normal; }
      .stats span { color: var(--muted); font-size: .6rem; }

      .dark-band { margin: 4.5rem -3rem 0; padding: 4rem 3rem 3rem; color: var(--cream); background: var(--ink); }
      .dark-heading { display: flex; justify-content: space-between; align-items: flex-end; gap: 3rem; margin-bottom: 2rem; }
      .dark-heading h2 { color: var(--cream); max-width: 11ch; }
      .dark-band h2 em { color: var(--lime); }
      .dark-heading > p { max-width: 22rem; margin: 0 0 .5rem; color: rgba(243,239,229,.63); font-size: .82rem; }
      .coral-band { display: grid; grid-template-columns: 1fr .7fr; gap: 4rem; align-items: end; margin: 4.5rem -3rem 0; padding: 4rem 3rem; color: var(--white); background: var(--coral-deep); }
      .coral-band h2 { color: var(--white); margin: 0; }
      .coral-band h2 em { color: var(--lime); }
      .coral-band .eyebrow { color: var(--white); }
      .coral-band-copy p { color: var(--white); font-size: .8rem; line-height: 1.7; }
      .coral-band-copy .address { margin-top: 1.2rem; padding-top: 1.2rem; border-top: 1px solid rgba(255,253,248,.25); font-size: .7rem; }

      .page-header { padding: clamp(2.2rem, 4vw, 3.5rem) 0 2.7rem; }
      .page-header.cream { margin-inline: -3rem; padding-inline: 3rem; background: var(--cream); }
      .page-header.dark { margin-inline: -3rem; padding-inline: 3rem; color: var(--cream); background: var(--ink); }
      .page-header.dark h1 { color: var(--cream); }
      .page-header.dark h1 em { color: var(--lime); }
      .page-header.dark .eyebrow { color: rgba(255,253,248,.8); }
      .page-header.dark .wide-copy { color: rgba(255,253,248,.7); }
      .page-header h1 { max-width: 15ch; font-size: clamp(3rem, 5.7vw, 5.5rem); }
      .page-header .wide-copy { max-width: 38rem; margin: 0; }
      .page-header.dark > p:not(.eyebrow) { max-width: 35rem; color: rgba(255,253,248,.67); font-size: .85rem; }

      [data-testid="stVerticalBlockBorderWrapper"] { border: 1px solid var(--line) !important; border-radius: 0 !important; background: rgba(255,253,248,.6); padding: 0.1rem; }
      [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlockBorderWrapper"] { border: 0 !important; background: transparent; }
      [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p { color: var(--muted) !important; opacity: 1 !important; }
      .programme-top i { color: var(--muted); font-family: var(--serif); font-size: .9rem; }
      .programme-top span { padding: .25rem .5rem; border: 1px solid var(--line); color: var(--ink-soft); font-size: .55rem; }
      .programme-school { margin: 0 0 .5rem !important; color: var(--muted) !important; font-size: .57rem !important; font-weight: 600 !important; letter-spacing: .04em; }
      .programme-card h3 { margin: 0 0 .6rem; font-size: 1.5rem; line-height: 1.05; }
      .programme-card > p:last-child { color: var(--muted) !important; font-size: .7rem !important; line-height: 1.6; }
      [data-testid="stVerticalBlockBorderWrapper"] .stButton > button { border: 0 !important; border-top: 1px solid var(--line) !important; border-radius: 0 !important; color: var(--ink) !important; background: transparent !important; text-align: left !important; justify-content: flex-start !important; min-height: 2.3rem; }
      [data-testid="stVerticalBlockBorderWrapper"] .stButton > button:hover { color: var(--coral-deep) !important; background: transparent !important; }

      div[data-testid="stTextInput"], div[data-testid="stSelectbox"], div[data-testid="stTextArea"], div[data-testid="stCheckbox"] { font-size: .75rem; }
      div[data-testid="stTextInput"] label, div[data-testid="stSelectbox"] label, div[data-testid="stTextArea"] label, div[data-testid="stCheckbox"] label, div[data-testid="stSegmentedControl"] label { font-size: .66rem !important; font-weight: 700 !important; color: var(--ink) !important; }
      div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] div[data-baseweb="select"] > div, div[data-testid="stTextArea"] textarea {
        border-radius: 2px !important; border-color: rgba(23,51,47,.25) !important; background: var(--white) !important; font-size: .75rem !important;
      }
      div[data-testid="stTextInput"] input:focus, div[data-testid="stTextArea"] textarea:focus { border-color: var(--ink) !important; box-shadow: 0 0 0 3px rgba(23,51,47,.12) !important; }
      div[data-testid="stSegmentedControl"] div[role="radiogroup"] { background: transparent; gap: .3rem; }
      div[data-testid="stSegmentedControl"] button { border: 1px solid var(--line) !important; border-radius: 3rem !important; background: transparent !important; color: var(--ink-soft) !important; font-size: .61rem !important; }
      div[data-testid="stSegmentedControl"] button[aria-checked="true"], div[data-testid="stSegmentedControl"] button[aria-pressed="true"] { border-color: var(--ink) !important; background: var(--ink) !important; color: var(--white) !important; }

      .note-panel { margin-top: 1.6rem; padding: 1.35rem; background: var(--cream); border: 1px solid var(--line); }
      .note-panel > div { display: flex; flex-direction: column; gap: .2rem; }
      .note-panel strong { font-size: .78rem; }
      .note-panel span { color: var(--muted); font-size: .68rem; }
      .step-note { margin-top: 2.2rem; }

      .admissions-visual { position: relative; margin-bottom: 2.5rem; }
      .admissions-visual > img { width: 100%; height: 29rem; object-fit: cover; }
      .deadline { position: absolute; right: -1.4rem; bottom: -1.8rem; width: 16.5rem; max-width: calc(100% - 1rem); padding: 1.3rem; color: var(--white); background: var(--coral-deep); box-shadow: 0 24px 70px rgba(23,51,47,.15); }
      .deadline > p { margin: 0 0 .6rem; font-size: .57rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
      .deadline > strong { display: block; margin-bottom: .5rem; font-family: var(--serif); font-size: 1.8rem; font-weight: 400; line-height: 1; }
      .deadline em { color: var(--lime); font-style: normal; }
      .deadline > span { color: var(--white); font-size: .64rem; }

      div[data-testid="stExpander"] { border: 0 !important; border-top: 1px solid var(--line) !important; border-radius: 0 !important; background: transparent !important; }
      div[data-testid="stExpander"]:last-of-type { border-bottom: 1px solid var(--line) !important; }
      div[data-testid="stExpander"] summary { padding: .85rem 0 !important; font-size: .8rem !important; font-weight: 700 !important; }
      div[data-testid="stExpander"] p, div[data-testid="stExpander"] li { font-size: .7rem; color: var(--ink-soft); }

      .campus-grid { display: grid; grid-template-columns: repeat(12,1fr); grid-template-rows: 15rem 15rem; gap: .8rem; margin-bottom: 2.5rem; }
      .campus-grid figure { position: relative; margin: 0; overflow: hidden; }
      .campus-grid .campus-main { grid-column: 1/7; grid-row: 1/3; }
      .campus-grid figure:nth-child(2) { grid-column: 7/13; }
      .campus-grid figure:nth-child(3) { grid-column: 7/10; grid-row: 2; }
      .campus-grid figure img { width: 100%; height: 100%; object-fit: cover; }
      .campus-grid figcaption { position: absolute; right: 0; bottom: 0; left: 0; display: flex; gap: .5rem; align-items: center; padding: 2rem .8rem .65rem; color: var(--white); background: linear-gradient(transparent,rgba(16,40,37,.8)); font-size: .58rem; font-weight: 600; }
      .campus-grid figcaption span { color: var(--lime); font-family: var(--serif); font-style: italic; }
      .campus-quote { grid-column: 10/13; grid-row: 2; display: flex; flex-direction: column; justify-content: space-between; padding: 1.1rem; color: var(--white); background: var(--coral-deep); }
      .campus-quote blockquote { margin: 0; font-family: var(--serif); font-size: 1.05rem; font-style: italic; line-height: 1.25; }
      .campus-quote p { font-size: .57rem; color: var(--white); }
      .campus-quote strong { font-size: .61rem; }
      .campus-features { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.4rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
      .campus-features > div > span { color: var(--coral-deep); font-family: var(--serif); font-size: .7rem; font-style: italic; }
      .campus-features h3 { margin: .4rem 0; font-size: 1.25rem; }
      .campus-features p { color: var(--muted); font-size: .71rem; line-height: 1.6; }

      .research-hero { display: grid; grid-template-columns: .9fr 1fr; gap: clamp(2.5rem, 7vw, 6rem); align-items: center; padding: 3rem 0 1rem; }
      .research-hero h1 { font-size: clamp(3rem, 5.2vw, 5rem); }
      .research-hero > div > p:not(.eyebrow) { max-width: 30rem; color: var(--ink-soft); font-size: .83rem; line-height: 1.7; }
      .research-stats { display: flex; gap: 2.7rem; margin: 1.8rem 0 0; padding-top: 1rem; border-top: 1px solid var(--line); }
      .research-stats p { display: flex; flex-direction: column; margin: 0; }
      .research-stats strong { font-family: var(--serif); font-size: 2.2rem; font-weight: 400; line-height: 1; }
      .research-stats span { color: var(--muted); font-size: .59rem; }
      .research-feature { margin: 0; background: var(--white); box-shadow: 0 20px 60px rgba(23,51,47,.08); }
      .research-feature > img { width: 100%; height: 18rem; object-fit: cover; }
      .research-feature figcaption { padding: 1.3rem 1.4rem 1.5rem; }
      .research-feature figcaption > span { color: var(--coral-deep); font-size: .56rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
      .research-feature h3 { margin: .5rem 0; font-size: 1.55rem; }
      .research-feature p { color: var(--muted); font-size: .7rem; line-height: 1.6; }
      .news-section { margin-top: 3.5rem; }
      .news-heading { grid-template-columns: 1fr .55fr; align-items: end; }
      .news-heading > p { padding-bottom: .5rem; color: var(--muted); font-size: .75rem; }
      .news-card { min-height: 21rem; }
      .news-card h3 { margin: .5rem 0; font-size: 1.18rem; line-height: 1.1; }
      .news-card > p:not(.news-meta) { color: var(--muted); font-size: .67rem; line-height: 1.6; }
      .news-image { position: relative; height: 7.5rem; margin: -0.1rem -0.1rem .8rem; overflow: hidden; }
      .news-image img { width: 100%; height: 100%; object-fit: cover; }
      .news-image span { position: absolute; bottom: .5rem; left: .5rem; padding: .22rem .4rem; color: var(--ink); background: var(--cream); font-size: .5rem; font-weight: 700; text-transform: uppercase; }
      .news-meta { color: var(--muted); font-size: .54rem; }
      .events-section { display: grid; grid-template-columns: .7fr 1.5fr; gap: 2rem; margin-top: 3.5rem; padding: 1.6rem; background: var(--cream); border: 1px solid var(--line); }
      .events-heading h2 { font-size: 2.2rem; }
      .event-list { display: flex; flex-direction: column; }
      .event { display: grid; grid-template-columns: 2.8rem 1fr; gap: .8rem; align-items: center; padding: .8rem 0; border-bottom: 1px solid var(--line); }
      .event:last-child { border-bottom: 0; }
      .event-date { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 3.2rem; border: 1px solid var(--line); }
      .event-date span { color: var(--muted); font-size: .51rem; font-weight: 700; text-transform: uppercase; }
      .event-date strong { font-family: var(--serif); font-size: 1.3rem; font-weight: 400; line-height: 1; }
      .event p { margin: 0; color: var(--coral-deep); font-size: .5rem; font-weight: 700; text-transform: uppercase; }
      .event h3 { margin: .1rem 0; font-family: var(--sans); font-size: .73rem; font-weight: 700; letter-spacing: 0; }
      .event span { color: var(--muted); font-size: .55rem; }

      .contact-details { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.8rem; }
      .contact-details h3 { margin: 0 0 .35rem; font-family: var(--sans); font-size: .61rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
      .contact-details p { color: var(--ink-soft); font-size: .69rem; line-height: 1.7; }
      .contact-details a { display: inline-block; min-height: 1.5rem; text-decoration: underline; text-underline-offset: .2em; }
      .map-card { padding: 1.5rem; color: var(--cream); background: var(--ink); }
      .map-card span { color: var(--lime); font-size: .55rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
      .map-card strong { display: block; margin: .6rem 0 .25rem; font-family: var(--serif); font-size: 1.5rem; font-weight: 400; }
      .map-card p { color: rgba(243,239,229,.72); font-size: .66rem; }
      .form-heading h2 { margin: 0 0 .2rem; font-size: 2.2rem; }
      .form-heading p { color: var(--muted); font-size: .72rem; margin-bottom: .7rem; }
      div[data-testid="stForm"] { border: 1px solid var(--line) !important; border-radius: 0 !important; background: var(--white); padding: 1.3rem !important; }
      div[data-testid="stAlert"] { border-radius: 2px; font-size: .72rem; }

      .site-footer { display: grid; grid-template-columns: 1.6fr .75fr .75fr .75fr; gap: 3rem; margin: 4.5rem -3rem 0; padding: 3.4rem 3rem; color: rgba(243,239,229,.7); background: var(--ink-deep); }
      .site-footer .brand-mark { color: var(--cream); }
      .site-footer .brand-name { color: var(--cream); }
      .site-footer .brand-name small { color: rgba(243,239,229,.55); }
      .footer-tagline { margin: 1rem 0; color: var(--cream); font-family: var(--serif); font-size: 1rem; font-style: italic; }
      .footer-address { color: rgba(243,239,229,.7); font-size: .65rem; line-height: 1.7; }
      .site-footer h3 { margin: 0 0 .8rem; color: var(--cream); font-family: var(--sans); font-size: .59rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
      .site-footer > div:not(:first-child) p { margin: 0; color: rgba(243,239,229,.67); font-size: .68rem; line-height: 1.9; }
      .site-footer a { text-decoration: underline; text-underline-offset: .2em; }
      .footer-bottom { display: flex; justify-content: space-between; gap: 1rem; margin: 0 -3rem; padding: .9rem 3rem; color: rgba(243,239,229,.62); background: var(--ink-deep); border-top: 1px solid rgba(255,253,248,.13); font-size: .55rem; }

      @media (max-width: 980px) {
        .hero, .research-hero { grid-template-columns: 1fr; }
        .hero-visual { margin-top: 1rem; }
        .quick-grid { grid-template-columns: 1fr 1fr; }
        .quick:nth-child(2) { border-right: 0; }
        .quick:nth-child(3), .quick:nth-child(4) { border-top: 1px solid var(--line); }
        .split-heading, .coral-band, .dark-heading { grid-template-columns: 1fr; display: grid; gap: 1.5rem; }
        .about-grid { grid-template-columns: 1.1fr .9fr; }
        .campus-grid { grid-template-rows: 13rem 13rem; }
        .campus-quote { grid-column: 10/13; }
        .campus-quote blockquote { font-size: .85rem; }
        .research-feature { margin-top: 1.5rem; }
        .site-footer { grid-template-columns: 1.5fr 1fr 1fr; }
        .site-footer > div:last-child { grid-column: 2/4; }
      }

      @media (max-width: 720px) {
        [data-testid="stMainBlockContainer"] { width: calc(100% - 1.5rem) !important; }
        .announcement { justify-content: center; text-align: center; font-size: .59rem; }
        .announcement span:last-child { display: none; }
        .brand-utility { display: none; }
        div[data-testid="stRadio"] div[role="radiogroup"] { gap: 1rem; overflow-x: auto; flex-wrap: nowrap; scrollbar-width: none; }
        div[data-testid="stRadio"] label[data-baseweb="radio"] { flex: 0 0 auto; }
        div[data-testid="stRadio"] div[role="radiogroup"]::-webkit-scrollbar { display: none; }
        .hero { gap: 2rem; padding-top: 1.5rem; padding-bottom: 2.5rem; }
        .hero h1, .page-header h1, .research-hero h1 { font-size: clamp(2.9rem, 13vw, 4.3rem); }
        .hero h1 br, .page-header h1 br, .research-hero h1 br, .split-heading h2 br, .coral-band h2 br { display: none; }
        .hero-visual > img { height: 24rem; border-radius: 8rem 8rem .4rem .4rem; }
        .open-day { left: .7rem; right: .7rem; bottom: -2.3rem; }
        .hero + div { margin-top: 2rem; }
        .quick { padding: 1rem; }
        .quick strong { font-size: .68rem; }
        .quick small { font-size: .56rem; }
        .split-heading, .news-heading { grid-template-columns: 1fr; }
        .about-grid { grid-template-columns: 1fr; }
        .about-photo { height: 21rem; }
        .about-side { grid-template-columns: 1fr 1fr; grid-template-rows: 1fr; }
        .about-side > img { height: 12rem; }
        .stat-card strong { font-size: 2.7rem; }
        .stat-card span { font-size: .85rem; }
        .stats { grid-template-columns: 1fr 1fr; }
        .stats > div:nth-child(2) { border-right: 0; }
        .stats > div:nth-child(3), .stats > div:nth-child(4) { border-top: 1px solid var(--line); }
        .dark-band, .coral-band, .page-header.cream, .page-header.dark, .site-footer, .footer-bottom { margin-left: -0.75rem; margin-right: -0.75rem; padding-left: 1.25rem; padding-right: 1.25rem; }
        .dark-band, .coral-band { padding-top: 2.5rem; padding-bottom: 2.5rem; }
        .coral-band { grid-template-columns: 1fr; gap: 1.5rem; }
        .campus-grid { display: flex; overflow-x: auto; gap: .7rem; margin-inline: -0.75rem; padding-inline: .75rem; scroll-snap-type: x mandatory; }
        .campus-grid figure, .campus-quote { flex: 0 0 82vw; height: 20rem; scroll-snap-align: start; }
        .campus-quote blockquote { font-size: 1.4rem; }
        .campus-features { grid-template-columns: 1fr; gap: 1.4rem; }
        .research-hero { padding-top: 2rem; }
        .events-section { grid-template-columns: 1fr; }
        .about-photo figcaption { font-size: .56rem; }
        .contact-details { grid-template-columns: 1fr 1fr; }
        .site-footer { grid-template-columns: 1fr 1fr; gap: 2rem; }
        .site-footer > div:first-child { grid-column: 1 / -1; }
        .site-footer > div:last-child { grid-column: auto; }
        .footer-bottom { flex-direction: column; gap: .4rem; }
        .research-section { padding-top: 0; }
      }

      @media (max-width: 430px) {
        .quick-grid { grid-template-columns: 1fr 1fr; }
        .about-side { grid-template-columns: 1fr; }
        .about-side > img { height: 10rem; }
        .stat-card { min-height: 12rem; }
        .contact-details { grid-template-columns: 1fr; }
        .hero-visual > img { height: 21rem; }
        .page-header h1 { font-size: 2.8rem; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

render_header()
render_nav()

page = st.session_state.get("nav", "Discover")

if page == "Discover":
    render_home()
elif page == "Study":
    render_study()
elif page == "Admissions":
    render_admissions()
elif page == "Campus life":
    render_campus()
elif page == "Research & news":
    render_research()
elif page == "Visit":
    render_visit()

render_footer()
