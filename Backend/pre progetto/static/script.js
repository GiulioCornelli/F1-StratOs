
const API_URL = ""; // Lascia vuoto se il frontend è servito dallo stesso server

function showForm(type) {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');
    const msg = document.getElementById('response-msg');

    msg.className = 'message';
    msg.textContent = '';

    if (type === 'login') {
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
        tabLogin.classList.add('active');
        tabRegister.classList.remove('active');
    } else {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
        tabLogin.classList.remove('active');
        tabRegister.classList.add('active');
    }
}

// Gestione Login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    const msg = document.getElementById('response-msg');

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            msg.textContent = `Benvenuto, ${data.nome}! Login effettuato.`;
            msg.className = 'message success';
        } else {
            msg.textContent = data.detail || 'Errore nel login';
            msg.className = 'message error';
        }
    } catch (err) {
        msg.textContent = 'Errore di connessione al server';
        msg.className = 'message error';
    }
});

// Gestione Registrazione
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const msg = document.getElementById('response-msg');

    const payload = {
        nome: document.getElementById('reg-nome').value,
        cognome: document.getElementById('reg-cognome').value,
        email: document.getElementById('reg-email').value,
        paese: document.getElementById('reg-paese').value,
        regione: document.getElementById('reg-regione').value,
        citta: document.getElementById('reg-citta').value,
        password: document.getElementById('reg-password').value,
        id_privilegio: 1
    };

    try {
        const response = await fetch(`${API_URL}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            msg.textContent = 'Registrazione completata! Ora puoi fare il login.';
            msg.className = 'message success';
            setTimeout(() => showForm('login'), 2000);
        } else {
            msg.textContent = data.detail || 'Errore nella registrazione';
            msg.className = 'message error';
        }
    } catch (err) {
        msg.textContent = 'Errore di connessione al server';
        msg.className = 'message error';
    }
});
