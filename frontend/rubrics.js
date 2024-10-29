const domain = 'http://127.0.0.1:8000/api/';

const list = document.querySelector('#list');

async function loadList() {
    const result = await fetch(`${domain}rubrics`);

    if(result.ok) {
        const data = await result.json();
        let s = '', d;
        for (let i = 0; i < data.length; i++) {
            d = data[i];
            s += `<li>${d.name}</li>`
        }

        list.innerHTML = s;
    } else {
        window.alert(result.statusText);
    }
}

loadList();