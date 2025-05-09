# Welcome to Chainlit Agent-Powered UI🚀

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/waheed444/Chainlit.svg?style=social)](https://github.com/waheed444/Chainlit)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)


**Build interactive UIs for your AI agents with the power of Chainlit!**

## Table of Contents

* [Documentation](https://docs.chainlit.io/get-started/overview)
* [Description](#description)
* [Features](#features)
* [Tools](#Tools-Required)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)


## Description

This project demonstrates how to build interactive and user-friendly interfaces for your AI agents using Chainlit.  It leverages Chainlit's robust framework to create seamless conversational experiences, integrating seamlessly with powerful tools like LangChain, OpenAI, Gemini, and your custom Python logic.  Perfect for rapid prototyping and deployment of sophisticated agent workflows.


## Features

* 🧠 **Agent-based backend:**  Built with Python for flexibility and extensibility.
* 💬 **Real-time conversational interface:**  Powered by Chainlit for a smooth user experience.
* ⚙️ **Tool Integrations:**  Seamlessly integrates with LangChain, OpenAI, and Gemini APIs.
* 📂 **Modular Architecture:**  Easy to customize and scale to meet your needs.
* 🧪 **Local Development with Hot Reload (uv):**  Rapid iteration and development using `uv`.
* 🧱 **VS Code Compatibility:**  Seamless integration with your preferred IDE.
* 📈 **Extensible:**  Easily add advanced features like multi-agent orchestration, memory management, and custom tools.

## Tools-Required

To run and develop this Chainlit-based agent UI, make sure the following tools are installed on your system:

| Tool                | Description                                                                 | Install Command / Link                                      |
|---------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------|
| **Python 3.10+**     | Core programming language used in this project                              | [Download Python](https://www.python.org/downloads/)         |
| **Chainlit**         | Framework to build conversational UIs for LLMs                              | `uv pip install chainlit` or `pip install chainlit`          |
| **uv** *(optional)*  | Fast Python package manager (drop-in replacement for pip+virtualenv)        | `pip install uv` or see [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv) |
| **VS Code**          | Recommended code editor for development                                     | [Download VS Code](https://code.visualstudio.com/)           |
| **Git**              | Version control tool to clone and manage your project                       | [Install Git](https://git-scm.com/downloads)                 |
| **OpenAI / Gemini API Keys** | For accessing LLM models via LangChain or directly                     | [OpenAI](https://platform.openai.com/) / [Google AI Studio](https://aistudio.google.com/) |


## Installation

Before you begin, ensure you have Python 3.10 or higher installed.  We recommend using `uv` for faster dependency installation and hot reloading, but `pip` is also supported.


1. **Clone the repository:**

```bash
git clone https://github.com/waheed444/Chainlit.git
cd chainlit-agent-ui
```

2. **Install Chainlit:**

   * **Using `uv` (recommended):**

     ```bash
     uv add chainlit
     ```

   * **Using `pip`:**

     ```bash
     pip install chainlit
     ```

## Usage

To run the application locally:

```bash
chainlit run main.py -w   # For uv users : uv run chainlit run main.py -w 
```

The `-w` flag enables hot reloading, allowing you to see changes reflected instantly without restarting the server.

Once the application is running, open your web browser and navigate to `http://localhost:8000` to interact with your agent.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing

We welcome contributions to improve this project! Please follow these steps:

1. **Fork** the repository.
2. **Create a new branch:** `git checkout -b feature-name`
3. **Make your changes** and ensure they adhere to the project's coding style and best practices.
4. **Commit your changes:** `git commit -m "Add feature"`
5. **Push to the branch:** `git push origin feature-name`
6. **Submit a pull request** with a clear description of your changes and their benefits.
If you find any issues or want to improve this project, feel free to open a [GitHub issue](https://github.com/waheed444/Chainlit/issues) or submit a pull request.

This repo is only for learning and exploring new things, feel free to fork it, explore, or give suggestions!

**Star ⭐ the repo if it helps you!**

---

## 🙌 Let's Connect

<p align="left">
  <a href="https://www.linkedin.com/in/waheed444/?originalSubdomain=pk)" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://github.com/waheed444" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="waheedahmad5519@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</p>

---
