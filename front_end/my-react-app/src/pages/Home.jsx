import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {
  return (
    <>
      <Navbar />

      <div className="container">
        <h2>Welcome to Hotel Management System</h2>

        <p style={{ fontSize: "14px", color: "#555" }}>
          Manage your bookings, profile, and hotel services from one place.
        </p>

        <Link to="/register">
          <button>Create Account</button>
        </Link>

        <Link to="/login">
          <button className="btn-secondary">Sign In</button>
        </Link>

        <Link to="/profile">
          <button className="btn-secondary">View Profile</button>
        </Link>

        <Link to="/bookings">
          <button className="btn-secondary">View Bookings</button>
        </Link>
      </div>
    </>
  );
}

export default Home;
