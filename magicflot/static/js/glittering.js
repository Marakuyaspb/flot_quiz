const numStars = 100; // Number of stars
    const stars = document.getElementById('stars');

    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.top = Math.floor(Math.random() * 100) + '%';
        star.style.left = Math.floor(Math.random() * 100) + '%';
        star.style.animationDelay = Math.random() + 's';
        stars.appendChild(star);
    }