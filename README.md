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

Install the agent

```bash
cd tonai-agent; poetry install
```

Run the agent

```bash
poetry run serve
```