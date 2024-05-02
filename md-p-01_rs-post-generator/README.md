# May Day's post generator

A tool developed with Python and CrewAI to generate LinkedIn posts to promote May Day's projects

![post_img]()

## Features

Automatically generate LinkedIn posts for May Day project using name, description and technologies.

## Prerequisites

Python3 installed
Ollama installed
SERPER API key

## Installation
Clone the GitHub repository:

```bash
git clone https://github.com/Phenixjj/Maydays.git
git checkout project/md-p-01_rs-post_generator
```

Navigate to the project directory:

```bash
cd md-p-01_rs-post_generator
```

Install dependencies:

```bash
poetry install --no-root
```

create .env file with : 
```
SERPER_API_KEY=your_api_key
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_MODEL_NAME=crewai-llama2 or crewai-mistral
OPENAI_API_KEY=NA
```

Usage

Create custom model and start application:

```bash
cd script
bash create-mistral-model-file.sh
cd ..
python main.py
```

Follow the steps in the terminal

## Technologies Used
Python CrewAI Ollama

## Contributing
Contributions to the project are welcome! To contribute:

Fork the repository

Create a new branch (git checkout -b feature/my-feature)
Commit your changes (git commit -am 'Add a new feature')
Push the branch (git push origin feature/my-feature)
Open a Pull Request

## Author
Jean LECIGNE

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to adapt this template based on the specifics of your project, such as the repository name, technologies used, implemented features, etc. Ensure to provide clear instructions on installation, usage, and contribution to make your README informative and accessible to anyone interested in exploring or contributing to the project.
