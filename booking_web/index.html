<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>e-VTOL Booking Website</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f8fc;
      margin: 0;
      padding: 0;
    }

    .container {
      width: min(800px, 92%);
      margin: 40px auto;
      background: white;
      border-radius: 14px;
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }

    h1 {
      text-align: center;
      color: #1d4f91;
      margin-top: 0;
    }

    label {
      font-weight: bold;
      display: block;
      margin-top: 15px;
      margin-bottom: 6px;
    }

    select,
    input[type="text"] {
      width: 100%;
      padding: 10px;
      border: 1px solid #cfd8e3;
      border-radius: 8px;
      font-size: 14px;
      box-sizing: border-box;
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

    .secondary-btn {
      background: #6b7280;
      margin-top: 10px;
    }

    .secondary-btn:hover {
      background: #4b5563;
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
      margin-top: 6px;
    }

    h3 {
      margin-top: 0;
      color: #1d4f91;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>e-VTOL Ticket Booking</h1>

    <div id="messageBox"></div>

    <form id="bookingForm">
      <label for="ticket_type">Ticket Type</label>
      <select name="ticket_type" id="ticket_type"></select>
      <div class="small">
        If a flight does not have enough seats, it will not appear in the list.
      </div>

      <label for="flight_id">Flight Time</label>
      <select name="flight_id" id="flight_id"></select>

      <div id="passengerFields"></div>

      <label>Safety & Privacy Agreement</label>
      <div class="policy">
        By booking this flight, the passenger confirms that all personal details and ID information
        entered are accurate and valid. The operator will use this information only for booking,
        safety verification, identity checks, and operational communication. The passenger confirms
        that they are fit to travel and acknowledges that pregnancy, heart disease, high blood
        pressure, or other serious medical conditions may require prior medical clearance or may
        affect eligibility to fly. Passengers must comply with baggage rules, health declarations,
        and all flight safety procedures. (Disclaimer: this is for illustration purposes only and
        does not represent a real agreement.)
      </div>

      <div class="checkbox-row">
        <input type="checkbox" name="agree" id="agree" />
        <label for="agree" style="display:inline; font-weight:normal;">
          I have read and agree to the Safety & Privacy Agreement
        </label>
      </div>

      <button type="submit">Book Now</button>
      <button type="button" class="secondary-btn" id="resetBtn">Reset Flight Data</button>
    </form>
  </div>

  <script>
    const defaultFlights = [
      { id: 1, name: "Flight A", time: "09:00", seats: 3 },
      { id: 2, name: "Flight B", time: "11:30", seats: 0 },
      { id: 3, name: "Flight C", time: "14:00", seats: 2 },
      { id: 4, name: "Flight D", time: "17:30", seats: 1 }
    ];

    const ticketOptions = {
      single_short: { label: "Single Ticket - Short Trip: 399 GBP (1 passenger)", count: 1 },
      double_short: { label: "Double Ticket - Short Trip: 368 GBP (2 passengers)", count: 2 },
      triple_short: { label: "Triple Ticket - Short Trip: 388 GBP (3 passengers)", count: 3 },
      four_short: { label: "Four-Person Ticket - Short Trip: 399 GBP (4 passengers)", count: 4 },
      single_long: { label: "Single Ticket - Long Trip: 749 GBP (1 passenger)", count: 1 },
      double_long: { label: "Double Ticket - Long Trip: 768 GBP (2 passengers)", count: 2 },
      triple_long: { label: "Triple Ticket - Long Trip: 788 GBP (3 passengers)", count: 3 },
      four_long: { label: "Four-Person Ticket - Long Trip: 799 GBP (4 passengers)", count: 4 }
    };

    const DEFAULT_TICKET = "single_short";
    const STORAGE_KEY = "evtol_flights_data";

    function getFlights() {
      const saved = localStorage.getItem(STORAGE_KEY);
      return saved ? JSON.parse(saved) : [...defaultFlights];
    }

    function saveFlights(flights) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(flights));
    }

    function resetFlights() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(defaultFlights));
    }

    function showMessage(message, category) {
      const messageBox = document.getElementById("messageBox");
      if (!message) {
        messageBox.innerHTML = "";
        return;
      }
      messageBox.innerHTML = `<div class="message ${category}">${message}</div>`;
    }

    function populateTicketOptions() {
      const ticketSelect = document.getElementById("ticket_type");
      ticketSelect.innerHTML = "";

      for (const key in ticketOptions) {
        const option = document.createElement("option");
        option.value = key;
        option.textContent = ticketOptions[key].label;
        ticketSelect.appendChild(option);
      }
    }

    function getSelectedTicket() {
      const selected = document.getElementById("ticket_type").value || DEFAULT_TICKET;
      return ticketOptions[selected] ? selected : DEFAULT_TICKET;
    }

    function renderFlights() {
      const flights = getFlights();
      const selectedTicket = getSelectedTicket();
      const passengerCount = ticketOptions[selectedTicket].count;
      const flightSelect = document.getElementById("flight_id");

      const availableFlights = flights.filter(f => f.seats >= passengerCount);

      flightSelect.innerHTML = "";

      if (availableFlights.length === 0) {
        const option = document.createElement("option");
        option.value = "";
        option.textContent = "No available flights for this ticket type";
        flightSelect.appendChild(option);
      } else {
        availableFlights.forEach(flight => {
          const option = document.createElement("option");
          option.value = flight.id;
          option.textContent = `${flight.name} | Departure Time: ${flight.time} | Seats left: ${flight.seats}`;
          flightSelect.appendChild(option);
        });
      }
    }

    function renderPassengerFields() {
      const selectedTicket = getSelectedTicket();
      const passengerCount = ticketOptions[selectedTicket].count;
      const container = document.getElementById("passengerFields");
      container.innerHTML = "";

      for (let i = 0; i < passengerCount; i++) {
        const box = document.createElement("div");
        box.className = "passenger-box";
        box.innerHTML = `
          <h3>Passenger ${i + 1}</h3>
          <label>Name</label>
          <input type="text" name="name_${i}" placeholder="Enter passenger name" />

          <label>ID Number</label>
          <input type="text" name="id_${i}" placeholder="Enter passport / ID number" />
        `;
        container.appendChild(box);
      }
    }

    function refreshUI(clearMessage = true) {
      if (clearMessage) showMessage("", "");
      renderPassengerFields();
      renderFlights();
    }

    function handleBooking(event) {
      event.preventDefault();

      const flights = getFlights();
      const selectedTicket = getSelectedTicket();
      const passengerCount = ticketOptions[selectedTicket].count;
      const ticketLabel = ticketOptions[selectedTicket].label;
      const flightId = document.getElementById("flight_id").value;
      const agree = document.getElementById("agree").checked;

      const availableFlights = flights.filter(f => f.seats >= passengerCount);

      if (availableFlights.length === 0) {
        showMessage("No flights are available for the selected ticket type.", "error");
        return;
      }

      if (!agree) {
        showMessage("You must read and accept the Safety & Privacy Agreement before booking.", "error");
        return;
      }

      const selectedFlight = flights.find(f => String(f.id) === String(flightId));

      if (!selectedFlight || selectedFlight.seats < passengerCount) {
        showMessage("This flight is unavailable or does not have enough seats.", "error");
        return;
      }

      const passengers = [];

      for (let i = 0; i < passengerCount; i++) {
        const nameField = document.querySelector(`[name="name_${i}"]`);
        const idField = document.querySelector(`[name="id_${i}"]`);

        const name = nameField ? nameField.value.trim() : "";
        const idNum = idField ? idField.value.trim() : "";

        if (!name || !idNum) {
          showMessage("Please complete all passenger names and ID numbers.", "error");
          return;
        }

        passengers.push(`${i + 1}. ${name} | ID: ${idNum}`);
      }

      selectedFlight.seats -= passengerCount;
      saveFlights(flights);

      const passengerList = passengers.join("<br>");
      showMessage(
        `<b>Booking successful!</b><br><br>
         Ticket type: ${ticketLabel}<br>
         Flight: ${selectedFlight.name} | Departure Time: ${selectedFlight.time}<br><br>
         <b>Passengers:</b><br>${passengerList}`,
        "success"
      );

      document.getElementById("bookingForm").reset();
      document.getElementById("ticket_type").value = DEFAULT_TICKET;
      refreshUI(false);
    }

    document.getElementById("ticket_type").addEventListener("change", () => {
      refreshUI();
    });

    document.getElementById("bookingForm").addEventListener("submit", handleBooking);

    document.getElementById("resetBtn").addEventListener("click", () => {
      resetFlights();
      document.getElementById("bookingForm").reset();
      document.getElementById("ticket_type").value = DEFAULT_TICKET;
      refreshUI();
      showMessage("Flight data has been reset.", "success");
    });

    populateTicketOptions();
    document.getElementById("ticket_type").value = DEFAULT_TICKET;

    if (!localStorage.getItem(STORAGE_KEY)) {
      saveFlights(defaultFlights);
    }

    refreshUI();
  </script>
</body>
</html>
