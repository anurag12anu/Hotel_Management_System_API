import { useEffect, useState } from "react";
import API from "../api/api";

function Bookings() {
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    API.get("bookings/").then((res) => setBookings(res.data));
  }, []);

  return (
    <div>
      <h2>My Bookings</h2>
      {bookings.map((b) => (
        <div key={b.id}>
          <p>Room: {b.room_number}</p>
          <p>Check-in: {b.check_in}</p>
          <p>Check-out: {b.check_out}</p>
          <p>Total: ₹{b.total_price}</p>
        </div>
      ))}
    </div>
  );
}

export default Bookings;
