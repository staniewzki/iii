"use strict";

const itemTranslations = {
    "Excavator": "Koparka",
    "Concrete mixer": "Betoniarka",
    "Bulldozer": "Buldożer",
    "Jackhammer": "Młot pneumatyczny",
    "Drill": "Wiertarka",
    "Scaffolding": "Rusztowanie",
    "Concrete pump": "Pompa do betonu",
    "Chainsaw": "Piła łańcuchowa",
    "Angle grinder": "Szlifierka kątowa"
}

const updatePage = () => {
    const kindSelect = document.getElementById("kind");
    const offersHeader = document.getElementById("offers-header");
    const noOffersHeader = document.getElementById("no-offers-header");

    if (kindSelect) {
        for (const item in itemTranslations) {
            const option = document.createElement("option");
            option.value = item;
            option.innerText = itemTranslations[item];
            kindSelect.appendChild(option);
        }
    }

    if (offersHeader) {
        const innerText = offersHeader.innerText;
        const translated = itemTranslations[innerText.match(/\$(.*)\$/)[1]];
        offersHeader.innerText = innerText.replace(/\$.*\$/g, translated);
    }

    if (noOffersHeader) {
        const innerText = noOffersHeader.innerText;
        const translated = itemTranslations[innerText.match(/\$(.*)\$/)[1]];
        noOffersHeader.innerText = innerText.replace(/\$.*\$/g, translated);
    }
}

window.onload = updatePage;
