import {createServer} from 'node:http'
import { readFile } from 'node:fs/promises';

const PORT = 3000;
const server = createServer(async(req, res)=>{
try {
    const file = await readFile('./index.html');
    res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"})
    res.end(file)
    
} catch (error) {
    res.writeHead(404, {"content-type":"text/plain"});
    res.end("No se ha encontrado la pagina, lo sentimos")
    }
});
server.listen(PORT, HOST, ()=>{
    console.log(`>>> seridor corriendo en http://localhost:${PORT}`)
})