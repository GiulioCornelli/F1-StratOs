// src/pages/Root.tsx
import Navbar from '../components/Navbar';

const Root = () => {
  return (
    // Aggiungiamo overflow-hidden per contenere i blob sfocati
    <div className="min-h-screen relative overflow-hidden">
      {/* Elementi decorativi di sfondo (Liquid Blobs) */}
      <div className="liquid-blob bg-f1-red top-[-10%] left-[-10%] w-[500px] h-[500px]"></div>
      <div className="liquid-blob bg-blue-600 bottom-[-10%] right-[-10%] w-[600px] h-[600px] animation-delay-2000"></div>

      <Navbar />

      <main className="relative z-10 flex flex-col items-center justify-center pt-40 px-4 text-center">
        {/* Esempio di glass-panel leggero per il titolo */}
        <div className="glass-panel-light p-10 mb-8 inline-block">
          <h1 className="text-6xl md:text-8xl font-black italic tracking-tighter uppercase drop-shadow-lg">
            F1-<span className="text-transparent bg-clip-text bg-gradient-to-r from-f1-red to-orange-500">StratOS</span>
          </h1>
        </div>

        <p className="text-xl text-gray-300 max-w-2xl mb-12 font-medium leading-relaxed ">
          Domina la pista con l'analisi dei dati in tempo reale.
          Telemetria, strategie e performance dei piloti in un'interfaccia fluida.
        </p>


      </main>
    </div>
  );
};

export default Root;