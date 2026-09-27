
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ARCTIS | Polar Mission Control",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Session state
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "tutorial_step" not in st.session_state:
    st.session_state.tutorial_step = 0
if "tutorial_active" not in st.session_state:
    st.session_state.tutorial_active = True

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #07111f;
        color: #eaf3ff;
    }

    [data-testid="stSidebar"] {
        background: #0a1727;
        border-right: 1px solid #1b344d;
    }

    .brand {
        font-size: 30px;
        font-weight: 800;
        letter-spacing: 1px;
        color: #f3f8ff;
        margin-bottom: 0;
    }

    .subtitle {
        color: #8da9c2;
        font-size: 13px;
        margin-top: -4px;
        margin-bottom: 18px;
    }

    .topbar {
        background: linear-gradient(90deg, #0d2236, #0a1727);
        border: 1px solid #1c3b55;
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 18px;
    }

    .status {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        background: #113c35;
        color: #76e4c2;
        border: 1px solid #1d6959;
    }

    .card {
        background: #0b1b2c;
        border: 1px solid #1b344d;
        border-radius: 14px;
        padding: 18px;
        min-height: 125px;
        margin-bottom: 12px;
    }

    .card h3 {
        margin: 0 0 7px 0;
        font-size: 18px;
    }

    .card p {
        color: #9db4c9;
        margin: 0;
        font-size: 13px;
        line-height: 1.45;
    }

    .metric {
        background: #0b1b2c;
        border: 1px solid #1b344d;
        border-radius: 12px;
        padding: 15px;
    }

    .metric-label {
        color: #8da9c2;
        font-size: 12px;
    }

    .metric-value {
        font-size: 25px;
        font-weight: 800;
        margin-top: 4px;
    }

    .bubble {
        background: #f2f7fc;
        color: #142333;
        border-radius: 16px;
        padding: 16px 18px;
        margin: 10px 0 18px 0;
        border-left: 5px solid #4da3ff;
        box-shadow: 0 8px 22px rgba(0,0,0,.22);
    }

    .bubble-title {
        font-weight: 800;
        margin-bottom: 5px;
    }

    .small {
        color: #8da9c2;
        font-size: 12px;
    }

    .danger {
        background: #35161b;
        border: 1px solid #7b3039;
        color: #ffb6bd;
        border-radius: 12px;
        padding: 13px;
    }

    .info {
        background: #102a40;
        border: 1px solid #24567a;
        color: #b9ddfa;
        border-radius: 12px;
        padding: 13px;
    }

    div.stButton > button {
        border-radius: 10px;
        border: 1px solid #23445f;
        background: #0d2236;
        color: #eaf3ff;
    }

    div.stButton > button:hover {
        border-color: #4da3ff;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Demo data
# -----------------------------
cargo = [
    {"id": "CRG-001", "item": "Scientific Equipment Crate", "destination": "Station Aurora", "status": "In Transit", "priority": "High"},
    {"id": "CRG-002", "item": "Medical Supplies", "destination": "Field Camp Alpha", "status": "Delivered", "priority": "Critical"},
    {"id": "CRG-003", "item": "Fuel Containers", "destination": "Research Vessel", "status": "Loading", "priority": "High"},
    {"id": "CRG-004", "item": "Food Supplies", "destination": "Station Aurora", "status": "In Transit", "priority": "Normal"},
]

personnel = [
    {"id": "P-014", "name": "Field Member 014", "team": "Alpha", "status": "Active", "location": "CP-03"},
    {"id": "P-021", "name": "Field Member 021", "team": "Alpha", "status": "Active", "location": "CP-03"},
    {"id": "P-033", "name": "Field Member 033", "team": "Bravo", "status": "Resting", "location": "Camp B"},
    {"id": "P-041", "name": "Field Member 041", "team": "Bravo", "status": "Communication Check", "location": "Sector 7"},
]

assets = [
    {"id": "AST-03", "asset": "Snow Vehicle 03", "location": "Camp B", "condition": "Operational", "fuel": "62%"},
    {"id": "AST-07", "asset": "Portable Radar", "location": "Station Aurora", "condition": "Operational", "fuel": "N/A"},
    {"id": "AST-12", "asset": "Generator 12", "location": "Field Camp Alpha", "condition": "Maintenance Due", "fuel": "41%"},
]

inventory = [
    ("Food supplies", "1,240 units", "18 days"),
    ("Fuel", "4,820 L", "21 days"),
    ("Medical kits", "86", "Adequate"),
    ("Batteries", "312", "12 days"),
]

# -----------------------------
# Navigation
# -----------------------------
pages = [
    ("Home", "⌂"),
    ("Mission Control", "◈"),
    ("Cargo", "▣"),
    ("Personnel", "♙"),
    ("Assets", "⚙"),
    ("Inventory", "▤"),
    ("Communications", "⌁"),
    ("Emergency", "SOS"),
    ("AI Advisor", "✦"),
]

with st.sidebar:
    st.markdown('<div class="brand">ARCTIS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Polar Expedition Command System</div>', unsafe_allow_html=True)
    st.markdown("### Navigation")

    for name, icon in pages:
        if st.button(f"{icon}  {name}", key=f"nav_{name}", use_container_width=True):
            st.session_state.page = name
            st.session_state.tutorial_active = False
            st.rerun()

    st.divider()
    st.markdown("**System Status**")
    st.markdown('<span class="status">● OFFLINE-READY</span>', unsafe_allow_html=True)
    st.caption("Last HQ synchronization: 14:32 UTC")

    if st.button("🎓 Restart Tutorial", use_container_width=True):
        st.session_state.page = "Home"
        st.session_state.tutorial_step = 0
        st.session_state.tutorial_active = True
        st.rerun()

# -----------------------------
# Tutorial bubble
# -----------------------------
tutorials = {
    "Home": [
        ("ARCTIS Mission Control", "This is the entry point for the expedition. We designed it to give the commander one operational picture instead of making them switch between separate logistics, personnel, asset and emergency systems."),
        ("Mission Modules", "Each module represents a real operational requirement from the problem statement. Selecting a module takes us into the detailed workflow instead of leaving the information as static dashboard numbers."),
        ("Why this matters", "Polar missions involve people, cargo, equipment and environmental risks at the same time. The home screen connects these otherwise separate activities so a change in one area can later influence the AI's recommendations."),
    ],
    "Cargo": [
        ("Why Cargo Management exists", "Polar expeditions depend on carefully planned movement of scientific equipment, food, fuel and medical supplies. A delay or misplaced shipment can affect an entire mission, so cargo needs to be tracked as an operational asset rather than just recorded in a spreadsheet."),
        ("Shipment Details", "Each shipment has an identity, destination, priority and status. In the full system, this record can also contain route history, telemetry, documents and predicted arrival time."),
        ("Why AI is connected here", "The purpose is not only to know where cargo is. The central AI can later combine cargo status with weather, route conditions, inventory and mission schedules to identify possible delays or shortages before they become operational problems."),
    ],
    "Mission Control": [
        ("Why Mission Control exists", "The expedition commander needs a single operational picture. Mission Control brings personnel, assets, logistics, communications and risk information together so decisions are based on the state of the whole expedition."),
        ("From monitoring to decision support", "This is where the central AI becomes useful. Instead of presenting isolated numbers, it can correlate them—for example, a delayed cargo shipment plus worsening weather plus low inventory can trigger a planning recommendation."),
    ],
    "Personnel": [
        ("Why Personnel Tracking exists", "In a polar environment, knowing where field personnel are and whether they are safe is a core operational requirement. Personnel tracking connects movement, assignments and communication status to the central mission picture."),
        ("Automatic distress detection", "The field node can detect unusual inactivity, but inactivity alone should not trigger an SOS. The final system can combine inactivity with route deviation, environmental conditions and lack of response before escalating an alert."),
        ("Why the field node matters", "Personnel should not need a phone or continuous internet connection to remain part of the mission network. The dedicated node provides essential location, communication and emergency functions with low power requirements."),
    ],
    "Assets": [
        ("Why Asset Management exists", "Polar missions depend on expensive and difficult-to-replace vehicles, generators, scientific instruments and communication equipment. Losing track of an asset or missing maintenance can cause major mission disruption."),
        ("Operational condition", "Each asset is linked to its location, condition and resource status. This creates a live asset inventory rather than a static equipment list."),
        ("Future predictive layer", "The central AI can later combine usage, telemetry and maintenance history to identify assets that may require servicing before failure."),
    ],
    "Inventory": [
        ("Why Inventory exists", "A polar expedition cannot simply purchase supplies locally when something runs out. Food, fuel, batteries and medical supplies therefore need projected consumption and resupply planning."),
        ("Beyond stock counting", "The important question is not only 'how much do we have?' but 'how long will it last?' The system therefore tracks projected remaining days."),
        ("AI forecasting", "The central AI can later use personnel count, consumption trends, mission duration and resupply schedules to identify potential shortages early."),
    ],
    "Communications": [
        ("Why this module exists", "Conventional internet and cellular connectivity cannot be assumed in polar field operations. The system therefore treats communication as a resilient layer using whatever approved channels are available."),
        ("Store-and-forward", "When a field node cannot reach HQ, important information is stored locally instead of being lost. When another field node, radio relay or satellite link becomes available, the message can be forwarded."),
        ("Priority communication", "Bandwidth may be limited. SOS and mission-critical messages therefore receive priority over routine telemetry and bulk data."),
    ],
    "Emergency": [
        ("Why Emergency Response exists", "A polar emergency can become critical quickly because distance, weather and limited infrastructure can delay assistance. The system therefore turns an alert into an actionable response workflow."),
        ("Automatic SOS", "A field node can initiate SOS manually, but it can also detect possible distress. The system first checks context and prompts the user before escalating, reducing false alarms."),
        ("Response intelligence", "The central system can combine the person's last location with nearby personnel, available vehicles, weather and safe locations to help the commander coordinate a response."),
    ],
    "AI Advisor": [
        ("Why the AI is centralized", "Heavy AI computation does not need to run on every field device. Keeping the main intelligence engine at the ship, research station or HQ allows larger models and data processing while keeping field nodes small, power-efficient and reliable."),
        ("What the AI combines", "The AI can correlate logistics, inventory, personnel, assets, environmental observations and mission plans instead of analysing each category independently."),
        ("Why the AI is advisory", "The system should explain why it recommends an action and leave the final operational decision to authorized personnel. This is decision support, not autonomous command."),
        ("Internet update cycle", "When HQ has internet access, validated weather data, satellite observations, maps, research and model updates can be incorporated. The relevant updates can then be synchronized to the mission environment."),
    ],
}

def render_tutorial_bubble(page, step=0):
    steps = tutorials.get(page, [])
    if not steps:
        return
    idx = min(step, len(steps) - 1)
    title, text = steps[idx]
    st.markdown(
        f"""
        <div class="bubble">
            <div class="bubble-title">💬 {title}</div>
            <div>{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("← Previous", key=f"prev_{page}_{idx}", disabled=(idx == 0)):
            st.session_state.tutorial_step -= 1
            st.rerun()
    with c2:
        if idx < len(steps) - 1:
            if st.button("Next →", key=f"next_{page}_{idx}"):
                st.session_state.tutorial_step += 1
                st.rerun()
        else:
            if st.button("Close explanation", key=f"close_{page}_{idx}"):
                st.session_state.tutorial_active = False
                st.rerun()

# -----------------------------
# Header
# -----------------------------
st.markdown(
    f"""
    <div class="topbar">
        <div style="font-size:12px;color:#8da9c2;">MISSION / {st.session_state.page.upper()}</div>
        <div style="font-size:25px;font-weight:800;margin-top:4px;">Antarctic Expedition Alpha</div>
        <div class="small">Central Mission Node • Prototype Environment • {datetime.utcnow().strftime("%d %b %Y, %H:%M UTC")}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Pages
# -----------------------------
def metric(label, value):
    st.markdown(
        f"""
        <div class="metric">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.session_state.page == "Home":
    st.subheader("Mission Overview")

    cols = st.columns(5)
    for col, label, value in zip(
        cols,
        ["Personnel", "Cargo", "Assets", "Inventory", "Alerts"],
        ["24", "18", "37", "82%", "2"],
    ):
        with col:
            metric(label, value)

    st.markdown("### Mission Modules")
    cards = [
        ("Cargo", "▣", "Track shipments, cargo status, destinations and priorities."),
        ("Personnel", "♙", "Monitor field teams, movement and personnel safety."),
        ("Assets", "⚙", "Track vehicles, equipment, condition and maintenance."),
        ("Inventory", "▤", "Monitor supplies, consumption and projected shortages."),
        ("Communications", "⌁", "Monitor satellite, radio and field-relay connectivity."),
        ("Emergency", "SOS", "Manage SOS, hazard, lost-person and assistance alerts."),
        ("AI Advisor", "✦", "View forecasts, risks, recommendations and simulations."),
        ("Mission Control", "◈", "See the complete operational picture."),
    ]

    for row in range(0, len(cards), 4):
        cols = st.columns(4)
        for col, (name, icon, desc) in zip(cols, cards[row:row+4]):
            with col:
                st.markdown(
                    f'<div class="card"><h3>{icon} {name}</h3><p>{desc}</p></div>',
                    unsafe_allow_html=True,
                )
                if st.button(f"Open {name}", key=f"home_{name}", use_container_width=True):
                    st.session_state.page = name
                    st.session_state.tutorial_step = 0
                    st.session_state.tutorial_active = True
                    st.rerun()

    if st.session_state.tutorial_active:
        st.markdown("### Why these modules exist")
        render_tutorial_bubble("Home", st.session_state.tutorial_step)

    st.markdown("### Current Mission Alerts")
    st.markdown('<div class="danger">🔴 <b>2 active alerts</b> — Field Member 041 requires communication check.</div>', unsafe_allow_html=True)
    st.markdown('<div class="info">🔵 <b>Research observation</b> — New ice observation recorded at Sector 7.</div>', unsafe_allow_html=True)

elif st.session_state.page == "Mission Control":
    st.subheader("Mission Control")
    if st.session_state.tutorial_active: render_tutorial_bubble("Mission Control", st.session_state.tutorial_step)
    cols = st.columns(4)
    for col, label, value in zip(cols, ["Mission Progress", "Team Status", "Communication", "Overall Risk"], ["64%", "23 / 24", "82%", "MEDIUM"]):
        with col:
            metric(label, value)

    st.markdown("### Operational Picture")
    st.info("Prototype map area — this can later be replaced with a live Folium/Plotly polar map.")
    st.markdown("**Current route:** Base → CP-01 → CP-02 → CP-03 → Research Zone → Base")
    st.progress(0.64)

elif st.session_state.page == "Cargo":
    st.subheader("Cargo Management")
    if st.session_state.tutorial_active: render_tutorial_bubble("Cargo", st.session_state.tutorial_step)
    cols = st.columns(4)
    for col, label, value in zip(cols, ["Total Shipments", "In Transit", "Delivered", "High Priority"], ["18", "7", "9", "5"]):
        with col:
            metric(label, value)

    st.markdown("### Shipment Records")
    status_filter = st.selectbox("Filter by status", ["All", "In Transit", "Delivered", "Loading"])
    search = st.text_input("Search cargo", placeholder="e.g. Medical Supplies")

    filtered = [
        x for x in cargo
        if (status_filter == "All" or x["status"] == status_filter)
        and (not search or search.lower() in x["item"].lower() or search.lower() in x["id"].lower())
    ]

    for item in filtered:
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([1.2, 3, 2, 1.2])
            c1.write(f"**{item['id']}**")
            c2.write(f"**{item['item']}**")
            c3.write(f"{item['destination']}  \n{item['status']}")
            if c4.button("Details", key=f"cargo_{item['id']}"):
                st.session_state.selected_cargo = item["id"]
                st.rerun()

    if "selected_cargo" in st.session_state:
        item = next((x for x in cargo if x["id"] == st.session_state.selected_cargo), None)
        if item:
            st.markdown("### Shipment Details")
            st.json(item)
            st.success("Prototype action: shipment details loaded. Future version can show route, telemetry, documents and predicted arrival.")

elif st.session_state.page == "Personnel":
    st.subheader("Personnel Tracking")
    if st.session_state.tutorial_active: render_tutorial_bubble("Personnel", st.session_state.tutorial_step)
    for p in personnel:
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([1.1, 2.4, 1.5, 2])
            c1.write(f"**{p['id']}**")
            c2.write(p["name"])
            c3.write(p["team"])
            c4.write(f"{p['status']} • {p['location']}")

    st.markdown("### Safety Logic Preview")
    st.info("Future automatic SOS logic: inactivity + route deviation + environmental risk + no response → warning → escalation → SOS.")

elif st.session_state.page == "Assets":
    st.subheader("Asset Management")
    if st.session_state.tutorial_active: render_tutorial_bubble("Assets", st.session_state.tutorial_step)
    for a in assets:
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([1, 2.5, 2, 2])
            c1.write(f"**{a['id']}**")
            c2.write(a["asset"])
            c3.write(a["location"])
            c4.write(f"{a['condition']} • Fuel: {a['fuel']}")

elif st.session_state.page == "Inventory":
    st.subheader("Inventory Management")
    if st.session_state.tutorial_active: render_tutorial_bubble("Inventory", st.session_state.tutorial_step)
    for name, amount, duration in inventory:
        with st.container(border=True):
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(f"**{name}**")
            c2.write(amount)
            c3.write(f"Projected: {duration}")

    st.warning("Prototype forecast: battery stock may require resupply within 12 days.")

elif st.session_state.page == "Communications":
    st.subheader("Communication Network")
    if st.session_state.tutorial_active: render_tutorial_bubble("Communications", st.session_state.tutorial_step)
    cols = st.columns(3)
    for col, label, value in zip(cols, ["Satellite Link", "Radio Network", "Field Relay"] , ["AVAILABLE", "AVAILABLE", "3 NODES"]):
        with col:
            metric(label, value)

    st.markdown("### Message Queue")
    st.dataframe(
        [
            {"Priority": "CRITICAL", "Message": "SOS packet", "Status": "Delivered", "Source": "P-041"},
            {"Priority": "HIGH", "Message": "Storm observation", "Status": "Queued", "Source": "P-033"},
            {"Priority": "NORMAL", "Message": "Routine telemetry", "Status": "Synced", "Source": "P-021"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif st.session_state.page == "Emergency":
    st.subheader("Emergency Response Center")
    if st.session_state.tutorial_active: render_tutorial_bubble("Emergency", st.session_state.tutorial_step)
    st.markdown('<div class="danger"><b>ACTIVE ALERT — P-041</b><br>Communication check required. Last known location: Sector 7.</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("📡 Contact Personnel", use_container_width=True)
    with c2:
        st.button("🚑 Start Response", use_container_width=True)
    with c3:
        st.button("📍 Open Location", use_container_width=True)

    st.markdown("### Automatic SOS Logic")
    st.write("1. Detect abnormal inactivity")
    st.write("2. Check route and environmental context")
    st.write("3. Prompt field member for confirmation")
    st.write("4. Escalate if there is no response")
    st.write("5. Broadcast emergency packet through available links")

elif st.session_state.page == "AI Advisor":
    st.subheader("Central Mission Intelligence")
    if st.session_state.tutorial_active: render_tutorial_bubble("AI Advisor", st.session_state.tutorial_step)
    st.markdown('<div class="info"><b>AI Engine: CENTRAL HQ</b><br>Heavy AI computation is intentionally kept at the ship/research station. Field nodes remain lightweight and power efficient.</div>', unsafe_allow_html=True)

    st.markdown("### Current Recommendations")
    st.success("Inventory: Review battery resupply schedule within 12 days.")
    st.warning("Personnel: P-041 requires communication verification.")
    st.info("Environment: New field observation recorded in Sector 7.")

    st.markdown("### What-if Simulation")
    scenario = st.selectbox("Scenario", ["Continue current route", "Delay departure by 4 hours", "Reroute through Checkpoint 4"])
    if st.button("Simulate"):
        st.write(f"Prototype simulation generated for: **{scenario}**")
        st.success("Future version will use trained forecasting models and live mission data.")

st.caption("ARCTIS Prototype • UI/UX demonstration only • AI/ML outputs are simulated in this version.")
