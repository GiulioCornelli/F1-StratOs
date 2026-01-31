// src/pages/Home.tsx
import { useSelector } from 'react-redux';
import Navbar from '../components/Navbar';

const Home = () => {
  const user = useSelector((state: any) => state.auth.user);

  return (
    <div className="min-h-screen bg-[#0b0b0b] text-white">
      <Navbar />
      <div className="p-8 pt-24">
        <h1 className="text-3xl font-bold mb-6">Bentornato, <span className="text-[#E10600]">{user}</span></h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Mockup di card dati */}
          {[1, 2, 3].map((i) => (
            <div key={i} className="bg-[#15151E] p-6 rounded-xl border border-gray-800 hover:border-[#E10600] transition-colors">
              <p className="text-gray-400 text-sm uppercase">Telemetria Slot {i}</p>
              <p className="text-2xl font-mono mt-2">--:--:---</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;