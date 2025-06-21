import React from "react";
import { Link } from "react-router-dom";

const Navbar: React.FC = () => (
    <nav style={{ padding: "1rem", background: "#eee", marginBottom: "2rem" }}>
        <Link to="/" style={{ marginRight: "1rem" }}>Ask</Link>
        <Link to="/history">History</Link>
    </nav>
);

export default Navbar;
