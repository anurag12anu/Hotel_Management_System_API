function Navbar() {
  return (
    <div className="navbar">
      <div className="nav-left">Hotel Management</div>

      <div className="nav-right">
        <a href="/profile">Profile</a>
        <a href="/bookings">Bookings</a>
        <a href="/login">Logout</a>
      </div>
    </div>
  );
}

export default Navbar;
