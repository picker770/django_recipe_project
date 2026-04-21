const search = document.getElementById('search');

search.addEventListener('keyup', function () {
    let value = this.value.toLowerCase();
    document.querySelectorAll('.recipe-card').forEach(card => {
        card.style.display = card.innerText.toLowerCase().includes(value) ? '' : 'none';
    });
});