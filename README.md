![tonai-stark](./assets/tonai-stark.png)

<h1 align="center">Ton<span style='color:red'>AI</span> Stark</h1>
<p>
</p>

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Installation Guide](#installation-guide)

## Project Overview

## Technologies Used

## Screenshots


## Installation Guide

This guide will walk you through installing and running both the client and agent components of the Tonai application.

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or newer)
- [pnpm](https://pnpm.io/installation)
- [Python](https://www.python.org/downloads/) (v3.8 or newer)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Git](https://git-scm.com/downloads)

### Client Setup

#### 1. Install Dependencies

Navigate to the client directory and install the required packages:

```bash
cd tonai-client
pnpm install
```

#### 2. Configure Environment

Create a local environment configuration file:

```bash
cp .env.example .env
```

> **Note:** You may need to update values in the `.env` file based on your specific configuration requirements.

#### 3. Start Development Server

Launch the client in development mode:

```bash
pnpm dev
```

The client should now be running at `http://localhost:3000` (or another port if configured differently).

### Agent Setup

#### 1. Install Poetry (if not already installed)

```bash
pip install poetry
```

#### 2. Install AVNU API Python Client (SDK)

First, install the required setuptools:

```bash
pip install setuptools
```

Then navigate to the SDK directory and install it:

```bash
cd sdk/avnu-python-client
python setup.py install
```

#### 3. Install Agent Dependencies

Navigate to the agent directory and install dependencies using Poetry:

```bash
cd tonai-agent
poetry install
```

#### 4. Run the Agent

Start the agent service:

```bash
poetry run server
```

The agent should now be running and ready to connect with the client.

## Troubleshooting

If you encounter issues:

- Verify that the `.env` file contains correct configuration values
- Ensure no other services are running on the required ports