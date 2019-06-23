# configuration
If you are using (or adapting) exampleProg.py, do this:
- In the folder in which exampleProg.py resides, create a file called 'config.json'
- Open 'config.json' in a file editor, and insert the following:

    ```
    {
	    "apikey": 9d8d10a65c45d780252da98ba275f4c4
    }
    ```
    
- Paste your APIkey (obtained from http://dev.elsevier.com) in the right place
- If you don't have a valid insttoken (which you would have received from Elsevier support staff), delete the placeholder text. If you enter a dummy value, your API requests will fail.

The '.gitignore' file lists 'config.json' as a file to be ignored when committing elsapy to a GIT repository, which is to prevent your APIkey from being shared with the world. Make similar provisions when you change your configuration setup.
