# Data Broker Tutorial Materials

## Usage

```
# Download the materials.
git clone https://github.com/NSLS-II/broker-tutorial

# Create a new "conda environment" and install the required Python packages.
cd broker-tutorial
conda create -n SOME_ENVIRONMENT_NAME python=3.5 numpy pandas matplotlib
pip install -r requirements.txt

# Start IPython
ipython

# In IPython, run a script that generates data and defines a Broker, db.
%run generate_data.py

# Try examples, such as:
db(proposal_id=1)
all_scans = db(plan_name='scan')
db.get_table(all_scans)
```
