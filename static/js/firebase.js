// firebase.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-auth.js";

// Configuração do Firebase
const firebaseConfig = {
    apiKey: "AIzaSyD--bRxybPKnMVXK32a-TxJUZv9XYM_joQ",
    authDomain: "x-jao-faa0a.firebaseapp.com",
    projectId: "x-jao-faa0a",
    storageBucket: "x-jao-faa0a.firebasestorage.app",
    messagingSenderId: "157238814297",
    appId: "1:157238814297:web:fce1d3b623714a414eb348",
    measurementId: "G-JK1PFRDWK0"
};

// Inicializando o Firebase
const app = initializeApp(firebaseConfig);

// Exportando para ser usado em outros arquivos
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider, signInWithPopup };
