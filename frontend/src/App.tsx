import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AskPage from "./pages/AskPage";
import HistoryPage from "./pages/HistoryPage";
import Navbar from "./components/Navbar";

const App: React.FC = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<AskPage />} />
        <Route path="/history" element={<HistoryPage />} />
      </Routes>
    </Router>
  );
};

export default App;
