import { getCookie, switchActions, resetActionStates } from "../modules/utils.js";

// get reference to currently active delete row
let activeDeleteRow = null;

document.addEventListener("click", function (e) {
    // --- click on 🗑️ (delete) ---
    const deleteBtn = e.target.closest(".delete-btn");
    if (deleteBtn) {
        const row = deleteBtn.closest("tr");
        const table = document.querySelector("#collection-table");
        resetActionStates(table, row);

        if (activeDeleteRow && activeDeleteRow !== row) {
            switchActions(activeDeleteRow, "actions-default");
            activeDeleteRow = null;
        }

        switchActions(row, "actions-confirm-delete");
        activeDeleteRow = row;
        return;
    }

    // --- click on ✅ (confirm) ---
    const confirmBtn = e.target.closest(".confirm-delete-btn");
    if (confirmBtn) {
        const row = confirmBtn.closest("tr");
        const id = row.dataset.id;
        const collectionType = row.dataset.type;

        fetch("/table/delete-item/", {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: new URLSearchParams({
                id: id,
                collection_type: collectionType,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.ok) {
                    // actualize table content
                    document.getElementById("table").innerHTML = data.html;
                    activeDeleteRow = null;
                } else {
                    alert("Error: " + data.html);
                }
            })
            .catch((err) => console.error(err));
        return;
    }

    // --- click on ❌ (cancel) ---
    const cancelBtn = e.target.closest(".cancel-btn");
    if (cancelBtn) {
        const row = cancelBtn.closest("tr");
        switchActions(row, "actions-default");

        // if cancel was for the active delete row, clear the reference
        if (activeDeleteRow === row) {
            activeDeleteRow = null;
        }
        return;
    }
});
