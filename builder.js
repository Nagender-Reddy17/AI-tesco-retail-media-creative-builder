function gen() {
    fetch('/generate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            brand: brand.value,
            product: product.value,
            offer: offer.value
        })
    })
    .then(res => res.json())
    .then(data => {
        out.innerText =
            data.creative +
            "\n\nStatus: " + data.validation;
    });
}
