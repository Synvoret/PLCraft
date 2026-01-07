import { getCookie, replaceTable, renderMessages, resetActionStates } from "../modules/utils.js";

/**
 * Reser all rows in the table to "actions-default" state.
 * except excludeRow, which will remain unchanged.
 * Work in two contexts:
 * - closes delete confirmation mode (confirm/cancel)
 * - close open add item form
 * @param {HTMLElement} table
 * @param {HTMLTableRowElement} excludeRow
 */

document.addEventListener("click", async function(e) {
    const addBtn = e.target.closest(".add-btn");
    if (!addBtn) return;

    const addRow = addBtn.closest("tr");
    const table = document.querySelector("#collection-table");
    const collectionType = table.dataset.collectionType;
    const fields = JSON.parse(table.dataset.fields || "[]");

    // First, reset other rows to default
    resetActionStates(table, addRow);

    // optionally: prevent multiple clicks
    addBtn.disabled = true;

    try {
        const resp = await fetch(`/table/add-item/?collection_type=${encodeURIComponent(collectionType)}`);
        const data = await resp.json();

        if (!data.ok) {
            alert("Error: " + data.html);
            addBtn.disabled = false;
            return;
        }

        const temp = document.createElement("tbody");
        temp.innerHTML = data.html.trim();
        const newRow = temp.querySelector("tr");
        addRow.replaceWith(newRow);

        const lpNumber = table.querySelectorAll("tbody tr[data-id]").length + 1;
        const lpCell = newRow.querySelector(".lp-cell");
        if (lpCell) lpCell.textContent = lpNumber;

        // SAVE
        newRow.querySelector(".save-btn").addEventListener("click", function() {
            const formData = new FormData();
            formData.append("collection_type", collectionType);

            for (const field of fields) {
                const input = newRow.querySelector(`[name="${CSS.escape(field)}"]`);
                if (!input) continue;

                if (input.type === "file" && input.files.length > 0) {
                    formData.append(field, input.files[0]);
                } else {
                    formData.append(field, input.value.trim());
                }
            }

            fetch("/table/add-item/", {
                method: "POST",
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                body: formData
            })
            .then(r => r.json())
            .then(data => {
                if (data.ok) {
                    replaceTable(data.html);
                } else {
                    renderMessages(data.messages);
                }
            })
            .catch(error => console.error(error));
        });

        // CANCEL
        newRow.querySelector(".cancel-add-btn").addEventListener("click", function() {
            newRow.outerHTML = `
                <tr id="add-row" data-type="${collectionType}">
                    <td colspan="${fields.length + 1}"></td>
                    <td class="d-flex justify-content-center align-items-center flex-nowrap gap-2">
                        <button class="btn btn-sm btn-outline-info add-btn">➕</button>
                    </td>
                </tr>
            `;
        });

    } catch (err) {
        console.error(err);
        alert("Form could not be downloaded.");
    } finally {
        // Re-enable Add (if addRow was replaced, this button no longer exists)
        if (document.body.contains(addBtn)) {
            addBtn.disabled = false;
        }
    }
});