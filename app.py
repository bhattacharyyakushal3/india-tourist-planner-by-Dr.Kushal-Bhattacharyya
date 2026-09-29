# ============================================================
# INDIA TOURIST PLANNER - STREAMLIT FRONTEND
# ============================================================

import streamlit as st

from backend import (
    get_destinations,
    create_itinerary,
    calculate_estimated_cost
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="India Tourist Planner By Dr.Kushal Bhattacharyya ",
    page_icon="🇮🇳",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title(" Tourist Planner By Dr.Kushal Bhattacharyya")

st.write(
    "Plan your trip to popular destinations in India "
    "with a simple itinerary and estimated cost."
)

st.divider()


# ============================================================
# LOAD DESTINATIONS
# ============================================================

destinations = get_destinations()

destination_names = list(destinations.keys())


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("⚙️ Trip Settings")

name = st.sidebar.text_input(
    "Traveller Name",
    value=""
)

adults = st.sidebar.number_input(
    "Number of Adults",
    min_value=1,
    max_value=50,
    value=2,
    step=1
)

children = st.sidebar.number_input(
    "Number of Children",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)

days = st.sidebar.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3,
    step=1
)

budget = st.sidebar.selectbox(
    "Budget Category",
    [
        "Budget",
        "Standard",
        "Premium"
    ]
)


# ============================================================
# DESTINATION
# ============================================================

st.header("📍 Select Destination")

destination = st.selectbox(
    "Choose your tourist destination",
    destination_names
)


# ============================================================
# DESTINATION INFORMATION
# ============================================================

destination_data = destinations[destination]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Destination",
        destination
    )

with col2:
    st.metric(
        "State / UT",
        destination_data["state"]
    )

with col3:
    st.metric(
        "Recommended Days",
        destination_data["recommended_days"]
    )


st.info(destination_data["description"])


# ============================================================
# AVAILABLE TOURIST PLACES
# ============================================================

st.subheader("🏛️ Tourist Attractions")

places = destination_data["places"]

for place in places:

    with st.expander(
        f"📌 {place['name']}"
    ):

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(
                "**Activity:**",
                place["activity"]
            )

        with col2:
            st.write(
                "**Duration:**",
                place["duration"]
            )

        with col3:
            st.write(
                "**Entry Cost:** ₹",
                place["entry_cost"]
            )


# ============================================================
# GENERATE TOUR PLAN
# ============================================================

st.divider()

st.header("🗓️ Generate Tour Plan")

if st.button(
    "🚀 Generate Tour Plan",
    use_container_width=True
):

    if not name.strip():

        name = "Guest Traveller"

    itinerary = create_itinerary(
        destination,
        days,
        adults,
        children
    )

    estimated_cost = calculate_estimated_cost(
        destination,
        days,
        adults,
        children,
        budget
    )


    # ========================================================
    # SUCCESS MESSAGE
    # ========================================================

    st.success(
        "Tour plan generated successfully!"
    )


    # ========================================================
    # TRIP SUMMARY
    # ========================================================

    st.subheader("👤 Trip Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write("**Traveller**")
        st.write(name)

    with col2:
        st.write("**Destination**")
        st.write(destination)

    with col3:
        st.write("**Adults**")
        st.write(adults)

    with col4:
        st.write("**Children**")
        st.write(children)

    with col5:
        st.write("**Days**")
        st.write(days)


    # ========================================================
    # ESTIMATED COST
    # ========================================================

    st.subheader("💰 Estimated Trip Cost")

    st.metric(
        "Estimated Cost",
        f"₹{estimated_cost:,}"
    )

    st.caption(
        "This is an approximate estimate based on the "
        "selected budget category and does not include "
        "long-distance travel such as flights or trains."
    )


    # ========================================================
    # DAILY ITINERARY
    # ========================================================

    st.subheader("🗓️ Daily Itinerary")

    for day_plan in itinerary:

        st.markdown(
            f"### Day {day_plan['day']} — "
            f"{day_plan['theme']}"
        )

        for place in day_plan["places"]:

            st.write(
                f"📍 **{place['name']}**"
            )

            st.write(
                f"   Activity: {place['activity']}"
            )

            st.write(
                f"   Duration: {place['duration']}"
            )

            st.write(
                f"   Entry cost: ₹{place['entry_cost']}"
            )

        st.divider()


    # ========================================================
    # TRAVEL TIPS
    # ========================================================

    st.subheader("💡 Travel Tips")

    for tip in destination_data["tips"]:

        st.write(
            f"✅ {tip}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🇮🇳 India Tourist Planner | "
    "Developed using Python and Streamlit"
)

