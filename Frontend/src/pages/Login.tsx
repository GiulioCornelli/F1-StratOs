// src/pages/Login.tsx
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { login } from '../store/slices/authSlice';

const Login = () => {
  const [email, setEmail] = useState('');
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if(email) {
      dispatch(login(email));
      navigate('/home');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 relative overflow-hidden">
       {/* Blob di sfondo per dare profondità al vetro */}
       <div className="liquid-blob bg-f1-red/40 top-[20%] right-[30%] w-[300px] h-[300px]"></div>

      {/* APPLICAZIONE DELLA CLASSE GLASS-PANEL */}
      <div className="glass-panel p-12 w-full max-w-md relative z-10 border-t-4 border-t-f1-red">
        
        <h2 className="text-4xl font-black text-white mb-8 text-center italic tracking-tight">
          User <span className="text-f1-red">Login</span>
        </h2>
        
        <form onSubmit={handleLogin} className="space-y-8">
          <div>
            <label className="block text-gray-300 text-sm font-bold mb-3 ml-2 uppercase tracking-wider">Email dell'Utente</label>
            {/* APPLICAZIONE DELLA CLASSE GLASS-INPUT */}
            <input 
              type="email" 
              className="glass-input"
              placeholder="hamilton@mercedes.com"
              onChange={(e) => setEmail(e.target.value)}
            />
            <label className="block text-gray-300 text-sm font-bold mb-3 ml-2 uppercase tracking-wider">Password</label>
            <input 
              type="password" 
              className="glass-input"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          {/* APPLICAZIONE DELLA CLASSE BTN-LIQUID-PRIMARY */}
          <button className="btn-liquid-primary w-full">
            Login
          </button>
        </form>
        
      </div>
    </div>
  );
};

export default Login;