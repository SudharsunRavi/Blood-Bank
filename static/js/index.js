const capitalizeFirstLetter=(inputId)=> {
    var inputElement = document.getElementById(inputId);
    var inputValue = inputElement.value.toLowerCase();
    inputValue = inputValue.charAt(0).toUpperCase() + inputValue.slice(1);
    inputElement.value = inputValue;
}

const applySentenceCase=()=> {
    var inputs = document.querySelectorAll('input[type="text"], select');
    inputs.forEach(function(input) {
        capitalizeFirstLetter(input.id);
    });
}

const filterDonorsByCity=()=> {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchCity");
    filter = input.value.toUpperCase();
    table = document.getElementById("donorsTable");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[3];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}