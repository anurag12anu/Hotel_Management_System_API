import { useState } from "react";
import API from "../api/api";
import Navbar from "../components/Navbar";

function Login() {
  const [form, setForm] = useState({ username: "", password: "" });

  const submit = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("login/", form);
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      window.location.href = "/profile";
    } catch {
      alert("Invalid username or password");
    }
  };

  return (
    <>
      <Navbar />
      <div className="container">
        <h2>Sign in</h2>

        <form onSubmit={submit}>
          <input
            placeholder="Username"
            value={form.username}
            onChange={(e) => setForm({ ...form, username: e.target.value })}
          />

          <input
            type="password"
            placeholder="Password"
            value={form.password}
            onChange={(e) => setForm({ ...form, password: e.target.value })}
          />

          <button type="submit">Sign In</button>
        </form>
      </div>
    </>
  );
}

export default Login;
