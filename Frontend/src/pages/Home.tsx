// src/pages/Home.tsx
// import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

// librerie custom
import Navbar from '../components/Navbar';



const Home = () => {
  // const user = useSelector((state: any) => state.auth.user);

  return (
    <>
      <Navbar />
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <Card className="glass-card transition-all hover:scale-[1.02] hover:shadow-2xl">
            <CardHeader>
              <CardTitle>Gare Live</CardTitle>
              <CardDescription>Dati in tempo reale delle gare</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex h-24 items-center justify-center rounded-2xl bg-muted/50">
                <p className="text-sm text-muted-foreground">Contenuto in arrivo...</p>
              </div>
            </CardContent>
          </Card>
        </div>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <Card className="glass-card transition-all hover:scale-[1.02] hover:shadow-2xl">
            <CardHeader>
              <CardTitle>Piloti</CardTitle>
              <CardDescription>Dati in tempo reale delle gare</CardDescription>
            </CardHeader>
            <CardContent>
              <Link to="/home/drivers">
                <button className="btn-liquid-primary w-full">
                  Vedi Piloti
                </button>
              </Link>
            </CardContent>
          </Card>
        </div>
    </>
  );
};

export default Home;