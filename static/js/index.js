const rulesLink = document.querySelector('.rules_link');

rulesLink.addEventListener('click', () => {
    swal("Criterias", "01) Username must have atleast one uppercase character. \n 02) Username must have atleast one lowercase character. \n 03) Username must end with a number.");
})