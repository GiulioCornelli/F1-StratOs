// src/pages/Home.tsx
// import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

// librerie custom
import Navbar from '../components/Navbar';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/Card';



const Home = () => {
  // const user = useSelector((state: any) => state.auth.user);

  return (
    <>
      <Navbar />
      
      {/* 1. Il contenitore 'main' aggiunge il padding per non finire sotto la Navbar */}
      <main className="min-h-screen pt-32 px-6 md:px-12 max-w-7xl mx-auto">
        
        {/* 2. Titolo della pagina per dare respiro al layout */}
        <header className="mb-10">
          <h1 className="text-3xl font-black italic uppercase text-white">
            Paddock <span className="text-f1-red">Control</span>
          </h1>
        </header>

        {/* 3. UN SOLO div 'grid' che contiene TUTTE le Card */}
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          
          {/* Card 1: Piloti */}
          <Card className="glass-card transition-all hover:scale-[1.02] hover:shadow-2xl">
            <CardHeader>
              <CardTitle>Piloti</CardTitle>
              <CardDescription>Visualizza la griglia di partenza</CardDescription>
            </CardHeader>
            <CardContent>
              <Link to="/home/drivers">
                <button className="btn-liquid-primary w-full py-4 uppercase font-black italic tracking-widest">
                  Vedi Piloti
                </button>
              </Link>
            </CardContent>
          </Card>

          <Card className="glass-card opacity-50 grayscale hover:grayscale-0 transition-all">
            <CardHeader>
              <CardTitle>Gare Live</CardTitle>
              <CardDescription>Gare Live</CardDescription>
            </CardHeader>
            <CardContent>
               <div className="h-24 flex items-center justify-center border-2 border-dashed border-white/10 rounded-2xl">
                  <span className="text-[10px] uppercase font-bold text-gray-500">Coming Soon</span>
               </div>
            </CardContent>
          </Card>         

          <Card className="glass-card opacity-50 grayscale hover:grayscale-0 transition-all">
            <CardHeader>
              <CardTitle>Circuiti</CardTitle>
              <CardDescription>Mappe e statistiche piste</CardDescription>
            </CardHeader>
            <CardContent>
               <div className="h-24 flex items-center justify-center border-2 border-dashed border-white/10 rounded-2xl">
                  <span className="text-[10px] uppercase font-bold text-gray-500">Coming Soon</span>
               </div>
            </CardContent>
          </Card>

        </div>
      </main>
    </>
  );
};

export default Home;