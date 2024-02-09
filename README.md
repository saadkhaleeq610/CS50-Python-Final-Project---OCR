# Image to Text Converter

[Watch the video](https://youtu.be/MPeyLcwCQ4g)


This project is a simple Python application that converts images containing text into editable text format using optical character recognition (OCR) technology. It provides two main functionalities: capturing text from a webcam feed in real-time and extracting text from uploaded images. The extracted text can then be saved in a PDF document for further use.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [About the Author](#about-the-author)

## Installation
To use this application, you need to have Python installed on your system. You can then install the required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage
1. **Clone the Repository**:
   Clone the repository to your local machine by running the following command:

   ```bash
   git clone https://github.com/your_username/your_project.git
   cd your_project
   ```

2. **Run the Application**:
   Run the main script `project.py`:

   ```bash
   python project.py
   ```

3. **Using the Application**:
   - The main window of the application provides two options: "Use Webcam" and "Upload from computer".
   - Clicking on "Use Webcam" opens a new window displaying the webcam feed. Click the "Capture" button to capture an image and extract text from it.
   - Clicking on "Upload from computer" allows you to select an image file from your computer. The application will extract text from the uploaded image.

## Testing
To ensure the correctness of the application, unit tests are provided in `test_project.py`. You can run the tests using pytest:

```bash
pytest test_project.py
```

## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About the Author
This project was created by Saad Khaleeq. If you have any questions or suggestions, feel free to reach out to me at [saadkhaleeq610@example.com].
