// dark theme
$(document).ready(function () {
    //check for localStorage, add as browser preference if missing
    if (!localStorage.getItem("mode")) {
        if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
            localStorage.setItem("mode", "dark-theme");
        } else {
            localStorage.setItem("mode", "light-theme");
        }
    }

    //set interface to match localStorage
    if (localStorage.getItem("mode") == "dark-theme") {
        $("html").addClass("dark-theme");
        $("html").removeClass("light-theme");
        document.getElementById("theme_toggle").checked = true;
    } else {
        $("html").removeClass("dark-theme");
        $("html").addClass("light-theme");
        document.getElementById("theme_toggle").checked = false;
    }

    //add toggle
    $("#theme_toggle").on("click", function () {
        if ($("html").hasClass("dark-theme")) {
            $("html").removeClass("dark-theme");
            $("html").addClass("light-theme");
            localStorage.setItem("mode", "light-theme");
        } else {
            $("html").addClass("dark-theme");
            $("html").removeClass("light-theme");
            localStorage.setItem("mode", "dark-theme");
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {

    new Splide('.splide-months-index', {
        // type: 'loop',
        padding: '3em',
        pagination: false,
        autoHeight: true,
        // isNavigation: true,
        gap: '25px',
        perPage: 4,
        arrows: false,
        waitForTransition: false,
        breakpoints: {
            720: {
                perPage: 2,
            },
        },
        // classes: {
        //     arrows: "slide-months"
        // }
    }).mount();
    new Splide('.splide-months-income-index', {
        // type: 'loop',
        padding: '3em',
        pagination: false,
        autoHeight: true,
        // isNavigation: true,
        waitForTransition: false,
        gap: '25px',
        perPage: 4,
        arrows: false,
        breakpoints: {
            720: {
                perPage: 2,
            },
        },
        // perMove: 4,
        // classes: {
        //     arrows: "slide-months2"
        // }
    }).mount();

    new Splide('.splide-by-months', {
        // type: 'loop',
        padding: '3em',
        pagination: false,
        autoHeight: true,
        // isNavigation: true,
        gap: '25px',
        perPage: 3,
        arrows: false,
        waitForTransition: false,
        breakpoints: {
            720: {
                perPage: 2,
            },
            480: {
                perPage: 1,
            },
        }
        // perMove: 4,
        // classes: {
        //     arrows: "slide-months2"
        // }
    }).mount();


    // new Splide('.splide-years', {
    //     // type: 'loop',
    //     // padding: '30px',
    //     pagination: false,
    //     autoHeight: true,
    //     drag: false,
    //     classes: {
    //         arrows: "slide-years"
    //     },
    //     waitForTransition: false
    //
    // }).mount();


    // var elms = document.getElementsByClassName('splide-months');
    // for (var i = 0; i < elms.length; i++) {
    //     new Splide(elms[i], {
    //         // type: 'loop',
    //         padding: '50px',
    //         pagination: true,
    //         autoHeight: true,
    //         isNavigation: true,
    //         classes: {
    //             arrows: "slide-months"
    //
    //         }
    //
    //     }).mount();
    //
    // }


});


// menu
// $.sidebarMenu = function (menu) {
//     var animationSpeed = 300;
//
//     $(menu).on('click', 'li a', function (e) {
//         var $this = $(this);
//         var checkElement = $this.next();
//
//         if (checkElement.is('.treeview-menu') && checkElement.is(':visible')) {
//             checkElement.slideUp(animationSpeed, function () {
//                 checkElement.removeClass('menu-open');
//             });
//             checkElement.parent("li").removeClass("active");
//         }
//
//         //If the menu is not visible
//         else if ((checkElement.is('.treeview-menu')) && (!checkElement.is(':visible'))) {
//             //Get the parent menu
//             var parent = $this.parents('ul').first();
//             //Close all open menus within the parent
//             var ul = parent.find('ul:visible').slideUp(animationSpeed);
//             //Remove the menu-open class from the parent
//             ul.removeClass('menu-open');
//             //Get the parent li
//             var parent_li = $this.parent("li");
//
//             //Open the target menu and add the menu-open class
//             checkElement.slideDown(animationSpeed, function () {
//                 //Add the class active to the parent li
//                 checkElement.addClass('menu-open');
//                 parent.find('li.active').removeClass('active');
//                 parent_li.addClass('active');
//             });
//         }
//         //if this isn't a link, prevent the page from being redirected
//         if (checkElement.is('.treeview-menu')) {
//             e.preventDefault();
//         }
//     });
// }
//
// $.sidebarMenu($('.sidebar-menu'))


$("[data-toggle=\"datepicker\"]").flatpickr({
    // enableTime: true,
    // dateFormat: "Y-m-d H:i",
    // enableSeconds: true
});


//uncheck radio
// $(document).ready(function () {
//     $('input[type=radio]').click(function () {
//         if (this.previous) {
//             this.checked = false;
//         }
//         this.previous = this.checked;
//     });
// });


// delete alert
$(document).ready(function () {

    $(".alert-delete").click(function (e) {
        e.preventDefault();
        $(this).parent().remove();
    });

    setTimeout(function () {
        $('.alert').fadeOut('fast');
    }, 5000); // <-- time in milliseconds


});


// sidebar toggle
// document.querySelector(".side-panel-toggle").addEventListener("click", () => {
//     document.querySelector(".container").classList.toggle("side-panel-close");
//     document.querySelector("body").classList.toggle("overflow-hidden");
//     document.querySelector(".side-panel-toggle").classList.toggle("active");
// });


// mmenu


document.addEventListener(
    "DOMContentLoaded", () => {
        new Mmenu("#menu", {
            "slidingSubmenus": false,
            "extensions": [
                "theme-dark"
            ],
            "navbar": {
                "add": false
            },

            "sidebar": {
                // collapsed: {
                //     use: "(min-width: 820px)"
                // },
                expanded: {
                    use: "(min-width: 1080px)"
                }
            },
            "iconPanels": {
                "add": true,
                "visible": 1
            },

            "navbars": [
                {
                    "position": "bottom",
                    "content": [
                        "<div class='checkbox' ><div ><label ><input class='custom-form' type='checkbox' id='theme_toggle' ><span >Dark Theme</span > </label > </div >"
                    ]
                }
            ]
        });
    }
);


// document.getElementById('go-back').addEventListener('click', () => {
//     history.back();
// });


// sleect subcategroies
$('#select-add-category input').on('change', function () {
    $('#subcategories-add').hide();
    const id_cat = $('#select-add-category input:checked').attr('id');
    $('#subcategories-add label').hide();
    const sub_length = $('#subcategories-add' + ' .sub_' + id_cat).length;
    if (sub_length > 0) {
        $('#subcategories-add').css("display", "flex")
        $('#subcategories-add' + ' .sub_' + id_cat).show();
    }

    // $('#subcategories-add .Localuri').show();
});


