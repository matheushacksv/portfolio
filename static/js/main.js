import Alpine from "https://cdn.jsdelivr.net/npm/alpinejs@3.14.1/dist/module.esm.js";
import intersect from "https://cdn.jsdelivr.net/npm/@alpinejs/intersect@3.14.1/dist/module.esm.js";

window.Alpine = Alpine;
Alpine.plugin(intersect);
Alpine.start();

if (window.initFlowbite) {
    window.initFlowbite();
}