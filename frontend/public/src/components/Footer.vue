<template>
    <footer class="footer">
        <div class="footer-grid">
            <nav class="footer-links">
            <RouterLink to="/about">Про нас</RouterLink>
            <RouterLink to="/delivery">Доставка</RouterLink>
            <RouterLink to="/items">Товари</RouterLink>
            <a href="mailto:contact@evimora.com">contact@evimora.com</a>
            </nav>
    
            <div class="social-icons">
            <a href="#" target="_blank" aria-label="Telegram">
                <img src="https://cdn.simpleicons.org/telegram/0088cc" alt="Telegram" />
            </a>
            <a href="#" target="_blank" aria-label="Instagram">
                <img src="https://cdn.simpleicons.org/instagram/E4405F" alt="Instagram" />
            </a>
            <a href="#" target="_blank" aria-label="Facebook">
                <img src="https://cdn.simpleicons.org/facebook/1877F2" alt="Facebook" />
            </a>
            </div>
        </div>

        <p class="copyright">© 2025 Evimora. Всі права захищені.</p>
    </footer>
</template>

<script setup>
    import { RouterLink } from 'vue-router';
</script>

<style scoped>
.footer {
    background-color: #fff;
    box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.06);
    color: black;
    padding: 24px 16px;
    text-align: center;
    font-size: 14px;
    border-top: 1px solid #e0e0e0;
    margin-top: 100px;
}

.footer-grid {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    max-width: 1200px;
    margin: 0 auto 12px;
    padding: 0 10px;
    gap: 12px;
}

.footer-links {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: flex-start;
}

.footer-links a {
    color: #1a1a1a;
    text-decoration: none;
    transition: color 0.3s;
}

.footer-links a:hover {
    color: #216f5b;
}

.social-icons {
    display: flex;
    gap: 16px;
    justify-content: flex-end;
}

.social-icons img {
    width: 24px;
    height: 24px;
    transition: transform 0.3s ease, opacity 0.3s;
    cursor: pointer;
}

.social-icons img:hover {
    transform: scale(1.2);
    opacity: 0.8;
}

.copyright {
    margin-top: 20px;
}
@media (max-width: 768px) {
    .footer-grid {
        flex-direction: column;
        align-items: center;
    }

    .footer-links {
        justify-content: center;
    }

    .social-icons {
        justify-content: center;
        margin-top: 10px;
    }
}
</style>
