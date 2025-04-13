# TonAIStark


## Client

Install dependencies:

```bash
cd tonai-client; pnpm install
```

Copy the `.env`

```bash
cp .env.example .env
```

Run client:

```bash
pnpm dev
```

## Agent

Install the agent 

Install poetry

```bash
pip install poetry
```

### SDK (AVNU API Python Client)
```bash
pip install setuptools
cd sdk/avnu-python-client
python setup.py install
```

Install the agent

```bash
cd tonai-agent; poetry install
```

Run the agent

```bash
poetry run server
```

