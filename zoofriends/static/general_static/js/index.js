/* VK VIDEO ADAPTIVE */
const vkVideo = document.getElementById('vk-video');

if (vkVideo) {
    const vkVideoWidth = vkVideo.getBoundingClientRect().width;
    const HEIGHT_TO_WIDTH_RATIO = .6;
    const vkVideoHeight = vkVideoWidth * HEIGHT_TO_WIDTH_RATIO;

    vkVideo.style.height = `${vkVideoHeight}px`;
}

/* BURGER */
const burger = document.getElementById('burger');

burger.addEventListener('click', () => {
    const navMobile = document.getElementById('nav-mobile');
    const body = document.body;

    if (burger.classList.contains('burger--active')) {
        navMobile.classList.remove('nav__mobile--show');
        burger.classList.remove('burger--active');
        body.classList.remove('body--no-scroll');
    } else {
        navMobile.classList.add('nav__mobile--show');
        burger.classList.add('burger--active');
        body.classList.add('body--no-scroll');
    }
})

/* nav */
const toggleMobileClassForNav = () => {
    const windowWidth = window.innerWidth;
    const isMobile = windowWidth < 968;

    if (isMobile) {
        const nav = document.getElementById('nav');
        nav.classList.add('nav--mobile');
    } else {
        nav.classList.remove('nav--mobile');
    }
}

toggleMobileClassForNav();
window.addEventListener('resize', () => {
    toggleMobileClassForNav();
});

/* select-photo */
const selectPhotoItems = [...document.querySelectorAll('.select-photo')];

for (const selectPhoto of selectPhotoItems) {
    const input = selectPhoto.querySelector('input');
    const btn = selectPhoto.querySelector('button');
    const urlField = selectPhoto.querySelector('span');
    const imgPreview = document.getElementById(selectPhoto.dataset.for);

    btn.onclick = () => {
        input.click()
        console.log(input);
    }
    input.onchange = () => {
        const files = input.files;
        urlField.innerText = input.value;

        if (files[0]) {
            imgPreview.setAttribute('src', URL.createObjectURL(files[0]));
        }
    }
}

/* dropdown */
const dropdowns = [...document.querySelectorAll('.dropdown')];

for (const dropdown of dropdowns) {
    dropdown.addEventListener('click', () => {
        dropdown.classList.toggle('dropdown--active');
    })
}

window.addEventListener('click', (event) => {
    if (
        !event.target.classList.contains('dropdown')
        &&
        !event.target.classList.contains('dropdown__label')
        &&
        !event.target.classList.contains('dropdown__content')
    ) {
        for (const dropdown of dropdowns) {
            dropdown.classList.remove('dropdown--active');
        }
    }
})

/* card-zoo */
const cardsZoo = [...document.querySelectorAll('.card-zoo')];

for (const cardZoo of cardsZoo) {
    const userId = cardZoo.dataset.userid;
    const animalId = cardZoo.dataset.animalid;
    const btn_mark_as_fav = cardZoo.querySelector('.card-zoo__mark-as-favorite');

    if (btn_mark_as_fav) {
        btn_mark_as_fav.addEventListener('click', async () => {
            cardZoo.classList.toggle('card-zoo--is-favorite');
            await fetch(`/animalprofile/toggle-in-favorites/${userId}/${animalId}`);
        });
    }
}

/* add-to-favorite */
const btnAddToFavorites = [...document.querySelectorAll('.zooprofile__add-to-favorite')];

for (const btn of btnAddToFavorites) {
    const userId = btn.dataset.userid;
    const animalId = btn.dataset.animalid;

    btn.addEventListener('click', async () => {
        btn.classList.toggle('zooprofile__mark-as-favorite');
        await fetch(`/animalprofile/toggle-in-favorites/${userId}/${animalId}`);
    })
}