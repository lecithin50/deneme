// script.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('product-form');
    const productTable = document.getElementById('products');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const serialNumber = document.getElementById('serialNumber').value;
        const name = document.getElementById('name').value;
        const manufactureDate = document.getElementById('manufactureDate').value;
        const manufacturer = document.getElementById('manufacturer').value;
        const materialComposition = document.getElementById('materialComposition').value;
        const fuelConsumption = document.getElementById('fuelConsumption').value;
        const carbonEmission = document.getElementById('carbonEmission').value;

        addProductToTable(serialNumber, name, manufactureDate, manufacturer, materialComposition, fuelConsumption, carbonEmission);

        form.reset();
    });

    function addProductToTable(serialNumber, name, manufactureDate, manufacturer, materialComposition, fuelConsumption, carbonEmission) {
        const row = document.createElement('tr');
        
        row.innerHTML = `
            <td>${serialNumber}</td>
            <td>${name}</td>
            <td>${manufactureDate}</td>
            <td>${manufacturer}</td>
            <td>${materialComposition}</td>
            <td>${fuelConsumption}</td>
            <td>${carbonEmission}</td>
        `;

        productTable.appendChild(row);
    }
});
