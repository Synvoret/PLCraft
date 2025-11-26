
document.addEventListener("click", function(e) {
    const addBtn = e.target.closest(".add-btn");
    if (addBtn) {
        const addRow = addBtn.closest("tr");
        const table = document.querySelector("#collection-table");
        const collectionType = table.dataset.collectionType;
        console.log(table.dataset.fields)
        const fields = JSON.parse(table.dataset.fields);

        // Generuj formularz
        const lpNumber = table.querySelectorAll("tbody tr[data-id]").length + 1;
        let formHtml = `<td>${lpNumber}</td>`;
        fields.forEach(field => {
            formHtml += `<td><input type="text" name="${field}" class="form-control form-control-sm" placeholder="${field}"></td>`;
        });

        addRow.innerHTML = `
            ${formHtml}
            <td class="d-flex justify-content-center">
                <button class="btn btn-sm btn-outline-success save-btn">💾</button>
                <button class="btn btn-sm btn-outline-secondary cancel-add-btn">❌</button>
            </td>
        `;

        // Obsługa Save
        addRow.querySelector(".save-btn").addEventListener("click", function() {
            const formData = new URLSearchParams();
            formData.append("collection_type", collectionType);
            fields.forEach(field => {
                const value = addRow.querySelector(`[name="${field}"]`).value.trim();
                formData.append(field, value);
            });

            fetch("/collection-table/add-item", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.ok) {
                    replaceTable(data.html);
                } else {
                    alert("Error: " + data.html);
                }
            })
            .catch(err => console.error(err));
        });

        // Obsługa Cancel
        addRow.querySelector(".cancel-add-btn").addEventListener("click", function() {
            addRow.innerHTML = `
                <td colspan="${fields.length + 1}"></td>
                <td class="d-flex justify-content-center">
                    <button class="btn btn-sm btn-outline-info add-btn">➕</button>
                </td>
            `;
        });
    }
});

function replaceTable(html) {
    const wrapper = document.createElement("div");
    wrapper.innerHTML = html.trim();
    const newTable = wrapper.querySelector("table");
    document.querySelector("#collection-table").replaceWith(newTable);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
