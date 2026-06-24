import { NavLink } from "react-router-dom";

const Header = () => {
  const navStyle = ({ isActive }) =>
    `px-4 py-2 rounded-lg font-medium transition-all duration-300 ${
      isActive
        ? "bg-blue-600 text-white"
        : "bg-gray-100 text-gray-700 hover:bg-blue-500 hover:text-white"
    }`;

  return (
    <header className="w-full bg-white shadow-md">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">
        
        {/* Logo */}
        <h1 className="text-3xl font-bold text-blue-600">
          AI Agent
        </h1>

        {/* Navigation */}
        <nav>
          <ul className="flex gap-4 flex-wrap">
            <li>
              <NavLink to="/" className={navStyle}>
                Home
              </NavLink>
            </li>

            <li>
              <NavLink to="/marketplace" className={navStyle}>
                Marketplace
              </NavLink>
            </li>

            <li>
              <NavLink to="/agentic" className={navStyle}>
                Agentic AI
              </NavLink>
            </li>

            <li>
              <NavLink to="/setting" className={navStyle}>
                Settings
              </NavLink>
            </li>

            <li>
              <NavLink to="/about-me" className={navStyle}>
                About Me
              </NavLink>
            </li>
          </ul>
        </nav>

      </div>
    </header>
  );
};

export default Header;