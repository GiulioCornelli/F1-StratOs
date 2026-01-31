// src/components/CarDriver.tsx
import type { Driver } from "../types/driver";

interface Props {
  driver: Driver;
}

function CarDriver({driver}: Props) {
  // Prepariamo il colore del team (es: #FF0000) aggiungendo l'hash se manca
  const teamColor = driver.team_colour ? `#${driver.team_colour}` : '#E10600';

  return (
    <div className="glass-panel group relative p-5 transition-all duration-500 hover:-translate-y-2 hover:shadow-glass-hover">
      
      {/* Glow d'accento liquido in alto a destra basato sul team */}
      <div 
        className="absolute -top-10 -right-10 w-32 h-32 blur-[60px] opacity-20 group-hover:opacity-50 transition-opacity duration-500"
        style={{ backgroundColor: teamColor }}
      />

      <div className="flex flex-col items-center gap-4">
        
        {/* Container Immagine Smussato */}
        <div className="relative">
          <div className="w-28 h-28 rounded-liquid overflow-hidden border border-white/10 bg-gradient-to-b from-white/5 to-transparent p-1">
            <img 
              src={driver.headshot_url} 
              alt={driver.full_name} 
              className="w-full h-full object-cover rounded-[3.5rem]" 
            />
          </div>
          {/* Badge Numero Pilota */}
          <div className="absolute -bottom-2 -right-1 bg-f1-red text-white text-xs font-black italic px-3 py-1 rounded-full shadow-lg border border-white/20">
            {driver.driver_number}
          </div>
        </div>

        {/* Info Box */}
        <div className="text-center w-full">
          <p className="text-lg font-black italic uppercase tracking-tighter text-white">
            {driver.first_name} <span className="text-f1-red">{driver.last_name}</span>
          </p>
          
          <div className="flex items-center justify-center gap-2 mt-1">
            <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-400">
              {driver.team_name}
            </p>
            {driver.country_code && (
              <span className="text-[10px] bg-white/10 px-2 py-0.5 rounded-md text-gray-300 font-mono border border-white/5">
                {driver.country_code}
              </span>
            )}
          </div>
        </div>

      </div>
    </div>
  );
}

export default CarDriver;