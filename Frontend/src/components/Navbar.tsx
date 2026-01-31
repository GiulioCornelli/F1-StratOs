// src/components/Navbar.tsx
import { Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { logout } from '../store/slices/authSlice';

const Navbar = () => {
  const { isAuthenticated } = useSelector((state: any) => state.auth);
  const dispatch = useDispatch();

  return (
    // Navbar glassmorphism: sfondo semitrasparente + sfocatura + bordo sottile
    <nav className="fixed top-4 left-1/2 -translate-x-1/2 w-[95%] max-w-7xl z-50 bg-f1-card-a60/50 backdrop-blur-md border border-white/10 rounded-full px-8 py-4 flex justify-between items-center shadow-glass">     
      {
        isAuthenticated ? (
          <Link to="/home" className="text-2xl font-black text-white italic tracking-tighter drop-shadow-md">
            F1-<span className="text-f1-red">StratOS</span>
          </Link>
        ) : (
          <Link to="/" className="text-2xl font-black text-white italic tracking-tighter drop-shadow-md">
            F1-<span className="text-f1-red">StratOS</span>
          </Link>
        )
      }
      <div>
        {isAuthenticated ? (
          <button 
            onClick={() => dispatch(logout())}
            // Bottone ghost liquido
            className="btn-glass-ghost"
          >
            Logout
          </button>
        ) : (
          <Link to="/login" className="btn-liquid-primary py-3 px-8 text-sm">
            Login
          </Link>
        )}
      </div>
    </nav>
  );
};

export default Navbar;