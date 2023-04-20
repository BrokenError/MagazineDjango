function confirm_save()
    {
        if (confirm("Bы уверены, что хотите обновить данные своего аккаунта?\nНезаполненные поля будут очищены!!!"))
        return true;
        else return false;
    }

document.addEventListener('DOMContentLoaded', function() {

    var modalButtons = document.querySelectorAll('#modal_open'), closeButtons = document.querySelectorAll('#modal_close'),
        footer = document.getElementById("block-hidden"), window = document.getElementById("more");
    
    
    modalButtons.forEach(function(item){
        
        item.addEventListener('click', function(e) {
            e.preventDefault();
        footer.classList.add("hidden");
        window.classList.remove("user_personal_about-hidden");
        window.classList.add('user_personal_about-visible');
        });
    });

    closeButtons.forEach(function(items){
        
        items.addEventListener('click', function(e) {
            e.preventDefault();
        footer.classList.remove("hidden");
        window.classList.add("user_personal_about-hidden");
        window.classList.remove('user_personal_about-visible');
        });
    });
});