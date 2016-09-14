# Data Broker Tutorial Materials

[Documentation](https://nsls-ii.github.io/databroker)

## Usage

```
# Download the materials.
git clone https://github.com/NSLS-II/broker-tutorial

# Create a new "conda environment" and install the required Python packages.
cd broker-tutorial
conda create -n broker-tutorial python=3.5 numpy pandas matplotlib
source activate broker-tutorial
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
