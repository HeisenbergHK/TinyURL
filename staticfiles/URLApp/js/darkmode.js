const body = document.getElementById('body');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

function applyTheme(mode) {
    const toggleBtn = document.querySelector('.btn-toggle');
    if (mode === 'dark') {
        body.classList.add('dark-mode');
        body.classList.remove('light-mode');
        toggleBtn.textContent = '🌞';
        toggleBtn.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        toggleBtn.textContent = '🌙';
        toggleBtn.classList.remove('dark-mode');
    }

    document.querySelectorAll('.card, .form-control, .navbar').forEach(el => {
        el.classList.toggle('dark-mode', mode === 'dark');
    });
}

function toggleDarkMode() {
    const current = localStorage.getItem('theme') || 'light';
    const newTheme = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', newTheme);
    applyTheme(newTheme);
}

document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('theme') || (prefersDark ? 'dark' : 'light');
    applyTheme(saved);
});

document.querySelectorAll('.card, .form-control, .navbar').forEach(el => {
    if (mode === 'dark') {
        el.classList.add('dark-mode');
    } else {
        el.classList.remove('dark-mode');
    }
});