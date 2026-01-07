import { getCookie, replaceTable, renderMessages, resetActionStates } from "../modules/utils.js";

document.addEventListener("click", async function (e) {
    const editBtn = e.target.closest(".edit-btn");
    if (!editBtn) return;

    const row = editBtn.closest("tr");
    const table = document.querySelector("#collection-table");
    const collectionType = table.dataset.collectionType;
    const fields = JSON.parse(table.dataset.fields || "[]");
    const id = row.dataset.id;

    if (!id) {
        alert("Identifier of the item to edit is missing.");
        return;
    }

    resetActionStates(table, row);

    const originalRowHTML = row.outerHTML;

    editBtn.disabled = true;

    try {
        const resp = await fetch(`/table/edit-item/?collection_type=${encodeURIComponent(collectionType)}&id=${encodeURIComponent(id)}`);
        const data = await resp.json();

        if (!data.ok) {
            alert("Error: " + (data.html || "Failed to fetch edit form."));
            editBtn.disabled = false;
            return;
        }

        const temp = document.createElement("tbody");
        temp.innerHTML = data.html.trim();
        const editRow = temp.querySelector("tr");
        row.replaceWith(editRow);

        const lpCell = editRow.querySelector(".lp-cell");
        if (lpCell) {
            const index = [...table.querySelectorAll("tbody tr[data-id], tbody tr")].findIndex(tr => tr === editRow) + 1;
            lpCell.textContent = index;
        }

        // --- SAVE ---
        const saveBtn = editRow.querySelector(".save-edit-btn");
        if (saveBtn) {
            saveBtn.addEventListener("click", function () {
                const formData = new FormData();
                formData.append("collection_type", collectionType);
                formData.append("id", id);

                for (const field of fields) {
                    const input = editRow.querySelector(`[name="${CSS.escape(field)}"]`);
                    if (!input) continue;

                    if (input.type === "file" && input.files.length > 0) {
                        formData.append(field, input.files[0]);
                    } else if (input.type === "checkbox") {
                        if (input.checked) {
                            formData.append(field, "on");
                        }
                    } else if (input.tagName === "SELECT" && input.multiple) {
                        [...input.selectedOptions].forEach(opt => formData.append(field, opt.value));
                    } else {
                        formData.append(field, (input.value ?? "").toString().trim());
                    }
                }

                fetch("/table/edit-item/", {
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
        }

        // --- CANCEL ---
        const cancelBtn = editRow.querySelector(".cancel-edit-btn");
        if (cancelBtn) {
            cancelBtn.addEventListener("click", function () {
                editRow.outerHTML = originalRowHTML;
            });
        }

    } catch (err) {
        console.error(err);
        alert("The edit form could not be fetched.");
    } finally {
        if (document.body.contains(editBtn)) {
            editBtn.disabled = false;
        }
    }
});
