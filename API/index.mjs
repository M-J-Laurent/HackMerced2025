import express, { request, response } from 'express';
import { spawn } from 'child_process';

// set up the server
const app = express();
app.use(express.json())
const PORT = 4000;

// graph data
let points = ''

// post route
app.post('/api', (request, response) => {
    const { body } = request;

    // set up child process
    const pythonScript = spawn('python3', ['script.py']);

    // Passing data to Python script
    pythonScript.stdin.write("Hello there from python!");  
    pythonScript.stdin.end();

    // print the output of python script
    pythonScript.stdout.on('data', (data) => {
        points = data.toString();
    });

    // if error
    pythonScript.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    //  close the child process
    pythonScript.on('close', (code) => {
        console.log(`Python script finished with code ${code}`);
        return response.status(200).json(points)
    });
    // return response.status(200).json(points)
})

// run the server
app.listen(PORT, () => {
    console.log("Running on Port", PORT)
})