export function getCookie(name) {
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

export function replaceTable(html) {
    const wrapper = document.createElement("div");
    wrapper.innerHTML = html.trim();
    const newTable = wrapper.querySelector("table");
    const oldTable = document.querySelector("#collection-table");
    if (newTable && oldTable) oldTable.replaceWith(newTable);
}

export function renderMessages(messages) {
    const box = document.querySelector('.messages');
    if (!box) return;
    box.innerHTML = '';
    const div = document.createElement('div');
    div.className = 'd-grid gap-2 col-12 col-sm-10 col-md-8 col-lg-6 mx-auto';
    box.appendChild(div);
    (messages || []).forEach(msg => {
        const p = document.createElement('p');
        p.className = `alert alert-${msg.tags}`;
        p.textContent = msg.message;
        div.appendChild(p);
    });
}

export function resetActionStates(table, excludeRow = null) {
    if (!table) return;

    // 1) Close all "delete confirmations"
    const confirmationButtons = table.querySelectorAll(".confirm-delete-btn, .cancel-btn");
    confirmationButtons.forEach(btn => {
        const tr = btn.closest("tr");
        if (tr && tr !== excludeRow) {
            switchActions(tr, "actions-default");
        }
    });

    // 2) Close all open add item forms
    const openAddRows = table.querySelectorAll("tbody tr");
    openAddRows.forEach(tr => {
        if (tr === excludeRow) return;
        const cancelAdd = tr.querySelector(".cancel-add-btn");
        if (cancelAdd) {
            cancelAdd.click();
        }
    });
    
    // 3) Close all open edit forms
    const editRows = table.querySelectorAll("tbody tr.edit-row");
        editRows.forEach(tr => {
            if (tr === excludeRow) return;
            const cancelEdit = tr.querySelector(".cancel-edit-btn");
            if (cancelEdit) {
                cancelEdit.click();
            } else {
                switchActions(tr, "actions-default");
            }
        });
}

export function switchActions(row, templateId) {
    const template = document.getElementById(templateId);

    if (!template) return;

    const actionsCell = row.querySelector("td:last-child");
    if (!actionsCell) return;

    const clone = template.content.firstElementChild.cloneNode(true);

    actionsCell.replaceChildren(...clone.childNodes);
}
