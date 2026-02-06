import Navbar from "../components/Navbar";

function Bookings() {
  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Your Bookings</h2>

        <table>
          <thead>
            <tr>
              <th>Room</th>
              <th>Check-in</th>
              <th>Check-out</th>
              <th>Total Price</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>101</td>
              <td>2026-02-10</td>
              <td>2026-02-12</td>
              <td>₹4000</td>
            </tr>
          </tbody>
        </table>
      </div>
    </>
  );
}

export default Bookings;
