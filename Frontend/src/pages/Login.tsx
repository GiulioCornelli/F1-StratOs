// src/pages/Login.tsx
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { login } from '../store/slices/authSlice';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

  // Campi registrazione
  const [nome, setNome] = useState('');
  const [cognome, setCognome] = useState('');
  const [paese, setPaese] = useState('');
  const [regione, setRegione] = useState('');
  const [citta, setCitta] = useState('');

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8070/api/auth/login', {
        email,
        password
      });

      const { id_utente, nome } = response.data;
      dispatch(login({ id_utente, nome, email }));
      navigate('/home');
    } catch (error: any) {
      alert(error.response?.data?.detail || 'Errore durante il login');
    }
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8070/api/auth/register', {
        nome,
        cognome,
        email,
        paese,
        regione,
        citta,
        password,
        id_privilegio: 1
      });
      alert('Registrazione completata! Ora puoi effettuare il login.');
      setIsRegistering(false);
    } catch (error: any) {
      alert(error.response?.data?.detail || 'Errore durante la registrazione');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 relative overflow-hidden">
      {/* Blob di sfondo per dare profondità al vetro */}
      <div className="liquid-blob bg-f1-red/40 top-[20%] right-[30%] w-[300px] h-[300px]"></div>

      {/* APPLICAZIONE DELLA CLASSE GLASS-PANEL */}
      <div className="glass-panel p-12 w-full max-w-md relative z-10 border-t-4 border-t-f1-red">

        <h2 className="text-4xl font-black text-white mb-8 text-center italic tracking-tight">
          User <span className="text-f1-red">{isRegistering ? 'Register' : 'Login'}</span>
        </h2>

        <form onSubmit={isRegistering ? handleRegister : handleLogin} className="space-y-6">
          {isRegistering && (
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Nome</label>
                <input
                  type="text"
                  className="glass-input py-2"
                  placeholder="Max"
                  value={nome}
                  onChange={(e) => setNome(e.target.value)}
                  required
                />
              </div>
              <div>
                <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Cognome</label>
                <input
                  type="text"
                  className="glass-input py-2"
                  placeholder="Verstappen"
                  value={cognome}
                  onChange={(e) => setCognome(e.target.value)}
                  required
                />
              </div>
            </div>
          )}

          <div>
            <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Email</label>
            <input
              type="email"
              className="glass-input py-2"
              placeholder="hamilton@mercedes.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          {isRegistering && (
            <>
              <div className="grid grid-cols-3 gap-2">
                <div>
                  <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Paese</label>
                  <input
                    type="text"
                    className="glass-input py-2 text-sm"
                    placeholder="Italia"
                    value={paese}
                    onChange={(e) => setPaese(e.target.value)}
                    required
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Regione</label>
                  <input
                    type="text"
                    className="glass-input py-2 text-sm"
                    placeholder="Lombardia"
                    value={regione}
                    onChange={(e) => setRegione(e.target.value)}
                    required
                  />
                </div>
                <div>
                  <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Città</label>
                  <input
                    type="text"
                    className="glass-input py-2 text-sm"
                    placeholder="Monza"
                    value={citta}
                    onChange={(e) => setCitta(e.target.value)}
                    required
                  />
                </div>
              </div>
            </>
          )}

          <div>
            <label className="block text-gray-400 text-xs font-bold mb-1 ml-2 uppercase tracking-wider">Password</label>
            <input
              type="password"
              className="glass-input py-2"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn-liquid-primary w-full mt-4">
            {isRegistering ? 'Crea Account' : 'Accedi'}
          </button>
        </form>

        <div className="mt-8 text-center">
          <button
            onClick={() => setIsRegistering(!isRegistering)}
            className="text-gray-400 hover:text-f1-red text-sm font-medium transition-colors"
          >
            {isRegistering
              ? 'Hai già un account? Accedi'
              : 'Non hai un account? Registrati ora'}
          </button>
        </div>

      </div>
    </div>
  );
};

export default Login;














































































//giada