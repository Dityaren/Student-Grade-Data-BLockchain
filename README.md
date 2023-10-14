# Student Grade Data BLockchain

This is a simple blockchain web application implemented using FastAPI and Python. The application allows you to create blocks with student data and view the blockchain.

## Installation

To run the web application, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Dityaren/Student-Grade-Data-BLockchain
```

2. Change into the project directory:

```bash
cd Student-Grade-Data-BLockchain
```

3. Install the dependencies:

```bash
pip install fastapi
pip install Jinja2
```

4. Run the application:

```bash
uvicorn main:app --reload
```

The application will start running on `http://localhost:8000`.

## Usage

### Create a Block

To create a new block with student data, make a GET request to `/buat_block/` with the following parameters:

- `nama`: Student name
- `kelas`: Student class
- `bahasa_indonesia`: Indonesian language grade (integer)
- `bahasa_inggris`: English language grade (integer)
- `ipa`: Science grade (integer)
- `ips`: Social science grade (integer)

The server will respond with the created block.

### View the Blockchain

To view the entire blockchain, make a GET request to `/blockchain/`. The server will respond with the blockchain data.

### Check Blockchain Validity

To check the validity of the blockchain, make a GET request to `/cek`. The server will respond with the validity status of the blockchain.

### Web Interface

The web application provides a user interface to interact with the blockchain. Access the following routes:

- `/` - Home page displaying student data and menu options.
- `/{menu}` - Dynamic routes based on the menu option selected. Available options:
  - `tambah` - Add student data to the blockchain.
  - `lihat` - View the blockchain.
  - `cek` - Check the validity of the blockchain.

## Templates

The web application uses Jinja2 templates to render HTML pages. The HTML templates can be found in the `htmldirectory` directory.

## Contributing

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
