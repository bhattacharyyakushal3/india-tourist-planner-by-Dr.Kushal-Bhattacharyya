# ============================================================
# INDIA TOURIST PLANNER - BACKEND
# ============================================================

def get_destinations():

    return {

        "Kolkata": {
            "state": "West Bengal",
            "best_season": "October - March",
            "recommended_days": 3,
            "description": "Kolkata is famous for history, culture, colonial architecture and Bengali cuisine.",
            "places": [
                {"name": "Victoria Memorial", "duration": "2 hours", "activity": "Historical sightseeing", "entry_cost": 50},
                {"name": "Indian Museum", "duration": "2 hours", "activity": "Museum visit", "entry_cost": 50},
                {"name": "Howrah Bridge", "duration": "1 hour", "activity": "Photography", "entry_cost": 0},
                {"name": "Science City", "duration": "3 hours", "activity": "Science and educational visit", "entry_cost": 100},
                {"name": "Prinsep Ghat", "duration": "2 hours", "activity": "Riverfront sightseeing", "entry_cost": 0}
            ],
            "tips": [
                "Try Bengali cuisine.",
                "Visit Victoria Memorial in the morning.",
                "Use public transport for city travel."
            ]
        },

        "Darjeeling": {
            "state": "West Bengal",
            "best_season": "March - May and October - December",
            "recommended_days": 4,
            "description": "Darjeeling is famous for Himalayan views, tea gardens and the Darjeeling Himalayan Railway.",
            "places": [
                {"name": "Tiger Hill", "duration": "2 hours", "activity": "Sunrise and Himalayan views", "entry_cost": 50},
                {"name": "Batasia Loop", "duration": "1 hour", "activity": "Railway sightseeing", "entry_cost": 30},
                {"name": "Darjeeling Himalayan Railway", "duration": "3 hours", "activity": "Toy train journey", "entry_cost": 800},
                {"name": "Tea Garden", "duration": "2 hours", "activity": "Tea garden visit", "entry_cost": 100},
                {"name": "Himalayan Zoo", "duration": "2 hours", "activity": "Wildlife sightseeing", "entry_cost": 100},
                {"name": "Peace Pagoda", "duration": "1 hour", "activity": "Sightseeing", "entry_cost": 0}
            ],
            "tips": [
                "Carry warm clothing.",
                "Start early for Tiger Hill.",
                "Allow extra time for mountain traffic."
            ]
        },

        "Delhi": {
            "state": "Delhi",
            "best_season": "October - March",
            "recommended_days": 3,
            "description": "Delhi combines historical monuments, museums, markets and modern attractions.",
            "places": [
                {"name": "India Gate", "duration": "1 hour", "activity": "Sightseeing", "entry_cost": 0},
                {"name": "Red Fort", "duration": "2 hours", "activity": "Historical sightseeing", "entry_cost": 50},
                {"name": "Qutub Minar", "duration": "2 hours", "activity": "Historical sightseeing", "entry_cost": 40},
                {"name": "Humayun's Tomb", "duration": "2 hours", "activity": "Historical sightseeing", "entry_cost": 40},
                {"name": "Lotus Temple", "duration": "1 hour", "activity": "Architecture", "entry_cost": 0},
                {"name": "Akshardham Temple", "duration": "3 hours", "activity": "Cultural sightseeing", "entry_cost": 0}
            ],
            "tips": [
                "Use Delhi Metro.",
                "Carry water during summer.",
                "Check monument opening days."
            ]
        },

        "Jaipur": {
            "state": "Rajasthan",
            "best_season": "October - March",
            "recommended_days": 3,
            "description": "Jaipur, the Pink City, is famous for forts, palaces and Rajasthan's royal heritage.",
            "places": [
                {"name": "Amber Fort", "duration": "3 hours", "activity": "Fort sightseeing", "entry_cost": 100},
                {"name": "City Palace", "duration": "2 hours", "activity": "Palace sightseeing", "entry_cost": 200},
                {"name": "Hawa Mahal", "duration": "1 hour", "activity": "Architecture and photography", "entry_cost": 50},
                {"name": "Jantar Mantar", "duration": "1 hour", "activity": "Astronomical monument", "entry_cost": 50},
                {"name": "Jal Mahal", "duration": "1 hour", "activity": "Photography", "entry_cost": 0}
            ],
            "tips": [
                "Visit forts early.",
                "Try Rajasthani cuisine.",
                "Carry sunscreen."
            ]
        },

        "Mumbai": {
            "state": "Maharashtra",
            "best_season": "October - February",
            "recommended_days": 3,
            "description": "Mumbai is famous for its coastline, heritage architecture and cultural attractions.",
            "places": [
                {"name": "Gateway of India", "duration": "1 hour", "activity": "Historical sightseeing", "entry_cost": 0},
                {"name": "Marine Drive", "duration": "2 hours", "activity": "Seafront sightseeing", "entry_cost": 0},
                {"name": "CSMT", "duration": "1 hour", "activity": "Heritage sightseeing", "entry_cost": 0},
                {"name": "Elephanta Caves", "duration": "4 hours", "activity": "Cave sightseeing", "entry_cost": 40}
            ],
            "tips": [
                "Use local trains or Metro.",
                "Avoid peak traffic.",
                "Try local food."
            ]
        },

        "Goa": {
            "state": "Goa",
            "best_season": "November - February",
            "recommended_days": 4,
            "description": "Goa is famous for beaches, Portuguese heritage and coastal attractions.",
            "places": [
                {"name": "Baga Beach", "duration": "3 hours", "activity": "Beach activities", "entry_cost": 0},
                {"name": "Calangute Beach", "duration": "2 hours", "activity": "Beach sightseeing", "entry_cost": 0},
                {"name": "Basilica of Bom Jesus", "duration": "1 hour", "activity": "Heritage sightseeing", "entry_cost": 0},
                {"name": "Fort Aguada", "duration": "2 hours", "activity": "Fort sightseeing", "entry_cost": 20},
                {"name": "Dudhsagar Falls", "duration": "Full day", "activity": "Nature sightseeing", "entry_cost": 500}
            ],
            "tips": [
                "Carry sunscreen.",
                "Check weather before water activities.",
                "Keep sufficient travel time."
            ]
        },

        "Agra": {
            "state": "Uttar Pradesh",
            "best_season": "October - March",
            "recommended_days": 2,
            "description": "Agra is a major heritage destination and home to the Taj Mahal.",
            "places": [
                {"name": "Taj Mahal", "duration": "3 hours", "activity": "Heritage sightseeing", "entry_cost": 50},
                {"name": "Agra Fort", "duration": "2 hours", "activity": "Fort sightseeing", "entry_cost": 50},
                {"name": "Mehtab Bagh", "duration": "1 hour", "activity": "Taj Mahal viewpoint", "entry_cost": 30},
                {"name": "Itmad-ud-Daulah", "duration": "1 hour", "activity": "Historical sightseeing", "entry_cost": 30}
            ],
            "tips": [
                "Visit the Taj Mahal early.",
                "Check monument opening days.",
                "Carry water."
            ]
        },

        "Srinagar": {
            "state": "Jammu & Kashmir",
            "best_season": "April - October",
            "recommended_days": 4,
            "description": "Srinagar is famous for Dal Lake, houseboats, gardens and Himalayan scenery.",
            "places": [
                {"name": "Dal Lake", "duration": "3 hours", "activity": "Shikara ride", "entry_cost": 500},
                {"name": "Mughal Gardens", "duration": "2 hours", "activity": "Garden sightseeing", "entry_cost": 30},
                {"name": "Shankaracharya Temple", "duration": "2 hours", "activity": "Temple and mountain views", "entry_cost": 0},
                {"name": "Nishat Bagh", "duration": "1 hour", "activity": "Garden sightseeing", "entry_cost": 30}
            ],
            "tips": [
                "Carry suitable clothing.",
                "Check local travel conditions.",
                "Allow extra time for mountain journeys."
            ]
        },

        "Puri": {
            "state": "Odisha",
            "best_season": "October - February",
            "recommended_days": 3,
            "description": "Puri is known for the Jagannath Temple, beaches and nearby Konark.",
            "places": [
                {"name": "Jagannath Temple", "duration": "2 hours", "activity": "Temple visit", "entry_cost": 0},
                {"name": "Puri Beach", "duration": "2 hours", "activity": "Beach sightseeing", "entry_cost": 0},
                {"name": "Konark Sun Temple", "duration": "3 hours", "activity": "Heritage sightseeing", "entry_cost": 40},
                {"name": "Chandrabhaga Beach", "duration": "2 hours", "activity": "Beach sightseeing", "entry_cost": 0}
            ],
            "tips": [
                "Respect temple regulations.",
                "Visit beaches during morning or evening.",
                "Combine Puri with Konark."
            ]
        }
    }


# ============================================================
# ITINERARY GENERATOR
# ============================================================

def create_itinerary(destination, days, adults, children):

    destinations = get_destinations()

    if destination not in destinations:
        return []

    places = destinations[destination]["places"]

    itinerary = []

    themes = [
        "Major Attractions",
        "Historical & Cultural Exploration",
        "Nature & Local Experiences",
        "Leisure & Nearby Attractions",
        "Adventure & Exploration"
    ]

    expanded_places = []

    while len(expanded_places) < days * 2:
        expanded_places.extend(places)

    for day in range(days):

        start = day * 2
        selected = expanded_places[start:start + 2]

        itinerary.append({
            "day": day + 1,
            "theme": themes[day % len(themes)],
            "places": selected
        })

    return itinerary


# ============================================================
# COST CALCULATOR
# ============================================================

def calculate_estimated_cost(
    destination,
    days,
    adults,
    children,
    budget
):

    if budget == "Budget":

        hotel = 1000
        food = 500
        transport = 400

    elif budget == "Standard":

        hotel = 2500
        food = 1000
        transport = 700

    else:

        hotel = 5000
        food = 2000
        transport = 1500

    adult_daily = hotel + food + transport

    child_daily = (
        hotel * 0.60
        + food * 0.60
        + transport * 0.60
    )

    total = (
        adults * adult_daily * days
        + children * child_daily * days
    )

    destinations = get_destinations()

    if destination in destinations:

        places = destinations[destination]["places"]

        sightseeing = sum(
            place["entry_cost"]
            for place in places
        )

        total += sightseeing

    return int(total)