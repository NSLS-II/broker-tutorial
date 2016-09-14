# Data Broker Tutorial Materials

## Usage

```
# Download the materials.
git clone https://github.com/NSLS-II/broker-tutorial

# Create a new "conda environment" and install the required Python packages.
cd broker-tutorial
conda create -n SOME_ENVIRONMENT_NAME python=3.5
pip install -r requirements.txt

# Start IPython
ipython

# In IPython, run a script that defines a Broker instance, db.
%run setup_broker.py

# Try examples, such as:
db(proposal_id=1)
```
