// src/store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    // Qui aggiungerai altri reducer in futuro: telemetry, circuits, ecc.
  },
  // Middleware opzionali (es. per logging o persistenza)
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false, // Spesso utile quando si gestiscono dati complessi di F1
    }),
});

// Esportiamo i tipi per TypeScript
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;