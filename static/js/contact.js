function init() {
    console.log("Contact page");


    const serviceId = "service_zd4273f";
    const templateId = "template_qss8wks";
    const publicKey = "h-qTcgavsz4l69AGF";

    emailjs.init(publicKey)

    document.getElementById("emailForm").addEventListener("submit", function(event) {
        event.preventDefault();
        console.log("sending");
        const form = event.target;
        
        const name = form.elements.name.value;
        const email = form.elements.email.value;
        const company = form.elements.company.value;
        const scope = form.elements.scope.value;
        const budget = form.elements.budget.value;


        const params = {
            name,
            email,
            company,
            scope,
            budget,
        };

        
        emailjs.send(serviceId, templateId, params).then(res => {
            alert("Email sent");
        },
        error => {
            console.log(error);
            alert("Error sending email");
        })

        
    });
    
}

window.onload = init;


