// src/App.tsx
import { createBrowserRouter, RouterProvider, Navigate, Outlet } from 'react-router-dom';

// librerie custom
import Root from './pages/Root';
import Login from './pages/Login';
import Home from './pages/Home';
import Drivers from './pages/Drivers';
import ProtectedRoute from './components/ProtectedRoute';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />, // Pagina di presentazione
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: '/home',
    element: (
      <ProtectedRoute>
        <Outlet /> 
      </ProtectedRoute>
    ),
    children: [
      { index: true, element: <Home /> },        // URL: /home (Dashboard principale)
      { path: 'drivers', element: <Drivers /> }, // URL: /home/drivers
      
    ],
  },
  {
    path: '*',
    element: <Navigate to="/" replace />, // Fallback per rotte inesistenti
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}