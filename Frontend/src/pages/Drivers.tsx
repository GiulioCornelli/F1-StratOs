// librerie esterne
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

// librerie custom
import type { Driver } from "../types/driver";
import CarDriver from "../components/CarDriver";
import Navbar from "../components/Navbar";

const Drivers = () => {
    const [drivers, setDrivers] = useState<Driver[]>([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchDrivers = async () => {
            const host = "localhost";
            const port = 8070;
            const url = `http://${host}:${port}/api/drivers/getAllDrivers`;
            
            try {
                const res = await axios.get(url);
                
                // Gestione caso: Dati assenti o array vuoto
                if (!res.data || res.data.length === 0) {
                    throw new Error("No drivers found in the database");
                }

                setDrivers(res.data);
            } catch (error) {
                // 1. Print dell'eccezione in console
                console.error("F1-StratOS Error Fetching Drivers:", error);
                
                // 2. Alert Errore 500 (o errore generico di connessione)
                alert("Errore 500: Impossibile recuperare i dati dei piloti.");
                
                // 3. Ritorno alla Home
                navigate("/home");
            }
        };

        fetchDrivers();
    }, [navigate]);

    return (
        <>
            <div className="min-h-screen relative overflow-hidden bg-[#0b0b0b]">
                <Navbar />
                
                <div className="liquid-blob bg-f1-red/20 top-[10%] left-[-5%] w-[400px] h-[400px]" />
                
                <main className="relative z-10 pt-32 px-8 max-w-7xl mx-auto">
                    <header className="mb-12">
                        <h1 className="text-5xl font-black italic uppercase tracking-tighter text-white">
                            Grid <span className="text-f1-red">Lineup</span>
                        </h1>
                        <p className="text-gray-400 mt-2 uppercase tracking-widest text-sm font-bold">
                            Sessione 2026 - Live Data
                        </p>
                    </header>

                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
                        {drivers.map((d) => (
                            <CarDriver key={d.driver_number} driver={d} />
                        ))}
                    </div>
                </main>
            </div>
        </>
    );
};

export default Drivers;