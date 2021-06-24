# Osintin Framework

Osintin is a framework with Component-based architecture. Osintin provides the component development platform for Osint software.

### Requirements

- Wikipedia 1.4.0
- Requests 2.25.1

### Deployment

```bash
git clone git@github.com:vispamir/osintin.git
cd osintin

# Create virtualenv named build
virtualenv -p python3 build
source build/bin/activate

# Install requirements, migration and run
pip install -r requirements.txt
python main.py [cli | rest]
```

If runned project with rest interface, all endpoints available on `http://localhost:7000`
