// src/components/Card.tsx
import React from 'react';

export const Card = ({ children, className = "" }: { children: React.ReactNode, className?: string }) => (
  <div className={`glass-panel overflow-hidden transition-all ${className}`}>
    {children}
  </div>
);

export const CardHeader = ({ children }: { children: React.ReactNode }) => (
  <div className="p-6 pb-2">{children}</div>
);

export const CardTitle = ({ children }: { children: React.ReactNode }) => (
  <h3 className="text-xl font-black italic uppercase tracking-tighter text-white">{children}</h3>
);

export const CardDescription = ({ children }: { children: React.ReactNode }) => (
  <p className="text-sm text-gray-400">{children}</p>
);

export const CardContent = ({ children }: { children: React.ReactNode }) => (
  <div className="p-6 pt-0">{children}</div>
);