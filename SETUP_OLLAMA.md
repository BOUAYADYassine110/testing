# Setup Ollama (Free Local LLM)

## Install Ollama

### Windows
1. Download from: https://ollama.com/download/windows
2. Run the installer
3. Ollama will start automatically

### macOS
```bash
brew install ollama
```

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Pull the Model

```bash
# Pull Llama 3.2 (recommended, ~2GB)
ollama pull llama3.2

# Or use a smaller model
ollama pull llama3.2:1b

# Or use a larger model
ollama pull llama3.1:8b
```

## Verify Ollama is Running

```bash
# Check if Ollama is running
ollama list

# Test the model
ollama run llama3.2 "Hello, how are you?"
```

## Run Your Crew

```bash
crewai run
```

## Alternative Free LLMs

### Option 1: Groq (Fast, Free API)
```bash
# Get free API key from: https://console.groq.com
# Add to .env:
GROQ_API_KEY=your_key_here
```

Update agents.yaml:
```yaml
llm: groq/llama-3.1-70b-versatile
```

### Option 2: Google Gemini (Free tier)
```bash
# Get free API key from: https://makersuite.google.com/app/apikey
# Add to .env:
GOOGLE_API_KEY=your_key_here
```

Update agents.yaml:
```yaml
llm: gemini/gemini-pro
```

### Option 3: Anthropic Claude (Free trial)
```bash
# Get API key from: https://console.anthropic.com
# Add to .env:
ANTHROPIC_API_KEY=your_key_here
```

Update agents.yaml:
```yaml
llm: anthropic/claude-3-haiku-20240307
```

## Troubleshooting

### "Connection refused"
- Make sure Ollama is running: `ollama serve`
- Check if port 11434 is available

### "Model not found"
- Pull the model first: `ollama pull llama3.2`

### Slow performance
- Use a smaller model: `ollama pull llama3.2:1b`
- Or use Groq for faster cloud inference

## Recommended Setup

**For Local Development:**
- Use Ollama with llama3.2 (free, private)

**For Production/Deployment:**
- Use Groq (free, fast, cloud-based)
- Or OpenAI (paid, most reliable)
