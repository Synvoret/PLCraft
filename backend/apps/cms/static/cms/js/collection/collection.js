document.addEventListener("DOMContentLoaded", function () {
    const selectElement = document.getElementById("id_collection_type");


    function table() {
        const selected = selectElement.value;
        if (!selected) {
            document.getElementById("table").innerHTML = "";
            return;
        }

        fetch(`/table/?collection_type=${selected}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById("table").innerHTML = data.html;
            })
            .catch(error => console.error("Error:", error));
    }

    if (selectElement) {
        selectElement.addEventListener("change", table);
    }

    if (selectElement && selectElement.value) {
        table();
    }
});
