let graphs = [
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=620285480&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=2094634423&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=671397841&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=1477512222&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=1635957491&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=1891157947&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=1933790701&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=219869682&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=2109091130&amp;format=interactive"></iframe>', 
    '<iframe class="graph" width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTVls1Sx-UMOjgUFjnbc_2-kpsSf6MXqwoMhRfDzyR6E9IBNo7PkTUvNo3C4COdE7AhatRNR-VT_Atb/pubchart?oid=289815464&amp;format=interactive"></iframe>']

console.log(graphs.length)

let i = 1

function btn(n) {
    if (n === 1) {
        i++
    } else if (n === 2) {
        i--
    }

    if (i > 10) {
        i=1
    } else if (i < 1) {
        i=10
    }

    document.getElementById('graph-num').innerHTML = i;
    document.getElementById('graphs12').innerHTML = graphs[i-1];
}