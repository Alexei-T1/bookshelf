

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modal');
    const openBtn = document.getElementById('open-modal-btn');

    if (!modal) return;

    const openModal = () => modal.classList.add('modal--open');
    const closeModal = () => modal.classList.remove('modal--open');

    // Открыть по кнопке
    if (openBtn) {
        openBtn.addEventListener('click', openModal);
    }

    // Закрыть по кнопкам с data-close-modal (оверлей и "Отмена")
    modal.querySelectorAll('[data-close-modal]').forEach(el => {
        el.addEventListener('click', closeModal);
    });

    // Закрыть по Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('modal--open')) {
            window.location.href = '/books/';
        }
    });
});