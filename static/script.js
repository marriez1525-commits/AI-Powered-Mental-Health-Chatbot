function sendMessage() {

    let text = document.getElementById("user-input").value;
    let box = document.getElementById("chat-box");

    let btn = document.getElementById("btn");
    let loader = document.getElementById("loader");

    if (text.trim() === "") return;

    loader.style.display = "inline-block";
    btn.disabled = true;

    fetch("/get_response", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: text})
    })
    .then(res => res.json())
    .then(data => {

        loader.style.display = "none";
        btn.disabled = false;

        box.innerHTML = "";

        let div = document.createElement("div");
        div.className = "box";

        div.innerHTML = `
            <div><b>MENTAL STATE:</b> ${data.response}</div>
            <div style="margin-top:10px;"><b>CONFIDENCE:</b> ${data.confidence}%</div>
            <div style="margin-top:10px; color:${data.color}">
                ${data.advice}
            </div>
        `;

        box.appendChild(div);
    });
}