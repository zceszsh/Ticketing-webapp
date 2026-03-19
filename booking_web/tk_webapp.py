from flask import Flask, request, render_template_string

app = Flask(__name__)

flights = [
    {"id": 1, "name": "Flight A", "time": "09:00", "seats": 3},
    {"id": 2, "name": "Flight B", "time": "11:30", "seats": 0},
    {"id": 3, "name": "Flight C", "time": "14:00", "seats": 2},
    {"id": 4, "name": "Flight D", "time": "17:30", "seats": 1},
]

ticket_options = {
    "single": {"label": "Single Ticket (1 passenger)", "count": 1},
    "double": {"label": "Double Ticket (2 passengers)", "count": 2},
    "triple": {"label": "Triple Ticket (3 passengers)", "count": 3},
    "four": {"label": "Four-Person Ticket (4 passengers)", "count": 4},
    "student": {"label": "Student Ticket (1 passenger)", "count": 1},
    "child": {"label": "Child Ticket (1 passenger)", "count": 1},
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>e-VTOL Booking Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f8fc;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 800px;
            margin: 40px auto;
            background: white;
            border-radius: 14px;
            padding: 30px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }
        h1 {
            text-align: center;
            color: #1d4f91;
        }
        label {
            font-weight: bold;
            display: block;
            margin-top: 15px;
            margin-bottom: 6px;
        }
        select, input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #cfd8e3;
            border-radius: 8px;
            font-size: 14px;
        }
        .passenger-box {
            border: 1px solid #dbe5ef;
            border-radius: 10px;
            padding: 15px;
            margin-top: 15px;
            background: #f9fbfd;
        }
        .policy {
            margin-top: 15px;
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            background: #fafafa;
            font-size: 14px;
            line-height: 1.6;
        }
        .checkbox-row {
            margin-top: 12px;
        }
        button {
            width: 100%;
            margin-top: 20px;
            padding: 12px;
            background: #1565c0;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #0f4fa0;
        }
        .message {
            margin-top: 20px;
            padding: 15px;
            border-radius: 10px;
        }
        .success {
            background: #e8f5e9;
            color: #1b5e20;
            border: 1px solid #a5d6a7;
        }
        .error {
            background: #ffebee;
            color: #b71c1c;
            border: 1px solid #ef9a9a;
        }
        .small {
            color: #666;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>e-VTOL Ticket Booking</h1>

        {% if message %}
            <div class="message {{ category }}">
                {{ message|safe }}
            </div>
        {% endif %}

        <form method="POST">
            <label for="ticket_type">Ticket Type</label>
            <select name="ticket_type" id="ticket_type" onchange="this.form.submit()">
                {% for key, value in ticket_options.items() %}
                    <option value="{{ key }}" {% if selected_ticket == key %}selected{% endif %}>
                        {{ value.label }}
                    </option>
                {% endfor %}
            </select>
            <div class="small">If a flight does not have enough seats, it will not appear in the list.</div>

            <label for="flight_id">Flight Time</label>
            <select name="flight_id" id="flight_id">
                {% if available_flights %}
                    {% for flight in available_flights %}
                        <option value="{{ flight.id }}">
                            {{ flight.name }} | Departure Time: {{ flight.time }} | Seats left: {{ flight.seats }}
                        </option>
                    {% endfor %}
                {% else %}
                    <option value="">No available flights for this ticket type</option>
                {% endif %}
            </select>

            {% for i in range(passenger_count) %}
                <div class="passenger-box">
                    <h3>Passenger {{ i + 1 }}</h3>
                    <label>Name</label>
                    <input type="text" name="name_{{ i }}" placeholder="Enter passenger name">

                    <label>ID Number</label>
                    <input type="text" name="id_{{ i }}" placeholder="Enter passport / ID number">
                </div>
            {% endfor %}

            <label>Safety & Privacy Agreement</label>
            <div class="policy">
                By booking this flight, the passenger confirms that all personal details and ID information
                entered are accurate and valid. The operator will use this information only for booking,
                safety verification, identity checks, and operational communication. The passenger confirms
                that they are fit to travel and acknowledges that pregnancy, heart disease, high blood
                pressure, or other serious medical conditions may require prior medical clearance or may
                affect eligibility to fly. Passengers must comply with baggage rules, health declarations,
                and all flight safety procedures.
            </div>

            <div class="checkbox-row">
                <input type="checkbox" name="agree" id="agree">
                <label for="agree" style="display:inline; font-weight:normal;">
                    I have read and agree to the Safety & Privacy Agreement
                </label>
            </div>

            <button type="submit" name="action" value="book">Book Now</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    category = ""
    selected_ticket = "single"

    if request.method == "POST":
        selected_ticket = request.form.get("ticket_type", "single")

    if selected_ticket not in ticket_options:
        selected_ticket = "single"

    passenger_count = ticket_options[selected_ticket]["count"]
    ticket_label = ticket_options[selected_ticket]["label"]

    available_flights = [f for f in flights if f["seats"] >= passenger_count]

    if request.method == "POST" and request.form.get("action") == "book":
        flight_id = request.form.get("flight_id")
        agree = request.form.get("agree")

        if not available_flights:
            message = "No flights are available for the selected ticket type."
            category = "error"
        elif not agree:
            message = "You must read and accept the Safety & Privacy Agreement before booking."
            category = "error"
        else:
            selected_flight = next((f for f in flights if str(f["id"]) == str(flight_id)), None)

            if not selected_flight or selected_flight["seats"] < passenger_count:
                message = "This flight is unavailable or does not have enough seats."
                category = "error"
            else:
                passengers = []
                missing = False

                for i in range(passenger_count):
                    name = request.form.get(f"name_{i}", "").strip()
                    id_num = request.form.get(f"id_{i}", "").strip()

                    if not name or not id_num:
                        missing = True
                        break

                    passengers.append(f"{i+1}. {name} | ID: {id_num}")

                if missing:
                    message = "Please complete all passenger names and ID numbers."
                    category = "error"
                else:
                    selected_flight["seats"] -= passenger_count
                    passenger_list = "<br>".join(passengers)
                    message = (
                        f"<b>Booking successful!</b><br><br>"
                        f"Ticket type: {ticket_label}<br>"
                        f"Flight: {selected_flight['name']} | Departure Time: {selected_flight['time']}<br><br>"
                        f"<b>Passengers:</b><br>{passenger_list}"
                    )
                    category = "success"
                    available_flights = [f for f in flights if f["seats"] >= passenger_count]

    return render_template_string(
        HTML,
        selected_ticket=selected_ticket,
        ticket_options=ticket_options,
        passenger_count=passenger_count,
        available_flights=available_flights,
        message=message,
        category=category,
    )

if __name__ == "__main__":
    app.run(debug=True)