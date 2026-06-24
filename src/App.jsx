import { Routes, Route, useLocation } from "react-router-dom";

import Header from "./components/header";
import Chatbot from "./components/chatbot";

import Home from "./features/home";
import Marketplace from "./features/marketplace";
import Agentic from "./features/agentic";
import Setting from "./features/setting";
import AboutMe from "./features/about_me";

function App() {
  const location = useLocation();

  return (
    <div className="min-h-screen bg-slate-100">
      <Header />

      <main className="p-4">
        {location.pathname === "/" ? (
          <Chatbot />
        ) : (
          <Routes>
            <Route path="/home" element={<Home />} />
            <Route path="/marketplace" element={<Marketplace />} />
            <Route path="/agentic" element={<Agentic />} />
            <Route path="/setting" element={<Setting />} />
            <Route path="/about-me" element={<AboutMe />} />
          </Routes>
        )}
      </main>
    </div>
  );
}

export default App;