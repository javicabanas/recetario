// Botón de impresión flotante
document.addEventListener('DOMContentLoaded', function() {
  // Crear botón solo en páginas de recetas (no en índice)
  if (window.location.pathname !== '/' && window.location.pathname !== '/index.html') {
    const printButton = document.createElement('button');
    printButton.className = 'print-button';
    printButton.setAttribute('aria-label', 'Imprimir esta receta');
    printButton.innerHTML = 'Imprimir';
    
    printButton.addEventListener('click', function() {
      window.print();
    });
    
    document.body.appendChild(printButton);
  }
});

// Agregar atajo de teclado Ctrl+P / Cmd+P
document.addEventListener('keydown', function(e) {
  if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
    e.preventDefault();
    window.print();
  }
});
