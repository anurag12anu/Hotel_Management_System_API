import { useState } from "react";
import API from "../api/api";
import Navbar from "../components/Navbar";

function Register() {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
  });

  const submit = async (e) => {
    e.preventDefault();
    try {
      await API.post("register/", form);
      window.location.href = "/login";
    } catch {
      alert("Registration failed");
    }
  };

  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Create account</h2>

        <form onSubmit={submit}>
          <input
            placeholder="Username"
            value={form.username}
            onChange={(e) => setForm({ ...form, username: e.target.value })}
          />

          <input
            placeholder="Email"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
          />

          <input
            type="password"
            placeholder="Password"
            value={form.password}
            onChange={(e) => setForm({ ...form, password: e.target.value })}
          />

          <button type="submit">Create account</button>
        </form>
      </div>
    </>
  );
}

export default Register;
