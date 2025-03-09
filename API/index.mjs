import express, { request, response } from 'express';
import { spawn } from 'child_process';

// set up the server
const app = express();
app.use(express.json())
const PORT = 4000;

// post route
app.post('/api', (request, response) => {
    console.log(request.body);
    const { body } = request;

    // set up child process
    const pythonScript = spawn('python3', ['script.py']);

    // Passing data to Python script
    pythonScript.stdin.write("Hello there from python!");  
    pythonScript.stdin.end();

    // print the output of python script
    pythonScript.stdout.on('data', (data) => {
        console.log(data.toString());
    });

    // if error
    pythonScript.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    //  close the child process
    pythonScript.on('close', (code) => {
        console.log(`Python script finished with code ${code}`);
    });


    return response.status(200).send("Hi there, I got your post request!")
})

// run the server
app.listen(PORT, () => {
    console.log("Running on Port", PORT)
})