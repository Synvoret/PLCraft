
document.addEventListener("click", function(e) {
    const btn = e.target.closest(".delete-btn");
    if (btn) {
        const row = btn.closest("tr");
        const actionsCell = btn.closest("td");

        const id = row.dataset.id;
        const collectionType = row.dataset.type;

        actionsCell.innerHTML = `
            <span>Sure?</span>
            <button class="btn btn-sm btn-outline-warning flex-fill confirm-delete">✅</button>
            <button class="btn btn-sm btn-outline-danger flex-fill cancel-delete">❌</button>
        `;

        actionsCell.querySelector(".confirm-delete").addEventListener("click", function() {
            fetch("/collection-table/delete-item", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: new URLSearchParams({
                    id: id,
                    collection_type: collectionType
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.ok) {
                    document.querySelector("#collection-table").innerHTML = data.html;
                } else {
                    alert("Error: " + data.html);
                }
            })
            .catch(err => console.error(err));
        });

        actionsCell.querySelector(".cancel-delete").addEventListener("click", function() {
            actionsCell.innerHTML = `
                <button class="btn btn-sm btn-outline-info flex-fill" title="View">👁️</button>
                <button class="btn btn-sm btn-outline-primary flex-fill" title="Edit">✏️</button>
                <button class="btn btn-sm btn-outline-danger flex-fill delete-btn" title="Delete">🗑️</button>
            `;
        });
    }
});

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
