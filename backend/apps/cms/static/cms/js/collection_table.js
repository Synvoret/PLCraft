document.addEventListener("DOMContentLoaded", function() {
    const selectElement = document.getElementById("id_collection_type");
    if (selectElement) {
        selectElement.addEventListener("change", function() {
            const selected = this.value;
            if (!selected) {
                document.getElementById("collection-table").innerHTML = "";
                return; // do not send request
            }
            fetch(`/collection-table/?collection_type=${selected}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById("collection-table").innerHTML = data.html;
                })
                .catch(error => console.error("Error:", error));
        });
    }
});

