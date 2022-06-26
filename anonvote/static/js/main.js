(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()

const createModal = document.getElementById('createModal')
if (createModal) {
    createModal.addEventListener('hidden.bs.modal', () => {
        const form = document.getElementById("createForm");
        form.classList.remove('was-validated');
        form.reset();
    })
}

// const alert = bootstrap.Alert.getOrCreateInstance('#findPollError')
// alert.close()