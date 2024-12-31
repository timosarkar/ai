# install ollama
brew install ollama

# install pip deps
sudo python3 -m pip install -r requirements.txt --break-system-packages

# run this in current session
ollama serve

# run this in different session
ollama pull phi3

# run the agent
python3 duckduckgoagent.py